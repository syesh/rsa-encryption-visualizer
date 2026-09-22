import React from 'react';

export default function InteractivePipelineGraph({ stepData, activeStep, totalSteps }) {
  const nodes = [
    { id: 1, label: 'Plaintext', value: `'${stepData.char}'`, icon: '📝', color: '#60a5fa' },
    { id: 2, label: 'ASCII Code', value: `m = ${stepData.ascii}`, icon: '🔢', color: '#93c5fd' },
    { id: 3, label: 'RSA Encrypt', value: `c = ${stepData.cipher}`, icon: '🔒', color: '#c084fc' },
    { id: 4, label: 'Network Transmission', value: `Packet #${stepData.index + 1}`, icon: '🌐', color: '#f472b6' },
    { id: 5, label: 'RSA Decrypt', value: `m' = ${stepData.decAscii}`, icon: '🔓', color: '#34d399' },
    { id: 6, label: 'Recovered Text', value: `'${stepData.decChar}'`, icon: '📨', color: '#10b981' }
  ];

  return (
    <div style={{ background: 'rgba(5, 7, 12, 0.95)', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '24px', padding: '1.75rem', marginBottom: '2rem' }}>
      <div style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '1.25rem', textAlign: 'center' }}>
        ⚡ Animated Cryptographic Transformation Graph
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '0.75rem', alignItems: 'center' }}>
        {nodes.map((node, index) => (
          <React.Fragment key={node.id}>
            <div
              style={{
                background: 'rgba(15, 23, 42, 0.9)',
                border: `2px solid ${node.color}`,
                borderRadius: '16px',
                padding: '1rem 0.75rem',
                textAlign: 'center',
                boxShadow: `0 0 20px ${node.color}33`,
                transform: 'translateY(-2px)',
                transition: 'all 0.3s ease'
              }}
            >
              <div style={{ fontSize: '1.6rem', marginBottom: '0.25rem' }}>{node.icon}</div>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#f8fafc', textTransform: 'uppercase', letterSpacing: '0.04em' }}>{node.label}</div>
              <div style={{ fontSize: '0.85rem', fontFamily: 'var(--font-mono)', fontWeight: 700, color: node.color, marginTop: '0.35rem' }}>{node.value}</div>
            </div>

            {index < nodes.length - 1 && (
              <div style={{ display: 'flex', justifyContent: 'center', color: '#475569', fontSize: '1.2rem', fontWeight: 'bold' }}>
                ➔
              </div>
            )}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
}
