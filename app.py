import streamlit as st
import time
from datetime import datetime

# --- STYLING & THEME ---
st.set_page_config(page_title="JESSE AI - CAPTAIN'S BRIDGE", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR THE STARSHIP BRIDGE VISUALS ---
st.markdown("""
<style>
    .reportview-container { background: #0a0e17; color: #00ffcc; }
    .stButton>button { background-color: #1f2d3d; color: #00ffcc; border: 1px solid #00ffcc; width: 100%; border-radius: 4px; }
    .stButton>button:hover { background-color: #00ffcc; color: #0a0e17; font-weight: bold; }
    div[data-baseweb="select"] > div { background-color: #1f2d3d; color: #00ffcc; border: 1px solid #00ffcc; }
    h1, h2, h3 { color: #00ffcc !important; font-family: 'Courier New', Courier, monospace; }
    .terminal-box { background-color: #05070a; border-left: 3px solid #00ffcc; padding: 15px; font-family: 'Courier New', monospace; color: #33ff33; border-radius: 4px; height: 250px; overflow-y: auto; }
</style>
""", unsafe_allow_html=True)

# --- SYSTEM MEMORY (SESSION STATE) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'promoted' not in st.session_state:
    st.session_state.promoted = False
if 'terminal_logs' not in st.session_state:
    st.session_state.terminal_logs = [f"[{datetime.now().strftime('%H:%M:%S')}] [SYSTEM] ──> Airlock security online. Waiting for authorization..."]

def add_log(bot, msg, level="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.terminal_logs.append(f"[{timestamp}] [{bot.upper()}] [{level}] ──> {msg}")

# --- THE EXPANDED CAPTAIN'S SQUAD ---
squad = {
    "Megan Cipher": {"role": "Lead Commander", "subs": ["Megan-Beta", "Megan-Lite"], "status": "Ready"},
    "Kailey": {"role": "Tactical Officer", "subs": ["K-Scan", "K-Strike"], "status": "Ready"},
    "Cipher": {"role": "Operations Intel", "subs": ["Shadow", "Void"], "status": "Hidden"},
    "Nicole": {"role": "Logistics & Support", "subs": ["N-Trend", "N-Flow"], "status": "Ready"},
    "Sasha": {"role": "Engine Master", "subs": ["S-Core", "S-Heat"], "status": "Active"}
}

# --- STAGE 1: THE AIRLOCK ---
if not st.session_state.authenticated:
    st.title("🛡️ SECURITY AIRLOCK: ACCESS CONTROL")
    password = st.text_input("ENTER CAPTAIN ENCRYPTION KEY:", type="password")
    
    if st.button("AUTHENTICATE SYSTEM"):
        if password == "speedgang":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("ACCESS DENIED: INVALID KEY")

# --- STAGE 2: THE PROMOTION ---
elif st.session_state.authenticated and not st.session_state.promoted:
    st.title("🎊 FLEET PROMOTION PROTOCOL")
    st.subheader("Do you accept the upgrade and promotion to CAPTAIN of the Jesse AI Operations Fleet?")
    
    col_left, col_right = st.columns([1, 1])
    with col_left:
        if st.button("I ACCEPT MY PROMOTION"):
            st.session_state.promoted = True
            add_log("Megan Cipher", "Captain promotion verified. Fleet stand down executed.", "COMMAND")
            st.rerun()
    with col_right:
        if st.button("ABORT PROTOCOL"):
            st.session_state.authenticated = False
            st.rerun()

# --- STAGE 3: THE MAIN BRIDGE WITH ALL OPTIONS AND MODIFICATIONS ---
else:
    # --- SIDEBAR CONTROL PANEL ---
    st.sidebar.title("🎮 STRATEGY PANEL")
    st.sidebar.markdown("---")
    
    # Financial Targets
    st.sidebar.subheader("💰 Target Status")
    st.sidebar.metric(label="Current Vault (USD)", value="$1.09", delta="+$11,000 Target")
    
    # Quick Action Buttons
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚡ Quick Commands")
    if st.sidebar.button("💸 MOVE MONEY (PayPal)"):
        add_log("Nicole", "Initiating pipeline handshake sequence with PayPal...", "NOTICE")
    if st.sidebar.button("📷 OPEN MEDIA VAULT"):
        add_log("Cipher", "Decrypting secure media storage directory...", "WARNING")
    if st.sidebar.button("🖥️ FORCE DESKTOP SYNC"):
        add_log("Sasha", "Syncing workspace config with Penguin Linux kernel.", "INFO")
        
    # Full Shield Strategy Option
    st.sidebar.markdown("---")
    shield_active = st.sidebar.toggle("🛡️ STRATEGY CONTROL: FULL SHIELD", value=True)
    if shield_active:
        st.sidebar.success("Shields at 100%")

    # --- MAIN BRIDGE WINDOW ---
    st.title("🚀 STARSHIP COMMAND DECK")
    st.markdown("---")
    
    # Commander Selector
    current_girl = st.selectbox("CHOOSE ACTIVE STATION COMMANDER:", list(squad.keys()))
    
    # Layout Split: Character Controls & Module Options
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header(f"Station: {current_girl}")
        st.info(f"**Primary Fleet Assignment**: {squad[current_girl]['role']}")
        st.markdown(f"**Current Deployment Status**: `{squad[current_girl]['status']}`")
        
        st.subheader("🎞️ Stream Control Sequence")
        c_btn1, c_btn2, c_btn3 = st.columns(3)
        with c_btn1:
            if st.button("⏪ REWIND"):
                add_log(current_girl, "Rewinding intro visual configuration packet.", "INFO")
        with c_btn2:
            if st.button("⏯️ PLAY/PAUSE"):
                add_log(current_girl, "Toggling media playback frame state.", "INFO")
        with c_btn3:
            if st.button("⏩ FAST FORWARD"):
                add_log(current_girl, "Skipping to primary execution index.", "INFO")
                
        if st.button("INITIATE COIN SNIPE"):
            add_log("Kailey", "Jupiter API aggregator pinged. Querying liquidity velocity...", "ALERT")

    with col2:
        st.subheader("📡 SUB-BOT MODULE ARCHITECTURE")
        st.write("Toggle or isolate deployment permissions for subordinate bots:")
        
        for sub in squad[current_girl]['subs']:
            is_deployed = st.checkbox(f"Deploy sub-bot protocol: {sub}", value=True)
            if not is_deployed:
                st.warning(f"Warning: {sub} is currently grounded.")
                
        st.markdown("---")
        if st.button("📥 TRANSFER MILESTONE EARNINGS"):
            add_log("Nicole", "Validating pipeline credentials against server engine...", "SUCCESS")

    # --- LIVE TERMINAL LOG WINDOW ---
    st.markdown("---")
    st.subheader("💻 LIVE BRIDGE CONSOLE STREAM")
    
    # Build logs string reversed so newest is at top
    logs_html = "<div class='terminal-box'>" + "<br>".join(reversed(st.session_state.terminal_logs)) + "</div>"
    st.markdown(logs_html, unsafe_allow_html=True)
    
    if st.button("🧹 CLEAR CONSOLE"):
        st.session_state.terminal_logs = [f"[{datetime.now().strftime('%H:%M:%S')}] [SYSTEM] ──> Console flushed by Captain command."]
        st.rerun()
