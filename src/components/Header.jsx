import React from 'react';
import { Lock } from 'lucide-react';

export default function Header() {
  return (
    <header className="hero-header">
      <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
        <div style={{ background: 'linear-gradient(135deg, #3b82f6, #a855f7)', padding: '0.6rem', borderRadius: '14px', color: '#fff', display: 'flex' }}>
          <Lock size={28} />
        </div>
        <h1 className="hero-title" style={{ margin: 0 }}>RSA Cryptography Guided Visualizer</h1>
      </div>
      <p className="hero-subtitle">Interactive web laboratory demonstrating RSA key derivation, encryption, network payload transmission, and decryption.</p>
    </header>
  );
}
