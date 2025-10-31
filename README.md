# Causal-Sentiment-Engine

Causal-Sentiment-Engine is an open-source tool that uses real-time unstructured data (social media, news articles, economic feeds) to identify causal links in stock market movements, map market narratives and detect sentiment anomalies.

> **Disclaimer:** This project is for research and developer use only. Nothing in this repository constitutes financial advice. Always consult a professional before making investment decisions.

## Features

- Collect real-time data from social media, news, blogs, and financial indicators.
- Build a fine-tuned NLP pipeline to extract sentiment, causal relations and narrative themes.
- Align sentiment signals with price movements to highlight anomalies and potential causal effects.
- Visualise market narratives, sentiment anomalies and simulation results.
- Modular backend and API for custom data ingestion, modelling and inference.

## Quickstart

### Installation

Install Causal-Sentiment-Engine from source (editable mode) or using pip. Python 3.9+ is required.

```bash
# Clone the repository
git clone https://github.com/JTall1ne/Causal-Sentiment-Engine.git
cd Causal-Sentiment-Engine

# Install core dependencies
pip install -e .

# Install optional NLP dependencies (transformers and torch) for deep language models
pip install -e .[nlp]
```

### Configuration

Copy the provided environment template to `.env` and fill in your API keys. At minimum you should provide API keys for the data sources you intend to use.

```bash
cp .env.template .env
# Open .env in your editor and set:
# OPENAI_API_KEY=...
# NEWSAPI_API_KEY=...
# TWITTER_BEARER_TOKEN=...
```

### Running the pipeline

Causal-Sentiment-Engine exposes functions and scripts via the Python API. A minimal example to fetch data, build sentiment signals and explore causal links might look like this:

```python
from causal_sentiment_engine import pipeline

# Fetch data and compute sentiment
data = pipeline.fetch_data()
signals = pipeline.compute_sentiment(data)

# Detect anomalies and causal links
anomalies = pipeline.detect_anomalies(signals)
```

The `notebooks/` directory includes Jupyter notebooks demonstrating end-to-end use on sample data. You can run them with Jupyter or your favourite environment.

### Running tests

Install development dependencies and run the test suite:

```bash
pip install -e ".[nlp]"  # to include optional NLP dependencies like transformers/torch
pytest -q
```

## Repository structure

- `src/` – Core Python code for data ingestion, modelling and causal inference.
- `api/` – FastAPI backend for serving model endpoints (e.g., predictions, narrative maps, alerts, simulations).
- `web/` – React front-end for visualising narrative maps, sentiment anomalies and running simulations.
- `notebooks/` – Jupyter notebooks for exploratory data analysis and model training.
- `.github/workflows/` – CI/CD pipelines for testing, linting and documentation generation.

## Contributing

We welcome contributions of all kinds! To get started, please see the [`CONTRIBUTING.md`](CONTRIBUTING.md) guide. Discussions about the roadmap live in the `PROJECT_PLAN.md` document; feel free to open issues or pull requests to suggest improvements.

## License

This project is licensed under the Apache License, Version 2.0. See the [`LICENSE`](LICENSE) file for details.

## Disclaimer

The outputs of this project are for research and educational purposes only and **do not constitute financial advice**. Use this software at your own risk. Always consult a professional financial advisor before making investment decisions.
