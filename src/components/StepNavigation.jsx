import React from 'react';
import { Key, MessageSquare, TestTube, BarChart3 } from 'lucide-react';

export default function StepNavigation({ activeTab, setActiveTab }) {
  const steps = [
    { id: 'step1', label: '1. Key Setup', icon: Key },
    { id: 'step2', label: '2. Message & Encrypt', icon: MessageSquare },
    { id: 'step3', label: '3. Interactive Stepper', icon: TestTube },
    { id: 'step4', label: '4. Summary Matrix', icon: BarChart3 }
  ];

  return (
    <nav className="nav-tabs">
      {steps.map((step) => {
        const Icon = step.icon;
        const isActive = activeTab === step.id;
        return (
          <button
            key={step.id}
            className={`nav-tab-btn ${isActive ? 'active' : ''}`}
            onClick={() => setActiveTab(step.id)}
          >
            <Icon size={18} />
            <span>{step.label}</span>
          </button>
        );
      })}
    </nav>
  );
}
