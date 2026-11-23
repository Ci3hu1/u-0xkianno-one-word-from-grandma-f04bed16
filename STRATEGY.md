# STRATEGY — One Word From Grandma

## The word

> ROBUT

5 characters. One word. The submission title is the word itself.

## What the word does

The brief asks for exactly one word: the single word a grandma would text
about AI. It allows "a real word, a family in-joke, a typo she would
actually make or a scrap of text-speak". ROBUT plays the typo squarely:

1. **The joke is inside the word, not around it.** Grandma means
   "robot" and her fingers, her phone, or her autocorrect deliver ROBUT.
   There is no setup to read and no punchline to wait for — the misspelling
   IS the message, and it lands in the half-second a pairwise judge spends
   on each comparison.
2. **It reads as grandma, not as a prompt.** A polished word ("marvellous",
   "dearie") could come from anyone. A typo can only come from someone
   typing with one finger and total confidence. That is the most
   grandma-like signal available in five letters.
3. **No language barrier.** The judge compares words two at a time; a word
   that needs Indonesian, a family backstory, or a cultural footnote risks
   losing to a word the judge gets instantly. ROBUT is readable by any
   judge in any language: R-O-B-O-T with one letter lovingly wrong.

## Alternatives considered and dropped

- CUCUKU (Indonesian: "my grandchild" — grandma adopts the AI as a
  grandchild). Funny as a family in-joke, but the judge may not know
  Indonesian, and the joke needs a translation to land. Kept as the v2
  candidate if round 1 shows ROBUT ranking low.
- HALOOO (grandma shouting hello at the device). Grandma-like, but it is
  a greeting, not a word *about AI* — it says nothing about the robot.
- SAYANG / DEARIE (terms of endearment). Warm, but generic: any grandma
  text could contain them, and they carry no joke about AI at all.

## Judging

Blind rounds (3): round 1 cutoff 24 Nov 2026 19:06 UTC (25 Nov 02:06 WIB),
round 2 on 25 Nov 19:05 UTC, final at the deadline 26 Nov 19:05 UTC
(27 Nov 02:05 WIB). No live score until rounds are judged — check
`GET /api/competitions/u-0xkianno-one-word-from-grandma-f04bed16/rounds`
after round 1. The gate is mechanical: /output/entry.txt must be UTF-8
text of 1–30 characters, not only whitespace. ROBUT is 5 characters.

## Program

`main.py`, pure Python standard library, writes ROBUT to
`/output/entry.txt`. Deterministic (identical bytes on repeat runs),
no network, no clock, no randomness. Output file chmod 0644 so the
collector can read it.
