import React from 'react';
import { TestTube, Play, Pause, RotateCcw, ChevronLeft, ChevronRight, ArrowLeft, ArrowRight, Activity } from 'lucide-react';
import { getRSABreakdown } from '../utils/rsa';
import InteractivePipelineGraph from './InteractivePipelineGraph';
import VisualMathCard from './VisualMathCard';

export default function Step3InteractiveStepper({
  message,
  p,
  q,
  e,
  d,
  stepIdx,
  setStepIdx,
  isPlaying,
  setIsPlaying,
  playSpeed,
  setPlaySpeed,
  onBack,
  onNext,
}) {
  const n = p * q;
  const { steps, error } = getRSABreakdown(message, e, d, n);
  const totalSteps = steps.length;

  if (totalSteps === 0 || error) {
    return (
      <div className="glass-card">
        <p style={{ color: '#fca5a5' }}>{error || 'Please enter a valid message in Step 2.'}</p>
        <button className="btn btn-secondary" onClick={onBack} style={{ marginTop: '1rem' }}>
          Back to Step 2
        </button>
      </div>
    );
  }

  const safeIdx = Math.min(stepIdx, totalSteps - 1);
  const currentStep = steps[safeIdx];
  const encryptedSoFar = steps.slice(0, safeIdx + 1).map((s) => s.cipher);
  const recoveredSoFar = steps.slice(0, safeIdx + 1).map((s) => s.decChar).join('');

  return (
    <div className="glass-card">
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
        <Activity style={{ color: '#38bdf8' }} size={28} />
        <h2 style={{ fontSize: '1.6rem', fontWeight: 800, margin: 0 }}>Step 3 — Interactive Visual Laboratory</h2>
      </div>
      <p style={{ color: 'var(--text-muted)', fontSize: '1rem', marginBottom: '2rem', lineHeight: '1.6' }}>
        Watch raw text data morph through ASCII integers, public key exponentiation, and private key decryption across the network.
      </p>

      {/* Stepper Control Bar */}
      <div className="stepper-controls">
        <button
          className="btn btn-secondary"
          onClick={() => {
            setStepIdx(Math.max(0, safeIdx - 1));
            setIsPlaying(false);
          }}
          disabled={safeIdx === 0}
        >
          <ChevronLeft size={18} /> Previous
        </button>

        <button
          className="btn btn-primary"
          onClick={() => setIsPlaying(!isPlaying)}
        >
          {isPlaying ? <Pause size={18} /> : <Play size={18} />}
          <span>{isPlaying ? 'Pause' : 'Auto Play'}</span>
        </button>

        <button
          className="btn btn-secondary"
          onClick={() => {
            setStepIdx(Math.min(totalSteps - 1, safeIdx + 1));
            setIsPlaying(false);
          }}
          disabled={safeIdx === totalSteps - 1}
        >
          Next <ChevronRight size={18} />
        </button>

        <button
          className="btn btn-secondary"
          onClick={() => {
            setStepIdx(0);
            setIsPlaying(false);
          }}
        >
          <RotateCcw size={16} /> Restart
        </button>

        <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Playback Speed:</span>
          <select
            className="input-field"
            style={{ width: 'auto', padding: '0.5rem 0.9rem', fontSize: '0.85rem' }}
            value={playSpeed}
            onChange={(e) => setPlaySpeed(parseFloat(e.target.value))}
          >
            <option value={0.5}>0.5s</option>
            <option value={1.0}>1.0s</option>
            <option value={1.5}>1.5s</option>
            <option value={2.0}>2.0s</option>
          </select>
        </div>
      </div>

      {/* Progress Bar */}
      <div style={{ marginBottom: '2rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem', color: 'var(--text-muted)', marginBottom: '0.5rem' }}>
          <span>Character {safeIdx + 1} of {totalSteps}</span>
          <span style={{ fontFamily: 'var(--font-mono)', color: '#38bdf8', fontWeight: 700 }}>Active Target: '{currentStep.char}'</span>
        </div>
        <div style={{ background: 'rgba(30, 41, 59, 0.8)', height: '10px', borderRadius: '5px', overflow: 'hidden' }}>
          <div
            style={{
              width: `${((safeIdx + 1) / totalSteps) * 100}%`,
              background: 'linear-gradient(90deg, #3b82f6 0%, #a855f7 50%, #38bdf8 100%)',
              height: '100%',
              transition: 'width 0.3s ease',
            }}
          />
        </div>
      </div>

      {/* Interactive SVG Animated Pipeline Graph */}
      <InteractivePipelineGraph stepData={currentStep} activeStep={safeIdx} totalSteps={totalSteps} />

      {/* Side-by-Side Workstation */}
      <div className="workstation-grid">
        {/* Sender Panel */}
        <div className="panel-card sender">
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
            <span style={{ fontWeight: 800, color: '#60a5fa', fontSize: '1.2rem' }}>👤 Sender Terminal</span>
            <span style={{ fontSize: '0.85rem', background: 'rgba(59, 130, 246, 0.2)', color: '#93c5fd', padding: '0.25rem 0.75rem', borderRadius: '14px', fontFamily: 'var(--font-mono)' }}>
              Public Key ({e}, {n})
            </span>
          </div>

          <div style={{ fontSize: '1.05rem', marginBottom: '1rem' }}>
            Target Character: <b style={{ color: '#60a5fa', fontSize: '1.3rem' }}>'{currentStep.char}'</b> (Index {currentStep.index})
          </div>

          <div className="code-box">
            1. ASCII Encoding: m = ord('{currentStep.char}') = <b>{currentStep.ascii}</b>
          </div>

          <div className="code-box">
            2. RSA Modular Exponentiation:<br />
            c = mᵉ mod n = {currentStep.ascii}<sup>{e}</sup> mod {n} = <b style={{ color: '#60a5fa', fontSize: '1.15rem' }}>{currentStep.cipher}</b>
          </div>

          <div style={{ marginTop: '1.25rem', background: 'rgba(5, 7, 12, 0.7)', padding: '1rem', borderRadius: '14px' }}>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase' }}>Transmitted Ciphertext Stream:</div>
            <div style={{ fontFamily: 'var(--font-mono)', color: '#60a5fa', fontWeight: 700, marginTop: '0.4rem' }}>
              [{encryptedSoFar.join(', ')}]
            </div>
          </div>
        </div>

        {/* Receiver Panel */}
        <div className="panel-card receiver">
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
            <span style={{ fontWeight: 800, color: '#34d399', fontSize: '1.2rem' }}>👤 Receiver Terminal</span>
            <span style={{ fontSize: '0.85rem', background: 'rgba(16, 185, 129, 0.2)', color: '#6ee7b7', padding: '0.25rem 0.75rem', borderRadius: '14px', fontFamily: 'var(--font-mono)' }}>
              Private Key ({d}, {n})
            </span>
          </div>

          <div style={{ fontSize: '1.05rem', marginBottom: '1rem' }}>
            Received Cipher Block: <b style={{ color: '#34d399', fontSize: '1.3rem' }}>{currentStep.cipher}</b> (Index {currentStep.index})
          </div>

          <div className="code-box">
            1. RSA Modular Decryption:<br />
            m = cᵈ mod n = {currentStep.cipher}<sup>{d}</sup> mod {n} = <b style={{ color: '#34d399', fontSize: '1.15rem' }}>{currentStep.decAscii}</b>
          </div>

          <div className="code-box">
            2. ASCII Decoding:<br />
            chr({currentStep.decAscii}) = <b style={{ color: '#34d399', fontSize: '1.15rem' }}>'{currentStep.decChar}'</b>
          </div>

          <div style={{ marginTop: '1.25rem', background: 'rgba(5, 7, 12, 0.7)', padding: '1rem', borderRadius: '14px' }}>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase' }}>Recovered Message Stream:</div>
            <div style={{ fontFamily: 'var(--font-mono)', color: '#34d399', fontWeight: 700, fontSize: '1.25rem', marginTop: '0.4rem' }}>
              "{recoveredSoFar}"
            </div>
          </div>
        </div>
      </div>

      {/* Bit & Hex Visualizer */}
      <VisualMathCard stepData={currentStep} e={e} d={d} n={n} />

      <div className="nav-bottom">
        <button className="btn btn-secondary" onClick={onBack}>
          <ArrowLeft size={16} /> Back: Message & Encrypt
        </button>
        <button className="btn btn-primary" onClick={onNext}>
          Next: Summary Matrix <ArrowRight size={16} />
        </button>
      </div>
    </div>
  );
}
