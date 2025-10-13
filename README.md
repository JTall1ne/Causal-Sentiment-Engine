# Causal-Sentiment-Engine

Causal-Sentiment-Engine is an open-source project that uses real-time unstructured data (social media, news articles, economic feeds) to identify causal links in stock market movements, map market narratives and detect sentiment anomalies.

## Project Goals

- Develop a transformer-based NLP model to extract sentiment and narrative causal signals from streaming data sources.
- Build a real-time data ingestion pipeline (e.g. Kafka) to process social media posts, news articles and economic data feeds.
- Provide a probabilistic reasoning layer that goes beyond simple correlation to infer potential causation between narratives and market movements.
- Offer narrative maps and impact simulations to help investors understand how narratives might influence markets.
- Expose the model via a FastAPI service so other applications can consume narrative maps, anomaly alerts and simulations.
- Deliver a React-based web dashboard that visualises narrative maps, sentiment anomalies and simulation results.

## Repository Structure

- `src/` – Core Python code for data ingestion, modelling and causal inference.
- `api/` – FastAPI backend serving model endpoints (narrative maps, anomaly alerts, simulations).
- `web/` – React front-end for visualising narratives, sentiment anomalies and running simulations.
- `notebooks/` – Jupyter notebooks for exploratory data analysis and model training.
- `.github/workflows/` – CI/CD pipelines for testing, building and documentation generation.

## Contributing

We welcome contributions of all kinds! To get started, please open an issue to discuss your idea or bug report, or submit a pull request. A `CONTRIBUTING.md` guide and `PROJECT_PLAN.md` roadmap will be added to outline processes and priorities.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.
