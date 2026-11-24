#!/usr/bin/env python3
"""Build the team share zip: dist/Sound-Creations-Company-Profile-2026-Team-Package.zip

Contents: final PDF, one JPG preview per page, the Illustrator-Editable package
(copy of illustrator/) and READ-ME-FIRST.txt (from build/team-READ-ME-FIRST.txt).
Run after build-pdf.py and build-svg.py.
Previews are kept modest (scale 1.6, JPEG q82) so the zip stays under ~20 MB,
the size the repo commit tool can handle.  Needs: pip install pypdfium2
"""
import os, shutil, tempfile, zipfile
import pypdfium2 as pdfium

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "dist", "Sound-Creations-Company-Profile.pdf")
OUT = os.path.join(ROOT, "dist", "Sound-Creations-Company-Profile-2026-Team-Package.zip")
NAME = "Sound-Creations-Company-Profile-2026"

with tempfile.TemporaryDirectory() as tmp:
    top = os.path.join(tmp, NAME)
    os.makedirs(os.path.join(top, "Page-Previews"))
    shutil.copy(PDF, os.path.join(top, NAME + ".pdf"))
    shutil.copytree(os.path.join(ROOT, "illustrator"), os.path.join(top, "Illustrator-Editable"))
    shutil.copy(os.path.join(ROOT, "build", "team-READ-ME-FIRST.txt"), os.path.join(top, "READ-ME-FIRST.txt"))
    names = sorted(os.path.splitext(f)[0] for f in os.listdir(os.path.join(ROOT, "illustrator", "svg")))
    doc = pdfium.PdfDocument(PDF)
    for i in range(len(doc)):
        doc[i].render(scale=1.6).to_pil().convert("RGB").save(
            os.path.join(top, "Page-Previews", names[i] + ".jpg"), quality=82)
    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _, fs in os.walk(top):
            for f in sorted(fs):
                full = os.path.join(dp, f)
                z.write(full, os.path.relpath(full, tmp))
print("Wrote", OUT, round(os.path.getsize(OUT) / 1e6, 1), "MB")
