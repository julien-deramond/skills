# Writing and checking the fix

## The change

- **Smallest, in the right place.** Change the rule, mixin, map or function that already handles
  the case. A new block next to it is a second place to keep in sync. A one-line fix stays one line.
- **The project's idiom.** Variables and tokens instead of hard-coded values, the project's mixins
  instead of raw properties, logical properties on v6, the existing naming. Match the code around it.
- **Where the problem repeats.** Look for the same pattern elsewhere: sibling components, the other
  sizes or variants, the RTL copy of an example, the other bundler guides, the same page on the other
  release line. Fix them in the same branch when they're the same topic, or say in the report where
  else it happens.
- **A test when the change is testable.** A JavaScript change gets a unit test that fails before it
  and passes after (`js/tests/unit/`). A visual case that a unit test can't hold can get a page in
  `js/tests/visual/`. Sass has no rendering tests: the evidence is the compiled CSS diff.
- **Docs when behaviour or API changes.** An option, a default, a class or markup that changes
  updates its docs page. On v6, a breaking change gets its line in the migration guide.
- **One topic.** A second problem met on the way is a separate branch or a note in the report, never
  part of this fix.
- **Backports are separate branches.** A v5 fix that v6 also needs, or the other way round, is a
  second branch on the other base, with the same direction name.

## Checks

Run the ones the change touches, from the base's `package.json`:

- Sass: `npm run css-lint`, then `npm run css-compile` (or `npm run css`) on both sides, and
  `diff -u` of `dist/css/bootstrap.css` between the base build and yours. Keep that diff for the
  description. `npm run css-test` when the change touches what it covers.
- JavaScript: `npm run js-lint`, and `npm run js-test-unit` on v6 or `npm run js-test-karma` on v5.
- Docs: `npm run docs-lint` when it exists, and the docs build only when the change can break it
  (MDX components, links, frontmatter).
- Size: the `bundlewatch` budget in `.bundlewatch.config.json`. Raise it in the same commit when the
  fix needs it, in steps of 0.25 kB.

Then revert `dist/` and `js/dist/`.

## Evidence for a visual change

A change is visual when it can change how something looks. Take the same page, width, theme and
state on both sides, base and fix, so the two line up: screenshots in pairs, or a computed-value
table when the change is a few pixels. Check the states the change can reach (hover, focus, disabled,
validation, dark mode, right to left, a narrow width) and the pages around it, since a global rule
shows its regressions elsewhere.

## Branch and commit

- Name the branch the way the caller says. Without a rule, `issue-<n>-<base>`, then `-2`, `-3` for
  more directions on the same base.
- One commit, two at most, so it cherry-picks cleanly. The message is direct prose on what changes
  and why, in the style of the repository's recent commits.
