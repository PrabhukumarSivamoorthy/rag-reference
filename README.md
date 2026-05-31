# rag-reference

A hands-on reference of Retrieval-Augmented Generation (RAG) patterns —
architectures, chunking strategies, and retrieval techniques — each with a
short explanation and a runnable example.

## Setup

```bash
uv sync                         # create the venv from pyproject.toml
cp .env.example .env            # then fill in your API keys
uv run python env_checker.py    # verify .env + installed packages
uv run jupyter lab              # open the notebooks
```

## Index

### Architectures
End-to-end RAG patterns — see [architectures/](architectures/).

- [Naive RAG](architectures/naive-rag/)
- [Hierarchical RAG](architectures/hierarchical-rag/)
- [Graph RAG](architectures/graph-rag/)
- [Agentic RAG](architectures/agentic-rag/)
- [Self-RAG](architectures/self-rag/)
- [HyDE](architectures/hyde/)

### Loading
Turning raw source files into text/documents — see [loading/](loading/).

- [PDF](loading/pdf.ipynb)
- [HTML](loading/html.ipynb)
- [Markdown](loading/markdown.ipynb)
- [Python (.py)](loading/python.ipynb)

### Chunking
How documents are split before embedding — see [chunking/](chunking/).

- [Fixed-size](chunking/fixed-size/)
- [Recursive](chunking/recursive/)
- [Semantic](chunking/semantic/)
- [Sentence-window](chunking/sentence-window/)
- [Document-specific](chunking/document-specific/)

### Embedding
Turning chunks into dense vectors — see [embedding/](embedding/).

- [OpenAI](embedding/openai.ipynb)
- [HuggingFace (local)](embedding/huggingface.ipynb)

### Vector stores
Persisting and searching embedded chunks — see [vector-stores/](vector-stores/).

- [Chroma](vector-stores/chroma.ipynb)

### Retrieval
Improving what gets retrieved and how it's ranked — see [retrieval/](retrieval/).

- [Hybrid search](retrieval/hybrid-search/)
- [Reranking](retrieval/reranking/)
- [Query transformation](retrieval/query-transformation/)
- [LCEL](retrieval/LCEL/)

### Supporting
- [shared/](shared/) — reusable utils, embeddings, sample data
- [assets/](assets/) — diagrams, images, sample documents

## Stack

Python 3.12 · [uv](https://docs.astral.sh/uv/) · Chroma (vector store) ·
OpenAI / Anthropic models · LangSmith tracing
