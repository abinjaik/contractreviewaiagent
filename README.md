
# Contract Review AI Agent (On-premise, Opensource)

> End-to-end, local-first contract review AI Agent that combines  LLAMA 3.18B LLM  (served via **Ollama**) with a lightweight **TF‑IDF + Logistic Regression** text classifier for clause risk labeling.

## Architecture

<p align="center">
  <img src="./archdiagrams/ContractReviewAIAgent.svg" alt="Contract Review AI Agent Architecture"/>
</p>

The agent orchestrates clause extraction and classification, calling a domain-tuned scikit‑learn model as a **tool** while using an on‑prem LLM (e.g., **LLaMA 3 via Ollama**) for reasoning, clause extraction and control.


## Key Components (by folder)

- `/contractreviewagent.py, /agentexecutor.py` – Agent executor, prompt templates, chunking, and tool wiring.
- `/tools ,/tools/regressionmodeltrainer/` – The scikit‑learn **clause_text_classifier.joblib** (TF‑IDF + Logistic Regression) , labelled datasets and training scripts.
- `archdiagrams/` – Documentations, Architecture diagrams etc.


## How It Works

1. **Ingestion & Chunking** – The agent/executor ingests contract text , normalizes text, and chunks content.
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
git checkout main
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```



### Train (optional) & Load Classifier
If you need to retrain the classifier:
```bash
python /tools/regressionmodeltrainer/linearmodelclassification.py  # expects msa_clauses_dataset_v3.csv
```
The classifier model (`TfidfVectorizer` + `LogisticRegression`) is saved as `clause_text_classifier.joblib`.




### Run the Agent 
```bash
python agentexecutor.py --input CONTRACTTEXT
```
This will save the output JSON inside extracted_clauses

#

The LLM agent can call `classify_clause_risk` during execution to produce deterministic, low‑latency labels.

## Future Plans
- Set up and configure jobs to parse, extract the PDF, Word content and ingest it to  the Agent
- Store the JSON output from Agent to a Object store and Map with the source document
- Seemless integration between Web Front end, and Object store
- Setup MLFlow - Tracebility, Auditing 

## License
Apache 3.0 
