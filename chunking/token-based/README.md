# Token-based Chunking

> Part of [chunking](../README.md) · [back to index](../../README.md)

## What it is

`TokenTextSplitter` sizes chunks by **tokens** (via `tiktoken`) instead of
characters. Since model context windows and embedding limits are expressed in
tokens, token-based chunks map directly onto those limits — character counts
don't, because characters-per-token varies with the text.

## Files

- `token-based.ipynb` — load PDF/HTML, then split with `TokenTextSplitter`
  (`cl100k_base` encoding), verifying chunks stay within the token budget

## Notes

Use the encoding that matches your model (`cl100k_base` for `text-embedding-3-*`
and GPT-4-class models).
