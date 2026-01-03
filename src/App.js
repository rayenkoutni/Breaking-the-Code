import React, { useState } from "react";
import { analyzeCiphertext } from "./api";
import "./App.css";

export default function App() {
  const [ciphertext, setCiphertext] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleAnalyze() {
    if (!ciphertext.trim()) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await analyzeCiphertext(ciphertext);
      setResult(data);
    } catch (err) {
      setError("Unable to analyze the ciphertext.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <div className="card">
        <h1>Cryptanalysis Analyzer</h1>
        <p className="subtitle">
          Automatic cryptanalysis without prior knowledge of the key
        </p>

        <textarea
          placeholder="Paste the encrypted text here..."
          value={ciphertext}
          onChange={(e) => setCiphertext(e.target.value)}
        />

        <button onClick={handleAnalyze} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>

        {error && <div className="error">{error}</div>}

        {result && (
          <div className="result">
            <h2>Decrypted Text</h2>
            <pre>{result.plaintext}</pre>

            {result.key && (
              <>
                <h3>Detected Key</h3>
                <code>{result.key}</code>
              </>
            )}

            {result.score !== undefined && (
              <>
                <h3>Confidence Score</h3>
                <code>{result.score}</code>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
