import React from 'react';
import styles from './CalculatorInput.module.css';

export default function CalculatorInput({ expression, setExpression, calculateExpression, error }) {
    return (
        <div className={styles.calculatorSection}>
            <h2 className={styles.sectionTitle}>Calculer un financement</h2>
            <div className={styles.calculator}>
                <input
                    type="text"
                    value={expression}
                    onChange={(e) => setExpression(e.target.value)}
                    placeholder="Entrez une expression NPI (ex: '3 4 +')"
                    className={styles.input}
                />
                <button onClick={calculateExpression} className={styles.button}>
                    Calculer
                </button>
            </div>
            {error && <div className={styles.error}>{error}</div>}
        </div>
    );
}
