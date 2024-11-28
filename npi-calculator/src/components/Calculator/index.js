import { useState, useEffect } from 'react';
import ProgressBar from '../ProgressBar';
import CalculatorInput from '../CalculatorInput';
import HistoryList from '../HistoryList';
import styles from './Calculator.module.css';

const TARGET_AMOUNT = 100000;

export default function Calculator() {
  const [expression, setExpression] = useState('');
  const [history, setHistory] = useState([]);
  const [error, setError] = useState('');
  const [totalAmount, setTotalAmount] = useState(0);

  useEffect(() => {
    const loadHistory = async () => {
      try {
        const response = await fetch('http://localhost:8000/calculations');
        if (!response.ok) throw new Error('Failed to load history');
        const data = await response.json();
        setHistory(data);
        setTotalAmount(data.reduce((sum, item) => sum + item.result, 0));
      } catch (error) {
        setError('Failed to load history');
      }
    };
    
    loadHistory();
  }, []);

  const calculateExpression = async () => {
    try {
      setError('');
      const response = await fetch('http://localhost:8000/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ expression })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail);
      }

      const data = await response.json();
      const newHistory = [...history, { expression, result: data.result }];
      setHistory(newHistory);
      setTotalAmount(prev => prev + data.result);
      setExpression('');
    } catch (error) {
      setError(error.message);
    }
  };

  const downloadCSV = () => window.open('http://localhost:8000/calculations/csv', '_blank');

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Projet de financement AYOMI.FR</h1>
      <ProgressBar totalAmount={totalAmount} TARGET_AMOUNT={TARGET_AMOUNT} />
      <CalculatorInput
        expression={expression}
        setExpression={setExpression}
        calculateExpression={calculateExpression}
        error={error}
      />
      <HistoryList history={history} downloadCSV={downloadCSV} />
    </div>
  );
}
