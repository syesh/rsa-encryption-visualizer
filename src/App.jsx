import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import StepNavigation from './components/StepNavigation';
import Step1KeySetup from './components/Step1KeySetup';
import Step2MessageEncrypt from './components/Step2MessageEncrypt';
import Step3InteractiveStepper from './components/Step3InteractiveStepper';
import Step4SummaryMatrix from './components/Step4SummaryMatrix';
import { modInverse, getRSABreakdown } from './utils/rsa';

export default function App() {
  const [activeTab, setActiveTab] = useState('step1');

  // RSA Parameters
  const [p, setP] = useState(61);
  const [q, setQ] = useState(53);
  const [e, setE] = useState(17);

  // Message & Stepper State
  const [message, setMessage] = useState('HELLO RSA');
  const [stepIdx, setStepIdx] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [playSpeed, setPlaySpeed] = useState(1.0);

  const n = p * q;
  const phi = (p - 1) * (q - 1);
  const d = modInverse(e, phi);

  const { steps } = getRSABreakdown(message, e, d, n);

  // Auto-play Timer Interval
  useEffect(() => {
    let interval = null;
    if (isPlaying && activeTab === 'step3') {
      interval = setInterval(() => {
        setStepIdx((prev) => {
          if (prev < steps.length - 1) {
            return prev + 1;
          } else {
            setIsPlaying(false);
            return prev;
          }
        });
      }, playSpeed * 1000);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [isPlaying, activeTab, steps.length, playSpeed]);

  return (
    <div className="container">
      <Header />

      <StepNavigation activeTab={activeTab} setActiveTab={setActiveTab} />

      {activeTab === 'step1' && (
        <Step1KeySetup
          p={p}
          setP={setP}
          q={q}
          setQ={setQ}
          e={e}
          setE={setE}
          onNext={() => setActiveTab('step2')}
        />
      )}

      {activeTab === 'step2' && (
        <Step2MessageEncrypt
          message={message}
          setMessage={setMessage}
          p={p}
          q={q}
          e={e}
          d={d}
          onBack={() => setActiveTab('step1')}
          onNext={() => setActiveTab('step3')}
        />
      )}

      {activeTab === 'step3' && (
        <Step3InteractiveStepper
          message={message}
          p={p}
          q={q}
          e={e}
          d={d}
          stepIdx={stepIdx}
          setStepIdx={setStepIdx}
          isPlaying={isPlaying}
          setIsPlaying={setIsPlaying}
          playSpeed={playSpeed}
          setPlaySpeed={setPlaySpeed}
          onBack={() => setActiveTab('step2')}
          onNext={() => setActiveTab('step4')}
        />
      )}

      {activeTab === 'step4' && (
        <Step4SummaryMatrix
          message={message}
          p={p}
          q={q}
          e={e}
          d={d}
          onBack={() => setActiveTab('step3')}
          onRestart={() => {
            setStepIdx(0);
            setIsPlaying(false);
            setActiveTab('step1');
          }}
        />
      )}
    </div>
  );
}
