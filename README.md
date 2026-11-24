# Sound Creations Ltd Company Profile

Company profile for **Sound Creations Ltd** (https://soundcreationsltd.com), built by Pimofy Digital. Current version: **1.16.2** (see `CHANGELOG.md`).

One source, two outputs:
- **Web profile:** `index.html` (responsive; works on GitHub Pages or any static host).
- **Printable PDF (A4 landscape, 297 x 210 mm, 19 pages):** `dist/Sound-Creations-Company-Profile.pdf`, generated from the same `index.html` with print CSS.

## Pages
1 Cover - 2 Contents - 3 Our journey - 4 How we work - 5 Professional audio - 6 Acoustics & engineering - 7 Projects showcase - 8-15 Featured projects (West Nairobi School, RPF Rubavu Multipurpose Hall, Sarit Expo Centre, Parklands Baptist Church, PCEA Kahawa Farmers Church, CITAM Buruburu, Playza Prestige Plaza, COVO NBO) - 16 Other completed projects - 17 Brands & partners (15 brands) - 18 Regional reach - 19 Contact.

## Structure
| Path | What |
|---|---|
| `index.html` | All profile content |
| `assets/css/profile.css` | Brand styles: screen layout, phone layout and `@media print` A4 landscape pages |
| `assets/fonts/` | Space Grotesk (headings) + Inter (body), self-hosted |
| `assets/img/logo-color.png`, `logo-white.png` | Official Sound Creations logos (from soundcreationsltd.com) |
| `assets/img/photos/` | Profile photography (taken from the 2026 PDF profile) |
| `assets/img/projects/` | Real Sound Creations project photos |
| `assets/img/brands/` | Manufacturer logos for the brands page |
| `build/build-pdf.py` | Rebuilds the PDF with WeasyPrint |
| `build/build-svg.py` | Rebuilds the layered, Illustrator-editable SVG pages in `illustrator/svg/` |
| `build/build-team-package.py` | Builds the team share zip `dist/Sound-Creations-Company-Profile-2026-Team-Package.zip` (PDF + page previews + Illustrator package + READ-ME-FIRST from `build/team-READ-ME-FIRST.txt`) |
| `illustrator/` | Illustrator package: layered SVG per page, fonts, full-resolution images, print PDF, README-Illustrator.txt, open-all-in-illustrator.jsx |
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

## Illustrator
After any change run `python3 build/build-pdf.py && python3 build/build-svg.py`, copy the PDF into `illustrator/`, then `python3 build/build-team-package.py`, and commit everything. Install the fonts in `illustrator/fonts/` before opening the SVGs in Illustrator (see `illustrator/README-Illustrator.txt`).

## Team share package
Download: https://moselanto.github.io/sound-creationsltdprofile/dist/Sound-Creations-Company-Profile-2026-Team-Package.zip
Rebuild it with `python3 build/build-team-package.py` after the PDF and SVGs (needs `pip install pypdfium2`).
