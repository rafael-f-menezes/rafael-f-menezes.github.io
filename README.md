# rafael-f-menezes.github.io

Personal academic website of Rafael Ferreira de Menezes, served at https://rafael-f-menezes.github.io. Static HTML, CSS, and a little JavaScript; no build step.

- `index.html`, `research.html`, `publications.html`, `animations.html`, `outreach.html`: the pages.
- `data/publications.json`: the publication list. Edit this file to add a paper; `publications.html` renders it.
- `assets/cv/`: the CV PDF (built from the LaTeX source kept outside this repo).
- `assets/video/`: looping MP4 clips and poster frames, produced by `tools/encode_media.sh` from the original animations.
- `tools/build_pages.py`: optional helper that regenerates the pages from shared header/footer templates.

Serve locally with `python3 -m http.server 8000` and open http://localhost:8000.
