# Sound Creations Ltd Company Profile

Company profile for **Sound Creations Ltd** (https://soundcreationsltd.com), built by Pimofy Digital. Current version: **1.3.0** (see `CHANGELOG.md`).

One source, two outputs:
- **Web profile:** `index.html` (responsive; works on GitHub Pages or any static host).
- **Printable PDF (A4 landscape, 297 x 210 mm, 23 pages):** `dist/Sound-Creations-Company-Profile.pdf`, generated from the same `index.html` with print CSS.

## Pages
1 Cover - 2 Contents - 3 Who we are - 4 Our journey - 5 Vision, mission & values - 6 How we work - 7 Our solutions - 8 Professional audio - 9 Acoustics & engineering - 10 Industries we serve - 11 Projects showcase - 12-15 Featured projects (West Nairobi School, RPF Rubavu Multipurpose Hall, Sarit Expo Centre, Parklands Baptist Church) - 16-17 Case studies - 18 Other completed projects - 19 Our clients - 20 Brands & partners (15 brands) - 21 Why choose us (4 Google reviews) - 22 Regional reach - 23 Contact.

## Structure
| Path | What |
|---|---|
| `index.html` | All profile content |
| `assets/css/profile.css` | Brand styles: screen layout, phone layout and `@media print` A4 landscape pages |
| `assets/fonts/` | Space Grotesk (headings) + Inter (body), self-hosted |
| `assets/img/logo-color.png`, `logo-white.png` | Official Sound Creations logos (from soundcreationsltd.com) |
| `assets/img/photos/` | Profile photography (taken from the 2026 PDF profile) |
| `assets/img/projects/` | Real Sound Creations project photos |
| `assets/img/clients/` | Client logos for page 19 (c01-c19 corporate, c20-c32 worship, c33-c43 education) |
| `assets/img/brands/` | Manufacturer logos for the brands page |
| `build/build-pdf.py` | Rebuilds the PDF with WeasyPrint |
| `docs/FACTS-NEEDED.md` | Items still worth confirming with Sound Creations |
| `AGENTS.md` | Rules for anyone (human or AI) editing this repo |

## Live web page (GitHub Pages)
Published from `main` / root at **https://moselanto.github.io/sound-creationsltdprofile/** (Settings > Pages > Deploy from a branch > `main` / `/ (root)`). The "Download PDF" button links to `dist/Sound-Creations-Company-Profile.pdf`, so rebuild and commit the PDF with every change. `.nojekyll` makes GitHub serve the files as they are.

## Build the PDF
```
pip install weasyprint
python3 build/build-pdf.py
```
Or open `index.html` in Chrome > Print > Save as PDF (A4 landscape, margins None, background graphics on).

## Brand
Near-black `#0B0A10`, Sound Creations red `#E0262B` (deep `#BA0B0B`), purple `#A98BD6` (deep `#624489`) and white; Space Grotesk headings, Inter body. Tagline: "If it sounds good, it's Sound Creations."
