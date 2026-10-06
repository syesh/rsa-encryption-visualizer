# -*- coding: utf-8 -*-
import streamlit as st
import math
import sys
import io
import time

# Force UTF-8 stdout/stderr for cross-platform terminal compatibility
if hasattr(sys.stdout, "buffer") and (sys.stdout.encoding is None or sys.stdout.encoding.lower() != "utf-8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and (sys.stderr.encoding is None or sys.stderr.encoding.lower() != "utf-8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="RSA Cryptography Guided Lab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# MODERN DARK SAAS DESIGN SYSTEM
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
  --bg-app: #0b0f19;
  --bg-card: #151d2a;
  --border-color: #232f45;
  --border-color-hover: #374763;
  --text-main: #f8fafc;
  --text-muted: #cbd5e1;
  --text-subtle: #94a3b8;
  --primary-accent: #6366f1;
  --primary-hover: #4f46e5;
}

/* Global Font & Dark Background */
html, body, [class*="css"], [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: var(--bg-app) !important;
    color: var(--text-main) !important;
}

.stApp {
    background-color: var(--bg-app) !important;
    color: var(--text-main) !important;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* Sidebar Customization (Dark Slate) */
section[data-testid="stSidebar"] {
    background-color: #0d1320 !important;
    border-right: 1px solid var(--border-color) !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Header Banner - Sleek Dark Indigo Gradient Card */
.exp-header {
    background: linear-gradient(135deg, #1e1b4b 0%, #311b92 50%, #151d2a 100%);
    border: 1px solid rgba(129, 140, 248, 0.25);
    border-radius: 16px;
    padding: 26px 30px;
    margin-bottom: 22px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
}

.exp-header h1 {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.025em;
    color: #ffffff !important;
    margin: 0 0 6px 0;
    display: flex;
    align-items: center;
    gap: 12px;
}

.exp-header p {
    color: #a5b4fc !important;
    font-size: 14px;
    line-height: 1.6;
    margin: 0;
}

/* Dark Soft Badges */
.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.badge-indigo {
    background: rgba(99, 102, 241, 0.15);
    color: #818cf8 !important;
    border: 1px solid rgba(129, 140, 248, 0.3);
}

.badge-emerald {
    background: rgba(16, 185, 129, 0.15);
    color: #34d399 !important;
    border: 1px solid rgba(52, 211, 153, 0.3);
}

.badge-purple {
    background: rgba(168, 85, 247, 0.15);
    color: #c084fc !important;
    border: 1px solid rgba(192, 132, 252, 0.3);
}

.badge-amber {
    background: rgba(245, 158, 11, 0.15);
    color: #fbbf24 !important;
    border: 1px solid rgba(251, 191, 36, 0.3);
}

/* Dark Surface Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #151d2a !important;
    border: 1px solid #232f45 !important;
    border-radius: 14px !important;
    padding: 22px 26px !important;
    margin-bottom: 16px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease-in-out;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #374763 !important;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.015em;
    color: #f8fafc !important;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.card-desc {
    color: #cbd5e1 !important;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 16px;
}

/* Metric Display Cards (Dark Surface) */
div[data-testid="stMetric"] {
    background: #0f172a !important;
    border: 1px solid #232f45 !important;
    border-radius: 12px !important;
    padding: 14px 16px !important;
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

div[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 20px !important;
    font-weight: 700 !important;
}

/* Form Controls (Inputs, Selectboxes, Dropdowns) */
div[data-baseweb="input"], 
div[data-baseweb="base-input"], 
div[data-baseweb="select"] > div,
input, textarea {
    background-color: #0f172a !important;
    border-color: #232f45 !important;
    color: #f8fafc !important;
    border-radius: 8px !important;
}

div[data-baseweb="popover"], div[role="listbox"], ul[role="listbox"] {
    background-color: #151d2a !important;
    border: 1px solid #232f45 !important;
    color: #f8fafc !important;
}

li[role="option"] {
    color: #f8fafc !important;
}

li[role="option"]:hover, li[aria-selected="true"] {
    background-color: #232f45 !important;
}

button[aria-label="Step up"], 
button[aria-label="Step down"] {
    background-color: #172033 !important;
    color: #cbd5e1 !important;
    border-color: #232f45 !important;
}

/* Expanders */
details[data-testid="stExpander"], div[data-testid="stExpander"] {
    background-color: #151d2a !important;
    border: 1px solid #232f45 !important;
    border-radius: 12px !important;
}

details[data-testid="stExpander"] summary, div[data-testid="stExpander"] summary {
    color: #f8fafc !important;
}

/* Tables & Dataframes */
div[data-testid="stDataFrame"], .stDataFrame, table {
    background-color: #0f172a !important;
    border-radius: 10px !important;
    border: 1px solid #232f45 !important;
}

div[data-testid="stDataFrame"] th, table th {
    background-color: #172033 !important;
    color: #f8fafc !important;
}

div[data-testid="stDataFrame"] td, table td {
    background-color: #0f172a !important;
    color: #cbd5e1 !important;
}

/* Alerts */
div[data-testid="stNotification"], .stAlert {
    background-color: #151d2a !important;
    border: 1px solid #232f45 !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
}

/* Code & Highlight Boxes (Dark Monospace) */
.code-box {
    background: #090d16;
    border: 1px solid #232f45;
    border-left: 4px solid #6366f1;
    border-radius: 10px;
    padding: 12px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    color: #818cf8;
    word-break: break-all;
    margin: 8px 0;
}

.code-box-dec {
    background: #090d16;
    border: 1px solid #232f45;
    border-left: 4px solid #10b981;
    border-radius: 10px;
    padding: 12px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    color: #34d399;
    word-break: break-all;
    margin: 8px 0;
}

/* Stepper Pipeline Flow Bar (Dark Cards) */
.pipeline-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    background: #090d16;
    border: 1px solid #232f45;
    border-radius: 14px;
    padding: 16px 20px;
    margin: 16px 0 20px 0;
}

.pipeline-step {
    flex: 1;
    text-align: center;
    padding: 10px 12px;
    border-radius: 10px;
    background: #151d2a;
    color: #94a3b8;
    font-size: 12px;
    font-weight: 600;
    border: 1px solid #232f45;
    transition: all 0.2s ease-in-out;
}

.pipeline-step.active {
    background: #4f46e5;
    color: #ffffff;
    border-color: #6366f1;
    box-shadow: 0 0 16px rgba(99, 102, 241, 0.4);
}

.pipeline-separator {
    color: #475569;
    font-size: 16px;
    font-weight: 700;
}

/* Dark Buttons */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 0.55rem 1.1rem !important;
    border: 1px solid #232f45 !important;
    background-color: #151d2a !important;
    color: #f8fafc !important;
    transition: all 0.15s ease-in-out !important;
}

.stButton > button:hover {
    background-color: #232f45 !important;
    border-color: #374763 !important;
    color: #ffffff !important;
}

.stButton > button[kind="primary"] {
    background-color: #4f46e5 !important;
    border-color: #6366f1 !important;
    color: #ffffff !important;
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35) !important;
}

.stButton > button[kind="primary"]:hover {
    background-color: #4338ca !important;
    border-color: #818cf8 !important;
}

/* Clean Native Streamlit Tabs Styling */
button[data-baseweb="tab"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #94a3b8 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 10px 18px !important;
    background-color: transparent !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #818cf8 !important;
    font-weight: 700 !important;
}

div[data-baseweb="tab-highlight"] {
    background-color: #6366f1 !important;
}

/* Micro Spacing Utilities */
.spacer-sm { height: 10px; }
.spacer-md { height: 18px; }
.spacer-lg { height: 26px; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPER MATHEMATICAL & CRYPTO FUNCTIONS
# ============================================================

def is_prime(number):
    """Check if number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def gcd(a, b):
    """Euclidean algorithm for Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean algorithm."""
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def modular_inverse(e, phi):
    """Modular multiplicative inverse d = e^-1 mod phi."""
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi

def find_coprimes(phi, limit=5):
    """Find valid candidate public exponents e coprime to phi(n)."""
    candidates = [3, 5, 7, 17, 257, 65537]
    valid = [e for e in candidates if e < phi and gcd(e, phi) == 1]
    if len(valid) < limit:
        for e in range(19, phi, 2):
            if gcd(e, phi) == 1 and e not in valid:
                valid.append(e)
            if len(valid) >= limit:
                break
    return valid


# ============================================================
# SESSION STATE INITIALIZATION & BULLETPROOF CALLBACKS
# ============================================================

if "p" not in st.session_state:
    st.session_state.p = 61
if "q" not in st.session_state:
    st.session_state.q = 53
if "e" not in st.session_state:
    st.session_state.e = 17

if "mp_p" not in st.session_state:
    st.session_state.mp_p = 61
if "mp_q" not in st.session_state:
    st.session_state.mp_q = 53
if "mp_e" not in st.session_state:
    st.session_state.mp_e = 17

if "message" not in st.session_state:
    st.session_state.message = "HELLO RSA"
if "msg_input" not in st.session_state:
    st.session_state.msg_input = "HELLO RSA"

if "step_idx" not in st.session_state:
    st.session_state.step_idx = 0
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False
if "play_speed" not in st.session_state:
    st.session_state.play_speed = 1.0


# Callbacks for instant, bug-free widget synchronization
def apply_preset(p, q, e):
    st.session_state.p = p
    st.session_state.q = q
    st.session_state.e = e
    st.session_state.mp_p = p
    st.session_state.mp_q = q
    st.session_state.mp_e = e
    st.session_state.step_idx = 0
    st.session_state.is_playing = False

def apply_msg_preset(msg):
    st.session_state.message = msg
    st.session_state.msg_input = msg
    st.session_state.step_idx = 0
    st.session_state.is_playing = False

def step_prev():
    if st.session_state.step_idx > 0:
        st.session_state.step_idx -= 1
    st.session_state.is_playing = False

def step_next(max_steps):
    if st.session_state.step_idx < max_steps - 1:
        st.session_state.step_idx += 1
    st.session_state.is_playing = False

def toggle_play(max_steps):
    if st.session_state.step_idx >= max_steps - 1:
        st.session_state.step_idx = 0
    st.session_state.is_playing = not st.session_state.is_playing

def step_restart():
    st.session_state.step_idx = 0
    st.session_state.is_playing = False


# Compute active crypto variables safely
p_val, q_val, e_val = st.session_state.p, st.session_state.q, st.session_state.e
n_val = p_val * q_val
phi_val = (p_val - 1) * (q_val - 1) if p_val > 1 and q_val > 1 else 0
d_val = modular_inverse(e_val, phi_val) if phi_val > 0 else None
bit_len = n_val.bit_length() if n_val > 0 else 0


# ============================================================
# SIDEBAR CONFIGURATION & ACTIVE STATE
# ============================================================

with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
        <span style="font-size: 24px;">🔐</span>
        <div>
            <div style="font-size: 16px; font-weight: 800; color: #f8fafc; letter-spacing: -0.015em;">RSA Lab Control</div>
            <div style="font-size: 12px; color: #94a3b8;">Cryptographic State</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    with st.container(border=True):
        st.markdown('<span class="badge-pill badge-indigo">Active State</span>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 12.5px; margin-top: 8px;">
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Primes (p, q):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #f8fafc;">{p_val}, {q_val}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Modulus n:</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #818cf8;">{n_val}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Totient φ(n):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #818cf8;">{phi_val}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Public Key (e, n):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #818cf8;">({e_val}, {n_val})</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Private Key (d, n):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #34d399;">({d_val if d_val else 'Invalid'}, {n_val})</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Bit Length:</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;">{bit_len} bits</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown('<span class="badge-pill badge-purple">Quick Presets</span>', unsafe_allow_html=True)
        st.markdown("<div style='font-size: 12.5px; font-weight: 700; color: #f8fafc; margin-top: 6px; margin-bottom: 8px;'>Load Key Preset</div>", unsafe_allow_html=True)
        
        c_pr1, c_pr2 = st.columns(2)
        with c_pr1:
            st.button("🎲 Small\n(11, 13)", use_container_width=True, key="sb_p1", on_click=apply_preset, args=(11, 13, 7))
        with c_pr2:
            st.button("🚀 Standard\n(61, 53)", use_container_width=True, key="sb_p2", on_click=apply_preset, args=(61, 53, 17))
        
        st.button("🛡️ Medium (101, 103, e=7)", use_container_width=True, key="sb_p3", on_click=apply_preset, args=(101, 103, 7))

    with st.expander("ℹ️ Security & Bit Size Note"):
        st.markdown(f"""
        **Educational RSA:**
        - Modulus: **{bit_len} bits** (`n = {n_val}`)
        - Production RSA: **2048 - 4096 bits** with OAEP.
        """)


# ============================================================
# MAIN PANEL HEADER
# ============================================================

st.markdown("""
<div class="exp-header">
    <h1>🔐 RSA Cryptography Guided Experience</h1>
    <p>An interactive visual laboratory for understanding asymmetric RSA key generation, public key encryption, network transmission, and private key decryption.</p>
    <div style="display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap;">
        <span class="badge-pill badge-indigo">Wasm Engine ⚡</span>
        <span class="badge-pill badge-purple">Textbook RSA 📖</span>
        <span class="badge-pill badge-emerald">Interactive Stepper 🧪</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# STEP TABS (CLEAN NATIVE STREAMLIT TABS)
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "🔑 1. Key Setup", 
    "💬 2. Message & Encrypt", 
    "🧪 3. Interactive Stepper", 
    "📊 4. Summary Matrix"
])


# ============================================================
# TAB 1: KEY SETUP & PARAMETER SETUP
# ============================================================

with tab1:
    with st.container(border=True):
        st.markdown('<span class="badge-pill badge-indigo">Step 1 of 4</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title" style="margin-top: 4px;">🔑 Key Generation & Parameter Setup</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            RSA asymmetric cryptography relies on factoring the product of two prime numbers.
            Define prime numbers <b>p</b> and <b>q</b> below to derive active public and private keys.
        </div>
        """, unsafe_allow_html=True)

        # Custom Prime Parameter Input Form
        with st.container(border=True):
            st.markdown('<span class="badge-pill badge-purple">⚙️ Parameter Configuration</span>', unsafe_allow_html=True)
            st.markdown("<div style='font-size: 13.5px; font-weight: 700; color: #f8fafc; margin-top: 6px; margin-bottom: 10px;'>Custom Prime Inputs</div>", unsafe_allow_html=True)

            col_p, col_q, col_e = st.columns(3)
            with col_p:
                main_p = st.number_input("Prime p", min_value=2, step=1, key="mp_p", help="First prime number p")
            with col_q:
                main_q = st.number_input("Prime q", min_value=2, step=1, key="mp_q", help="Second prime number q")
            with col_e:
                main_e = st.number_input("Public Exponent e", min_value=2, step=1, key="mp_e", help="Coprime exponent e")

            # Quick Prime Presets Toolbar
            st.markdown("<div style='font-size: 11.5px; font-weight: 700; color: #94a3b8; margin-top: 8px; margin-bottom: 4px;'>QUICK PRIME PRESETS</div>", unsafe_allow_html=True)
            q_cols = st.columns(5)
            with q_cols[0]:
                st.button("🎲 Small (11, 13)", use_container_width=True, key="mp_preset1", on_click=apply_preset, args=(11, 13, 7))
            with q_cols[1]:
                st.button("🚀 Standard (61, 53)", use_container_width=True, key="mp_preset2", on_click=apply_preset, args=(61, 53, 17))
            with q_cols[2]:
                st.button("🛡️ Medium (101, 103)", use_container_width=True, key="mp_preset3", on_click=apply_preset, args=(101, 103, 7))
            with q_cols[3]:
                st.button("⚡ Fast (137, 149)", use_container_width=True, key="mp_preset4", on_click=apply_preset, args=(137, 149, 7))
            with q_cols[4]:
                st.button("🔒 Large (257, 263)", use_container_width=True, key="mp_preset5", on_click=apply_preset, args=(257, 263, 65537))

            # Live Validation
            mp_is_p = is_prime(main_p)
            mq_is_p = is_prime(main_q)
            mphi = (main_p - 1) * (main_q - 1) if mp_is_p and mq_is_p and main_p != main_q else 0
            me_valid = mphi > 0 and gcd(main_e, mphi) == 1 and 1 < main_e < mphi

            if not mp_is_p:
                st.warning(f"⚠️ `p = {main_p}` is not a prime number.")
            elif not mq_is_p:
                st.warning(f"⚠️ `q = {main_q}` is not a prime number.")
            elif main_p == main_q:
                st.warning("⚠️ `p` and `q` must be distinct prime numbers.")
            elif mphi > 0 and not me_valid:
                m_coprimes = find_coprimes(mphi)
                st.warning(f"⚠️ Public exponent `e = {main_e}` is not coprime to φ(n) = {mphi}. Suggested e: {m_coprimes}")

            st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
            if st.button("⚡ Apply Custom RSA Prime Parameters", type="primary", use_container_width=True, key="mp_apply_btn"):
                if not mp_is_p:
                    st.error(f"p ({main_p}) must be prime.")
                elif not mq_is_p:
                    st.error(f"q ({main_q}) must be prime.")
                elif main_p == main_q:
                    st.error("p and q must be distinct.")
                elif gcd(main_e, mphi) != 1:
                    st.error(f"e ({main_e}) must be coprime to φ(n) ({mphi}).")
                elif main_e >= mphi:
                    st.error(f"e ({main_e}) must be less than φ(n).")
                else:
                    md_check = modular_inverse(main_e, mphi)
                    if md_check is None:
                        st.error("Modular inverse does not exist.")
                    else:
                        st.session_state.p = main_p
                        st.session_state.q = main_q
                        st.session_state.e = main_e
                        st.session_state.step_idx = 0
                        st.success("🎉 RSA Parameters Applied Successfully!")
                        st.rerun()

        st.divider()

        st.markdown("<div style='font-size: 14.5px; font-weight: 700; color: #f8fafc; margin-bottom: 10px;'>Active Parameter Derivation</div>", unsafe_allow_html=True)

        k1, k2, k3, k4, k5 = st.columns(5)
        k1.metric("Primes (p, q)", f"{p_val}, {q_val}")
        k2.metric("Modulus n", f"{n_val}")
        k3.metric("Totient φ(n)", f"{phi_val}")
        k4.metric("Public Exp e", f"{e_val}")
        k5.metric("Private Exp d", f"{d_val if d_val else 'Invalid'}")

        st.divider()

        col_math1, col_math2 = st.columns([3, 2])

        with col_math1:
            st.markdown(f"""
            **Step-by-Step Derivation:**
            1. **Modulus Computation:** 
               $$n = p \\times q = {p_val} \\times {q_val} = \\mathbf{{{n_val}}}$$
            2. **Euler's Totient:** 
               $$\\phi(n) = (p-1)(q-1) = ({p_val}-1)({q_val}-1) = \\mathbf{{{phi_val}}}$$
            3. **Public Exponent:** Selected **$e = {e_val}$** ($\\gcd(e, \\phi(n)) = 1$)
            4. **Private Exponent:** 
               $d \\equiv e^{{-1}} \\pmod{{\\phi(n)}} \\implies d = \\mathbf{{{d_val}}}$
            """)

            if d_val is not None:
                st.latex(rf"e \cdot d = {e_val} \cdot {d_val} = {e_val * d_val} \equiv 1 \pmod{{{phi_val}}}")

        with col_math2:
            with st.container(border=True):
                st.markdown('<span class="badge-pill badge-indigo">Generated Key Pairs</span>', unsafe_allow_html=True)
                st.markdown("<div style='font-size: 13px; font-weight: 700; color: #f8fafc; margin-top: 8px;'>Public Key (Shared Publicly)</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="code-box">(e = {e_val}, n = {n_val})</div>', unsafe_allow_html=True)
                
                st.markdown("<div style='font-size: 13px; font-weight: 700; color: #f8fafc; margin-top: 10px;'>Private Key (Kept Secret)</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="code-box-dec">(d = {d_val if d_val else "Invalid"}, n = {n_val})</div>', unsafe_allow_html=True)


# ============================================================
# TAB 2: MESSAGE INPUT & ENCRYPTION OVERVIEW
# ============================================================

with tab2:
    with st.container(border=True):
        st.markdown('<span class="badge-pill badge-purple">Step 2 of 4</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title" style="margin-top: 4px;">💬 Plaintext Message & RSA Encryption</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            Specify the message to be encrypted by the Sender. Each character is converted to its ASCII value <b>m</b> and encrypted into ciphertext integer <b>c</b> using Public Key <b>(e, n)</b>.
        </div>
        """, unsafe_allow_html=True)

        col_in1, col_in2 = st.columns([3, 1])
        with col_in1:
            msg_in = st.text_input("Plaintext Message Input", key="msg_input", help="Enter text message to encrypt")
            if msg_in != st.session_state.message:
                st.session_state.message = msg_in
                st.session_state.step_idx = 0

            st.markdown("<div style='font-size: 11.5px; font-weight: 700; color: #94a3b8; margin-top: 8px; margin-bottom: 4px;'>MESSAGE PRESETS</div>", unsafe_allow_html=True)
            p_c1, p_c2, p_c3, p_c4 = st.columns(4)
            with p_c1:
                st.button("💬 'HELLO RSA'", use_container_width=True, key="msg_p1", on_click=apply_msg_preset, args=("HELLO RSA",))
            with p_c2:
                st.button("💬 'CRYPTO 101'", use_container_width=True, key="msg_p2", on_click=apply_msg_preset, args=("CRYPTO 101",))
            with p_c3:
                st.button("💬 'TOP SECRET'", use_container_width=True, key="msg_p3", on_click=apply_msg_preset, args=("TOP SECRET",))
            with p_c4:
                st.button("💬 '42'", use_container_width=True, key="msg_p4", on_click=apply_msg_preset, args=("42",))

        with col_in2:
            st.metric("Message Length", f"{len(st.session_state.message)} chars")

        if not st.session_state.message:
            st.warning("⚠️ Please enter a plaintext message above to proceed.")
            st.stop()

        if d_val is None:
            st.error("❌ Invalid RSA Parameters! Please select valid primes in Step 1.")
            st.stop()

        # Calculate encryption pipeline steps
        msg_text = st.session_state.message
        calc_steps = []
        bound_error = False
        for idx, char in enumerate(msg_text):
            ascii_v = ord(char)
            if ascii_v >= n_val:
                st.error(f"❌ Character '{char}' (ASCII {ascii_v}) exceeds RSA modulus n ({n_val}). Select larger primes in Step 1.")
                bound_error = True
                break
            c_v = pow(ascii_v, e_val, n_val)
            d_ascii = pow(c_v, d_val, n_val)
            calc_steps.append({
                "char": char,
                "ascii": ascii_v,
                "cipher": c_v,
                "dec_ascii": d_ascii,
                "dec_char": chr(d_ascii)
            })

        if bound_error:
            st.stop()

        st.divider()

        st.markdown("##### Encryption & Transmitted Payload Summary")
        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

        col_enc1, col_enc2 = st.columns(2)

        with col_enc1:
            with st.container(border=True):
                st.markdown('<span class="badge-pill badge-indigo">👤 Sender Workstation</span>', unsafe_allow_html=True)
                st.markdown(f"**Public Key Used:** `(e = {e_val}, n = {n_val})`", unsafe_allow_html=True)
                st.markdown(f"**Plaintext String:** `\"{msg_text}\"`")
                st.markdown("**ASCII Numerical Representation Array (m):**")
                st.markdown(f'<div class="code-box">{[s["ascii"] for s in calc_steps]}</div>', unsafe_allow_html=True)

        with col_enc2:
            with st.container(border=True):
                st.markdown('<span class="badge-pill badge-purple">🔒 Transmitted Ciphertext Payload</span>', unsafe_allow_html=True)
                st.markdown(f"**Encryption Function:** $c = m^e \\bmod n$", unsafe_allow_html=True)
                st.markdown("**Ciphertext Integers Network Array (c):**")
                st.markdown(f'<div class="code-box" style="border-left-color: #c084fc; color: #c084fc;">{[s["cipher"] for s in calc_steps]}</div>', unsafe_allow_html=True)


# ============================================================
# TAB 3: INTERACTIVE STEPPER & PIPELINE VISUALIZER
# ============================================================

with tab3:
    with st.container(border=True):
        st.markdown('<span class="badge-pill badge-emerald">Step 3 of 4</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title" style="margin-top: 4px;">🧪 Step-by-Step Interactive Laboratory</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            Step character-by-character through the RSA encryption and decryption lifecycle. Observe real-time dual workstation execution: Sender performs modular exponentiation with $e$, while Receiver decrypts with private exponent $d$.
        </div>
        """, unsafe_allow_html=True)

        msg_text = st.session_state.message
        if not msg_text:
            st.warning("⚠️ Please enter a message in Step 2 to use the visual stepper.")
            st.stop()

        if d_val is None:
            st.error("❌ Invalid RSA Parameters! Please select valid primes in Step 1.")
            st.stop()

        steps_data = []
        for idx, char in enumerate(msg_text):
            ascii_v = ord(char)
            if ascii_v >= n_val:
                st.error(f"❌ Character '{char}' (ASCII {ascii_v}) >= n ({n_val}). Return to Step 1 for larger primes.")
                st.stop()
            c_v = pow(ascii_v, e_val, n_val)
            d_ascii = pow(c_v, d_val, n_val)
            steps_data.append({
                "idx": idx,
                "char": char,
                "ascii": ascii_v,
                "cipher": c_v,
                "dec_ascii": d_ascii,
                "dec_char": chr(d_ascii)
            })

        total_steps = len(steps_data)
        if st.session_state.step_idx >= total_steps:
            st.session_state.step_idx = total_steps - 1

        cur_s = steps_data[st.session_state.step_idx]

        # Control Toolbar & Playback Speed
        ctl1, ctl2, ctl3, ctl4, ctl5 = st.columns([1, 1, 1.2, 1, 1.2])
        with ctl1:
            st.button("◀ Prev Char", use_container_width=True, disabled=(st.session_state.step_idx == 0), key="btn_prev", on_click=step_prev)
        with ctl2:
            st.button("Next Char ▶", use_container_width=True, disabled=(st.session_state.step_idx == total_steps - 1), key="btn_next", on_click=step_next, args=(total_steps,))
        with ctl3:
            play_label = "⏸ Pause" if st.session_state.is_playing else "⏯ Auto Play"
            st.button(play_label, type="primary", use_container_width=True, key="btn_play", on_click=toggle_play, args=(total_steps,))
        with ctl4:
            st.button("🔄 Restart", use_container_width=True, key="btn_restart", on_click=step_restart)
        with ctl5:
            speed_choice = st.selectbox("Play Speed", options=[0.5, 1.0, 2.0], format_func=lambda x: f"{x}s / step", index=1, label_visibility="collapsed", key="sb_speed")
            st.session_state.play_speed = speed_choice

        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
        st.progress((st.session_state.step_idx + 1) / total_steps, text=f"Character {st.session_state.step_idx + 1} of {total_steps}: '{cur_s['char']}' (Index {cur_s['idx']})")

        # Visual Pipeline Flow Bar
        st.markdown(f"""
        <div class="pipeline-bar">
            <div class="pipeline-step active">1. Input: '{cur_s['char']}'</div>
            <div class="pipeline-separator">➔</div>
            <div class="pipeline-step active">2. ASCII: {cur_s['ascii']}</div>
            <div class="pipeline-separator">➔</div>
            <div class="pipeline-step active">3. Encrypt (c={cur_s['cipher']})</div>
            <div class="pipeline-separator">➔</div>
            <div class="pipeline-step active">4. Decrypt (m={cur_s['dec_ascii']})</div>
            <div class="pipeline-separator">➔</div>
            <div class="pipeline-step active">5. Output: '{cur_s['dec_char']}'</div>
        </div>
        """, unsafe_allow_html=True)

        # Dual Workstations (Sender & Receiver)
        work_left, work_right = st.columns(2)

        with work_left:
            with st.container(border=True):
                st.markdown('<span class="badge-pill badge-indigo">👤 Sender Workstation (Encryption)</span>', unsafe_allow_html=True)
                st.markdown(f"**Active Character:** <b style='font-size: 20px; color: #818cf8;'>'{cur_s['char']}'</b> (ASCII `m = {cur_s['ascii']}`)", unsafe_allow_html=True)
                st.markdown(f"**Public Key Used:** `(e = {e_val}, n = {n_val})`")
                
                st.markdown(f'<div class="code-box">Formula: c = m^e mod n<br>c = {cur_s["ascii"]}^{{{e_val}}} mod {n_val} = <b>{cur_s["cipher"]}</b></div>', unsafe_allow_html=True)
                st.latex(rf"c = {cur_s['ascii']}^{{{e_val}}} \bmod {{{n_val}}} = \mathbf{{{cur_s['cipher']}}}")

                enc_stream = [s['cipher'] for s in steps_data[:st.session_state.step_idx + 1]]
                st.markdown(f"""
                <div style="background: #090d16; border: 1px solid #232f45; border-radius: 10px; padding: 12px; margin-top: 10px;">
                    <div style="font-size: 11px; color: #94a3b8; font-weight: 700;">TRANSMITTED CIPHERTEXT NETWORK STREAM:</div>
                    <div style="font-family: 'JetBrains Mono', monospace; color: #818cf8; font-weight: 700; margin-top: 4px;">{enc_stream}</div>
                </div>
                """, unsafe_allow_html=True)

        with work_right:
            with st.container(border=True):
                st.markdown('<span class="badge-pill badge-emerald">👤 Receiver Workstation (Decryption)</span>', unsafe_allow_html=True)
                st.markdown(f"**Received Block:** <b style='font-size: 20px; color: #34d399;'>{cur_s['cipher']}</b> (Index {cur_s['idx']})", unsafe_allow_html=True)
                st.markdown(f"**Private Key Used:** `(d = {d_val}, n = {n_val})`")

                st.markdown(f'<div class="code-box-dec">Formula: m = c^d mod n<br>m = {cur_s["cipher"]}^{{{d_val}}} mod {n_val} = <b>{cur_s["dec_ascii"]}</b></div>', unsafe_allow_html=True)
                st.latex(rf"m = {cur_s['cipher']}^{{{d_val}}} \bmod {{{n_val}}} = \mathbf{{{cur_s['dec_ascii']}}}")

                rec_stream = "".join([s['dec_char'] for s in steps_data[:st.session_state.step_idx + 1]])
                st.markdown(f"""
                <div style="background: #090d16; border: 1px solid #232f45; border-radius: 10px; padding: 12px; margin-top: 10px;">
                    <div style="font-size: 11px; color: #34d399; font-weight: 700;">RECOVERED PLAINTEXT MESSAGE STREAM:</div>
                    <div style="font-family: 'JetBrains Mono', monospace; color: #34d399; font-weight: 700; font-size: 18px; margin-top: 4px;">"{rec_stream}"</div>
                </div>
                """, unsafe_allow_html=True)

        # Auto-play loop handling
        if st.session_state.is_playing:
            if st.session_state.step_idx < total_steps - 1:
                time.sleep(st.session_state.play_speed)
                st.session_state.step_idx += 1
                st.rerun()
            else:
                st.session_state.is_playing = False


# ============================================================
# TAB 4: FULL SUMMARY MATRIX & VERIFICATION
# ============================================================

with tab4:
    with st.container(border=True):
        st.markdown('<span class="badge-pill badge-amber">Step 4 of 4</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title" style="margin-top: 4px;">📊 Complete Transformation Matrix & Integrity Verification</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            Review the complete character-by-character transformation table across the full RSA encryption-decryption lifecycle to verify plaintext recovery.
        </div>
        """, unsafe_allow_html=True)

        msg_text = st.session_state.message
        if not msg_text:
            st.warning("⚠️ No plaintext message specified.")
            st.stop()

        if d_val is None:
            st.error("❌ Invalid RSA Parameters! Please select valid primes in Step 1.")
            st.stop()

        summary_rows = []
        bound_error = False
        for idx, char in enumerate(msg_text):
            ascii_v = ord(char)
            if ascii_v >= n_val:
                st.error(f"❌ Character '{char}' (ASCII {ascii_v}) >= n ({n_val}). Modulus n is too small!")
                bound_error = True
                break
            c_v = pow(ascii_v, e_val, n_val)
            d_ascii = pow(c_v, d_val, n_val)
            d_char = chr(d_ascii)
            summary_rows.append({
                "Char #": idx + 1,
                "Input Char": f"'{char}'",
                "ASCII (m)": ascii_v,
                "Ciphertext (c)": c_v,
                "Decrypted ASCII (m')": d_ascii,
                "Recovered Char": f"'{d_char}'"
            })

        if bound_error:
            st.stop()

        st.dataframe(summary_rows, use_container_width=True, hide_index=True)

        st.divider()

        recovered_full = "".join([r['Recovered Char'].strip("'") for r in summary_rows])

        if recovered_full == msg_text:
            st.success(f"🎉 **Message Integrity Verified:** The recovered plaintext `\"{recovered_full}\"` matches the original input `\"{msg_text}\"` exactly!")
        else:
            st.error("❌ Integrity Verification Failed: Decrypted string does not match original plaintext.")

        # Cryptographic stats
        s_c1, s_c2, s_c3, s_c4 = st.columns(4)
        s_c1.metric("Total Characters", f"{len(msg_text)}")
        s_c2.metric("Total Cipher Blocks", f"{len(summary_rows)}")
        s_c3.metric("Max Ciphertext Integer", f"{max([r['Ciphertext (c)'] for r in summary_rows])}")
        s_c4.metric("Integrity Status", "100% MATCH" if recovered_full == msg_text else "FAILED")


# ============================================================
# FOOTER
# ============================================================

st.divider()
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 13px; padding: 10px 0;">
    🔐 <b>RSA Cryptography Guided Experience & Visualizer</b> | Built with Python, Streamlit & WebAssembly
</div>
""", unsafe_allow_html=True)