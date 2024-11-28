import React from 'react';
import styles from './ProgressBar.module.css';

export default function ProgressBar({ totalAmount, TARGET_AMOUNT }) {
    const percentage = (totalAmount / TARGET_AMOUNT) * 100;
    const progressBarWidth = Math.min(Math.max((totalAmount / TARGET_AMOUNT) * 100, 0), 100);

    return (
        <div className={styles.progressContainer}>
            <div className={styles.progressInfo}>
                <span>Objectif: {TARGET_AMOUNT.toLocaleString()} €</span>
                <span>Actuel: {totalAmount.toLocaleString()} €</span>
            </div>
            <div className={styles.progressBar}>
                <div className={styles.progressFill} style={{ width: `${progressBarWidth}%` }} />
            </div>
            <div className={styles.progressLabel}>
                {percentage.toFixed(1)}%
            </div>
        </div>
    );
}