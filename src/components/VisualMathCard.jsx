import React from 'react';
import { Binary, Shield, Cpu } from 'lucide-react';

export default function VisualMathCard({ stepData, e, d, n }) {
  const binaryAscii = stepData.ascii.toString(2).padStart(8, '0');
  const hexAscii = '0x' + stepData.ascii.toString(16).toUpperCase();
  const hexCipher = '0x' + stepData.cipher.toString(16).toUpperCase();

  return (
    <div style={{ background: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '20px', padding: '1.5rem', marginTop: '1.5rem' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', color: '#38bdf8', fontWeight: 700, fontSize: '1rem' }}>
        <Cpu size={20} />
        <span>Low-Level Bit & Integer Inspection</span>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1rem' }}>
        <div style={{ background: 'rgba(5, 7, 12, 0.7)', padding: '1rem', borderRadius: '14px', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase' }}>8-Bit Binary ASCII</div>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: '1.2rem', fontWeight: 700, color: '#60a5fa', marginTop: '0.25rem', letterSpacing: '0.1em' }}>
            {binaryAscii}
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.25rem' }}>
            Hex: {hexAscii} | Decimal: {stepData.ascii}
          </div>
        </div>

        <div style={{ background: 'rgba(5, 7, 12, 0.7)', padding: '1rem', borderRadius: '14px', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase' }}>Encrypted Cipher Block (Hex & Mod n)</div>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: '1.2rem', fontWeight: 700, color: '#c084fc', marginTop: '0.25rem' }}>
            {hexCipher}
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.25rem' }}>
            Decimal Integer: {stepData.cipher} (mod {n})
          </div>
        </div>
      </div>
    </div>
  );
}
