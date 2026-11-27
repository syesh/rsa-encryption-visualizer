# RSA Cryptography Guided Experience & Visualizer

An interactive web-based RSA cryptography visualizer built using **Python, Streamlit, and WebAssembly (Stlite)**. It demonstrates RSA key generation, encryption, and decryption through step-by-step visualizations, helping users understand the fundamentals of public-key cryptography.

## 🌐 Live Demo

**https://syesh.github.io/rsa-encryption-visualizer/**

## ✨ Features

- Interactive RSA key generation using prime numbers.
- Automatic calculation of Euler's Totient Function and modular inverse.
- Pre-configured prime number presets.
- Step-by-step encryption and decryption.
- Interactive sender and receiver workstations.
- ASCII conversion and ciphertext visualization.
- Auto-play mode with adjustable animation speed.
- Message integrity verification.
- Runs directly in the browser using WebAssembly, without requiring a backend server.

## 🛠️ Technologies Used

- **Language:** Python
- **Framework:** Streamlit
- **WebAssembly:** Stlite, Pyodide
- **Deployment:** GitHub Pages
- **Version Control:** Git, GitHub

## 🧠 RSA Cryptography

The visualizer demonstrates the following RSA operations:

1. Select two prime numbers: \(p\) and \(q\).
2. Calculate the modulus: \(n = p \times q\).
3. Calculate Euler's Totient: \(\phi(n) = (p-1)(q-1)\).
4. Select a valid public exponent \(e\).
5. Derive the private exponent \(d\) using the Extended Euclidean Algorithm.
6. Encrypt messages: \(c = m^e \bmod n\).
7. Decrypt messages: \(m = c^d \bmod n\).

**Note:** This project is intended for educational purposes. It uses small prime numbers to demonstrate RSA mathematical operations and is not suitable for securing real-world data.

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

Alternatively, run the static WebAssembly version locally:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## 📂 Project Structure

```text
.
├── .github/
│   └── workflows/
├── .streamlit/
├── docs/
├── public/
├── app.py
├── index.html
├── requirements.txt
├── PRESENTATION.md
├── LICENSE
└── README.md
```

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
