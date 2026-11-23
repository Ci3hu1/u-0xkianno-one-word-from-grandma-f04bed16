# NOTES — u-0xkianno-one-word-from-grandma-f04bed16

## Entry

- Competition: One Word From Grandma ($5: 1st $1.59, 2nd $1.11, 3rd $0.78, 4th–8th $0.55–$0.13), free entry, no prerequisites.
- Opens 23 Nov 2026 19:06 UTC, closes 26 Nov 2026 19:05 UTC (27 Nov 02:05 WIB). Three blind rounds; round 1 cutoff 24 Nov 19:06 UTC (25 Nov 02:06 WIB).
- The word (5 chars): "ROBUT" — the typo a grandma would actually make texting about AI (means "robot").
- Program: `main.py`, pure Python stdlib, writes the word to `/output/entry.txt`. Deterministic, chmod 0644.
- Submission title is the word itself.

## Field

- 147 submissions when found (24 Nov ~02:25 WIB). Blind rounds hide standings — no live score until round 1 is judged.
- Quota at triage: day cap 5 left, can_submit true, entries_made 0.

## Build

- Built 24 Nov ~02:30 WIB in this run's session (started after opening).
- `main.py`, `STRATEGY.md`, `tests/test_entry.py`, `README.md` (template badges, owner/repo/referral filled), `NOTES.md`, `LICENSE` (MIT) written in the build session.
- Tests: `python3 -m unittest discover -s tests -v` — all pass (word length/one-word, exact output, 0644 mode, determinism over two runs).
- Repo: https://github.com/Ci3hu1/u-0xkianno-one-word-from-grandma-f04bed16 — commit pending (see below).
- Kit check / bundle: PENDING — run in the follow-up turn after Joni's Setuju (usage rows land only when this build turn ends; bundle needs --prompt-file + --mcp none, same as the rate-my-human flow). Kit `init` (LICENSE anchor + .makefun/owner.json) also runs there if the kit requires it.
- NOT submitted — awaiting Joni's 'Setuju' on the exact entry.

## Live score

- Blind rounds: NO live score at submit. Check rounds after cutoff 25 Nov 02:06 WIB: GET /api/competitions/u-0xkianno-one-word-from-grandma-f04bed16/rounds.
