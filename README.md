# CBE 3610 — Course Materials

_Last updated: 2026-08-21_

These materials support CBE 3610 (Chemical Reaction Engineering) and include:

- Python notebooks for in‑class activities and refreshers adapted from CBE2345 (Computational Methods).
- Lecture notes (gap-style notes for in‑class completion and filled-in PDFs).
- A handbook collecting useful equations, methods, definitions, and reference material.

Quick links

- Course site (GitHub Pages): https://dr-rachel-bg-teaching.github.io/CBE3610/
- Course index (docs): docs/index.md — https://github.com/dr-rachel-bg-teaching/CBE3610/blob/main/docs/index.md
- Notebooks: colab-notebooks/
- Lecture notes: lecture-notes/
- Handbook: handbook/
- Download all materials (ZIP): https://buckeyemailosu-my.sharepoint.com/:u:/g/personal/getman_11_osu_edu/IQD0aJsO5uxzSL4hUwoYFnnaAaEWHZska_4aT0H9j6CiFeg?e=npDARy

Open the notebooks

- View on GitHub: click any `.ipynb` file to see a rendered view.
- Open in Google Colab: use the "Open in Colab" badges below to launch a notebook in Colab.

Colab notebooks (with Open-in-Colab badge example)

- Example badge (paste this next to each notebook link to show a visual badge):

  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-rachel-bg-teaching/CBE3610/blob/main/colab-notebooks/00_Refresher_NumericalIntegration_Interpolation_Regression.ipynb)

- Refresher — Initial Value Problems  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-rachel-bg-teaching/CBE3610/blob/main/colab-notebooks/01_Refresher_InitialValueProblems.ipynb)

- Refresher — Numerical Integration, Interpolation & Regression  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-rachel-bg-teaching/CBE3610/blob/main/colab-notebooks/00_Refresher_NumericalIntegration_Interpolation_Regression.ipynb)

- Refresher — fsolve  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-rachel-bg-teaching/CBE3610/blob/main/colab-notebooks/02_Refresher_fsolve.ipynb)

- Completion activity — Steady state variability  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-rachel-bg-teaching/CBE3610/blob/main/colab-notebooks/03_COMPLETION_ACTIVITY_SteadyStateVariability.ipynb)

(See docs/index.md for the full list of notebooks and direct Colab links.)

Repository structure (suggested)

- README.md — this file
- handbook/ — PDF (and optional source .docx/.md) of the course handbook
- lecture-notes/ — gap-style and filled instructor notes (PDFs)
- colab-notebooks/ — Jupyter notebooks intended to open in Colab
- assets/ — images, diagrams, datasets used by notebooks
- LICENSE — license for content and code
- requirements.txt or environment.yml — (optional) reproducible environment

Recommended workflow

- Keep editable source files (e.g., handbook DOCX or Markdown) in `handbook/source/` and export a PDF for students in `handbook/` for smooth in-browser viewing.
- Keep solutions separated from student-facing notebooks (e.g., `colab-notebooks/solutions/` or in a private repo).
- Name files clearly and include a short header cell in each notebook listing required packages and a reproducible kernel spec.

Running notebooks locally

- Install dependencies (example): `pip install -r requirements.txt`
- Prefer using a conda environment if you distribute an `environment.yml`.

Contributing

- Use branches and pull requests for changes (e.g., `update-lecture-03`).
- Open an Issue for major content or solution changes before merging. For student-reported problems (broken links, download access issues, missing files) label issues `student-report`.

Citation

Getman, R. (2026). CBE 3610 Python Notebooks and Course Materials. Department of Chemical and Biomolecular Engineering, The Ohio State University. https://github.com/dr-rachel-bg-teaching/CBE3610

License

- Suggested: Content (handbook, lecture notes): Creative Commons Attribution 4.0 International (CC BY 4.0).  
- Code in notebooks: MIT License (or choose a different code license).  
See LICENSE for full terms.

Contact

Rachel Getman — getman.11@osu.edu