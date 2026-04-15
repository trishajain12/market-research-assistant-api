import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [report, setReport] = useState(null);
  const [savedReports, setSavedReports] = useState([]);
  const [loading, setLoading] = useState(false);
  const [loadingReports, setLoadingReports] = useState(false);
  const [error, setError] = useState("");

  const fetchSavedReports = async () => {
    setLoadingReports(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/reports");

      if (!response.ok) {
        throw new Error("Failed to load saved reports");
      }

      const data = await response.json();
      setSavedReports([...data].reverse());
    } catch (err) {
      setError(err.message || "Something went wrong while loading reports");
    } finally {
      setLoadingReports(false);
    }
  };

  useEffect(() => {
    fetchSavedReports();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!topic.trim()) {
      setError("Please enter a topic.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/plan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ topic: topic.trim() }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate report");
      }

      const data = await response.json();
      setReport(data);
      setTopic("");
      await fetchSavedReports();
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const handleSelectReport = (selectedReport) => {
    setReport(selectedReport);
    setError("");
  };

  const handleDeleteReport = async (event, reportId) => {
    event.stopPropagation();

    try {
      const response = await fetch(`http://127.0.0.1:8000/reports/${reportId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Failed to delete report");
      }

      const updatedReports = savedReports.filter(
        (savedReport) => savedReport.report_id !== reportId
      );

      setSavedReports(updatedReports);

      if (report && report.report_id === reportId) {
        setReport(null);
      }
    } catch (err) {
      setError(err.message || "Something went wrong while deleting the report");
    }
  };

  const handleClearReports = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/reports", {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Failed to clear reports");
      }

      setSavedReports([]);
      setReport(null);
      setError("");
    } catch (err) {
      setError(err.message || "Something went wrong while clearing reports");
    }
  };

  const isSelectedReport = (savedReport) => {
    return report && report.report_id === savedReport.report_id;
  };

  return (
    <div className="page-layout">
      <aside className="sidebar">
        <div className="sidebar-header">
          <div>
            <p className="sidebar-label">History</p>
            <h2>Saved Reports</h2>
          </div>
          <button
            className="clear-button"
            onClick={handleClearReports}
            disabled={savedReports.length === 0}
          >
            Clear All
          </button>
        </div>

        {loadingReports ? (
          <p className="sidebar-text">Loading reports...</p>
        ) : savedReports.length === 0 ? (
          <p className="sidebar-text">No saved reports yet.</p>
        ) : (
          <ul className="report-list">
            {savedReports.map((savedReport) => (
              <li key={savedReport.report_id}>
                <button
                  className={`report-list-button ${
                    isSelectedReport(savedReport) ? "selected-report" : ""
                  }`}
                  onClick={() => handleSelectReport(savedReport)}
                >
                  <div className="report-list-top">
                    <div className="report-meta">
                      <span className="report-topic">{savedReport.topic}</span>
                      <span className="report-type">
                        {savedReport.research_type}
                      </span>
                    </div>

                    <button
                      className="delete-button"
                      onClick={(event) =>
                        handleDeleteReport(event, savedReport.report_id)
                      }
                      title="Delete report"
                    >
                      ×
                    </button>
                  </div>
                </button>
              </li>
            ))}
          </ul>
        )}
      </aside>

      <main className="app-container">
        <div className="hero">
          <p className="hero-label">AI Research Workflow</p>
          <h1>Market Research Assistant</h1>
          <p className="subtitle">
            Enter a topic to generate a structured research plan.
          </p>

          <form onSubmit={handleSubmit} className="topic-form">
            <input
              type="text"
              placeholder="Try: IBM AI strategy"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              className="topic-input"
            />
            <button type="submit" className="submit-button" disabled={loading}>
              {loading ? "Generating..." : "Generate"}
            </button>
          </form>

          {error && <p className="error-text">{error}</p>}
        </div>

        {report ? (
          <div className="report-card">
            <div className="report-header">
              <div>
                <p className="section-label">Current Report</p>
                <h2>Research Plan</h2>
              </div>
              <span className="report-badge">{report.research_type}</span>
            </div>

            <div className="report-summary-grid">
              <div className="summary-item">
                <span className="summary-label">Report ID</span>
                <span className="summary-value report-id">{report.report_id}</span>
              </div>
              <div className="summary-item">
                <span className="summary-label">Topic</span>
                <span className="summary-value">{report.topic}</span>
              </div>
              <div className="summary-item full-width">
                <span className="summary-label">Next Step</span>
                <span className="summary-value">{report.next_step}</span>
              </div>
            </div>

            <section>
              <h3>Subquestions</h3>
              <ul className="content-list">
                {report.subquestions?.map((question, index) => (
                  <li key={index}>{question}</li>
                ))}
              </ul>
            </section>

            <section>
              <h3>Report Outline</h3>
              <ul className="content-list">
                {report.report_outline?.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </section>

            <section>
              <h3>Keywords</h3>
              <div className="chip-row">
                {report.keywords?.map((keyword, index) => (
                  <span className="chip" key={index}>
                    {keyword}
                  </span>
                ))}
              </div>
            </section>

            <section>
              <h3>Suggested Sources</h3>
              <ul className="content-list">
                {report.suggested_sources?.map((source, index) => (
                  <li key={index}>{source}</li>
                ))}
              </ul>
            </section>

            <section>
              <h3>Starter Sources</h3>
              <ul className="content-list">
                {report.starter_sources?.map((source, index) => (
                  <li key={index}>
                    <a href={source.url} target="_blank" rel="noreferrer">
                      {source.label}
                    </a>
                  </li>
                ))}
              </ul>
            </section>
          </div>
        ) : (
          <div className="empty-state">
            <p className="section-label">No Selection</p>
            <h2>No report selected</h2>
            <p>Generate a new report or choose one from the sidebar.</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;