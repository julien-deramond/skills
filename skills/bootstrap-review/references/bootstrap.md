# Bootstrap's own checks

What `AGENTS.md`, `.github/CONTRIBUTING.md` and the project skills don't say, learned from reviews
of twbs/bootstrap pull requests. Read those files first, at the base commit: when they disagree
with this one, they win.

## The release line

- **v6 is `main`**: TypeScript in `js/src/`, Vitest in a real browser, CSS layers, token maps,
  logical properties, modern CSS. **v5 is `v5-dev`**: JavaScript, Karma, RTLCSS, and a browser floor
  that rules out `:has()` and `:is()`. **`gh-pages`** holds the frozen docs of old versions
  (`docs/5.2`, `docs/4.6`), changed only by PRs on that branch.
- v5 takes bug fixes that change no default and no output that users override: nothing that
  changes Reboot, the default variables or the default rendering in a patch release. A feature or a
  default change goes to v6.
- A v5 fix for a bug that v6 also has needs a v6 change too: say whether this PR should be
  forward-ported, and by whom. A v5 PR for something v6 already solves is closed with a pointer.
- A v6 change that breaks markup, a class, a variable or an option needs its line in the migration
  guide.

## Sass

- No hard-coded values where the framework has a scale: z-index, colors (hex in a component),
  spacing, radii. Use the variable, the token or the map, and loop over the theme colors map instead
  of listing colors.
- A new variable must be used, so overriding it does something, and documented where its siblings
  are (the `scss-docs-start` and `scss-docs-end` markers feed the docs).
- `@include` the project's mixins (`border-radius()`, `transition()`, the media query mixins) rather
  than raw properties or raw `@media`.
- An invalid option fails the build with `@error`; `@warn` scrolls past.
- It compiles. A missing partial or a broken `@use` is the first thing to check, from the CI log.

## The build and `dist/`

- `dist/` and `js/dist/` are built output. A PR that commits them is asked to drop those changes.
- A size change can fail `bundlewatch`. The budget is in `.bundlewatch.config.json`; it's raised in
  the PR that needs it, in steps of 0.25 kB.
- When the compiled CSS changes, the review shows the diff of `dist/css/bootstrap.css` built on both
  sides (and `bootstrap.rtl.css` on v5 when the change touches direction).

## JavaScript

- A behaviour change needs a unit test that fails before it and passes after: `js/tests/unit/` (Vitest
  on v6, `npm run js-test-unit`; Karma on v5, `npm run js-test-karma`). A visual-only case can go in
  `js/tests/visual/`.
- On v6, components extend `BaseComponent`, and `dispose()` undoes everything the component did to
  the DOM (attributes, inserted elements, moved names, listeners).
- On v6, a public API change also updates the type tests (`js/tests/types/api.ts`, `consumer.ts`).

## Docs

- An example must work in a default build. The docs site enables options that a default build
  doesn't, so check the option's default in `scss/` before trusting what the docs render.
- A default in an options table is checked against the source (`js/src/`, `scss/`), not against
  another docs page.
- A fix on one page usually belongs on its siblings too: the other bundler guides (Vite, Parcel,
  Webpack), the cheatsheet, the RTL copies of an example, the same component on another version's
  page.
- v6 pages carry no leftover v5 wording. Prose follows the writing rules in `AGENTS.md`.

## CI and workflows

- A first-time contributor's workflows wait for a maintainer to approve them: "CI hasn't run" isn't
  "CI is green".
- A change to `.github/workflows/` pins actions by commit SHA, keeps jobs that publish or deploy
  behind `if: github.repository_owner == 'twbs'`, and matches tags precisely enough that a prerelease
  tag doesn't publish as a release.
- A workflow triggered by a release also runs for GitHub prereleases (`release: published` fires
  for both). Ask whether a prerelease should publish too, and say what it would publish as.

## Scope and the pull request itself

- A feature, a new option or a new utility needs an issue where the team agreed to it. Without one,
  the review asks for the issue first, or closes the PR with that pointer.
- Unrelated changes go in separate PRs. Formatting changes to files the fix doesn't need are
  reverted.
- The title and description name the real change. The closing keyword is right: `Fixes #n` only
  when the PR fixes all of #n, else `Refs #n`.
- A PR written with AI help is judged on its code like any other, but its description's claims are
  checked one by one.

## Deploy preview

Every PR gets a Netlify preview at `https://deploy-preview-<n>--twbs-bootstrap.netlify.app/`, with the
docs under `docs/<version>/`. Check the rendering there before reading the code: many regressions
show on pages the diff doesn't mention. Compare with the base (getbootstrap.com for the released
version, or your own build of the base).

## Who else looks

Some calls belong to someone else on the team: design to the project lead, an accessibility finding
that needs a screen reader to the accessibility reviewer, a CSS or JS change to the `@twbs/css-review`
or `@twbs/js-review` team. The review says when a call is theirs.
