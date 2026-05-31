# Vector Stores

Persisting embedded chunks and running similarity / metadata search — the stage
between [embedding](../embedding/) and [retrieval](../retrieval/).
One notebook per backend.

- [chroma.ipynb](chroma.ipynb) — Chroma (embedded/local persistent store)

Add `faiss/`, `pinecone/`, etc. as notebooks here later. A vector store takes an
embedding function and handles embedding + storage in one call, so these notebooks
build directly on the [embedding](../embedding/) ones.

Each notebook's first cell loads `.env` and runs `env_checker`.

[← back to index](../README.md)
