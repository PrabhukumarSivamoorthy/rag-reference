# BM25 Retrieval

> Part of [retrieval](../README.md) · [back to index](../../README.md)

## What it is

BM25 is a sparse, lexical retriever: it ranks documents by term-frequency
statistics (TF-IDF with document-length normalization), matching the exact words
in the query. No embeddings or API calls — fast, free, and strong at keyword and
rare-term matching (IDs, code, proper nouns) where dense vector search can miss.

## Files

- `BM25.ipynb` — load + chunk a PDF, build a `BM25Retriever`, and query it

## Notes

Requires the `rank-bm25` package. BM25 is the sparse half of
[hybrid search](../hybrid-search/), which fuses it with dense (vector) retrieval.
