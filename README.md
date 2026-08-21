# CBE 3610 — Course Materials

Welcome — this repository hosts lecture notes, example problems, and Google Colab notebooks for CBE 3610 (Chemical Reaction Engineering).

Live course site (students)
- Course website (GitHub Pages): https://dr-rachel-bg-teaching.github.io/CBE3610/
  - Use the site to browse notebooks and lecture PDFs. Open any notebook in Colab by clicking its link on the site.

Quick links
- Repository: https://github.com/dr-rachel-bg-teaching/CBE3610
- Open a notebook in Colab:
  https://colab.research.google.com/github/dr-rachel-bg-teaching/CBE3610/blob/main/colab-notebooks/<notebook-filename>.ipynb
- Download all materials (ZIP): https://github.com/dr-rachel-bg-teaching/CBE3610/archive/refs/heads/main.zip
- Releases: https://github.com/dr-rachel-bg-teaching/CBE3610/releases

Student instructions (short)
1. Open a notebook:
   - Use the course site and click any notebook link, or paste a notebook filename into the Colab URL above.
2. Run the notebook:
   - In Colab: Runtime → Run all.
   - If a notebook requires data, follow the notebook top-cell instructions (download files or mount Google Drive).
3. Package dependencies:
   - If a notebook needs extra packages, run the provided install cell (example): `!pip install some-package`.
4. Problems?:
   - Open an Issue in this repository (label it “student-report”) or email course staff (see Contact below).

Instructor / maintainer notes
- The student-facing site is at /docs/index.md and is auto-generated from colab-notebooks/ by scripts/generate_index.py.
- To regenerate the index locally:
  - python3 scripts/generate_index.py --owner dr-rachel-bg-teaching --repo CBE3610 --branch main
  - Commit docs/index.md and push to main so Pages updates.
- To force a Pages rebuild:
  - git commit --allow-empty -m "trigger pages build"
  - git push origin main

Repository layout
- README.md — this file
- docs/ — GitHub Pages content (index.md lists notebooks)
- colab-notebooks/ — Jupyter notebooks intended for Colab
- lecture-notes/ — PDFs for lecture use
- handbook/ — course handbook PDF
- assets/ — images, datasets used by notebooks
- scripts/ — helper scripts (e.g., generate_index.py)

Publishing checklist (maintainers)
- Merge branch rename/syllabus-filenames into main (if not already).
- Ensure docs/index.md exists on main (auto-generated script above).
- In GitHub: Settings → Pages → Source: Branch `main`, Folder `/docs` → Save.
- After publication, paste the final Pages URL into this README (already done).

Contributing
- Use topic branches and open a pull request for changes (e.g., `update-lecture-07`).
- For major content or solution changes, open an Issue first.

License & citation
- Suggested licenses:
  - Content (handbook, lecture notes): CC BY 4.0 (or your preferred CC)
  - Code in notebooks: MIT (or your preferred code license)
- Citation:
  Getman, R. (2026). CBE 3610 Python Notebooks and Course Materials. Department of Chemical and Biomolecular Engineering, The Ohio State University. https://github.com/dr-rachel-bg-teaching/CBE3610

Contact
- Course staff: Rachel Getman — getman.11@osu.edu
