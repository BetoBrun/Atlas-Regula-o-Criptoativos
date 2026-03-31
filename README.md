# Crypto Regulation Atlas (Bilingual PT/EN)

A static GitHub Pages-ready observatory for comparing global crypto regulation with an interactive world map, filters, rankings, bilingual interface (Português/English), thematic explanatory sections, a comparative methodology block, and a lightweight jurisdiction comparison tool.

## What changed in this version
This version was adjusted to absorb the broader conceptual architecture of the project as an **analytical observatory**, not just a directory of laws. It now includes:
- a stronger homepage narrative
- methodology and thematic-pillar sections
- observatory-style hero metrics
- a country comparison module
- richer country panels with analytical reading and inferred institutional model

## Features
- Interactive world map with score-based country coloring
- Portuguese / English switcher with flag buttons
- Country detail panel with analytical interpretation
- Search and filters by region, trend, score, and topic
- Ranking of most favorable and most restrictive jurisdictions
- Table view
- Jurisdiction comparison table
- Static API in JSON (`/api`)
- GitHub Pages-ready static architecture

## Project structure
- `index.html` — main bilingual frontend
- `style.css` — UI styling
- `script.js` — map, filtering, i18n, rendering, comparison
- `data/manual-overrides.json` — editorial dataset
- `api/` — generated JSON API
- `scripts/build_api.py` — static API builder
- `scripts/run_pipeline.py` — minimal pipeline entrypoint

## Run locally
Because the frontend uses `fetch()` to load JSON, open the project with a simple local server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## GitHub Pages deployment
1. Push the repository to GitHub.
2. In **Settings > Pages**, select **Deploy from branch**.
3. Choose the main branch and `/root`.
4. Save. The site will publish from the repository root.

## Editing data
Update `data/manual-overrides.json`.
Then rebuild:

```bash
python scripts/build_api.py
```

## Methodological note
The score rewards:
- legal certainty
- proportionality
- innovation openness
- healthy conditions for exchanges
- room for stablecoins and tokenization
- mining / infrastructure feasibility
- lower risk of excessive state centralization

It does **not** assume that either deregulation or heavy regulation is automatically positive.

## Limitations
- Scores are editorial and comparative, not legal advice.
- Country profiles are simplified summaries.
- The pipeline is static-first and meant to be expanded with curated official feeds.
