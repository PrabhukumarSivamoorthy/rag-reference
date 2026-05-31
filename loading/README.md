# Loading

Document loaders — turning raw source files into text/documents ready for
[chunking](../chunking/). One notebook per source type.

- [pdf.ipynb](pdf.ipynb) — load PDFs (sample: `assets/sample-docs/sdlc-end-to-end.pdf`)
- [html.ipynb](html.ipynb) — load HTML (sample: `assets/RAG_Courses.html`)
- [markdown.ipynb](markdown.ipynb) — load Markdown via `TextLoader` (sample: `README.md`)
- [python.ipynb](python.ipynb) — load `.py` source via `PythonLoader` (sample: `env_checker.py`)

Each notebook's first cell loads `.env` and runs `env_checker` to verify setup.

[← back to index](../README.md)
