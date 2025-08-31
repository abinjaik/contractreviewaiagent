
# Contract Review AI Agent (dev branch)

> End-to-end, local-first contract analysis pipeline that combines an LLM agent (served via **Ollama**) with a lightweight **TF‑IDF + Logistic Regression** text classifier for clause risk labeling.

## Architecture

<p align="center">
  <img src="./docs/architecture.svg" alt="Contract Review AI Agent Architecture"/>
</p>

The agent orchestrates clause extraction and classification, calling a domain-tuned scikit‑learn model as a **tool** while using an on‑prem LLM (e.g., **LLaMA 3 via Ollama**) for reasoning and control.

## Repository & Branch

This README refers to the code in the **`dev`** branch of the repository:

- GitHub: `https://github.com/abinjaik/contractreviewaiagent/tree/dev`

> Tip: Clone the repo and check out the `dev` branch to match paths referenced below.

## Key Components (by folder)

- `agent/` – Agent executor, prompt templates, chunking, and tool wiring.
- `models/` – The scikit‑learn **clause_text_classifier.joblib** (TF‑IDF + Logistic Regression) and training scripts.
- `pipelines/` – Ingestion, preprocessing (batch classification), and persistence of JSON outputs.
- `services/` – Thin API/service layer for running the agent and exposing results.
- `notebooks/` – Experiments and evaluation (optional).
- `config/` – Environment and runtime configuration.
- `docs/` – Documentation assets (**place `architecture.svg` here**).

> Note: Folder names are indicative. Adjust to the actual repo structure in `dev`.

## How It Works

1. **Ingestion & Chunking** – The agent/executor ingests contract files (PDF/Word), normalizes text, and chunks content.
2. **Orchestration (LLM)** – An on‑prem LLM (e.g., **LLaMA 3**) hosted with **Ollama** handles reasoning, tool selection, and flow control.
3. **Risk Classification (Tool)** – The agent calls a local scikit‑learn classifier (`TF‑IDF + LogisticRegression`) to assign labels to clause text.
4. **Persistence** – Structured outputs (JSON) are stored for downstream use (UI, search, analytics).
5. **HMI/UI** – A simple UI or scripts consume the stored results for review.

## Quickstart

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed locally, with a model pulled, e.g.:
  ```bash
  ollama pull llama3
  ```
- (Optional) Poppler/Tesseract for PDF/OCR if needed by your pipeline.

### Setup
```bash
git clone https://github.com/abinjaik/contractreviewaiagent.git
cd contractreviewaiagent
git checkout dev
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### Environment
Create `.env` or configure your environment as needed (example):
```
OLLAMA_HOST=http://localhost:11434
LLM_MODEL=llama3
OUTPUT_DIR=./data/outputs
```

### Train (optional) & Load Classifier
If you need to retrain:
```bash
python models/train_classifier.py  # expects msa_clauses_dataset_v3.csv
```
The pipeline (`TfidfVectorizer` + `LogisticRegression`) is saved as `models/clause_text_classifier.joblib`.

### Run Batch Preprocessing
```bash
python pipelines/preprocess_contracts.py --input ./data/contracts --out ./data/outputs
```
This will extract clauses, classify risk using the saved model, and persist **JSON** results.

### Run the Agent (Online)
```bash
python services/run_agent.py --input ./data/contracts/contract1.pdf
```
The agent will use the preprocessed store when available, and fall back to live analysis as needed.

## Using the Classifier as a Tool

```python
import joblib
from langchain.tools import tool

clf = joblib.load("models/clause_text_classifier.joblib")

@tool("classify_clause_risk", return_direct=True)
def classify_clause_risk(clause_text: str) -> str:
    return clf.predict([clause_text])[0]
```

The LLM agent can call `classify_clause_risk` during execution to produce deterministic, low‑latency labels.

## Industry Practice

- **Hybrid pipeline**: Preprocess in batch (store JSON) + real‑time agent for query/triage.
- **Local-first**: Use Ollama for on‑prem LLM hosting; keep sensitive contracts in your environment.
- **Versioned models**: Store classifier versions and dataset hashes for reproducibility.

## Contributing
Issues and PRs are welcome. Please open an issue for architectural questions or to propose improvements to the `dev` branch pipeline.

## License
TBD (add your license text or `LICENSE` file here).
