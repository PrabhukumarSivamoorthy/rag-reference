# Embedding

Turning text (chunks) into dense vectors — the stage between
[chunking](../chunking/) and the [vector store](../vector-stores/).
One notebook per embedding provider.

- [openai.ipynb](openai.ipynb) — OpenAI API embeddings (needs `OPENAI_API_KEY`)
- [huggingface.ipynb](huggingface.ipynb) — local sentence-transformers (no API key)

Embeddings and vector stores vary independently — you can swap the model here
without changing the store. Reusable embedding clients can live in [shared/](../shared/).

Each notebook's first cell loads `.env` and runs `env_checker`.

[← back to index](../README.md)
