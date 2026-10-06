# 🔐 RSA Encryption Visualizer & Guided Cryptography Lab

An interactive, web-based Cryptography Virtual Laboratory built with **Python** and **Streamlit** to visualize RSA key generation, public key distribution, step-by-step message encryption, network transmission, and private key decryption.

---

## 📊 Presentation & Project Documentation
For presentation slide decks, project architecture details, and code explanations, see:
- 📖 [PRESENTATION.md](PRESENTATION.md) – Quick presentation slide outline & demo script.
- 📚 [docs/PRESENTATION_DOCS.md](docs/PRESENTATION_DOCS.md) – Full technical presentation documentation & file structure breakdown.

---

## 📌 Features & Highlights

- 🧭 **Guided 4-Step Experience Flow**: Learn and inspect RSA concepts one focused section at a time without visual clutter.
- 🔑 **Key Generation & Parameter Setup**: Interactive prime selection ($p, q$) and exponent selection ($e$) with preset small/standard prime buttons.
- 🔀 **Visual Transformation Pipeline**: Dynamic 5-stage transformation diagram showing Plaintext $\to$ ASCII $\to$ RSA Encryption $\to$ Transmission $\to$ RSA Decryption $\to$ Recovered Message.
- 🎮 **Interactive Stepper Animation Controls**: Step forward, step backward, and **Auto Play / Pause** auto-stepper with configurable playback speeds.
- 🖥️ **Side-by-Side Workstation**: Real-time side-by-side terminal views for **Sender (Encryption)** and **Receiver (Decryption)** with KaTeX math rendering.
- 📊 **Complete Transformation Matrix**: Comprehensive execution table tracking every character's journey with automated integrity verification (`🎉 Message Integrity Verified`).

---

## 🧭 The 4-Step Guided Experience

1. **🔑 Step 1: Key Generation & Setup**
   - Configure prime numbers $p$ and $q$, and public exponent $e$.
   - Derives modulus $n = p \times q$, totient $\phi(n) = (p-1)(q-1)$, Public Key $(e,n)$, and Private Key $(d,n)$.

2. **💬 Step 2: Message Input & Encryption**
   - Input custom plaintext message.
   - View character ASCII numerical representation array and generated network ciphertext array.

3. **🧪 Step 3: Interactive Stepper Visualizer**
   - Step character-by-character through the encryption and decryption pipeline.
   - Play/Pause timer auto-stepper.
   - Side-by-side Sender & Receiver terminal cards displaying active character math and accumulating payload streams.

4. **📊 Step 4: Full Summary Matrix & Verification**
   - End-to-end transformation summary table for all characters.
   - Live integrity verification badge.

---

## 🔑 RSA Algorithm Reference

### Key Derivation
- Select primes $p$ and $q$.
- Compute Modulus: $$n = p \times q$$
- Compute Euler's Totient: $$\phi(n) = (p-1)(q-1)$$
- Select Public Exponent $e$ such that: $$\gcd(e, \phi(n)) = 1$$
- Compute Private Exponent $d$ using modular inverse: $$d \times e \equiv 1 \pmod{\phi(n)}$$

### Keys
- **Public Key**: $(e, n)$
- **Private Key**: $(d, n)$

### Encryption & Decryption
- **Encryption**: $$c = m^e \bmod n$$
- **Decryption**: $$m = c^d \bmod n$$

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** (Web Application Framework)
- **KaTeX / LaTeX** (Mathematical Formula Rendering)
- **HTML5 / Custom CSS3** (Spacious UI Layout & Styling)

---

## ▶️ Getting Started

### 1. Clone & Navigate
```bash
git clone <repository-url>
cd rsa-encryption-visualizer
```

### 2. Install Dependencies
```bash
pip install streamlit
```

### 3. Run the App
```bash
python -m streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## 🧪 Example Test Values

```text
p = 61
q = 53
e = 17
```

Derived parameters:
```text
n = 3233
φ(n) = 3120
Public Key = (17, 3233)
Private Key = (2753, 3233)
```

Example message: `"HELLO RSA"` $\to$ Character-by-character modular transformation verified automatically.

---

## 🎓 Learning Outcomes

- Understand public-key asymmetric cryptography concepts.
- Learn RSA key generation, modular arithmetic, and inverse calculations.
- Visualize encryption/decryption transformations step-by-step.
- Verify message integrity over simulated transmission.

---

## ⚠️ Educational Note

This virtual lab uses textbook RSA for educational visualization and mathematical clarity. It is designed for teaching and learning cryptography concepts.
