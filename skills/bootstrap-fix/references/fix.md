# Writing and checking the fix

## The change

- **Smallest, in the right place.** Change the rule, mixin, map or function that already handles
  the case. A new block next to it is a second place to keep in sync. A one-line fix stays one line.
- **The project's idiom.** Variables and tokens instead of hard-coded values, the project's mixins
  instead of raw properties, logical properties on v6, the existing naming. Match the code around it.
- **Fix the topic globally, never one component at a time.** The issue names one place, but the
  cause is a pattern. Find every place the same pattern lives (sibling components, every size and
  variant, the docs examples, RTL copies, the other bundler guides) and fix them all in the same
  branch, the same way, so everything works together. A fix that leaves the same bug next door is
  incomplete. The release line is the one exception: the other line gets its own backport branch.
- **A test when the change is testable.** A JavaScript change gets a unit test that fails before it
  and passes after (`js/tests/unit/`). A visual case that a unit test can't hold can get a page in
  `js/tests/visual/`. Sass has no rendering tests: the evidence is the compiled CSS diff.
- **Docs when behaviour or API changes.** An option, a default, a class or markup that changes
  updates its docs page. On v6, a breaking change gets its line in the migration guide.
- **One topic, all of it.** Everything the topic reaches belongs in the branch. A different problem
  met on the way is a separate branch or a note in the report, never part of this fix.
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

## The impact on everything the fix touches

Check every component the change modifies, not only the case in the issue: all its states (hover,
focus, active, disabled, read-only, validation, checked), sizes and variants, every usage in the
docs and examples, and the odd ones (nested in other components, inside a dialog, a drawer or an
input group, long or wrapping content, right to left, dark mode, a narrow width, 200% zoom). A
regression in a case nobody reported is still a regression. The report lists what was checked and
what wasn't.

A JavaScript change also checks the component's events and public methods, on the base and on the
fix, with real input: which events fire, how many times and with what values, for every key, click
and method call the change reaches. That includes the ones that change nothing, such as
<kbd>Delete</kbd> after the last character or <kbd>Backspace</kbd> in an empty field: a plain input
fires nothing there. Count the events in the probe and in a unit test, not only the value and the
DOM.

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
