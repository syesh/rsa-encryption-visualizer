````markdown
# 🔐 RSA Key Distribution for Secure Chat

An interactive Cryptography Virtual Laboratory developed using Python and Streamlit to demonstrate RSA key generation, public-key distribution, message encryption, and decryption.

## 📌 Project Overview

This project implements RSA Key Distribution for Secure Chat.

The application allows users to:

- Enter RSA parameters
- Generate public and private keys
- Visualize public-key distribution
- Enter a message
- Encrypt the message using the receiver's public key
- Visualize the encryption process
- Transmit the encrypted ciphertext
- Decrypt the message using the receiver's private key
- Visualize the complete RSA communication process

## 🎯 Objective

The objective of this project is to demonstrate how RSA public-key cryptography can be used for secure communication between a sender and receiver.

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Python Standard Library
- HTML/CSS

## 🔑 RSA Algorithm

RSA uses two keys:

- **Public Key** — can be shared with others
- **Private Key** — must be kept secret

### Key Generation

Two prime numbers `p` and `q` are selected.

```text
n = p × q
````

Euler's Totient is calculated as:

```text
φ(n) = (p − 1)(q − 1)
```

The public exponent `e` is selected such that:

```text
gcd(e, φ(n)) = 1
```

The private exponent `d` is calculated using:

```text
d × e ≡ 1 (mod φ(n))
```

### Public Key

```text
(e, n)
```

### Private Key

```text
(d, n)
```

## 🔒 Encryption

The sender encrypts the message using the receiver's public key.

```text
c = mᵉ mod n
```

## 🔓 Decryption

The receiver decrypts the ciphertext using the private key.

```text
m = cᵈ mod n
```

## 🔄 Secure Chat Workflow

```text
             RSA SECURE CHAT

        ┌─────────────────────┐
        │      RECEIVER       │
        │                     │
        │   Generate Keys     │
        └──────────┬──────────┘
                   │
                   │ Public Key
                   ▼
        ┌─────────────────────┐
        │       SENDER        │
        │                     │
        │   Enter Message     │
        └──────────┬──────────┘
                   │
                   │ Encrypt
                   ▼
        ┌─────────────────────┐
        │     CIPHERTEXT      │
        │                     │
        │ Secure Transmission │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │      RECEIVER       │
        │                     │
        │    Private Key      │
        └──────────┬──────────┘
                   │
                   │ Decrypt
                   ▼
        ┌─────────────────────┐
        │  ORIGINAL MESSAGE   │
        └─────────────────────┘
```

## ✨ Features

### 🔑 RSA Key Generation

Users can provide prime numbers `p`, `q`, and public exponent `e` to generate the RSA key pair.

### 🔓 Public Key Distribution

The receiver shares the public key with the sender while keeping the private key secret.

### 💬 Secure Chat

Users can enter a message and encrypt it using the generated public key.

### 🔒 Encryption Visualization

The application displays:

1. Original message
2. Character-to-ASCII conversion
3. RSA encryption formula
4. Encrypted ciphertext
5. Secure transmission

### 🔓 Decryption Visualization

The application displays:

1. Received ciphertext
2. Private key
3. RSA decryption formula
4. Recovered original message

### 📐 Mathematical Visualization

The application displays the important RSA calculations and formulas.

### 🔄 Reset Laboratory

The experiment can be reset and performed again with different inputs.

## 📂 Project Structure

```text
rsa-encryption-visualizer/
│
├── app.py
│
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Open the Project Folder

```bash
cd rsa-encryption-visualizer
```

### 3. Install Streamlit

```bash
pip install streamlit
```

## ▶️ Running the Application

Run the application using:

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🧪 Example

Use the following values:

```text
p = 61
q = 53
e = 17
```

The application calculates:

```text
n = 3233
φ(n) = 3120
```

Public Key:

```text
(17, 3233)
```

Private Key:

```text
(2753, 3233)
```

A message can then be entered, encrypted using the public key, transmitted as ciphertext, and decrypted using the private key.

## 🎓 Learning Outcomes

After completing this virtual laboratory, students will be able to:

* Understand the basic working of RSA.
* Generate RSA public and private keys.
* Understand RSA key distribution.
* Differentiate between public and private keys.
* Encrypt messages using RSA.
* Decrypt RSA ciphertext.
* Understand the mathematical calculations involved in RSA.
* Visualize secure communication between a sender and receiver.

## ⚠️ Educational Purpose

This project is intended for educational and demonstration purposes.

The implementation uses textbook RSA so that the mathematical operations and encryption/decryption process can be easily visualized. It is not intended for production-grade secure messaging.

## 👨‍💻 Project Information

**Project Title:** RSA Key Distribution for Secure Chat

**Type:** Cryptography Virtual Laboratory

**Algorithm:** RSA (Rivest–Shamir–Adleman)

**Programming Language:** Python

**Framework:** Streamlit

**Application Type:** Web-Based Interactive Laboratory

```
```
