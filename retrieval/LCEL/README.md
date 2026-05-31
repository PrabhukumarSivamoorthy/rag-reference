# LCEL (LangChain Expression Language)

> Part of [retrieval](../README.md) · [back to index](../../README.md)

## What it is

LCEL composes components into a chain using the `|` pipe operator —
e.g. `retriever | prompt | llm | parser`. The composed `Runnable` supports
streaming, batching, and async invocation without extra code, which makes it
the idiomatic way to wire up a RAG query flow.

## Files

- `LCEL.ipynb` — runnable walkthrough (planned)

## Notes

_TODO: build a retrieval chain over the `rag_reference` Chroma collection._
