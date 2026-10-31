# Feedback: no word limits (2026-10-31)

A maintainer's feedback: a PR description, a reply on an issue and a posted review are as long as what
their reader needs, not shorter than a word count. The three limits (150 words for a PR description,
100 for a reply, 150 or 300 for a review message) are gone. Each text holds what its reader needs and
nothing else: no padding, no diff or PR restated, nothing the notes already hold. The 23 length graders
now judge that instead of counting words, and the `posted-review-is-short` graders are renamed
`posted-review-is-focused`.

Graded blind, once with the limits and once without:

| Case | With limits | Without | Preferred | Words in the posted text |
| --- | --- | --- | --- | --- |
| otp-supersede-pr | 6/8 | 5/8 | with, slight | PR 163, without 217 |
| form-label-tokens-fix | 7/7 | 6/7 | with, slight | PR 114 and reply 34, without 87 and 22 |
| form-adorn-focus-ring (review) | 6/7 | 7/7 | with, slight | review 120, without 214 |

The grader found no padding in any of the six texts. Two of the points lost without the limits are a
missing attribution line, which runs with the limits also missed in other rounds. Without the limits,
two texts out of three came out longer, and the grader slightly preferred the shorter one each time.
The change follows the maintainer's call: length follows content, and the graders now fail padding
rather than a count.
