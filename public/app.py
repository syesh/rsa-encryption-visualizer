# -*- coding: utf-8 -*-
import streamlit as st
import math
import sys
import io
import time

# Force UTF-8 stdout/stderr so emoji never crash on Windows terminals (safely guarded for WebAssembly/stlite)
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
# MODERN DESIGN SYSTEM & CUSTOM CSS
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* Base Font & Page Styling */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background-color: #090d16;
    color: #f1f5f9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #0f172a !important;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header Banner */
.exp-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311b92 100%);
    padding: 32px 36px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
    margin-bottom: 24px;
    text-align: left;
}

.exp-header h1 {
    font-size: 30px;
    font-weight: 800;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
    background: linear-gradient(90deg, #818cf8, #c084fc, #e879f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.exp-header p {
    color: #94a3b8;
    font-size: 15px;
    margin: 0;
    line-height: 1.5;
}

/* Container & Card Customizations */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #111827;
    border: 1px solid #1f2937 !important;
    border-radius: 16px !important;
    padding: 24px !important;
    margin-bottom: 16px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    transition: border-color 0.2s ease-in-out;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #374151 !important;
}

/* Section Headings */
.section-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 8px;
}

.badge-blue { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
.badge-purple { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }
.badge-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
.badge-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }

.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.card-desc {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 20px;
    line-height: 1.6;
}

/* Metric Cards */
div[data-testid="stMetric"] {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 14px 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

div[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 22px !important;
    font-weight: 700 !important;
}

/* Code & Formula Displays */
.highlight-box {
    background: #0f172a;
    border-left: 4px solid #3b82f6;
    border-radius: 8px;
    padding: 14px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    margin: 12px 0;
    color: #f1f5f9;
    word-break: break-all;
}

.highlight-box-dec {
    background: #0f172a;
    border-left: 4px solid #10b981;
    border-radius: 8px;
    padding: 14px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    margin: 12px 0;
    color: #f1f5f9;
    word-break: break-all;
}

.key-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 6px 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #38bdf8;
}

/* Pipeline Flow Visualizer */
.pipeline-container {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    background: #0f172a;
    border: 1px solid #1f2937;
    border-radius: 14px;
    padding: 16px 20px;
    margin: 16px 0 24px 0;
}

.pipeline-node {
    flex: 1;
    min-width: 140px;
    text-align: center;
    padding: 10px 14px;
    border-radius: 10px;
    background: #1e293b;
    color: #94a3b8;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #334155;
}

.pipeline-node.active {
    background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
    color: #ffffff;
    border-color: #60a5fa;
    box-shadow: 0 0 16px rgba(59, 130, 246, 0.35);
}

.pipeline-arrow {
    color: #475569;
    font-size: 18px;
    font-weight: bold;
    user-select: none;
}

/* Button Refinement */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.2s ease !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
    border: none !important;
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35) !important;
}

.stButton > button[kind="primary"]:hover {
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
    transform: translateY(-1px);
}

/* Spacing Helpers */
.spacer-sm { height: 12px; }
.spacer-md { height: 24px; }
.spacer-lg { height: 36px; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPER MATHEMATICAL FUNCTIONS
# ============================================================

def is_prime(number):
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
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def modular_inverse(e, phi):
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi


# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "1. Key Setup 🔑"

if "p" not in st.session_state:
    st.session_state.p = 61
if "q" not in st.session_state:
    st.session_state.q = 53
if "e" not in st.session_state:
    st.session_state.e = 17

if "message" not in st.session_state:
    st.session_state.message = "HELLO RSA"
if "step_idx" not in st.session_state:
    st.session_state.step_idx = 0
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False


# Derive active parameters
p_val, q_val, e_val = st.session_state.p, st.session_state.q, st.session_state.e
n_val = p_val * q_val
phi_val = (p_val - 1) * (q_val - 1)
d_val = modular_inverse(e_val, phi_val)


# ============================================================
# SIDEBAR OPTIMIZATION & CONFIGURATION
# ============================================================

with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
        <span style="font-size: 26px;">🔐</span>
        <span style="font-size: 20px; font-weight: 800; color: #f8fafc;">RSA Lab Config</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Configure global key parameters, quick presets, and inspect active cryptographic state.")
    
    st.divider()

    with st.container(border=True):
        st.markdown('<div class="section-badge badge-blue">Key Configuration</div>', unsafe_allow_html=True)
        st.markdown("<div style='font-size: 15px; font-weight: 700; color: #f8fafc; margin-bottom: 12px;'>Prime Parameters</div>", unsafe_allow_html=True)
        
        p_in = st.number_input("Prime p", min_value=2, value=st.session_state.p, step=1, help="Must be a prime number")
        q_in = st.number_input("Prime q", min_value=2, value=st.session_state.q, step=1, help="Must be a prime number distinct from p")
        e_in = st.number_input("Public Exponent e", min_value=2, value=st.session_state.e, step=1, help="Must be coprime to φ(n)")

        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

        if st.button("⚡ Update RSA Keys", type="primary", use_container_width=True):
            if not is_prime(p_in):
                st.error("p must be a prime number.")
            elif not is_prime(q_in):
                st.error("q must be a prime number.")
            elif p_in == q_in:
                st.error("p and q must be distinct.")
            else:
                n_check = p_in * q_in
                phi_check = (p_in - 1) * (q_in - 1)
                if gcd(e_in, phi_check) != 1:
                    st.error("e must be coprime to φ(n).")
                else:
                    d_check = modular_inverse(e_in, phi_check)
                    if d_check is None:
                        st.error("Modular inverse does not exist.")
                    else:
                        st.session_state.p = p_in
                        st.session_state.q = q_in
                        st.session_state.e = e_in
                        st.session_state.step_idx = 0
                        st.success("✅ Keys updated!")
                        st.rerun()

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown('<div class="section-badge badge-purple">Quick Presets</div>', unsafe_allow_html=True)
        st.markdown("<div style='font-size: 15px; font-weight: 700; color: #f8fafc; margin-bottom: 12px;'>Load Sample Keys</div>", unsafe_allow_html=True)
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            if st.button("🎲 Small\n(11, 13)", use_container_width=True):
                st.session_state.p = 11
                st.session_state.q = 13
                st.session_state.e = 7
                st.session_state.step_idx = 0
                st.rerun()
        with col_p2:
            if st.button("🚀 Standard\n(61, 53)", use_container_width=True):
                st.session_state.p = 61
                st.session_state.q = 53
                st.session_state.e = 17
                st.session_state.step_idx = 0
                st.rerun()

    st.divider()

    with st.container(border=True):
        st.markdown('<div class="section-badge badge-emerald">Active State</div>', unsafe_allow_html=True)
        st.markdown("<div style='font-size: 15px; font-weight: 700; color: #f8fafc; margin-bottom: 12px;'>Current RSA Keys</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Modulus n:</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #38bdf8;">{n_val}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Totient φ(n):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #38bdf8;">{phi_val}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Public Key (e, n):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #60a5fa;">({e_val}, {n_val})</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">Private Key (d, n):</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #34d399;">({d_val}, {n_val})</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# MAIN PANEL HEADER
# ============================================================

st.markdown("""
<div class="exp-header">
    <h1>🔐 RSA Cryptography Guided Experience</h1>
    <p>A high-precision visual laboratory for understanding asymmetric RSA key generation, encryption, decryption, and protocol flow</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# STEP NAVIGATION
# ============================================================

tabs = ["1. Key Setup 🔑", "2. Message & Encrypt 💬", "3. Interactive Stepper 🧪", "4. Full Summary Matrix 📊"]

selected_tab = st.radio(
    "Experience Step:",
    options=tabs,
    index=tabs.index(st.session_state.current_tab) if st.session_state.current_tab in tabs else 0,
    horizontal=True,
    label_visibility="collapsed"
)

st.session_state.current_tab = selected_tab
st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)


# ============================================================
# STEP 1: KEY SETUP & PARAMETERS
# ============================================================

if selected_tab == "1. Key Setup 🔑":
    with st.container(border=True):
        st.markdown('<div class="section-badge badge-blue">Step 1 of 4</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🔑 RSA Key Generation & Derivation</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            RSA asymmetric cryptography relies on the mathematical trapdoor function of factoring the product of two large prime numbers.
            Derive key parameters by defining prime numbers <b>p</b> and <b>q</b>, and validating the coprime public exponent <b>e</b>.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("##### Active Parameter Overview")
        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Prime Inputs (p, q)", f"{p_val}, {q_val}")
        k2.metric("Modulus n (p × q)", f"{n_val}")
        k3.metric("Euler Totient φ(n)", f"{phi_val}")
        k4.metric("Private Exponent d", f"{d_val}")

        st.divider()

        st.markdown("##### Mathematical Derivation & Verification")
        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

        col_math1, col_math2 = st.columns([3, 2])

        with col_math1:
            st.markdown("""
            **Key Derivation Steps:**
            1. **Modulus Computation:** $n = p \\times q = {p_val} \\times {q_val} = {n_val}$
            2. **Euler's Totient:** $\\phi(n) = (p-1)(q-1) = ({p_val}-1)({q_val}-1) = {phi_val}$
            3. **Public Exponent:** Choose $e$ such that $1 < e < \\phi(n)$ and $\\gcd(e, \\phi(n)) = 1$. Selected: **{e_val}**
            4. **Private Exponent:** $d \\equiv e^{{-1}} \\pmod{{\\phi(n)}}$. Computed $d = \\mathbf{{{d_val}}}$
            """.format(p_val=p_val, q_val=q_val, n_val=n_val, phi_val=phi_val, e_val=e_val, d_val=d_val))

            st.latex(rf"e \cdot d = {e_val} \cdot {d_val} = {e_val * d_val} \equiv 1 \pmod{{{phi_val}}}")

        with col_math2:
            with st.container(border=True):
                st.markdown('<div class="section-badge badge-purple">Generated Key Pairs</div>', unsafe_allow_html=True)
                st.markdown("<div style='font-size: 14px; font-weight: 700; color: #f8fafc;'>Public Key (Shared)</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="highlight-box" style="border-left-color: #60a5fa; color: #60a5fa;">(e = {e_val}, n = {n_val})</div>', unsafe_allow_html=True)
                
                st.markdown("<div style='font-size: 14px; font-weight: 700; color: #f8fafc; margin-top: 12px;'>Private Key (Secret)</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="highlight-box-dec">(d = {d_val}, n = {n_val})</div>', unsafe_allow_html=True)

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
    _, nav_col = st.columns([3, 1])
    with nav_col:
        if st.button("Next: Message & Encrypt ➔", type="primary", use_container_width=True):
            st.session_state.current_tab = "2. Message & Encrypt 💬"
            st.rerun()


# ============================================================
# STEP 2: MESSAGE INPUT & ENCRYPTION OVERVIEW
# ============================================================

elif selected_tab == "2. Message & Encrypt 💬":
    with st.container(border=True):
        st.markdown('<div class="section-badge badge-purple">Step 2 of 4</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💬 Plaintext Message & RSA Encryption</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            Specify the message to be encrypted by the Sender. Each character is converted to its ASCII code <b>m</b> and encrypted into ciphertext integer <b>c</b> using the recipient's Public Key <b>(e, n)</b>.
        </div>
        """, unsafe_allow_html=True)

        col_in1, col_in2 = st.columns([3, 1])
        with col_in1:
            msg_in = st.text_input("Plaintext Message", value=st.session_state.message, help="Enter message string")
            if msg_in != st.session_state.message:
                st.session_state.message = msg_in
                st.session_state.step_idx = 0
                st.rerun()
        with col_in2:
            st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
            st.metric("Message Length", f"{len(st.session_state.message)} chars")

        if not st.session_state.message:
            st.warning("⚠️ Please enter a message above to proceed.")
            st.stop()

        # Pre-calculate steps
        msg_text = st.session_state.message
        calc_steps = []
        for idx, char in enumerate(msg_text):
            ascii_v = ord(char)
            if ascii_v >= n_val:
                st.error(f"❌ Character '{char}' (ASCII {ascii_v}) exceeds RSA modulus n ({n_val}). Please select larger prime values in the sidebar!")
                st.stop()
            c_v = pow(ascii_v, e_val, n_val)
            d_ascii = pow(c_v, d_val, n_val)
            calc_steps.append({
                "char": char,
                "ascii": ascii_v,
                "cipher": c_v,
                "dec_ascii": d_ascii,
                "dec_char": chr(d_ascii)
            })

        st.divider()

        st.markdown("##### Encryption & Network Payload Summary")
        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

        col_enc1, col_enc2 = st.columns(2)

        with col_enc1:
            with st.container(border=True):
                st.markdown('<div class="section-badge badge-blue">👤 Sender Terminal</div>', unsafe_allow_html=True)
                st.markdown(f"**Public Key Used:** `(e = {e_val}, n = {n_val})`", unsafe_allow_html=True)
                st.markdown(f"**Original Text:** `\"{msg_text}\"`")
                st.markdown("**ASCII Numerical Values (m):**")
                st.markdown(f'<div class="highlight-box">{[s["ascii"] for s in calc_steps]}</div>', unsafe_allow_html=True)

        with col_enc2:
            with st.container(border=True):
                st.markdown('<div class="section-badge badge-purple">🔒 Transmitted Ciphertext</div>', unsafe_allow_html=True)
                st.markdown(f"**Encryption Function:** $c = m^e \\bmod n$", unsafe_allow_html=True)
                st.markdown("**Ciphertext Integers Payload (c):**")
                st.markdown(f'<div class="highlight-box" style="border-left-color: #c084fc; color: #c084fc;">{[s["cipher"] for s in calc_steps]}</div>', unsafe_allow_html=True)

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
    p_col1, p_col2 = st.columns([1, 1])
    with p_col1:
        if st.button("⏮ Back: Key Setup", use_container_width=True):
            st.session_state.current_tab = "1. Key Setup 🔑"
            st.rerun()
    with p_col2:
        if st.button("Next: Interactive Stepper ➔", type="primary", use_container_width=True):
            st.session_state.current_tab = "3. Interactive Stepper 🧪"
            st.rerun()


# ============================================================
# STEP 3: INTERACTIVE STEPPER & PIPELINE VISUALIZER
# ============================================================

elif selected_tab == "3. Interactive Stepper 🧪":
    with st.container(border=True):
        st.markdown('<div class="section-badge badge-emerald">Step 3 of 4</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🧪 Step-by-Step Interactive Laboratory</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            Step through each character transformation in real time to observe the dual terminal operation. Sender computes modular exponentiation for encryption, while Receiver performs decryption with secret $d$.
        </div>
        """, unsafe_allow_html=True)

        msg_text = st.session_state.message
        if not msg_text:
            st.warning("⚠️ Please enter a message in Step 2.")
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

        # Control Toolbar
        ctl1, ctl2, ctl3, ctl4 = st.columns([1, 1, 1, 1])
        with ctl1:
            if st.button("◀ Prev Char", use_container_width=True, disabled=(st.session_state.step_idx == 0)):
                st.session_state.step_idx -= 1
                st.session_state.is_playing = False
                st.rerun()
        with ctl2:
            if st.button("Next Char ▶", use_container_width=True, disabled=(st.session_state.step_idx == total_steps - 1)):
                st.session_state.step_idx += 1
                st.session_state.is_playing = False
                st.rerun()
        with ctl3:
            play_label = "⏸ Pause" if st.session_state.is_playing else "⏯ Auto Play"
            if st.button(play_label, type="primary", use_container_width=True):
                st.session_state.is_playing = not st.session_state.is_playing
                st.rerun()
        with ctl4:
            if st.button("🔄 Restart", use_container_width=True):
                st.session_state.step_idx = 0
                st.session_state.is_playing = False
                st.rerun()

        st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
        st.progress((st.session_state.step_idx + 1) / total_steps, text=f"Character {st.session_state.step_idx + 1} of {total_steps}: '{cur_s['char']}'")

        # Pipeline Flow Diagram
        st.markdown(f"""
        <div class="pipeline-container">
            <div class="pipeline-node active">1. Input: '{cur_s['char']}'</div>
            <div class="pipeline-arrow">➔</div>
            <div class="pipeline-node active">2. ASCII: {cur_s['ascii']}</div>
            <div class="pipeline-arrow">➔</div>
            <div class="pipeline-node active">3. Encrypt (c={cur_s['cipher']})</div>
            <div class="pipeline-arrow">➔</div>
            <div class="pipeline-node active">4. Decrypt (m={cur_s['dec_ascii']})</div>
            <div class="pipeline-arrow">➔</div>
            <div class="pipeline-node active">5. Output: '{cur_s['dec_char']}'</div>
        </div>
        """, unsafe_allow_html=True)

        # Workstation Terminals
        work_left, work_right = st.columns(2)

        with work_left:
            with st.container(border=True):
                st.markdown('<div class="section-badge badge-blue">👤 Sender Workstation</div>', unsafe_allow_html=True)
                st.markdown(f"**Active Character:** <b style='font-size: 20px; color: #60a5fa;'>'{cur_s['char']}'</b> (Index {cur_s['idx']})", unsafe_allow_html=True)
                st.markdown(f"**Public Key:** `({e_val}, {n_val})`")
                
                st.markdown(f'<div class="highlight-box">ASCII Code: m = ord("{cur_s["char"]}") = <b>{cur_s["ascii"]}</b></div>', unsafe_allow_html=True)
                st.latex(rf"c = {cur_s['ascii']}^{{{e_val}}} \bmod {{{n_val}}} = \mathbf{{{cur_s['cipher']}}}")

                enc_stream = [s['cipher'] for s in steps_data[:st.session_state.step_idx + 1]]
                st.markdown(f"""
                <div style="background: #0f172a; padding: 12px; border-radius: 8px; margin-top: 10px;">
                    <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">TRANSMITTED CIPHERTEXT STREAM:</div>
                    <div style="font-family: 'JetBrains Mono', monospace; color: #60a5fa; font-weight: bold; margin-top: 4px;">{enc_stream}</div>
                </div>
                """, unsafe_allow_html=True)

        with work_right:
            with st.container(border=True):
                st.markdown('<div class="section-badge badge-emerald">👤 Receiver Workstation</div>', unsafe_allow_html=True)
                st.markdown(f"**Received Block:** <b style='font-size: 20px; color: #34d399;'>{cur_s['cipher']}</b> (Index {cur_s['idx']})", unsafe_allow_html=True)
                st.markdown(f"**Private Key:** `({d_val}, {n_val})`")

                st.markdown(f'<div class="highlight-box-dec">Decryption: m = c^d mod n</div>', unsafe_allow_html=True)
                st.latex(rf"m = {cur_s['cipher']}^{{{d_val}}} \bmod {{{n_val}}} = \mathbf{{{cur_s['dec_ascii']}}}")

                rec_stream = "".join([s['dec_char'] for s in steps_data[:st.session_state.step_idx + 1]])
                st.markdown(f"""
                <div style="background: #0f172a; padding: 12px; border-radius: 8px; margin-top: 10px;">
                    <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">RECOVERED MESSAGE STREAM:</div>
                    <div style="font-family: 'JetBrains Mono', monospace; color: #34d399; font-weight: bold; font-size: 18px; margin-top: 4px;">"{rec_stream}"</div>
                </div>
                """, unsafe_allow_html=True)

        # Auto-play loop handling
        if st.session_state.is_playing:
            if st.session_state.step_idx < total_steps - 1:
                time.sleep(1.0)
                st.session_state.step_idx += 1
                st.rerun()
            else:
                st.session_state.is_playing = False

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
    p_col1, p_col2 = st.columns([1, 1])
    with p_col1:
        if st.button("⏮ Back: Message & Encrypt", use_container_width=True):
            st.session_state.current_tab = "2. Message & Encrypt 💬"
            st.rerun()
    with p_col2:
        if st.button("Next: Full Summary Matrix ➔", type="primary", use_container_width=True):
            st.session_state.current_tab = "4. Full Summary Matrix 📊"
            st.rerun()


# ============================================================
# STEP 4: FULL SUMMARY MATRIX & VERIFICATION
# ============================================================

elif selected_tab == "4. Full Summary Matrix 📊":
    with st.container(border=True):
        st.markdown('<div class="section-badge badge-amber">Step 4 of 4</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">📊 Complete Transformation Matrix & Integrity Verification</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-desc">
            Review the complete character-by-character transformation table across the full encryption-decryption lifecycle to verify plaintext recovery.
        </div>
        """, unsafe_allow_html=True)

        msg_text = st.session_state.message
        if not msg_text:
            st.warning("⚠️ No message entered.")
            st.stop()

        summary_rows = []
        for idx, char in enumerate(msg_text):
            ascii_v = ord(char)
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

        st.dataframe(summary_rows, use_container_width=True, hide_index=True)

        st.divider()

        recovered_full = "".join([r['Recovered Char'].strip("'") for r in summary_rows])

        if recovered_full == msg_text:
            st.success(f"🎉 **Message Integrity Verified:** The recovered string `\"{recovered_full}\"` matches the original plaintext `\"{msg_text}\"` exactly!")
        else:
            st.error("❌ Integrity check failed.")

    st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)
    p_col1, p_col2 = st.columns([1, 1])
    with p_col1:
        if st.button("⏮ Back: Interactive Stepper", use_container_width=True):
            st.session_state.current_tab = "3. Interactive Stepper 🧪"
            st.rerun()
    with p_col2:
        if st.button("🔄 Restart Experience", type="primary", use_container_width=True):
            st.session_state.current_tab = "1. Key Setup 🔑"
            st.session_state.step_idx = 0
            st.rerun()


# Footer
st.divider()
st.caption("🔐 RSA Cryptography Guided Experience | Production-Ready UI/UX Layout")
