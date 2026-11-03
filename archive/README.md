# Archive

These files are retained for reference and possible reuse. They are not loaded
by the live lab pages.

- `pages/`: the retired Research page, unused Lab Fun page, and template News page.
- `courses/3dv-fall-2024/`: the historical 3D vision course, its images, course
  styling, and schedule backup. Its former HTML URLs redirect here.
- `images/gallery/2025-spri-03.png`: an extra SPRI photo with no active reference.
- `legacy/`: unused Blueimp gallery scripts/styles, social-button styles, and
  their bundled icons.
- `development/`: previously tracked IDE settings and macOS directory metadata.

The old template pages and course already referenced some images, plugin
resources and anchors that were absent before this reorganization. Those
historical gaps have not been filled with unrelated replacement material.
Use `python3 scripts/check_site.py --include-archive` from the repository root
to list them. They do not affect the five live lab pages.

To restore an archived component, move it into the appropriate active directory,
update its relative references, remove its `noindex` tag if it becomes a live
page, and run the reference checker. The full path history is recorded in
[`../docs/file-moves.csv`](../docs/file-moves.csv).
