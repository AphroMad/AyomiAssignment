import React from 'react';
import styles from './HistoryList.module.css';

export default function HistoryList({ history, downloadCSV }) {
    return (
        <div className={styles.history}>
            <div className={styles.historyHeader}>
                <h2>Historique des financements</h2>
                <button onClick={downloadCSV} className={styles.downloadButton}>
                    Télécharger CSV
                </button>
            </div>
            <div className={styles.historyList}>
                {[...history].reverse().map((item, index) => (
                    <div key={index} className={styles.historyItem}>
                        <span>{item.expression}</span>
                        <span>{item.result.toLocaleString()} €</span>
                    </div>
                ))}
            </div>
        </div>
    );
}
