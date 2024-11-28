import React from 'react';
import styles from './ProgressBar.module.css';

export default function ProgressBar({ totalAmount, TARGET_AMOUNT }) {
    const progressPercentage = Math.min(Math.max((totalAmount / TARGET_AMOUNT) * 100, 0), 100);
  
    return (
      <div className={styles.progressContainer}>
        <div className={styles.progressInfo}>
          <span>Objectif: {TARGET_AMOUNT.toLocaleString()} €</span>
          <span>Actuel: {Math.abs(totalAmount).toLocaleString()} €</span>
        </div>
        <div className={styles.progressBar}>
          <div className={styles.progressFill} style={{ width: `${progressPercentage}%` }} />
        </div>
        <div className={styles.progressLabel}>
          {progressPercentage.toFixed(1)}%
          {totalAmount < 0 && <span className={styles.negative}> (Négatif)</span>}
        </div>
      </div>
    );
  }
