# -*- coding: utf-8 -*-
import streamlit as st
import math
import sys
import io
 
# Force UTF-8 stdout/stderr so emoji in this file never crash the
# server on Windows terminals that default to cp1252.
if sys.stdout.encoding is None or sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
 
# ============================================================
# PAGE CONFIGURATION
# ============================================================
 
st.set_page_config(
    page_title="RSA Secure Chat Lab",
    page_icon="🔐",
    layout="wide"
)
 
# ============================================================
# CUSTOM CSS
# ============================================================
 
st.markdown("""
<style>
 
.main {
    background-color: #f5f7fb;
}
 
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}
 
.hero {
    background: linear-gradient(135deg, #111827, #1e3a8a);
    padding: 30px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
}
 
.hero h1 {
    font-size: 38px;
    margin-bottom: 5px;
}
 
.hero p {
    color: #dbeafe;
    font-size: 17px;
}
 
.card {
    background: white;
    color: #111827;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}
 
.card h3, .card p, .card b {
    color: #111827;
}
 
.step-card {
    background: #ffffff;
    color: #111827;
    padding: 18px;
    border-radius: 14px;
    border-left: 5px solid #2563eb;
    margin-bottom: 12px;
}
 
.sender {
    background: #eff6ff;
    color: #111827;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #bfdbfe;
}
 
.receiver {
    background: #f0fdf4;
    color: #111827;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #bbf7d0;
}
 
.arrow {
    text-align: center;
    font-size: 35px;
    padding-top: 30px;
}
 
.result-box {
    background: #111827;
    color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    font-family: monospace;
    font-size: 17px;
    word-wrap: break-word;
}
 
.formula {
    background: #f8fafc;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    margin: 8px 0;
}
 
</style>
""", unsafe_allow_html=True)
 
 
# ============================================================
# RSA FUNCTIONS
# ============================================================
 
def is_prime(number):
    """Check whether a number is prime."""
 
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
    """Calculate GCD."""
 
    while b:
        a, b = b, a % b
 
    return a
 
 
def extended_gcd(a, b):
    """Extended Euclidean Algorithm."""
 
    if a == 0:
        return b, 0, 1
 
    gcd_value, x1, y1 = extended_gcd(b % a, a)
 
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd_value, x, y
 
 
def modular_inverse(e, phi):
    """Find d such that (d * e) mod phi = 1."""
 
    gcd_value, x, _ = extended_gcd(e, phi)
 
    if gcd_value != 1:
        return None
 
    return x % phi
 
 
def generate_keys(p, q, e):
    """Generate RSA public and private keys."""
 
    n = p * q
 
    phi = (p - 1) * (q - 1)
 
    if gcd(e, phi) != 1:
        return None
 
    d = modular_inverse(e, phi)
 
    if d is None:
        return None
 
    return n, phi, d
 
 
def encrypt_message(message, e, n):
    """Encrypt every character using RSA."""
 
    encrypted = []
 
    for character in message:
 
        ascii_value = ord(character)
 
        if ascii_value >= n:
            return None
 
        encrypted_value = pow(ascii_value, e, n)
 
        encrypted.append(encrypted_value)
 
    return encrypted
 
 
def decrypt_message(ciphertext, d, n):
    """Decrypt RSA ciphertext."""
 
    decrypted = ""
 
    for value in ciphertext:
 
        ascii_value = pow(value, d, n)
 
        decrypted += chr(ascii_value)
 
    return decrypted
 
 
# ============================================================
# SESSION STATE
# ============================================================
 
if "keys_generated" not in st.session_state:
    st.session_state.keys_generated = False
 
if "encrypted" not in st.session_state:
    st.session_state.encrypted = None
 
if "decrypted" not in st.session_state:
    st.session_state.decrypted = None
 
 
# ============================================================
# HEADER
# ============================================================
 
st.markdown("""
<div class="hero">
 
<h1>🔐 RSA Secure Chat Laboratory</h1>
 
<p>
Interactive Virtual Laboratory for RSA Key Distribution
and Secure Message Communication
</p>
 
</div>
""", unsafe_allow_html=True)
 
 
st.info(
    "🎯 Objective: Demonstrate how RSA public-key cryptography "
    "can be used to distribute a key securely and protect messages "
    "between a sender and receiver."
)
 
 
# ============================================================
# SIDEBAR
# ============================================================
 
with st.sidebar:
 
    st.header("📚 Laboratory Guide")
 
    st.markdown("""
### Experiment Steps
 
**1. Key Generation**
 
Choose two prime numbers and generate RSA keys.
 
**2. Key Distribution**
 
The receiver shares the public key with the sender.
 
**3. Encryption**
 
The sender encrypts the message using the public key.
 
**4. Transmission**
 
The encrypted message travels through the network.
 
**5. Decryption**
 
The receiver uses the private key to recover the message.
 
---
 
### RSA Formulas
 
`n = p × q`
 
`φ(n) = (p−1)(q−1)`
 
`c = mᵉ mod n`
 
`m = cᵈ mod n`
""")
 
    st.divider()
 
    if st.button("🔄 Reset Laboratory", use_container_width=True):
 
        st.session_state.keys_generated = False
        st.session_state.encrypted = None
        st.session_state.decrypted = None
 
        st.rerun()
 
 
# ============================================================
# SECTION 1 — KEY GENERATION
# ============================================================
 
st.header("1️⃣ RSA Key Generation")
 
st.markdown(
    "The receiver generates a public key and a private key. "
    "The public key can be distributed, while the private key "
    "must remain secret."
)
 
col1, col2, col3 = st.columns(3)
 
with col1:
 
    p = st.number_input(
        "Prime number p",
        min_value=2,
        value=61,
        step=1
    )
 
with col2:
 
    q = st.number_input(
        "Prime number q",
        min_value=2,
        value=53,
        step=1
    )
 
with col3:
 
    e = st.number_input(
        "Public exponent e",
        min_value=2,
        value=17,
        step=1
    )
 
 
if st.button("🔑 Generate RSA Keys", type="primary"):
 
    p = int(p)
    q = int(q)
    e = int(e)
 
    if not is_prime(p):
 
        st.error("❌ p must be a prime number.")
 
    elif not is_prime(q):
 
        st.error("❌ q must be a prime number.")
 
    elif p == q:
 
        st.error("❌ p and q must be different.")
 
    else:
 
        n = p * q
        phi = (p - 1) * (q - 1)
 
        if gcd(e, phi) != 1:
 
            st.error(
                "❌ Invalid value of e. "
                "e must be relatively prime to φ(n)."
            )
 
        else:
 
            d = modular_inverse(e, phi)
 
            st.session_state.p = p
            st.session_state.q = q
            st.session_state.e = e
            st.session_state.n = n
            st.session_state.phi = phi
            st.session_state.d = d
            st.session_state.keys_generated = True
            st.session_state.encrypted = None
            st.session_state.decrypted = None
 
            st.success("✅ RSA keys generated successfully!")
 
 
# ============================================================
# DISPLAY GENERATED KEYS
# ============================================================
 
if st.session_state.keys_generated:
 
    st.subheader("📊 Generated RSA Parameters")
 
    c1, c2, c3, c4 = st.columns(4)
 
    c1.metric("p", st.session_state.p)
    c2.metric("q", st.session_state.q)
    c3.metric("n", st.session_state.n)
    c4.metric("φ(n)", st.session_state.phi)
 
    st.markdown("### 🔓 Public Key")
 
    st.code(
        f"Public Key = ({st.session_state.e}, {st.session_state.n})",
        language="text"
    )
 
    st.markdown("### 🔐 Private Key")
 
    st.code(
        f"Private Key = ({st.session_state.d}, {st.session_state.n})",
        language="text"
    )
 
    st.warning(
        "🔐 The private key must never be shared with other users."
    )
 
 
# ============================================================
# SECTION 2 — KEY DISTRIBUTION
# ============================================================
 
if st.session_state.keys_generated:
 
    st.header("2️⃣ RSA Key Distribution")
 
    st.markdown(
        "The receiver distributes only the public key to the sender. "
        "The private key stays with the receiver."
    )
 
    sender_col, arrow_col, receiver_col = st.columns([4, 1, 4])
 
    with sender_col:
 
        st.markdown("""
        <div class="sender">
 
        ### 👤 Sender
 
        The sender wants to communicate securely.
 
        **Receives:**
 
        🔓 Public Key
 
        </div>
        """, unsafe_allow_html=True)
 
    with arrow_col:
 
        st.markdown(
            '<div class="arrow">🔑<br>→</div>',
            unsafe_allow_html=True
        )
 
    with receiver_col:
 
        st.markdown("""
        <div class="receiver">
 
        ### 👤 Receiver
 
        The receiver generates the RSA key pair.
 
        **Keeps:**
 
        🔐 Private Key
 
        **Shares:**
 
        🔓 Public Key
 
        </div>
        """, unsafe_allow_html=True)
 
    st.success(
        f"🔓 Public Key Distributed → "
        f"({st.session_state.e}, {st.session_state.n})"
    )
 
 
# ============================================================
# SECTION 3 — SECURE CHAT
# ============================================================
 
if st.session_state.keys_generated:
 
    st.header("3️⃣ Secure Chat")
 
    message = st.text_area(
        "💬 Sender's Message",
        value="HELLO RSA",
        height=100,
        help="Enter the message that the sender wants to transmit securely."
    )
 
    encrypt_button = st.button(
        "🔒 Encrypt Message",
        type="primary"
    )
 
    if encrypt_button:
 
        if message.strip() == "":
 
            st.error("Please enter a message.")
 
        else:
 
            encrypted = encrypt_message(
                message,
                st.session_state.e,
                st.session_state.n
            )
 
            if encrypted is None:
 
                st.error(
                    "Message contains a character value larger than n. "
                    "Use larger prime numbers."
                )
 
            else:
 
                st.session_state.encrypted = encrypted
                st.session_state.decrypted = None
 
                st.success("✅ Message encrypted successfully!")
 
 
# ============================================================
# ENCRYPTION VISUALIZATION
# ============================================================
 
if (
    st.session_state.keys_generated
    and st.session_state.encrypted is not None
):
 
    st.subheader("🔒 Encryption Process")
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 1 — Plaintext</b>
 
    The sender starts with the original message.
 
    </div>
    """, unsafe_allow_html=True)
 
    st.code(
        message,
        language="text"
    )
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 2 — Character Conversion</b>
 
    Each character is converted into its ASCII numerical value.
 
    </div>
    """, unsafe_allow_html=True)
 
    ascii_values = [ord(char) for char in message]
 
    st.code(
        str(ascii_values),
        language="text"
    )
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 3 — RSA Encryption</b>
 
    Each numerical value is encrypted using the receiver's public key.
 
    </div>
    """, unsafe_allow_html=True)
 
    st.latex(
        r"c = m^e \mod n"
    )
 
    st.code(
        str(st.session_state.encrypted),
        language="text"
    )
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 4 — Secure Transmission</b>
 
    Only the encrypted ciphertext is transmitted through the network.
 
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown(
        '<div class="result-box">' +
        str(st.session_state.encrypted) +
        '</div>',
        unsafe_allow_html=True
    )
 
 
# ============================================================
# SECTION 4 — RECEIVER DECRYPTION
# ============================================================
 
if (
    st.session_state.keys_generated
    and st.session_state.encrypted is not None
):
 
    st.header("4️⃣ Receiver Decryption")
 
    st.markdown(
        "The receiver uses the private key to recover the original message."
    )
 
    decrypt_button = st.button(
        "🔓 Decrypt Message",
        type="primary"
    )
 
    if decrypt_button:
 
        decrypted = decrypt_message(
            st.session_state.encrypted,
            st.session_state.d,
            st.session_state.n
        )
 
        st.session_state.decrypted = decrypted
 
 
# ============================================================
# DECRYPTION VISUALIZATION
# ============================================================
 
if st.session_state.decrypted is not None:
 
    st.subheader("🔓 Decryption Process")
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 1 — Ciphertext Received</b>
 
    The receiver receives the encrypted numerical values.
 
    </div>
    """, unsafe_allow_html=True)
 
    st.code(
        str(st.session_state.encrypted),
        language="text"
    )
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 2 — Private Key Applied</b>
 
    The receiver uses the private key `(d, n)`.
 
    </div>
    """, unsafe_allow_html=True)
 
    st.latex(
        r"m = c^d \mod n"
    )
 
    st.markdown("""
    <div class="step-card">
 
    <b>Step 3 — Original Message Recovered</b>
 
    The decrypted numerical values are converted back into characters.
 
    </div>
    """, unsafe_allow_html=True)
 
    st.success(
        f"📨 Decrypted Message: {st.session_state.decrypted}"
    )
 
 
# ============================================================
# SECTION 5 — COMPLETE COMMUNICATION FLOW
# ============================================================
 
if st.session_state.keys_generated:
 
    st.header("5️⃣ Complete RSA Secure Chat Flow")
 
    st.markdown("""
    <div class="card">
 
    <h3>🔐 RSA Communication Workflow</h3>
 
    <p>👤 <b>Receiver</b> generates RSA keys</p>
 
    ↓
 
    <p>🔓 <b>Public Key</b> is distributed to the sender</p>
 
    ↓
 
    <p>👤 <b>Sender</b> enters a message</p>
 
    ↓
 
    <p>🔒 Message is encrypted using the public key</p>
 
    ↓
 
    <p>🌐 <b>Ciphertext</b> is transmitted</p>
 
    ↓
 
    <p>🔐 <b>Receiver's private key</b> decrypts the ciphertext</p>
 
    ↓
 
    <p>📨 <b>Original message is recovered</b></p>
 
    </div>
    """, unsafe_allow_html=True)
 
 
# ============================================================
# SECTION 6 — MATHEMATICAL DETAILS
# ============================================================
 
st.header("6️⃣ RSA Algorithm Details")
 
with st.expander("📐 View Mathematical Calculations"):
 
    if st.session_state.keys_generated:
 
        st.markdown("### Step 1 — Calculate n")
 
        st.latex(
            rf"n = p \times q = "
            rf"{st.session_state.p} \times "
            rf"{st.session_state.q} = "
            rf"{st.session_state.n}"
        )
 
        st.markdown("### Step 2 — Calculate Euler's Totient")
 
        st.latex(
            rf"\phi(n) = (p-1)(q-1)"
        )
 
        st.latex(
            rf"\phi(n) = "
            rf"({st.session_state.p}-1)"
            rf"({st.session_state.q}-1)"
            rf" = {st.session_state.phi}"
        )
 
        st.markdown("### Step 3 — Public Key")
 
        st.latex(
            rf"(e,n) = "
            rf"({st.session_state.e},"
            rf"{st.session_state.n})"
        )
 
        st.markdown("### Step 4 — Private Key")
 
        st.latex(
            rf"(d,n) = "
            rf"({st.session_state.d},"
            rf"{st.session_state.n})"
        )
 
        st.markdown("### Step 5 — Encryption")
 
        st.latex(
            r"c = m^e \mod n"
        )
 
        st.markdown("### Step 6 — Decryption")
 
        st.latex(
            r"m = c^d \mod n"
        )
 
 
# ============================================================
# SECTION 7 — LEARNING OUTCOME
# ============================================================
 
st.header("7️⃣ Learning Outcome")
 
st.markdown("""
<div class="card">
 
After completing this virtual laboratory, the student can:
 
- Understand RSA public-key cryptography.
- Generate RSA public and private keys.
- Understand RSA key distribution.
- Encrypt a message using a public key.
- Decrypt a message using a private key.
- Understand the mathematical operations involved in RSA.
- Visualize secure communication between a sender and receiver.
 
</div>
""", unsafe_allow_html=True)
 
 
# ============================================================
# FOOTER
# ============================================================
 
st.divider()
 
st.caption(
    "🔐 RSA Key Distribution for Secure Chat | "
    "Cryptography Virtual Laboratory | Python + Streamlit"
)