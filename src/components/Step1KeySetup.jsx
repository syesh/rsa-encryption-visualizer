import React, { useState } from 'react';
import { Key, ArrowRight, CheckCircle, AlertCircle, Sparkles } from 'lucide-react';
import { isPrime, gcd, modInverse } from '../utils/rsa';

export default function Step1KeySetup({ p, setP, q, setQ, e, setE, onNext }) {
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const n = p * q;
  const phi = (p - 1) * (q - 1);
  const d = modInverse(e, phi);

  const handleUpdate = () => {
    setError(null);
    setSuccess(false);

    if (!isPrime(p)) {
      setError(`p (${p}) must be a prime number.`);
      return;
    }
    if (!isPrime(q)) {
      setError(`q (${q}) must be a prime number.`);
      return;
    }
    if (p === q) {
      setError('Primes p and q must be distinct.');
      return;
    }
    if (gcd(e, phi) !== 1) {
      setError(`Exponent e (${e}) must be coprime to φ(n) (${phi}).`);
      return;
    }
    if (d === null) {
      setError('Modular inverse d does not exist for the chosen exponent.');
      return;
    }

    setSuccess(true);
  };

  const handleSmallPrimes = () => {
    setP(11);
    setQ(13);
    setE(7);
    setError(null);
    setSuccess(true);
  };

  const handleStandardPrimes = () => {
    setP(61);
    setQ(53);
    setE(17);
    setError(null);
    setSuccess(true);
  };

  return (
    <div className="glass-card">
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
        <Key style={{ color: '#60a5fa' }} size={24} />
        <h2 style={{ fontSize: '1.4rem', fontWeight: 700, margin: 0 }}>Step 1 — RSA Key Generation & Derivation</h2>
      </div>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', marginBottom: '1.5rem', lineHeight: '1.6' }}>
        RSA uses two prime numbers <b>p</b> and <b>q</b> to create the modulus <b>n</b>. The public exponent <b>e</b> must be coprime to Euler's totient <b>φ(n)</b>.
      </p>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.25rem', marginBottom: '1.5rem' }}>
        <div>
          <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.4rem' }}>Prime p</label>
          <input type="number" className="input-field" value={p} onChange={(evt) => setP(parseInt(evt.target.value) || 2)} min={2} />
        </div>
        <div>
          <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.4rem' }}>Prime q</label>
          <input type="number" className="input-field" value={q} onChange={(evt) => setQ(parseInt(evt.target.value) || 2)} min={2} />
        </div>
        <div>
          <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.4rem' }}>Public Exponent e</label>
          <input type="number" className="input-field" value={e} onChange={(evt) => setE(parseInt(evt.target.value) || 2)} min={2} />
        </div>
      </div>

      <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap', marginBottom: '1.5rem' }}>
        <button className="btn btn-secondary" onClick={handleSmallPrimes}>
          <Sparkles size={16} /> Small Primes (p=11, q=13, e=7)
        </button>
        <button className="btn btn-secondary" onClick={handleStandardPrimes}>
          <Sparkles size={16} /> Standard Primes (p=61, q=53, e=17)
        </button>
        <button className="btn btn-primary" onClick={handleUpdate} style={{ marginLeft: 'auto' }}>
          Update & Validate Keys
        </button>
      </div>

      {error && (
        <div style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.3)', color: '#fca5a5', padding: '0.85rem 1rem', borderRadius: '12px', display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
          <AlertCircle size={18} />
          <span>{error}</span>
        </div>
      )}

      {success && (
        <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid rgba(16, 185, 129, 0.3)', color: '#6ee7b7', padding: '0.85rem 1rem', borderRadius: '12px', display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
          <CheckCircle size={18} />
          <span>RSA Keys validated successfully!</span>
        </div>
      )}

      <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginTop: '1.5rem', marginBottom: '0.75rem' }}>Derived Cryptographic Parameters</h3>

      <div className="metrics-grid">
        <div className="metric-box">
          <div className="metric-label">Modulus n (p×q)</div>
          <div className="metric-value">{n}</div>
        </div>
        <div className="metric-box">
          <div className="metric-label">Totient φ(n)</div>
          <div className="metric-value">{phi}</div>
        </div>
        <div className="metric-box">
          <div className="metric-label">🔓 Public Key (e, n)</div>
          <div className="metric-value" style={{ color: '#60a5fa' }}>({e}, {n})</div>
        </div>
        <div className="metric-box">
          <div className="metric-label">🔐 Private Key (d, n)</div>
          <div className="metric-value" style={{ color: '#34d399' }}>({d ?? 'NaN'}, {n})</div>
        </div>
      </div>

      <div className="nav-bottom">
        <div></div>
        <button className="btn btn-primary" onClick={onNext}>
          Next: Message & Encrypt <ArrowRight size={16} />
        </button>
      </div>
    </div>
  );
}
