# Semantic Chunking

> Part of [chunking](../README.md) · [back to index](../../README.md)

## What it is

`SemanticChunker` embeds each sentence and inserts a break where the embedding
similarity between consecutive sentences drops. Chunks therefore hold a coherent
idea and their sizes vary with the content — unlike fixed character/token windows.

## Files

- `semantic.ipynb` — load the PDF, then split with `SemanticChunker`
  (`OpenAIEmbeddings`, `breakpoint_threshold_type="percentile"`)

## Notes

Requires `langchain-experimental` and an embeddings model. It calls the embedding
model *during splitting*, so it costs more time/money than the character/token
splitters — `breakpoint_threshold_type` (`percentile` / `standard_deviation` /
`interquartile` / `gradient`) tunes how aggressively it breaks.
