# Evaluation

Measuring how well the RAG pipeline works — both the **retrieval** stage
(did we fetch the right context?) and the **generation** stage (did the answer
use that context faithfully and helpfully?).

## What this covers

**Retrieval metrics**
- Context precision / recall — is the retrieved context relevant and complete?
- Hit rate, MRR, nDCG — ranking quality of the retriever

**Generation metrics**
- Faithfulness / groundedness — is the answer supported by the context (no hallucination)?
- Answer relevance — does it actually address the question?
- Answer correctness — vs. a reference answer

**Approaches**
- LLM-as-judge scoring
- Frameworks: RAGAS, LangSmith evaluators, DeepEval
- Golden / reference test sets

## Files

**Faithfulness** — is the answer grounded in the retrieved context?
- `faithfulness_concept.ipynb` — the metric from scratch (LLM-as-judge)
- `faithfulness_with_examples.ipynb` — full RAG pipeline + RAGAS `Faithfulness`

**Context precision** — are relevant contexts ranked near the top?
- `context-precision.ipynb` — the metric from scratch (LLM-as-judge)
- `context-precision_with_examples.ipynb` — full RAG pipeline + RAGAS context precision

**Other**
- `string-evaluator.ipynb` — compare a prediction vs. reference string
  (`langchain_classic` `string_distance` / `embedding_distance`)

> **RAGAS note:** ragas 0.4.x does `from langchain_community.chat_models.vertexai import
> ChatVertexAI`, a submodule removed in langchain-community 0.4.x. The `*_with_examples`
> notebooks register a tiny stub module in their setup cell (it only imports the name,
> never instantiates it) so ragas works without the heavy `langchain-google-vertexai` package.

[← back to index](../README.md)
