# 🔐 RSA Cryptography Guided Experience
## Presentation Deck & Code Explanation

For complete technical documentation, mathematical proofs, and code architecture details, see [docs/PRESENTATION_DOCS.md](docs/PRESENTATION_DOCS.md).

---

## 🎯 Presentation Quick Outline (Slide Deck)

### 📌 Slide 1: Introduction
- **Project Title**: RSA Cryptography Guided Experience & Visualizer
- **Purpose**: An interactive visual laboratory that transforms abstract RSA mathematical equations into a step-by-step interactive demonstration.

### 📌 Slide 2: Problem & Solution
- **The Challenge**: Key derivation, Euler's Totient $\phi(n)$, and modular exponentiation are difficult to visualize conceptually.
- **Our Solution**: A 4-step pipeline featuring live dual-workstation views for **Sender (Encryption)** and **Receiver (Decryption)** with zero-server client WebAssembly execution.

### 📌 Slide 3: Core Mathematics
- **Modulus**: $n = p \times q$
- **Totient**: $\phi(n) = (p-1)(q-1)$
- **Public Key**: $(e, n)$ where $\gcd(e, \phi(n)) = 1$
- **Private Key**: $(d, n)$ where $d = e^{-1} \pmod{\phi(n)}$
- **Encryption**: $c = m^e \pmod n$
- **Decryption**: $m = c^d \pmod n$

### 📌 Slide 4: 4-Step Guided Experience
1. **🔑 Key Generation & Setup**: Interactive prime selection ($p, q, e$) with quick presets.
2. **💬 Plaintext & Encryption**: ASCII transformation & ciphertext integer array generation.
3. **🧪 Step-by-Step Stepper**: Auto-playing visual animation across dual workstations.
4. **📊 Complete Summary Matrix**: Comprehensive character transformation matrix & integrity verifier.

### 📌 Slide 5: File & Code Architecture
- `app.py`: Core Streamlit visual laboratory & RSA mathematical engine (`extended_gcd`, `modular_inverse`, `is_prime`).
- `index.html`: Client-side Pyodide WebAssembly launcher via `@stlite/mountable`.
- `vercel.json`: Vercel static hosting routing and headers (`@vercel/static`).
- `.streamlit/config.toml`: Enforced dark SaaS aesthetic theme.

---

## 🎬 Quick Presentation Demo Steps
1. **Key Generation**: Load preset `🎲 Small (11, 13)` ➔ Show $n=143, \phi(n)=120, e=7, d=103$.
2. **Encryption**: Input `"HELLO RSA"` ➔ Show ASCII values $[72, 69, 76, 76, 79, 32, 82, 83, 65]$.
3. **Interactive Stepper**: Click **`⏯ Auto Play`** ➔ Observe dual workstation sender/receiver simulation.
4. **Verification**: View transformation matrix ➔ Show **`🎉 Message Integrity Verified`**.
