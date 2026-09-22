import React from 'react';
import { BarChart3, ArrowLeft, RotateCcw, CheckCircle2 } from 'lucide-react';
import { getRSABreakdown } from '../utils/rsa';

export default function Step4SummaryMatrix({ message, p, q, e, d, onBack, onRestart }) {
  const n = p * q;
  const { steps } = getRSABreakdown(message, e, d, n);
  const recoveredFull = steps.map((s) => s.decChar).join('');
  const isMatch = recoveredFull === message;

  return (
    <div className="glass-card">
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
        <BarChart3 style={{ color: '#10b981' }} size={24} />
        <h2 style={{ fontSize: '1.4rem', fontWeight: 700, margin: 0 }}>Step 4 — Complete Transformation Summary Matrix</h2>
      </div>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', marginBottom: '1.5rem', lineHeight: '1.6' }}>
        Review the end-to-end character transformations and verify message integrity.
      </p>

      {isMatch && (
        <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid rgba(16, 185, 129, 0.3)', color: '#6ee7b7', padding: '1rem 1.25rem', borderRadius: '16px', display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
          <CheckCircle2 size={24} />
          <div>
            <div style={{ fontWeight: 700, fontSize: '1.05rem' }}>Message Integrity Verified!</div>
            <div style={{ fontSize: '0.9rem', color: '#a7f3d0' }}>
              Decrypted string <b>"{recoveredFull}"</b> exactly matches original plaintext <b>"{message}"</b>.
            </div>
          </div>
        </div>
      )}

      <div style={{ overflowX: 'auto' }}>
        <table className="data-table">
          <thead>
            <tr>
              <th>Step #</th>
              <th>Input Char</th>
              <th>ASCII (m)</th>
              <th>Encrypted Cipher (c)</th>
              <th>Decrypted ASCII (m')</th>
              <th>Recovered Char</th>
            </tr>
          </thead>
          <tbody>
            {steps.map((s) => (
              <tr key={s.index}>
                <td>Character {s.index + 1}</td>
                <td>'{s.char}'</td>
                <td>{s.ascii}</td>
                <td style={{ color: '#60a5fa', fontWeight: 600 }}>{s.cipher}</td>
                <td style={{ color: '#34d399' }}>{s.decAscii}</td>
                <td style={{ color: '#34d399', fontWeight: 700 }}>'{s.decChar}'</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="nav-bottom">
        <button className="btn btn-secondary" onClick={onBack}>
          <ArrowLeft size={16} /> Back: Interactive Stepper
        </button>
        <button className="btn btn-primary" onClick={onRestart}>
          <RotateCcw size={16} /> Restart Experience
        </button>
      </div>
    </div>
  );
}
