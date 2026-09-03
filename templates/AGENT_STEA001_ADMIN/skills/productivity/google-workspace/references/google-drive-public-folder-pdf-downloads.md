# Public Google Drive folder PDF downloads

Use this when a user provides public Google Drive folder URLs and asks for batch PDF downloads.

## Primary method: `gdown --folder`

```bash
uvx --from gdown gdown --folder 'https://drive.google.com/drive/folders/FOLDER_ID' -O source_pdfs/drive_1
```

Notes:
- `gdown` may fail partway through a folder if one file cannot retrieve a public link.
- Capture output to a log because `Processing file <id> <name>` lines are useful for retries:

```bash
uvx --from gdown gdown --folder "$FOLDER_URL" -O "$OUT" 2>&1 | tee logs/download.log
```

## Fallback: direct `drive.usercontent.google.com` download

If `gdown` reports:

```text
Cannot retrieve the public link of the file
```

or folder download stops after only some files, parse `Processing file` lines and download each missing file by ID with `curl`:

```bash
curl -L --fail --retry 3 --retry-delay 2 \
  -A 'Mozilla/5.0' \
  "https://drive.usercontent.google.com/download?id=${FILE_ID}&export=download&confirm=t" \
  -o "source_pdfs/${FILENAME}"
```

Verify the result starts with `%PDF-` before treating it as a PDF:

```bash
head -c 5 "$FILE" | grep -q '%PDF-'
```

## Robust retry script sketch

```python
from pathlib import Path
import subprocess

repo = Path.cwd()
outdir = repo / 'source_pdfs'
log = (repo / 'logs/download.log').read_text(errors='ignore').splitlines()

for line in log:
    if not line.startswith('Processing file '):
        continue
    _, _, fid, name = line.split(' ', 3)
    dest = outdir / name
    if dest.exists() and dest.stat().st_size > 0:
        continue
    url = f'https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t'
    subprocess.run([
        'curl', '-L', '--fail', '--retry', '3', '--retry-delay', '2',
        '-A', 'Mozilla/5.0', url, '-o', str(dest)
    ], check=False)
    if not dest.exists() or dest.read_bytes()[:5] != b'%PDF-':
        print('FAILED', fid, name)
        if dest.exists():
            dest.unlink()
```

## Pitfalls

- `gdown` versions differ; do not rely on unsupported flags such as `--remaining-ok` unless confirmed by `gdown --help`.
- Public Drive folders can contain subfolders; search recursively for `*.pdf` after download.
- Some files work in a browser but not via `gdown`; the `drive.usercontent.google.com` endpoint often succeeds.
