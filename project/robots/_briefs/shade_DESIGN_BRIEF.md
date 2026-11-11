# Robot design brief and derivation log: Shade (provisional name, 2026-11-10)

Draft 2026-11-10. Template: `../DESIGN_BRIEF_TEMPLATE.md`. Fields marked **(you)** need the project owner's decision.

- **Status:** draft
- **Date, author:** 2026-11-10, project owner with Claude (role section only)
- **Replaces (development placeholder):** Shadow (decided 2026-11-10)

## 1. Role (kept, because these are mechanics)

- Weight class and size feel: **(you)** medium, with a stealthy, unsettling presence.
- Range and speed identity: a trickster. Mid range, deceptive timing, positional tricks, not raw speed or armour.
- Move set: the Shadow move set is kept for now (decided 2026-11-10), which keeps parity work valid; revisit after the
  M2 parity gate. The original Shadow's shadow attacks (including a
  Shadow Punch available only at enhancement level 3) are mechanics; if kept, they need new names and new visual
  effects, since the visuals and names are what makes them look like the original.
- Signature special(s), by function only: an afterimage or decoy that confuses spacing; a teleport-style reposition; a
  delayed strike. Define each by what it does to the opponent's reads, in game terms.
- Pilot fit: **(you)**. For readability (spec section 5): deception must not break fight readability. Decoys and
  afterimages need a clear tell for the real hitbox, and no hit may come from a purely invisible source.
- Balance guardrail: no invulnerability or unreadable hits; deception comes from timing and spacing.

## 2. Identity (new, must not echo the original look)

- **Name:** Shade (provisional). Caution: "shade" is a synonym of "shadow", so the name points straight at the robot it
  replaces. Treat it as a placeholder name and review it against the derivation rule before it is final.
- **Concept in one sentence:** **(you)** for example "a stealth chassis that fights half out of sight".
- **Silhouette:** **(you)** three shapes. Must differ from the original Shadow's, and must not copy the character
  that inspired the mood (see references).
- **Proportions:** **(you)**
- **Materials and colour:** dark palette, but readable on every arena: use rim light, a coloured accent, or a
  distinct edge so it never disappears. A fully black figure also fails the readability rule.
- **Non-humanoid parts, if any:** **(you)** (trailing cloth, afterimage parts, detachable decoys: each a rig and
  collision question for R16 and R18; cosmetic parts stay deterministic and never touch hitboxes)
- **Damage regions:** **(you)**

## 3. Derivation log

- **Echoes the original robot:** Shadow (decided 2026-11-10)
- **Carried over:** trickster role, mid-range identity, the full move set (for now), and the shadow theme in the name (see name caution)
- **Deliberately different:** **(you)**
- **References used:** mood reference only: the "shadowy, half-seen" feeling that the project owner associated with
  Noob Saibot from Mortal Kombat. That is another company's character. Do not use his silhouette, outfit, colours,
  face, powers (clone, shadow-merge) or name; list here any generic references actually used instead (real-world
  stealth, ninja, black-ops, ink, smoke, night photography), with links.
- **Side-by-side silhouette check:** not done. Check against both the original Shadow and the mood reference.
- **Tracing or painting over original art:** none (confirm when art starts)

## 4. Production

- Blockout look, mesh look, asset sources, stage (H1 to H5): not started
- Open questions: final name (see caution); how the shadow effect is shown without hurting readability; new names and
  visuals for the kept shadow attacks
