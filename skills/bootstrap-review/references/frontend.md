# Front-end checks

For a change to CSS, markup, docs examples or behaviour in the browser. These checks apply to any
front-end project. `bootstrap.md` has Bootstrap's own.

## Find which rule wins

Don't reason about the cascade from the source: measure it. Build the CSS, load it in a page that
uses only that CSS, and read `getComputedStyle()` for the property in question, in every state the
change touches. Then explain the result from the source: the layer order (an unlayered rule beats
every layer, and a later layer beats an earlier one), specificity, then source order.

## Selectors

- **Dead selectors.** A selector that can never match: a pseudo-class on an element that never has
  that state (`:user-invalid` on a `<label>` or a `<div>`), a class combination the markup never
  produces. They're bytes for nothing, and they suggest the author misread the markup.
- **Structural side effects.** An element inserted by a script, even hidden, changes `:first-child`,
  `:last-child`, `:nth-child()` and `+` for its siblings. Check the rules that rely on them (rounded
  corners and negative margins of grouped controls, often).
- **Support.** `:has()`, `:is()`, `:where()`, `@layer`, `@container`, `color-mix()`, `light-dark()`
  and range media queries each have a browser floor. Check it against the project's
  `.browserslistrc` for the release line, not against the latest browsers.

## States

Check every component the change modifies, in every state it can reach, not only the one in the
issue: hover, `:focus-visible` against
`:focus-within` (a wrapper never matches `:focus-visible`), active, disabled, read-only, the
validation states, checked and indeterminate, dark mode, right to left, a narrow width, 200% zoom,
`prefers-reduced-motion`, and forced colors when the change touches borders, outlines or
backgrounds.

## The build

When the compiled CSS changes, build both sides and diff the compiled file (`diff -u`): the reviewer
sees what ships, not only the Sass. Watch for duplicated rules, doubled prefixes in generated names
(`--gray-gray-100`), new selectors that a loop multiplies, and the size against the project's budget.

## Rendering

Look at the pages that show the change: the deploy preview, or your own build of both sides. Compare
each with the base, at the same width, theme and state, and look at the pages around the change
too (a global rule shows its regressions elsewhere: the homepage, the sidebar, other components).
Screenshots go in pairs that line up.

## Accessibility

Name the WCAG criterion a finding rests on: 1.4.3 and 1.4.11 (contrast of text, and of borders and
focus indicators), 2.4.7 (focus visible), 2.5.3 (label in name), 3.3.1 (error identification),
4.1.2 (name, role, value). Check that `aria-labelledby` and `aria-describedby` point at elements that
exist and are visible at every width, that `aria-hidden` doesn't hide something a user operates or
reads, and that the change works with the keyboard alone. When a finding needs a screen reader you
didn't run, say so, and name it as a check for the project's accessibility reviewer.

## Forms

A disabled control isn't submitted, but a hidden input next to it is: check that a script's hidden
twin follows `disabled`. Build the form and read `new FormData(form)` instead of guessing what's
sent. Parsing typed text with `new Date()` reads `nn/nn/nnnn` month first, whatever the locale.

## Behaviour

Listeners added by the change are removed on teardown. Events are namespaced the way the project
does it. State that a method changes is restored by the method that undoes it.
