# 🔐 RSA Cryptography Guided Experience & Visualizer

An interactive, web-based visual laboratory for exploring asymmetric public-key cryptography. Built with **Python**, **Streamlit**, and **WebAssembly (Stlite)**, this visualizer demonstrates how prime numbers, Euler's totient function, and modular arithmetic power RSA encryption and decryption in real time—with zero server configuration needed.

---

## 🌟 Features

- **🔑 Dynamic Key Derivation**: Interactive prime selection ($p, q$) and public exponent ($e$) with instant validation, GCD calculations, and modular inverse derivation ($d$).
- **⚡ Pre-Configured Presets**: Quick-load prime presets (`Small (11, 13)`, `Standard (61, 53)`, `Medium (131, 137)`, `Fast (17, 19)`, `Large (251, 257)`).
- **💬 Dual-Workstation Transmission**: Visual simulation of two independent terminals:
  - **Sender**: Plaintext $\rightarrow$ ASCII encoding $\rightarrow$ Modular exponentiation ($c = m^e \bmod n$).
  - **Receiver**: Encrypted payload $\rightarrow$ Modular inverse exponentiation ($m = c^d \bmod n$) $\rightarrow$ ASCII decoding.
- **🧪 Interactive Stepper & Auto-Play**: Step through encryption/decryption character-by-character with adjustable animation speed (0.2s - 2.0s).
- **📊 Transformation Matrix**: Full ASCII conversion and ciphertext matrix with automated end-to-end message integrity verification.
- **🌐 100% Serverless / Client-Side**: Powered by [Stlite](https://github.com/whitphx/stlite) (WebAssembly + Pyodide). Runs completely inside the user's browser with no backend server required.

---

## 🚀 Yes, You Can Deploy on GitHub Pages!

**Yes! Because this application runs entirely in the browser using WebAssembly via Stlite, it is 100% static and can be deployed directly to GitHub Pages for free.**

### Option A: Standard GitHub Pages Deployment (2 Clicks)

1. Push your repository to GitHub.
2. Go to **Settings** $\rightarrow$ **Pages** in your GitHub repository.
3. Under **Build and deployment**:
   - **Source**: Select `Deploy from a branch`.
   - **Branch**: Select `main` and `/ (root)`.
4. Click **Save**.
5. Wait 1-2 minutes—your visualizer will be live at:
   ```
   https://<your-username>.github.io/<repository-name>/
   ```

> **Note:** A `.nojekyll` file has already been added to the repository to ensure GitHub Pages serves `app.py` and all assets without Jekyll filtering.

---

### Option B: GitHub Actions Workflow (Automated CI/CD)

An automated GitHub Actions workflow is provided at [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).

1. Go to **Settings** $\rightarrow$ **Pages** in your repository.
2. Under **Build and deployment** $\rightarrow$ **Source**, choose **GitHub Actions**.
3. Any push to `main` will automatically build and publish your site!

---

## 💻 Local Development

You can run the visualizer locally using either the standard Streamlit server or as a static WebAssembly web page.

### Method 1: Using Streamlit (Python)

1. Clone the repository and navigate into the folder:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the application:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser.

---

### Method 2: Pure Static / WebAssembly Mode

Test the exact client-side WebAssembly build that runs on GitHub Pages:

```bash
# Python 3 built-in HTTP server
python3 -m http.server 8000
```
Open `http://localhost:8000` in your browser.

---

## 🧠 RSA Mathematical Foundation

The visualizer implements textbook RSA asymmetric cryptography:

1. **Prime Selection**: Pick two distinct prime numbers $p$ and $q$.
2. **Modulus Calculation**:
   $$n = p \times q$$
3. **Euler's Totient**:
   $$\phi(n) = (p - 1) \times (q - 1)$$
4. **Public Key Selection ($e$)**:
   Choose $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.
   The **Public Key** is $(e, n)$.
5. **Private Key Derivation ($d$)**:
   Compute $d$ such that:
   $$d \times e \equiv 1 \pmod{\phi(n)}$$
   (Solved using the **Extended Euclidean Algorithm**).
   The **Private Key** is $(d, n)$.
6. **Encryption**:
   For each character message $m$ (converted to its ASCII integer):
   $$c = m^e \pmod n$$
7. **Decryption**:
   For each ciphertext integer $c$:
   $$m = c^d \pmod n$$

> ⚠️ **Educational Note**: This project uses small primes to clearly demonstrate the mathematical principles. Production RSA requires large primes (2048 to 4096 bits), cryptographically secure random number generators (CSPRNG), and optimal asymmetric encryption padding (RSA-OAEP) to protect against attacks.

---

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy-pages.yml    # GitHub Actions workflow for GitHub Pages
├── .streamlit/
│   └── config.toml             # Streamlit dark theme styling configuration
├── docs/
│   └── PRESENTATION_DOCS.md    # Detailed slides & architecture explanation
├── public/                     # Static distribution mirror
│   ├── app.py
│   ├── index.html
│   └── .nojekyll
├── .gitignore                  # Git ignore rules
├── .nojekyll                   # Bypasses Jekyll on GitHub Pages
├── .vercelignore               # Vercel deployment exclusions
├── app.py                      # Main Streamlit application & RSA engine
├── index.html                  # Stlite WebAssembly client mount
├── LICENSE                     # MIT License
├── PRESENTATION.md             # Quick slide presentation guide
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── vercel.json                 # Vercel deployment configuration
```

---

## 🌐 Other Deployment Options

### Vercel Deployment
This repository is pre-configured for Vercel using [`vercel.json`](vercel.json):
1. Import the repository into [Vercel](https://vercel.com).
2. Set Framework Preset to **Other** (Root directory: `.`).
3. Deploy!

### Streamlit Community Cloud
1. Fork or push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io).
3. Select your repository, set the branch to `main`, and specify `app.py` as the entry point.
4. Deploy!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
