# Rights position and release rules

Status: decided 2026-11-05 by the project owner. This is research, not legal advice.

## Decision

OMF2107 is a **free, non-commercial fan project**. It keeps the name, the HARs, the pilots and the
references to the original One Must Fall 2097. It ships **only original assets**: no art, audio, music,
text or data file taken from the original game.

## What the research found

- Rights holder: Diversions Entertainment (© 1994). Epic MegaGames published the game but does not claim
  ownership ([Epic forum thread](https://forums.unrealengine.com/t/who-owns-the-rights-to-one-must-fall-2097-and-is-it-freeware/405924)).
- **Primary source (found 2026-11-10):** a post by Rob Elam, 10 February 1999, from www.omf.com (Wayback capture of
  2011-07-08; saved as `rights_sources/omffree_rob_elam_1999-02-10.txt`). Key wording: "I talked to Epic about the state of OMF2097 and
  it's not available through them, or anyone else ... OMF2097 is now freeware! All you people that have copies of it can
  distribute it freely. It will not be available through this site or Epic's ... We will offer absolutely no technical
  support and neither will Epic." This covers **free distribution of copies of the game**. It says nothing about
  modification, derivative works, names, characters or trademarks, and it states no conditions. It is a forum-style
  post, not a licence document.
- The [Internet Archive item](https://archive.org/details/OneMustFall2097) (saved copy: `rights_sources/internet_archive_item_omf2097.html`) only carries an uploader
  note, added 2012-07-24: "Diversions Entertainment has generously made this game freeware." No date, no terms; not
  a primary source.
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
8. **Battlegrounds is off limits.** No code, assets, design documents or lore from One Must Fall: Battlegrounds
   without the owner's agreement. Reviewing it for ideas is allowed; copying is not.
9. **No sign of monetization** of any kind, including donation links, since the community reads this strictly.

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
> I am making a free, non-commercial fan game, OMF2107, a derivative of One Must Fall 2097 with new mechanics (a
> career mode with localized damage and repairs, a new story, and a 3D presentation). It uses the original
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
  is unknown (see "Findings 2026-11-10" below).

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

## Findings 2026-11-10 (OpenOMF Discord export, Battlegrounds agreement, Epic thread)

Sources are in `rights_sources/` (index in its `README.md`): the Discord export (dates DD/MM/YYYY), the Battlegrounds
agreement (unsigned copy) and the saved Epic thread. On 2026-11-10 the project owner posted a message to the Discord
asking whether the derivative reading is accurate and whether to rebrand (`rights_sources/discord_post_2026-11-10.md`);
replies are logged there.

**Replies (2026-11-10).** No written source, no takedown precedent, no contact for Rob. Opinions: the grant is "very
vague" (Vagabond); freeware means distributing the unmodified files, and directly remaking things "might be too close"
(joneirik); the OMF name may be licensed to others elsewhere, so avoid the original name (katajakasa); Rob Elam
"seems uninterested in exercising" remaining rights, and non-commercial use is "probably ok" (Vagabond). Battlegrounds
is not covered by the 2097 waiver (Vagabond). **Decision 2026-11-10 (project owner):** rebrand and credit, as the
safest course. See "Rebrand" below.

**Rebrand.** Provisional new title: Steel Skin 2100 (2026-11-10). Intended scope to be settled in `DEVPLAN.md` (open decision "Project name"): at minimum a new title with no
"One Must Fall" or "OMF" in it, with credit and a disclaimer; the further question is whether HAR names, pilot names and
HAR designs also change. A title change alone does not answer the likeness concern raised above. Credit is courtesy,
not permission: credit OpenOMF (its MIT notice is required for reused code), and credit Diversions Entertainment and Rob
Elam as inspiration with the "unofficial, not affiliated" disclaimer. Everything below is forum opinion or
second-hand unless marked otherwise. None of it is a licence or legal advice. **Re-check for newer developments before
relying on it** (see "Confirming").

- **Ownership.** The Battlegrounds agreement (template between Rob Elam / Diversions Entertainment and Travis Best, no
  signatures in our copy) says the Client "will hold all intellectual property rights to OMF and the Software including
  ... copyright and trademark rights". Discord statements differ: Malfrex (14/12/2020) said 2097 belongs to Epic and
  Battlegrounds to Rob Elam; joneirik (19/12/2022) said it is mostly Rob, with a few things at Epic. Kamekaze
  (07/03/2025) named Brandon Cobb (Super Fighter Team) as a current 2097 rights holder; Malfrex doubted it. Unverified.
- **Status.** Dormant. Nothing for sale (Vagabond, 14/12/2020). Malfrex (26/06/2024): "We also can't do anything with
  the IP proper, ie. make OMF 2."
- **Permission, as reported.** Rob Elam, second-hand via joneirik (26/06/2024): "Do whatever you want with omf2097 as
  long as you don't make money of it... and as long as you stop pestering me." Epic thread (atypic, 03/10/2017):
  confirmed with the IP owners that users "are invited to modify and distribute as they please, as long as they do not
  charge for it". Two second-hand sources agree on the non-commercial condition. Vagabond (OpenOMF web port, 2026):
  "should be in the clear" if non-commercial; katajakasa: "there can be no sign of monetization".
- **Limits.** "Freeware" is not a binding licence (MageKing17, 17/10/2021). "All we have is a promise" (Vagabond,
  25/11/2024); wholesale verbatim copying of assets is not fair use. A DMCA takedown was mentioned as cheap and easy
  (Vagabond, 14/12/2020). Fan art not for profit was called fine (Malfrex, 14/12/2020).
- **Battlegrounds agreement terms.** The licence is non-exclusive, non-transferable and non-sublicensable and covers
  only the Battlegrounds software and the Phoenix engine for the named developer. Compiled builds may go to users, but
  no externally licensed assets (textures, models, audio) without the approval of the external licensees. Payments
  such as Patreon are allowed for that project and revocable. It grants nothing to this project.
- **Naming.** No rule found. Malfrex (14/12/2020) said a fan game under another name would be fine but warned that
  HAR likenesses or calling robots "HARs" is risky. Vagabond was unsure the OMF trademarks are maintained.
- **Music.** Rights unclear (joneirik, 19/12/2022): composer Kenny Chou (CCCatch) made the score for Diversions.
- **Contacts.** Rob Elam: no address. "Rob is find-able" (Malfrex, 14/12/2020) but "effectively disappeared" (26/06/2024).
  A person called Justin may be able to reach him (joneirik, 25/11/2024; surname not given). Do not pester.
- **1999 declaration.** Obtained 2026-11-10 and quoted under "What the research found". Note the gap: it grants free
  distribution of copies only. The "modify and distribute... do not charge" wording exists only in the second-hand Epic
  thread and the Rob Elam quote relayed on Discord, so permission for derivative work with new mechanics rests on
  those, not on the declaration.

**Effect on the plan:** keep the free, non-commercial stance and the takedown plan; send at most one short permission
message; treat Battlegrounds as Rob Elam's and off limits; check how much HAR terminology and likeness the project
keeps (name decision in `DEVPLAN.md`).

### Confirming

Web search 2026-11-10: no public source found for the Cobb / Super Fighter Team claim (Cobb's known Super Fighter Team
rights were a gift from C&E for a different game), and no news of a change of OMF 2097 or Battlegrounds ownership. This
is absence of evidence, not a refutation; the Discord itself was not searchable from here.

Before relying on the above, look for developments after the dates in the sources: the OpenOMF Discord rights channel and
pinned posts (anything after the export date), the OpenOMF GitHub issues and discussions, omf2097.com, and the
superfighter.com site for the Cobb claim. Record what you find here with its date.

## Replacement checklist (assets only)

| Area | Currently from the original | Replace with |
| --- | --- | --- |
| Pilot portraits | `MELEE.BK` (no longer read by the story viewer since 2026-11-06; still used to compose the older Crystal-story frames and the news frames) | New portrait artwork (done for the viewer: `project/renders/`) |
| Arena backdrops (5) | `ARENA0.BK` to `ARENA4.BK` | New arena art |
| Story illustrated frames | Built from portraits, arenas, HAR sprites | New illustrations |
| Menu and battle sound | `SOUNDS.DAT` | New sound effects |
| Music | `.PSM` modules | New music |
| Dialogue and story text | Draft built from the original lore | Original writing (the rewrite is deferred) |
| HAR visuals | Blockout and Meshy stand-ins | Final original models |
| Game data at run time | OpenOMF reads `OMF2097/` | Own data format and converted rules, or a data-free path |

The options for that are in [ENGINE_PATHS.md](ENGINE_PATHS.md). The last row needs a design decision: a build that does not ship the original data files cannot run on OpenOMF as
it stands, because OpenOMF loads the AF/BK files. The release engine must read project-made data instead.
