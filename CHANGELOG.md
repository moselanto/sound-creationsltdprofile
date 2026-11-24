# Changelog

## 1.16.2 - 24 Nov 2026
- `illustrator/README-Illustrator.txt`: now says the print PDF is at the top level of the team zip (`Sound-Creations-Company-Profile-2026.pdf`), not inside the Illustrator-Editable folder. Team package rebuilt.

## 1.16.1 - 24 Nov 2026
- Owner request: the small inset photo on the CITAM Buruburu page (page 13) now uses the same client-supplied photo (`citam-buruburu-stage.jpg`), framed on the seating and stage (`#fp6 .fx-inset img{object-position:30% center}`). Old `citam-buruburu.jpg` removed.
- PDF, page 13 SVG, illustrator/ PDF and images, and the team share package rebuilt.

## 1.16.0 - 24 Nov 2026
- Client feedback (Sound Creations, after the review email): CITAM Buruburu main project photo (page 13) replaced with the client-supplied image `assets/img/projects/citam-buruburu-stage.jpg` (wide shot of the stage and dB Technologies system), framed on the stage with `#fp6 .fx-img>img{object-position:52% center}`. Old `citam-buruburu-1.jpg` removed. Inset photo unchanged.
- PDF, Illustrator SVGs, illustrator/ PDF and images, and the team share package rebuilt.

## 1.15.1 - 23 Nov 2026
- Added the team share package: `dist/Sound-Creations-Company-Profile-2026-Team-Package.zip` (final PDF, a JPG preview of every page, the Illustrator-Editable package and READ-ME-FIRST.txt), built by the new `build/build-team-package.py` from `build/team-READ-ME-FIRST.txt`. Downloadable from the live site.

## 1.15.0 - 21 Nov 2026
- Contents (page 2) redesigned on the owner's request: larger "Contents" heading with a one-line intro; the 8 sections are now numbered cards in two columns (01-04 left, 05-08 right), each with a short description and its page range (Projects Showcase 07-15, Regional Reach & Contact 18-19), filling the page to the footer; "At a glance" panel aligned with the bottom of the cards.
- Illustrator package rebuilt (illustrator/svg, print PDF) and zip updated.

## 1.14.0 - 21 Nov 2026
- Final page-by-page check of all 19 pages: contents page numbers and section numbers match every page; no text runs off a page or into the footer.
- Regional reach: head office photo re-framed so the "Sound Creations" sign reads from the left.
- New Illustrator package in illustrator/: one layered SVG per page (svg/), built by build/build-svg.py from the same index.html. Each page opens in Illustrator as a 297 x 210 mm artboard with named layers (Background, Photo, Headline, Project write-up, Brand logos, Logo, Header label, Footer, ...), named sub-groups, live editable text (one text object per line), vector shapes and gradients, and photos embedded at full resolution inside clipping masks. Also included: static Space Grotesk and Inter fonts (fonts/), every image at full resolution (images/), the print PDF, README-Illustrator.txt and open-all-in-illustrator.jsx (saves all pages as .ai).
- Image check: several photos taken from the original PDF or website are 100-150 ppi at printed size; listed in docs/FACTS-NEEDED.md for replacement with original camera files.

## 1.13.0 - 20 Nov 2026
- Regional reach (page 18) rebuilt in the owner's preferred format (reference screenshot): heading, intro and a tall head office photo on the left; large map on the right with bigger uppercase pin labels and the legend inside the map; four office cards (Kenya, Rwanda, DRC Congo, UAE) under the map, all aligned to the footer.
- Contact (last page) improved further: showroom photo panel on the right with the "Plan a project" card and Request a consultation button over it; headline, intro, four contact cards (phone, email, head office, hours) and social chips on the left, anchored above the closing bar.
- PDF rebuilt and checked.

## 1.12.0 - 20 Nov 2026
- Regional reach (page 18), owner request to improve: heading with "Regional impact." in red and intro alongside; larger map (true proportions, pins re-placed) with legend and "4 countries · 1 team"; head office photo with caption and four office cards (Kenya head office, Rwanda since 2022, DRC Congo since 2024, UAE since 2024) filling the right column to the footer.
- Contact (page 19), owner request to improve: larger headline with "extraordinary" in red; a "Plan a project" card with the website's three steps (consultation and site visit; system design and quotation; supply, installation, training and support) and the Request a consultation button; red sound-wave graphic; one contact panel (head office, phone/WhatsApp, email, open hours) and social handles as chips, anchored above the closing bar.
- PDF rebuilt and checked.

## 1.11.0 - 20 Nov 2026
- Removed the Why choose us page (Our competitive edge, including the 4 Google reviews) on the owner's request; the unused technician photo deleted.
- Profile is now 19 pages. Local presence is now section 08 (page 18) and Contact is page 19; contents updated. PDF rebuilt and checked.

## 1.10.0 - 20 Nov 2026
- Brands & partners (page 17) kept and improved on the owner's request: "supported locally." in red; the 15 logos grouped with count badges into Professional audio (9), Lighting & cabling (2) and Acoustics (4) with larger tiles; partner cards now carry a label (Authorised partner, Kenya sales office, Kenya distributor, Since 2024); the distribution footprint is a panel with East Africa, Middle East and Asia columns, anchored above the footer so the page is filled. PDF rebuilt and checked.

## 1.9.0 - 20 Nov 2026
- Removed the case studies page (More landmark installations, formerly Landmark installations and Hospitality, live & heritage) on the owner's request; its four unused photos deleted.
- Removed the Our Clients page (client logos) on the owner's request; the 43 client logo files deleted.
- Other completed projects (Track record) kept and redesigned to match the featured project pages: photo panel on the left with "850+ projects completed", the four categories on the right (Houses of worship 20, Education 8, Corporate & media 10, Hospitality & events 13) in four-column lists with count badges, spaced to fill the page.
- Profile is now 20 pages. Sections renumbered 01-09 (Track record 06, Brands & partners 07, Why choose us 08, Local presence 09); contents updated. PDF rebuilt and checked.

## 1.8.0 - 20 Nov 2026
- Featured projects expanded from 4 to 8, in this order everywhere (showcase list, project pages, page numbers): 01 West Nairobi School, 02 RPF Rubavu Multipurpose Hall, 03 Sarit Expo Centre, 04 Parklands Baptist Church, 05 PCEA Kahawa Farmers Church, 06 CITAM Buruburu, 07 Playza, Prestige Plaza, 08 COVO NBO. Text and photos for 05-08 taken from their project pages on soundcreationsltd.com (new photos: pcea-kahawa-1/2, citam-buruburu-1, playza-1/2, covo-1).
- All 8 project pages use one new layout: project photo on the left (large project number, inset photo where available, category chip), write-up on the right (title, sub-line, Category / Scope / Location / Status, description, Key technology & scope card) and an 01-08 progress strip, all anchored to keep every page balanced.
- Projects showcase opener now lists all 8 featured projects with page numbers 08-15.
- PCEA Kahawa Farmers, CITAM Buruburu, Playza and COVO left the case studies; the remaining four (Kenyatta University Amphitheatre, Oshwal Senior Academy, Roadshow Trucks, All Saints Cathedral) are combined on one "More landmark installations." page (page 16) with taller photos.
- Profile is now 22 pages; contents page numbers updated (Completed Projects 17, Clients 18, Brands 19, Why Choose Us 20, Regional Reach & Contact 21). PDF rebuilt and checked.

## 1.7.1 - 20 Nov 2026
- Projects showcase opener (page 7), owner request to improve and balance: larger headline with "Real results." in red and a red rule; stronger photo gradient; a "Featured projects" band anchored above the footer with four cards (West Nairobi School, RPF Rubavu Multipurpose Hall, Sarit Expo Centre, Parklands Baptist Church) showing category, location and page number (linked on the web page); a key-figures panel (850+ projects completed, 22+ years of expertise, 4 countries of operation) replaces the lone 850+ figure. PDF rebuilt and checked.

## 1.7.0 - 20 Nov 2026
- Removed the Sectors page (Engineered for how every space is used.) on the owner's request. The profile is now 19 pages; the five unused sector photos were deleted.
- Sections renumbered 01-10 and pages 01-19 on every page; contents page entries updated to match.
- PDF rebuilt and checked.

## 1.6.1 - 20 Nov 2026
- Professional audio (page 5), owner request to balance and improve: larger heading and intro; the six capabilities are now individual cards; the Parklands case card and the key brands strip are anchored above the footer so the right column fills the page evenly; larger brand tiles; photo colour softened slightly.
- Acoustics & engineering (page 6): taller method panel; the bottom row is now three equal columns, each with a heading (On site, Treatment solutions, Engineering & consultancy), equal-height photos and solution cards, so the columns line up top and bottom.
- PDF rebuilt and checked.

## 1.6.0 - 20 Nov 2026
- Removed the What we do page (One partner. Every discipline.) on the owner's request. The profile is now 20 pages; the three unused solution photos were deleted.
- Professional audio (now page 5, section 03) redesigned: photo panel on the left with a "Designed before it's hung" note; six capability items in a numbered two-column grid; Parklands Baptist Church case in point with key figures (2,500 seats, 360 degree coverage, 168 channels); key brands shown as logo tiles (dB Technologies, NEXO, Bose, Shure, Allen & Heath, Midas, FANE).
- Acoustics & engineering (now page 6, section 04) redesigned: heading with intro; five-step method panel (Measure, Analyse, Design, Treat, Verify); bottom row anchored above the footer with two captioned photos, treatment solutions (ceilings, wall panels, sound isolation), the engineering and consultancy capabilities list and the RPF Rubavu Hall case in point.
- Sections renumbered 01-11 and pages 01-20 on every page; contents page entries updated to match.
- PDF rebuilt and checked.

## 1.5.0 - 20 Nov 2026
- Removed the Purpose page (Vision, mission & values) on the owner's request. The profile is now 21 pages; the unused vision photo was deleted.
- How we work (now page 4, section 02) redesigned: the five steps (Consult, Design, Distribute, Integrate, Support) sit in one connected panel with large step numbers, chevron dividers and a fuller line of text each; "What we deliver" label above four taller service cards (Consultancy, Distribution & Dealership, Integration, After-Sale Services) with full-width photos, red number badges and red divider, anchored above the footer so the page is evenly filled.
- Sections renumbered 01-12 and pages 01-21 on every page; contents page entries updated to match.
- PDF rebuilt and checked.

## 1.4.1 - 20 Nov 2026
- Our journey (page 3), owner request: timeline moved down and anchored above the footer so the page is balanced instead of leaving empty space at the bottom; showroom photo enlarged to 100 mm high. PDF rebuilt and checked.

## 1.4.0 - 20 Nov 2026
- Removed the old page 3 (Who we are) on the owner's request. The profile is now 22 pages.
- Our journey (now page 3) redesigned around one photo only: the showroom at Mpaka Plaza, Westlands, using the higher-resolution showroom photo the owner supplied (replaces assets/img/photos/showroom.jpg). The three previous journey photos are no longer used on this page. Layout: heading and intro with a "2004 / Founded in Nairobi" marker on the left, large captioned showroom photo on the right, five-step timeline (2004, 2018, 2022, 2024, 2026) below.
- Section numbers renumbered 01-13 (Our journey is now section 01) on every page eyebrow and footer; page numbers renumbered 01-22; contents page updated to match. Contents page layout unchanged.
- PDF rebuilt and checked.

## 1.3.2 - 20 Nov 2026
- Cover (page 1), owner request: the Company Profile block (with the sound wave) moved back down to the bottom of the cover, where it sat on the original PDF. The process steps and headline stay where they were in 1.3.1. PDF rebuilt and checked.

## 1.3.1 - 20 Nov 2026
- Cover (page 1), owner request: moved the process steps, headline and Company Profile block up so the page is balanced, with clear space between the logo and the content and a short, even gap before the Company Profile block. PDF rebuilt and checked.

## 1.3.0 - 20 Nov 2026
- Cover (page 1), owner request with a reference screenshot: the "COMPANY PROFILE / 2026 EDITION · SINCE 2004" block now has its own thick red bar on the left, a larger white title, the edition line in brand purple, and a red sound-wave graphic running to its right (inline SVG). The long red bar that ran beside the whole cover text was removed so the bar belongs to this block only. PDF rebuilt and checked.

## 1.2.0 - 20 Nov 2026
- Cover (page 1), owner request: the headline is now the tagline "If it sounds good, it's Sound Creations." ("Sound Creations." in red). Removed "Engineering exceptional sound. Delivering complete solutions.", the small tagline line above the process steps and the "World-class professional audio..." sub-line.
- "COMPANY PROFILE / 2026 EDITION · SINCE 2004" restored below the headline. Process steps (Consult > Design > Distribute > Integrate > Support) kept above the headline. PDF rebuilt and checked.

## 1.1.0 - 20 Nov 2026
- Page 1 (cover) redesigned on the owner's request. It now carries only the logo (large, white), the tagline "If it sounds good, it's Sound Creations.", the Consult > Design > Distribute > Integrate > Support process (as linked pills), the headline "Engineering exceptional sound. Delivering complete solutions." and the sub-line "World-class professional audio, visual, lighting and acoustic solutions for Africa and the Middle East."
- Removed from the cover: the country strip, the "Company Profile / 2026 Edition / Since 2004" block and the bottom bar with website, email and phone (all still on the contact page).
- Stronger left and bottom gradient, red accent rule and a soft red glow for a cleaner, more premium cover. PDF rebuilt and checked.

## 1.0.0 - 20 Nov 2026
- Repo set up the same way as `moselanto/vtechprofile`: one `index.html` + `assets/css/profile.css` source for the web page and the PDF, `build/build-pdf.py` (WeasyPrint), README, AGENTS, FACTS-NEEDED, `.nojekyll` for GitHub Pages.
- Rebuilt the existing 23-page Sound Creations Company Profile 2026 PDF in HTML/CSS, page for page (A4 landscape 297 x 210 mm). Photos taken from the PDF; logos from soundcreationsltd.com; fonts Space Grotesk + Inter self-hosted.
- Fixes against the original PDF:
  - Brands page now says 15 brands ("15 world-class brands" and "a portfolio of 15 leading global brands"); 15 logos shown. "At a glance" on the contents page now reads 15 global brands (was 15+).
  - 4 countries vs Tanzania settled: offices in Kenya, Rwanda, DRC Congo and UAE (4 countries of operation); Tanzania shown only as a distribution market (map legend: head office / office / distribution market; Dar es Salaam pin marked "distribution only"; brands-page footprint and regional-reach intro reworded to match).
  - Contents page cleaned up: one clean page number per section (03, 04, 05, 06, 07, 08, 09, 10, 11, 18, 19, 20, 21, 22), entries link to their pages on the web version.
  - Why choose us now shows all 4 Google reviews from the website (Triad Kuolo, Michael Odida, Aalawy Balala, Brandon Tengeya), quoted in full as published.
  - "DR Congo" changed to "DRC Congo" everywhere, matching the website.
