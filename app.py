# -*- coding: utf-8 -*-
import streamlit as st
import math
import sys
import io
import time

# Force UTF-8 stdout/stderr so emoji never crash on Windows terminals
if sys.stdout.encoding is None or sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ============================================================
# PAGE CONFIGURATION & SPACIOUS STYLING
# ============================================================

st.set_page_config(
    page_title="RSA Cryptography Guided Lab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium Spacious CSS Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.main {
    background-color: #0b0f19;
    color: #f1f5f9;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 5rem;
    max-width: 1150px;
}

/* Header Banner */
.exp-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311b92 100%);
    padding: 36px 40px;
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
    margin-bottom: 32px;
    text-align: center;
}

.exp-header h1 {
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
    background: linear-gradient(90deg, #818cf8, #c084fc, #e879f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.exp-header p {
    color: #94a3b8;
    font-size: 16px;
    margin: 0;
}

/* Spacious Step Navigation Cards */
.exp-card {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 32px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.section-desc {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 24px;
    line-height: 1.6;
}

/* Key Metric Cards */
.key-box {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 16px 20px;
    text-align: center;
}

.key-box-title {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.key-box-val {
    color: #38bdf8;
    font-size: 22px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 6px;
}

/* Side-by-Side Workstation Cards */
.panel-sender {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    border: 1px solid #3b82f6;
    border-radius: 18px;
    padding: 26px;
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.12);
}

.panel-receiver {
    background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
    border: 1px solid #10b981;
    border-radius: 18px;
    padding: 26px;
    box-shadow: 0 8px 24px rgba(16, 185, 129, 0.12);
}

.panel-head {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.highlight-box {
    background: #0f172a;
    border-left: 4px solid #3b82f6;
    border-radius: 10px;
    padding: 14px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    margin: 12px 0;
    color: #f1f5f9;
}

.highlight-box-dec {
    background: #0f172a;
    border-left: 4px solid #10b981;
    border-radius: 10px;
    padding: 14px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    margin: 12px 0;
    color: #f1f5f9;
}

/* Pipeline Flow */
.pipeline-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #0f172a;
    border: 1px solid #1f2937;
    border-radius: 18px;
    padding: 20px 24px;
    margin: 20px 0 28px 0;
}

.pipeline-node {
    text-align: center;
    padding: 12px 18px;
    border-radius: 12px;
    background: #1e293b;
    color: #94a3b8;
    font-size: 13px;
    font-weight: 600;
}

.pipeline-node.active {
    background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
    color: #ffffff;
    box-shadow: 0 0 16px rgba(59, 130, 246, 0.45);
}

.pipeline-arrow {
    color: #475569;
    font-size: 20px;
    font-weight: bold;
}
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


# ============================================================
# APP HEADER
# ============================================================

st.markdown("""
<div class="exp-header">
    <h1>🔐 RSA Cryptography Guided Experience</h1>
    <p>A step-by-step virtual laboratory for understanding RSA encryption, decryption, and key distribution</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION STEPS (EXPERIENCE ONE SECTION AT A TIME)
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
st.write("")
st.write("")


# Derive active parameters
p_val, q_val, e_val = st.session_state.p, st.session_state.q, st.session_state.e
n_val = p_val * q_val
phi_val = (p_val - 1) * (q_val - 1)
d_val = modular_inverse(e_val, phi_val)


# ============================================================
# STEP 1: KEY SETUP & PARAMETERS
# ============================================================

if selected_tab == "1. Key Setup 🔑":
    st.markdown("""
    <div class="exp-card">
        <div class="section-title">🔑 Step 1 — RSA Key Generation & Derivation</div>
        <div class="section-desc">
            RSA relies on the mathematical difficulty of factoring the product of two large prime numbers.
            Configure your prime numbers <b>p</b> and <b>q</b>, and choose a public exponent <b>e</b> coprime to <b>φ(n)</b>.
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        p_in = st.number_input("Prime p", min_value=2, value=st.session_state.p, step=1)
    with c2:
        q_in = st.number_input("Prime q", min_value=2, value=st.session_state.q, step=1)
    with c3:
        e_in = st.number_input("Public Exponent e", min_value=2, value=st.session_state.e, step=1)

    st.write("")
    b_col1, b_col2, b_col3 = st.columns([1, 1, 2])
    with b_col1:
        if st.button("🎲 Small Primes (p=11, q=13)", use_container_width=True):
            st.session_state.p = 11
            st.session_state.q = 13
            st.session_state.e = 7
            st.rerun()
    with b_col2:
        if st.button("🚀 Standard Primes (p=61, q=53)", use_container_width=True):
            st.session_state.p = 61
            st.session_state.q = 53
            st.session_state.e = 17
            st.rerun()
    with b_col3:
        if st.button("✨ Update RSA Keys", type="primary", use_container_width=True):
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
                        st.success("✅ RSA Keys successfully generated!")

    st.write("")
    st.write("")
    st.markdown("### Derived Key Parameters & Key Pairs")
    
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(f'<div class="key-box"><div class="key-box-title">Modulus n (p×q)</div><div class="key-box-val">{n_val}</div></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="key-box"><div class="key-box-title">Euler Totient φ(n)</div><div class="key-box-val">{phi_val}</div></div>', unsafe_allow_html=True)
    k3.markdown(f'<div class="key-box"><div class="key-box-title">🔓 Public Key (e, n)</div><div class="key-box-val" style="color:#60a5fa;">({e_val}, {n_val})</div></div>', unsafe_allow_html=True)
    k4.markdown(f'<div class="key-box"><div class="key-box-title">🔐 Private Key (d, n)</div><div class="key-box-val" style="color:#34d399;">({d_val}, {n_val})</div></div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    n_col1, n_col2 = st.columns([4, 1])
    with n_col2:
        if st.button("Next: Message & Encrypt ➔", type="primary", use_container_width=True):
            st.session_state.current_tab = "2. Message & Encrypt 💬"
            st.rerun()


# ============================================================
# STEP 2: MESSAGE INPUT & ENCRYPTION OVERVIEW
# ============================================================

elif selected_tab == "2. Message & Encrypt 💬":
    st.markdown("""
    <div class="exp-card">
        <div class="section-title">💬 Step 2 — Plaintext Message & RSA Encryption</div>
        <div class="section-desc">
            Enter the message you want the Sender to send securely to the Receiver. Each character is converted into its ASCII code <b>m</b>, and encrypted into ciphertext integer <b>c</b> using the Public Key <b>(e, n)</b>.
        </div>
    """, unsafe_allow_html=True)

    msg_in = st.text_input("Plaintext Message", value=st.session_state.message)
    if msg_in != st.session_state.message:
        st.session_state.message = msg_in
        st.session_state.step_idx = 0
        st.rerun()

    if not st.session_state.message:
        st.info("Please enter a message above.")
        st.stop()

    # Pre-calculate steps
    msg_text = st.session_state.message
    calc_steps = []
    for idx, char in enumerate(msg_text):
        ascii_v = ord(char)
        if ascii_v >= n_val:
            st.error(f"Character '{char}' (ASCII {ascii_v}) is >= n ({n_val}). Please select larger primes in Step 1!")
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

    st.write("")
    st.markdown("### Encryption Breakdown Summary")
    
    col_enc1, col_enc2 = st.columns(2)
    
    with col_enc1:
        st.markdown(f"""
        <div class="panel-sender">
            <div class="panel-head" style="color: #60a5fa;">
                <span>👤 Sender View</span>
                <span>Public Key: ({e_val}, {n_val})</span>
            </div>
            <div><b>Original Message:</b> "{msg_text}"</div>
            <div style="margin-top: 10px;"><b>ASCII Numerical Representation:</b></div>
            <div class="highlight-box">
                {[s['ascii'] for s in calc_steps]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_enc2:
        st.markdown(f"""
        <div class="panel-sender" style="border-color: #818cf8;">
            <div class="panel-head" style="color: #c084fc;">
                <span>🔒 Encrypted Ciphertext Payload</span>
                <span>c = m<sup>e</sup> mod n</span>
            </div>
            <div><b>Transmitted Network Payload:</b></div>
            <div class="highlight-box" style="border-left-color: #c084fc; color: #c084fc;">
                {[s['cipher'] for s in calc_steps]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
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
    st.markdown("""
    <div class="exp-card">
        <div class="section-title">🧪 Step 3 — Interactive Step-by-Step Visual Laboratory</div>
        <div class="section-desc">
            Inspect the exact character-by-character transformations occurring across the network. Step through each character or press <b>Auto Play</b> to see real-time encryption and decryption side-by-side.
        </div>
    """, unsafe_allow_html=True)

    msg_text = st.session_state.message
    if not msg_text:
        st.info("Please enter a message in Step 2.")
        st.stop()

    steps_data = []
    for idx, char in enumerate(msg_text):
        ascii_v = ord(char)
        if ascii_v >= n_val:
            st.error(f"Character '{char}' (ASCII {ascii_v}) >= n ({n_val}). Return to Step 1 for larger primes.")
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

    # Stepper Control Bar
    ctl1, ctl2, ctl3, ctl4 = st.columns(4)
    with ctl1:
        if st.button("◀ Previous Character", use_container_width=True, disabled=(st.session_state.step_idx == 0)):
            st.session_state.step_idx -= 1
            st.session_state.is_playing = False
            st.rerun()
    with ctl2:
        if st.button("Next Character ▶", use_container_width=True, disabled=(st.session_state.step_idx == total_steps - 1)):
            st.session_state.step_idx += 1
            st.session_state.is_playing = False
            st.rerun()
    with ctl3:
        play_label = "⏸ Pause" if st.session_state.is_playing else "⏯ Auto Play"
        if st.button(play_label, type="primary", use_container_width=True):
            st.session_state.is_playing = not st.session_state.is_playing
            st.rerun()
    with ctl4:
        if st.button("🔄 Restart Stepper", use_container_width=True):
            st.session_state.step_idx = 0
            st.session_state.is_playing = False
            st.rerun()

    st.write("")
    st.progress((st.session_state.step_idx + 1) / total_steps, text=f"Character {st.session_state.step_idx + 1} of {total_steps}: '{cur_s['char']}'")

    # Pipeline Diagram
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
        <div class="pipeline-node active">5. Recovered: '{cur_s['dec_char']}'</div>
    </div>
    """, unsafe_allow_html=True)

    # Side-by-Side Workstation
    work_left, work_right = st.columns(2)

    with work_left:
        st.markdown(f"""
        <div class="panel-sender">
            <div class="panel-head" style="color: #60a5fa;">
                <span>👤 Sender Terminal</span>
                <span>Public Key ({e_val}, {n_val})</span>
            </div>
            <div style="font-size: 16px; margin-bottom: 12px;">
                Active Character: <b style="color: #60a5fa; font-size: 20px;">'{cur_s['char']}'</b> (Index {cur_s['idx']})
            </div>
            <div class="highlight-box">
                ASCII Code: m = ord('{cur_s['char']}') = <b>{cur_s['ascii']}</b>
            </div>
            <div class="highlight-box">
                Formula: c = m<sup>e</sup> mod n
            </div>
        """, unsafe_allow_html=True)

        st.latex(rf"c = {cur_s['ascii']}^{{{e_val}}} \bmod {{{n_val}}} = \mathbf{{{cur_s['cipher']}}}")

        enc_stream = [s['cipher'] for s in steps_data[:st.session_state.step_idx + 1]]
        st.markdown(f"""
            <div style="margin-top: 14px; background: #0f172a; padding: 12px; border-radius: 10px;">
                <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">TRANSMITTED CIPHERTEXT STREAM:</div>
                <div style="font-family: 'JetBrains Mono', monospace; color: #60a5fa; font-weight: bold; margin-top: 4px;">
                    {enc_stream}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with work_right:
        st.markdown(f"""
        <div class="panel-receiver">
            <div class="panel-head" style="color: #34d399;">
                <span>👤 Receiver Terminal</span>
                <span>Private Key ({d_val}, {n_val})</span>
            </div>
            <div style="font-size: 16px; margin-bottom: 12px;">
                Received Block: <b style="color: #34d399; font-size: 20px;">{cur_s['cipher']}</b> (Index {cur_s['idx']})
            </div>
            <div class="highlight-box-dec">
                Formula: m = c<sup>d</sup> mod n
            </div>
        """, unsafe_allow_html=True)

        st.latex(rf"m = {cur_s['cipher']}^{{{d_val}}} \bmod {{{n_val}}} = \mathbf{{{cur_s['dec_ascii']}}}")

        rec_stream = "".join([s['dec_char'] for s in steps_data[:st.session_state.step_idx + 1]])
        st.markdown(f"""
            <div class="highlight-box-dec">
                ASCII Decode: chr({cur_s['dec_ascii']}) = <b>'{cur_s['dec_char']}'</b>
            </div>
            <div style="margin-top: 14px; background: #0f172a; padding: 12px; border-radius: 10px;">
                <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">RECOVERED MESSAGE STREAM:</div>
                <div style="font-family: 'JetBrains Mono', monospace; color: #34d399; font-weight: bold; font-size: 18px; margin-top: 4px;">
                    "{rec_stream}"
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Auto-play loop handling
    if st.session_state.is_playing:
        if st.session_state.step_idx < total_steps - 1:
            time.sleep(1.0)
            st.session_state.step_idx += 1
            st.rerun()
        else:
            st.session_state.is_playing = False

    st.write("")
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
    st.markdown("""
    <div class="exp-card">
        <div class="section-title">📊 Step 4 — Complete Transformation Matrix & Integrity Verification</div>
        <div class="section-desc">
            Review the end-to-end mathematical transformations for every character in your message, and verify message integrity.
        </div>
    """, unsafe_allow_html=True)

    msg_text = st.session_state.message
    if not msg_text:
        st.info("No message entered.")
        st.stop()

    summary_rows = []
    for idx, char in enumerate(msg_text):
        ascii_v = ord(char)
        c_v = pow(ascii_v, e_val, n_val)
        d_ascii = pow(c_v, d_val, n_val)
        d_char = chr(d_ascii)
        summary_rows.append({
            "Character #": idx + 1,
            "Input Character": f"'{char}'",
            "ASCII (m)": ascii_v,
            "Encrypted Ciphertext (c)": c_v,
            "Decrypted ASCII (m')": d_ascii,
            "Recovered Character": f"'{d_char}'"
        })

    st.dataframe(summary_rows, use_container_width=True)

    st.write("")
    recovered_full = "".join([r['Recovered Character'].strip("'") for r in summary_rows])

    if recovered_full == msg_text:
        st.success(f"🎉 **Message Integrity Verified:** The decrypted string `\"{recovered_full}\"` is identical to the original plaintext `\"{msg_text}\"`!")
    else:
        st.error("❌ Integrity check failed.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
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
st.markdown("---")
st.caption("🔐 RSA Cryptography Guided Experience | Built with Python + Streamlit")