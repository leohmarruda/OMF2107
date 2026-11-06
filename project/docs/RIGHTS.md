# Rights position and release rules

Status: decided 2026-11-05 by the project owner. This is research, not legal advice.

## Decision

OMF2107 is a **free, non-commercial fan project**. It keeps the name, the HARs, the pilots and the
references to the original One Must Fall 2097. It ships **only original assets**: no art, audio, music,
text or data file taken from the original game.

## What the research found

- Rights holder: Diversions Entertainment (© 1994). Epic MegaGames published the game but does not claim
  ownership ([Epic forum thread](https://forums.unrealengine.com/t/who-owns-the-rights-to-one-must-fall-2097-and-is-it-freeware/405924)).
- The game was declared freeware on 10 February 1999 ([Internet Archive](https://archive.org/details/OneMustFall2097)).
  The only stated terms found: users may modify and distribute as they please, as long as they do not charge for it.
  That statement is second-hand; no primary license document from Diversions was found.
- OpenOMF code is MIT licensed; some of its resources (icons) are CC-BY 4.0. It does not ship the original data
  ([repository](https://github.com/omf2097/openomf), `BUILD.md`).

## Rules for release

1. **Free only.** No sale, paywall, ads or donation tied to the game.
2. **No original assets in any distributed build.** Every entry in [ASSET_LEDGER.md](ASSET_LEDGER.md) marked
   "Not distributable" needs a replacement before release. Private tester packages stay private.
3. **Code:** OpenOMF's MIT code may be reused with its copyright notice kept. Check `src/vendored/` licenses and the
   CC-BY icon attribution before release.
4. **Game rules** (move structure, timing, stats) are mechanics, not expression, and are kept through OpenOMF parity.
5. **Disclaimer** in the README, the title screen and the store page: unofficial fan project, not affiliated with or
   endorsed by Diversions Entertainment or Epic.
6. **Permission request** to Diversions Entertainment (draft below). Send it before any public release.
7. **Takedown plan:** if the rights holder objects, remove the build quickly and rename or rework as asked.

## Accepted risk

Keeping the name "One Must Fall", the HAR names (Jaguar, Shadow, and others), the pilot names and the story
references is the owner's choice. Freeware status does not clearly grant trademark or character rights, so a
public release could be asked to rename or come down. Mitigations: items 1, 5, 6 and 7 above, and keeping the
character and story text original even where the names are kept. If the rights holder objects, the fallback is a
rename pass; the work needed is limited to names, title and branding strings.

## Permission request (draft)

> Subject: Fan project based on One Must Fall 2097 — request for confirmation
>
> Hello,
>
> I am making a free, non-commercial fan game, OMF2107, inspired by One Must Fall 2097. It uses the original
> names, robots and pilots, and contains entirely new art, audio and writing. It does not include any file from
> the original game. It will be distributed free of charge, with a notice that it is unofficial.
>
> I understand One Must Fall 2097 was released as freeware in 1999. Could you confirm that a non-commercial
> fan project like this, using the name and characters, is acceptable? If there are conditions or credits you
> would like, I will follow them.
>
> Thank you,
> [name, contact]

Add before sending: a link to the project, one screenshot, a line crediting Diversions Entertainment and OpenOMF, and
the specific list of kept names (title, HAR names, pilot names). Silence is not permission.

## What OpenOMF has, and contact routes (searched 2026-11-05)

**OpenOMF's own authorization: none found.** Its site ([openomf.org](https://openomf.org/)) states only that the game is
"now freeware", that OpenOMF is MIT licensed, and a trademark notice that "One Must Fall 2097" is a trademark of
Diversions Entertainment. It does not mention any permission or agreement with Diversions, and no source I found
reports that the original developers were contacted or gave a blessing. OpenOMF's approach: ship no original assets
(users fetch the freeware data), credit the owner, and state the trademark. That is the same position you have chosen,
so it is a reasonable precedent, but it is a precedent of tolerance, not of a licence.

**Other statements found**
- Wikipedia: "In February 1999, the game was declared freeware by the developers", with "allowances for non-commercial
  redistribution and modification". It does not name the current rights holder
  ([article](https://en.wikipedia.org/wiki/One_Must_Fall:_2097)).
- Epic Developer Community thread (October 2017): an Epic account (atypic) wrote that Epic "doesn't claim on-going
  ownership rights", accepts "the owners giving it away as freeware", and had confirmed with the IP owners that "users are
  invited to modify and distribute as they please, as long as they do not charge for it"
  ([thread](https://forums.unrealengine.com/t/who-owns-the-rights-to-one-must-fall-2097-and-is-it-freeware/405924)).
  It names no owners and gives no contact. It shows that someone at Epic had a line to them in 2017.
- Credits found on fan-edited pages: Diversions Entertainment; designer Rob Elam (with Ryan Elam), Joshua Jensen, and
  composer Kenny Chou. Treat these as names to recognise, not as addresses; do not approach private individuals without
  a lead from a project that already knows them.
- A sequel, One Must Fall: Battlegrounds (2003), shows the franchise had an active owner after 1999. Who holds it now
  is unknown.

**Contact routes, in order of low risk**
1. **OpenOMF Discord** (<https://discord.gg/7CPPzab>, "chat with players and developers") or an issue on
   [github.com/omf2097/openomf](https://github.com/omf2097/openomf): ask the maintainers whether they ever corresponded with
   Diversions, and for an introduction if so. This is the best lead and costs nothing.
2. **The Epic forum thread:** a reply asking atypic or Epic whether the owners can be reached for a fan game that keeps
   the name. They answered once, in 2017.
3. **omf2097.com** (the wiki and community site, which did not load for me when fetched): look for a contact or an
   owners' notice.
4. Only after 1 to 3, write to any contact they provide.

Do not post your project's details publicly as a question until you are ready for the answer to be public.

## Replacement checklist (assets only)

| Area | Currently from the original | Replace with |
| --- | --- | --- |
| Pilot portraits | `MELEE.BK` | New portrait artwork |
| Arena backdrops (5) | `ARENA0.BK` to `ARENA4.BK` | New arena art |
| Story illustrated frames | Built from portraits, arenas, HAR sprites | New illustrations |
| Menu and battle sound | `SOUNDS.DAT` | New sound effects |
| Music | `.PSM` modules | New music |
| Dialogue and story text | Draft built from the original lore | Original writing (the rewrite is deferred) |
| HAR visuals | Blockout and Meshy stand-ins | Final original models |
| Game data at run time | OpenOMF reads `OMF2097/` | Own data format and converted rules, or a data-free path |

The options for that are in [ENGINE_PATHS.md](ENGINE_PATHS.md). The last row needs a design decision: a build that does not ship the original data files cannot run on OpenOMF as
it stands, because OpenOMF loads the AF/BK files. The release engine must read project-made data instead.
