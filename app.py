# app.py
import streamlit as st
from graph.workflow import graph

# Page Setup - Professional Look & Feel
st.set_page_config(
    page_title="Multi-Agent Autonomous Research System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Autonomous Research & Report Generation System")
st.markdown("---")

# Session State Initialization - Streamlit re-run handle karne ke liye
if "config" not in st.session_state:
    st.session_state.config = {"configurable": {"thread_id": "streamlit_session_1"}, "recursion_limit": 15}
if "phase" not in st.session_state:
    st.session_state.phase = "INPUT"  # Phases: INPUT -> PROPOSAL -> COMPLETED
if "query" not in st.session_state:
    st.session_state.query = ""
if "report" not in st.session_state:
    st.session_state.report = ""

# Sidebar - Project Metadata & Telemetry Logs
with st.sidebar:
    st.header("⚙️ Graph Metrics & Tracing")
    st.info("⚡ Powered by LangGraph & Mistral AI")
    st.success("🛰️ Observability: LangSmith Tracing Active")
    
    # Live Status Tracking Box
    st.markdown("### 🕒 Graph State Logs")
    if st.session_state.phase == "INPUT":
        st.write("🟢 System Idle. Waiting for User Query.")
    elif st.session_state.phase == "PROPOSAL":
        st.write("🟠 Graph Suspended at Breakpoint (`interrupt_before=['researcher']`). Awaiting Human Approval.")
    elif st.session_state.phase == "COMPLETED":
        st.write("🟢 Workflow Executed Successfully. State Reducer `operator.add` Synced.")

# --- PHASE 1: USER INPUT LAYER ---
if st.session_state.phase == "INPUT":
    st.subheader("🔍 Initiate Deep Research Engine")
    user_query = st.text_input("Enter the core research topic:", placeholder="e.g., Deep Learning Architecture, Autonomous Vehicles...")
    
    if st.button("Generate Research Proposal", type="primary"):
        if user_query.strip() == "":
            st.error("Please enter a valid topic before proceeding!")
        else:
            st.session_state.query = user_query
            
            with st.spinner("🧠 Orchestrator Node Active: Breaking topic into critical subtopics..."):
                # Initial execution - Trigger planner node and hit breakpoint before researcher
                graph.invoke({"query": st.session_state.query}, config=st.session_state.config)
            
            # Switch phase to prompt human approval
            st.session_state.phase = "PROPOSAL"
            st.rerun()

## --- PHASE 2: HUMAN-IN-THE-LOOP LAYER (BREAKPOINT PAUSE) ---
elif st.session_state.phase == "PROPOSAL":
    st.subheader("🚦 Human-in-the-Loop Intervention Gate")
    st.warning(f"The graph has paused before executing web searches on the topic: **{st.session_state.query}**")
    
    # Graph ka current snapshot aur proposed subtopics nikalna
    snapshot = graph.get_state(st.session_state.config)
    current_subtopics = snapshot.values.get("subtopics", [])
    
    st.markdown("### 🤖 Proposed Subtopics by AI Planner:")
    
    # DYNAMIC LAYOUT: Jitne subtopics hain, automatic utne hi columns banao!
    num_topics = len(current_subtopics) if len(current_subtopics) > 0 else 1
    cols = st.columns(num_topics)
    
    for idx, topic in enumerate(current_subtopics):
        with cols[idx]: # Ab ye kabhi out of range nahi hoga
            st.info(f"**Subtopic {idx+1}:** {topic}")
            
    st.markdown("---")
    st.markdown("### Do you approve this planning schema?")
    
    col_app, col_rej = st.columns([1, 4])
    
    # Scenario A: Approved
    with col_app:
        if st.button("Approve & Run", type="primary"):
            with st.spinner("🌐 Parallel Web Search & Analysis Nodes fired up... Writing final report..."):
                final_output = graph.invoke(None, config=st.session_state.config)
                st.session_state.report = final_output.get("report", "No report generated.")
                st.session_state.phase = "COMPLETED"
                st.rerun()
                
    # Scenario B: Rejected / Dynamic Modification
    with col_rej:
        with st.expander("❌ Reject & Provide Custom Subtopics"):
            st.write("Modify the subtopics manually to override the internal graph state:")
            custom_subs = []
            
            # Form bhi dynamically utne hi input box generate karega jitne topics hain
            for i in range(len(current_subtopics)):
                default_val = current_subtopics[i]
                val = st.text_input(f"Override Subtopic {i+1}:", value=default_val)
                custom_subs.append(val)
                
            if st.button("Update State & Force Execute"):
                with st.spinner("✍️ Overriding internal memory buffer... Resuming workflow..."):
                    graph.update_state(st.session_state.config, {"subtopics": custom_subs}, as_node="planner")
                    final_output = graph.invoke(None, config=st.session_state.config)
                    st.session_state.report = final_output.get("report", "No report generated.")
                    st.session_state.phase = "COMPLETED"
                    st.rerun()
# --- PHASE 3: REPORT VIEW & DOWNLOAD ---
elif st.session_state.phase == "COMPLETED":
    st.subheader(f"📊 Final Structured Research Report: {st.session_state.query}")
    
    # Markdown rendering engine inside streamlit
    st.markdown(st.session_state.report)
    st.markdown("---")
    
    col_reset, col_download = st.columns([1, 5])
    with col_reset:
        if st.button("Start New Session"):
            # Session wipeout for fresh memory thread
            st.session_state.clear()
            st.rerun()
            
    with col_download:
        # User direct report text file/markdown format me download kar sake
        st.download_button(
            label="📥 Download Report as Markdown File",
            data=st.session_state.report,
            file_name=f"Research_Report_{st.session_state.query.replace(' ', '_')}.md",
            mime="text/markdown"
        )