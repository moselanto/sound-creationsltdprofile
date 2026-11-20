# Rules for editing this repo

1. **Source of truth for facts** is the live site https://soundcreationsltd.com and the repo `moselanto/soundcreationsltd.com` (`AGENTS.md`, `WORK-LOG.md`). Do not contradict them.
2. **Never invent** clients, projects, results, team members, certifications, registration numbers, prices, reviews or awards. Use only facts supplied by Sound Creations or published on the site. Unknown items are left out rather than guessed.
3. **Contact details** (only these): +254 715 754 758 (call and WhatsApp), info@soundcreationsltd.com, Mpaka Plaza, Mpaka Road, Westlands, Nairobi. Hours: Mon-Fri 9:00 am - 5:30 pm, Sat 9:00 am - 1:30 pm, Sunday closed. Socials: IG @soundcreations_kenya, X @SCL_kenya, FB soundcreationsKE, LinkedIn soundcreationsltd.
4. **Stats must match the live site:** since 2004, 22+ years, 850+ projects, 4 countries of operation, 15 brands on the brands page.
5. **Countries:** offices in Kenya (HQ), Rwanda, DRC Congo and the UAE = 4 countries of operation. Tanzania is a distribution market only, never counted as an office or location. Spell it **DRC Congo**, as the website does.
6. **Reviews:** only the 4 Google reviews shown on the website homepage (Triad Kuolo, Michael Odida, Aalawy Balala, Brandon Tengeya), quoted as published.
7. Keep web and PDF in one source (`index.html`). After any content or style change, rebuild `dist/Sound-Creations-Company-Profile.pdf`, check every page for overflow, and commit both together.
8. No `todo` placeholders may remain in a client-facing release (`grep -ni todo index.html`).
9. Record each change in `CHANGELOG.md` and bump the version.
