import React from 'react';
import { MessageSquare, ArrowLeft, ArrowRight, Lock, ShieldCheck } from 'lucide-react';
import { getRSABreakdown } from '../utils/rsa';

export default function Step2MessageEncrypt({ message, setMessage, p, q, e, d, onBack, onNext }) {
  const n = p * q;
  const { steps, error } = getRSABreakdown(message, e, d, n);

  return (
    <div className="glass-card">
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
        <MessageSquare style={{ color: '#c084fc' }} size={24} />
        <h2 style={{ fontSize: '1.4rem', fontWeight: 700, margin: 0 }}>Step 2 — Message Input & RSA Encryption</h2>
      </div>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', marginBottom: '1.5rem', lineHeight: '1.6' }}>
        Type any plaintext message below. Each character is converted to its numerical ASCII code <b>m</b>, and encrypted into ciphertext integer <b>c</b> using the Public Key <b>({e}, {n})</b>.
      </p>

      <div style={{ marginBottom: '1.5rem' }}>
        <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.4rem' }}>Plaintext Message</label>
        <input
          type="text"
          className="input-field"
          value={message}
          onChange={(evt) => setMessage(evt.target.value)}
          placeholder="Type message here..."
        />
      </div>

      {error && (
        <div style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.3)', color: '#fca5a5', padding: '0.85rem 1rem', borderRadius: '12px', marginBottom: '1.5rem' }}>
          {error}
        </div>
      )}

      {steps.length > 0 && (
        <div className="workstation-grid">
          <div className="panel-card sender">
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
              <span style={{ fontWeight: 700, color: '#60a5fa', fontSize: '1.1rem' }}>👤 Sender Terminal</span>
              <span style={{ fontSize: '0.8rem', background: 'rgba(59, 130, 246, 0.2)', color: '#93c5fd', padding: '0.2rem 0.6rem', borderRadius: '12px', fontFamily: 'var(--font-mono)' }}>
                Public Key ({e}, {n})
              </span>
            </div>
            <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)', marginBottom: '0.5rem' }}>Original Message Stream:</div>
            <div className="code-box">"{message}"</div>
            <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)', marginTop: '0.75rem', marginBottom: '0.5rem' }}>ASCII Array [m₁...mₙ]:</div>
            <div className="code-box" style={{ color: '#60a5fa' }}>
              [{steps.map((s) => s.ascii).join(', ')}]
            </div>
          </div>

          <div className="panel-card" style={{ borderColor: 'rgba(168, 85, 247, 0.4)', boxShadow: '0 10px 30px rgba(168, 85, 247, 0.1)' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
              <span style={{ fontWeight: 700, color: '#c084fc', fontSize: '1.1rem' }}>🔒 Transmitted Payload</span>
              <span style={{ fontSize: '0.8rem', background: 'rgba(168, 85, 247, 0.2)', color: '#e9d5ff', padding: '0.2rem 0.6rem', borderRadius: '12px', fontFamily: 'var(--font-mono)' }}>
                c = mᵉ mod n
              </span>
            </div>
            <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)', marginBottom: '0.5rem' }}>Encrypted Ciphertext Stream [c₁...cₙ]:</div>
            <div className="code-box" style={{ color: '#c084fc', fontSize: '1.05rem', fontWeight: 700 }}>
              [{steps.map((s) => s.cipher).join(', ')}]
            </div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
              <ShieldCheck size={16} color="#34d399" />
              <span>Ready for transmission over insecure network</span>
            </div>
          </div>
        </div>
      )}

      <div className="nav-bottom">
        <button className="btn btn-secondary" onClick={onBack}>
          <ArrowLeft size={16} /> Back: Key Setup
        </button>
        <button className="btn btn-primary" onClick={onNext} disabled={!message || steps.length === 0}>
          Next: Interactive Stepper <ArrowRight size={16} />
        </button>
      </div>
    </div>
  );
}
