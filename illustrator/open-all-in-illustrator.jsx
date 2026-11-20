// Converts every SVG page in a chosen folder to an Illustrator .ai file.
// Illustrator > File > Scripts > Other Script... > select this file.
#target illustrator
(function () {
    var src = Folder.selectDialog("Choose the svg folder from the Sound Creations Illustrator package");
    if (!src) return;
    var dest = new Folder(src.parent.fsName + "/ai");
    if (!dest.exists) dest.create();
    var files = src.getFiles("*.svg");
    files.sort(function (a, b) { return a.name < b.name ? -1 : 1; });
    var opts = new IllustratorSaveOptions();
    opts.pdfCompatible = true;
    opts.embedLinkedFiles = true;
    for (var i = 0; i < files.length; i++) {
        var doc = app.open(files[i]);
        var out = new File(dest.fsName + "/" + files[i].name.replace(/\.svg$/i, ".ai"));
        doc.saveAs(out, opts);
        doc.close(SaveOptions.DONOTSAVECHANGES);
    }
    alert("Saved " + files.length + " pages to " + dest.fsName);
})();
