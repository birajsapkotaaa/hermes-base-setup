# PDF-to-Markdown knowledge extraction repository workflow

Use this when a user asks to download PDFs, convert them to Markdown, remove small copyright notices, extract knowledge, and commit results to GitHub.

## Recommended repository layout

```text
source_markdown/                 # committed converted markdown
extracted_knowledge/             # committed human-readable notes
  <book>_extracted_knowledge.md
scripts/convert_and_extract.py   # deterministic local workflow
logs/conversion_manifest.json    # processed files, outputs, failures
.gitignore                       # exclude source PDFs unless user explicitly asks otherwise
source_pdfs/                     # local only, ignored
```

If PDFs may be copyrighted, prefer a private repository unless the user explicitly requests public.

## Conversion approach

Use local extraction when browser upload converters are brittle, blocked, or too slow for batches:

```bash
uv run --with pymupdf python scripts/convert_and_extract.py
```

PyMuPDF works well for text-based PDFs. For scanned/OCR-heavy documents, fall back to `marker-pdf` after checking disk requirements.

## Copyright cleanup rule

Remove only short, explicit copyright/rights boilerplate lines, such as:

- `copyright`
- `©`
- `all rights reserved`
- `no part of this book/publication`
- publisher permission boilerplate
- ISBN boilerplate lines

Preserve author names, titles, citations, headings, and substantive content. Avoid broad deletion of paragraphs merely because they mention copyright in a substantive way.

## Fabric pattern usage when CLI is unavailable

If Fabric CLI is not installed and Go is unavailable to build it, use checked-out Fabric pattern prompts as extraction schemas and document that choice in `README.md`.

Patterns that worked well for book/report knowledge extraction:

- `extract_wisdom`
- `extract_insights`
- `create_summary`
- `analyze_paper` for report/paper-like documents

## Verification checklist

```bash
python - <<'PY'
from pathlib import Path
import json
repo = Path.cwd()
manifest = json.loads((repo/'logs/conversion_manifest.json').read_text())
print('processed_pdfs', len(manifest['processed']))
print('failures', len(manifest['failures']))
print('source_markdown_files', len(list((repo/'source_markdown').glob('*.md'))))
print('extracted_knowledge_files', len(list((repo/'extracted_knowledge').glob('*.md'))))
PY

git status --short --branch
```

Open a PR from the bot branch to `main` when done.
