# Vision and Learning Lab

Website: <https://siyuhuang.github.io/lab/>

## Repository layout

```text
lab/
├── index.html                  # Home and news
├── people.html                 # Faculty, students and alumni
├── publications.html           # Publications and resource links
├── teaching.html               # Current course listings
├── contact.html                # Join Us and activity photos
├── assets/
│   ├── css/                    # Site-owned styles
│   ├── images/
│   │   ├── campus/
│   │   ├── courses/
│   │   ├── gallery/
│   │   ├── people/
│   │   ├── publications/
│   │   └── sponsors/
│   └── vendor/                 # Bootstrap 2.3.1 and jQuery 1.9.1
├── archive/                    # Retired pages, course site and unused assets
├── docs/file-moves.csv          # Original-to-current path lookup
├── scripts/check_site.py        # Local reference checker
└── teaching/3dv_fall24/         # Compatibility redirects for the old course URLs
```

The five live HTML pages remain at their existing URLs. `research.html`,
`news.html`, `fun.html`, and the old course HTML URLs are small compatibility
redirects; their source content is under `archive/`. The archived pages are
marked `noindex` and are not part of the live navigation.

## File naming

Use lowercase names with hyphens, without spaces or personal abbreviations:

- Portraits: `assets/images/people/gabriel-serrano.jpg`.
- Publications: `assets/images/publications/2026-fast-2dgs-efficient-image-representation-with-deep-gaussian-prior.png`.
- Courses: `assets/images/courses/cpsc-4070-teaser.png`.
- Activities: `assets/images/gallery/2026-spri-interns.jpg` or `2025-eureka-01.jpg`.
- Sponsors: `assets/images/sponsors/knight-foundation.png`.

Keep third-party library filenames intact. Use relative paths for repository
assets rather than `raw.githubusercontent.com` URLs. The SPRI group photograph
is intentionally shared by the gallery and the two SVG portrait crops.

## Preview and check

No dependency installation is required for the reference checker:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000
```

Open <http://localhost:8000/>. The check validates live HTML/CSS references,
images, local page links, and section anchors. To report historical issues in
archived source pages as well, run `python3 scripts/check_site.py --include-archive`.

Before moving a file, update all referring HTML and CSS, including archived
pages and SVG `image` elements. Before replacing an image at the same path,
update its URL version query if necessary to refresh browser caches.

See [the archive notes](archive/README.md) and [the file migration map](docs/file-moves.csv)
for the November 2026 organization changes. Images were moved without changing
or recompressing their contents; nothing was discarded.
