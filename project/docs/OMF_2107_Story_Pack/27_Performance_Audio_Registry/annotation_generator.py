from pathlib import Path
import re, csv, json, collections, hashlib, shutil
from textblob import TextBlob

ROOT=Path(__file__).resolve().parents[1]
SPECS=[('Ari', [f'04_Screenplay_Reconstructions/Chapter_0{i}_{n}_v0.{v}.md' for i,n,v in [(1,'Anniversary',4),(2,'Champions_Shadow',4),(3,'Trouble_With_Attraction',4),(4,'No_Holding_Back',4),(5,'Fractures',4),(6,'One_Must_Fall',5)]]),('Lyra',['09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.5.md']),('Mara',['10_Mara_Campaign/Mara_Playable_Screenplay_v0.3.md']),('Ren',['11_Ren_Campaign/Ren_Playable_Screenplay_v0.3.md']),('Angel',['12_Angel_Campaign/Angel_Playable_Screenplay_v0.3.md']),('Crystal',['15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.7.md']),('Raven',['16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.6.md']),('Jean-Paul',['20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.2.md']),('Steffan',['21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.4.md']),('Dante',['22_Dante_Campaign/Dante_Playable_Screenplay_v0.4.md']),('Selene',['23_Selene_Campaign/Selene_Playable_Screenplay_v0.2.md']),('Milano',['24_Milano_Campaign/Milano_Playable_Screenplay_v0.2.md']),('Christian',['18_Christian_Subplot/OMF_2107_Christian_Independent_Storyline_v0.3.md'])]
ALL=[(name,ROOT/p) for name,paths in SPECS for p in paths]
assert all(p.is_file() for _,p in ALL)
EXPRESSIONS={
'amused':('EXP-SMILE','light, teasing'), 'grateful':('EXP-SMILE','sincere'), 'teasing':('EXP-SMIRK','playful'), 'flirtatious':('EXP-FLIRT','soft, inviting'), 'affectionate':('EXP-TENDER','soft and warm'), 'excited':('EXP-BRIGHT','animated'), 'proud':('EXP-PROUD','satisfied'), 'confident':('EXP-COMPOSED','firm'), 'defiant':('EXP-DEFIANT','sharp and steady'), 'determined':('EXP-FOCUSED','steady and purposeful'), 'angry':('EXP-GLARE','hard edged'), 'resentful':('EXP-BITTER','clipped'), 'hurt':('EXP-HURT','unsteady'), 'sad':('EXP-SAD','subdued'), 'grieving':('EXP-GRIEF','strained'), 'anxious':('EXP-WORRIED','uneasy'), 'afraid':('EXP-FEAR','tremulous'), 'suspicious':('EXP-SKEPTICAL','guarded'), 'guarded':('EXP-RESERVED','controlled'), 'concerned':('EXP-CONCERN','careful'), 'sympathetic':('EXP-TENDER','gentle'), 'hopeful':('EXP-HOPE','quietly hopeful'), 'ashamed':('EXP-DOWNCAST','lowered'), 'regretful':('EXP-REMORSE','hushed'), 'contemptuous':('EXP-DISDAIN','cool'), 'manipulative':('EXP-CALCULATING','smooth'), 'threatening':('EXP-MENACE','low'), 'surprised':('EXP-SURPRISED','startled'), 'relieved':('EXP-RELIEF','released'), 'conflicted':('EXP-CONFLICTED','halting'), 'sarcastic':('EXP-DRY','dry'), 'vulnerable':('EXP-VULNERABLE','exposed'), 'commanding':('EXP-INTENSE','controlled'), 'triumphant':('EXP-TRIUMPH','emphatic')}
# Only strong lexical cues. When ambiguous, leave neutral and add to review if explicit direction suggests otherwise.
RULES=[
 ('grieving',r'\b(?:killed my|lost (?:my|them|her|him)|funeral|murdered my|never see (?:her|him|them) again|my parents (?:died|were killed))\b',6),
 ('regretful',r'\b(?:i(?:’|\x27| a)?m sorry|i was wrong|i shouldn(?:’|\x27)t have|forgive me|my mistake|i regret|i owe you an apology)\b',7),
 ('afraid',r'\b(?:i(?:’|\x27)m scared|i(?:’|\x27)m afraid|i(?:’|\x27)m terrified|don(?:’|\x27)t hurt|i can(?:’|\x27)t breathe|we(?:’|\x27)re trapped)\b',7),
 ('hurt',r'\b(?:you hurt me|i trusted you|you betrayed|you used me|i thought you cared|you lied to me|why would you do that)\b',6),
 ('affectionate',r'\b(?:i love you|love you|i care about you|i missed you|missed you|i want to be with you|i want you close|stay with me|i trust you)\b',6),
 ('flirtatious',r'\b(?:kiss me|kiss you|you(?:’|\x27)re (?:beautiful|gorgeous|sexy|handsome|attractive)|dinner with me|buy you dinner|our date|on a date|you look good|i want you close|flirt|indecently attractive|i could get used to you)\b',6),
 ('threatening',r'\b(?:you(?:’|\x27)ll regret|don(?:’|\x27)t test me|i(?:’|\x27)ll (?:kill|destroy|break) you|you have no choice|or else|you will obey|you should be afraid|you(?:’|\x27)re going to pay)\b',7),
 ('contemptuous',r'\b(?:pathetic|coward|worthless|parasite|disgusting|i despise|i pity you|you(?:’|\x27)re beneath)\b',7),
 ('angry',r'\b(?:how dare|damn you|go to hell|shut up|enough!|i hate you|stay away from her|you don(?:’|\x27)t get to|stop using|stop pretending|you lied|you (?:sold|manipulated|betrayed))\b',6),
 ('anxious',r'\b(?:i(?:’|\x27)m worried|what if (?:we|they|i)|we may be too late|i(?:’|\x27)m nervous|i don(?:’|\x27)t feel safe|something(?:’|\x27)s wrong)\b',5),
 ('concerned',r'\b(?:are you (?:okay|all right|hurt|safe)|be careful|you(?:’|\x27)re bleeding|i(?:’|\x27)m worried about|we need to get (?:you|them|her|him) out|how badly)\b',6),
 ('sarcastic',r'\b(?:how charming|how convenient|how reassuring|how generous|how thoughtful|what a surprise|that(?:’|\x27)s adorable|isn(?:’|\x27)t that convenient|a wonderful idea|lucky me)\b',5),
 ('teasing',r'\b(?:adorable|you(?:’|\x27)re blushing|don(?:’|\x27)t flatter yourself|your fan club|is that an invitation|practicing that line|trying to impress|you always see him|that concern almost sounds affectionate)\b',5),
 ('resentful',r'\b(?:you always|you never|i hate it when|you took|of course you would|don(?:’|\x27)t pretend you care)\b',4),
 ('defiant',r'\b(?:i won(?:’|\x27)t (?:be|let|give|obey|accept)|you don(?:’|\x27)t own me|i refuse|not your (?:trophy|property|decision)|i(?:’|\x27)m not your|i make my own)\b',6),
 ('commanding',r'\b(?:look at me|do as i say|listen to me|stand down|move aside|let me through|leave now)\b',5),
 ('determined',r'\b(?:we(?:’|\x27)ll find|we have to|we need to stop|i(?:’|\x27)ll make sure|i intend to|we won(?:’|\x27)t stop|i(?:’|\x27)m going to win|i won(?:’|\x27)t back down)\b',5),
 ('suspicious',r'\b(?:who authorized|who gave|you(?:’|\x27)re hiding|what aren(?:’|\x27)t you telling|doesn(?:’|\x27)t add up|something is off|why (?:did|would) you|how did you know)\b',5),
 ('vulnerable',r'\b(?:i don(?:’|\x27)t know what i feel|i don(?:’|\x27)t know how to|i need you|i(?:’|\x27)m not sure i can|i wanted you to|i felt alone)\b',5),
 ('relieved',r'\b(?:thank god|you(?:’|\x27)re alive|we made it|it(?:’|\x27)s over|you(?:’|\x27)re safe now|what a relief)\b',6),
 ('surprised',r'\b(?:what\?!|you did what|you(?:’|\x27)re alive\?|impossible!|no way!|how is that possible)\b',5),
 ('triumphant',r'\b(?:i won!|we won!|we did it!|i told you i(?:’|\x27)d win|we(?:’|\x27)ve won)\b',6),
 ('excited',r'\b(?:can(?:’|\x27)t wait|this is incredible|fantastic!|amazing!|i love this|let(?:’|\x27)s go!)\b',4),
]
RULES += [
 ('amused',r'\b(?:you\x27re joking|you must be kidding|that\x27s funny|you\x27re impossible|i\x27m amused|that\x27s hilarious|you\x27re ridiculous)\b',5),
 ('teasing',r'\b(?:are you flirting|did you rehearse|nice try|you\x27re cute|you call that|someone\x27s jealous|did you miss me|you missed me|you sound jealous|you sound impressed|i\x27ll take that as|are you inviting)\b',5),
 ('flirtatious',r'\b(?:you look (?:lovely|beautiful|handsome)|i\x27d like to kiss|i\x27ve wanted to kiss|i wanted to kiss|you look stunning|you seem (?:more )?interesting without|you (?:still )?make me nervous)\b',5),
 ('guarded',r'\b(?:not here|not now|we can\x27t talk here|this stays between us|don\x27t tell anyone|i can\x27t tell you|i\x27m not discussing|i\x27d rather not say|you\x27ll have to ask)\b',5),
 ('conflicted',r'\b(?:i want to, but|part of me|i can\x27t decide|i\x27m torn|i don\x27t know if i should|i don\x27t know whether|i don\x27t know what to believe)\b',5),
 ('hopeful',r'\b(?:maybe we could|maybe someday|there\x27s still a chance|we might still|there\x27s hope|i hope we can|i want to believe)\b',5),
 ('proud',r'\b(?:i earned|you earned|i did it|you did it|i\x27m proud|you were brilliant|i knew you could|you fought well)\b',5),
 ('resentful',r'\b(?:you only care|you always get|you get everything|you took her|all you ever|you used her|you get to|because you\x27re better|i had to watch)\b',5),
 ('suspicious',r'\b(?:how convenient for you|who benefits|what are you hiding|you knew|did you know|who signed|what happened to the|why is it missing|where did it go|that\x27s not possible)\b',5),
 ('defiant',r'\b(?:don\x27t tell me what|i decide|i choose|my decision|i\x27ll do it myself|you can\x27t make me|i\x27m not afraid of you|you don\x27t decide)\b',5),
 ('concerned',r'\b(?:i don\x27t want you hurt|please be careful|are you sure you\x27re alright|what happens to them|we have to keep them safe)\b',5),
 ('determined',r'\b(?:i\x27m here to win|i\x27m planning to win|i\x27m going to find|i\x27ll find out|i\x27ll get to the bottom|this ends tonight|we\x27re not done)\b',5),
 ('vulnerable',r'\b(?:i liked talking to you|i didn\x27t expect to|i don\x27t want to lose you|i needed you|i\x27m not good at this|i\x27m trying to trust you)\b',5),
 ('sarcastic',r'\b(?:very reassuring|how noble|congratulations,? you|you\x27re being exceptionally nice|what an honor|that\x27s rich|naturally you would|brilliant deduction|must be nice)\b',5),
]
RULES=[(name,re.compile(pt,re.I),wt) for name,pt,wt in RULES]
DIRECTION=[('angry',r'\b(?:angrily|furious|snaps|rage|hisses|glowers|glares)\b'),('excited',r'\b(?:shouts excitedly|shouts her name|cheers|cheering)\b'),('amused',r'\b(?:laughs|chuckles)\b'),('sad',r'\b(?:sadly|tears|weeping|crying|voice breaks)\b'),('flirtatious',r'\b(?:flirtatious|seductive|seductively|flirts)\b'),('teasing',r'\b(?:teasingly|teases|playfully|grinning|grins)\b'),('affectionate',r'\b(?:tenderly|softens|affectionately|fondly|warmly)\b'),('anxious',r'\b(?:anxiously|nervously|uneasy|trembles)\b'),('conflicted',r'\b(?:hesitant|hesitates|conflicted|faltering)\b'),('threatening',r'\b(?:menacing|threatening|threatens)\b'),('sarcastic',r'\b(?:dryly|sarcastically|wryly)\b'),('vulnerable',r'\b(?:quietly|whispers|barely audible)\b')]
DIRECTION=[(n,re.compile(r,re.I)) for n,r in DIRECTION]
# Hand-curated performance overrides for character-defining moments (exactly targeted phrases).
# These distinguish outward performance from the character's hidden subtext.
OVERRIDES = {
 'RAVEN': [
  ("i miss knowing who paid for the chain", "sarcastic"),  ("you didn't even ask what i wanted",'manipulative'),
  ("i wasn't going to tell you what it meant",'guarded'),
  ("yes.", "commanding"),  ("lots of things passed through it", "guarded"),  ("if i were here to threaten you", "threatening"),  ("occasionally.", "amused"),  ("you're letting another person decide",'contemptuous'),
  ("depends what you", "guarded"),  ("that's never stopped anyone from losing it", "threatening")], 'CRYSTAL': [
  ("there's a very small list",'guarded'),
  ("don't mistake that for an invitation",'defiant'),
  ("you were going to enjoy it", "accusatory"),  ("i'm not asking for your permission",'defiant'),
  ("tell us what you know", "commanding")], 'STEFFAN': [
  ("i'd be overqualified",'proud'),
  ("finally. someone who could make this tournament", "excited"),  ("i don't need a mirror when you're looking at me",'flirtatious'),
  ("why limit yourself?", "manipulative"),  ("neither is he.", "guarded"),  ("only when they're wrong", "confident"),  ("so i'm bait?", "hurt"),  ("i thought he'd come looking for you", "guarded"),  ("that came out badly", "ashamed"),  ("i do admire it", "flirtatious"),  ("i like having your hand", "possessive"),  ("may i?", "vulnerable"),  ("i wouldn't dare", 'sarcastic')],
 'LYRA': [
  ("then my night's already productive", "teasing"),  ("deliciously. about the people", "conflicted"),  ("you can stand underneath it", "teasing"),  ("my secret is refusing questions",'sarcastic'),
  ("neither. that's not the prize", "defiant"),  ("and i expected a slow opponent",'teasing'),
  ("so i'm bait?", "hurt"),  ("you have this habit of taking my hand",'suspicious'),
  ("i believe you. i also see when", 'hurt'),
  ("not when you're watching his face",'defiant'),
  ("try being honest instead",'defiant'),
  ("nearly? recheck the replay", 'teasing')],
 'DANTE': [
  ("your reflection was booked?", "sarcastic"),  ("it wasn't the looking", "resentful"),  ("i didn't promise to be graceful", "conflicted"),  ("he never stops watching", "resentful"),  ("i thought you came here to insult me", "guarded"),  ("you want the honest answer?", "guarded"),  ("did he convince you, or did you decide?", "concerned"),  ("i know you'll make your own choices", "affectionate")], 'ANGEL': [
  ("that's an excellent question. no.", "sarcastic"),  ("you are not a museum piece", "sympathetic"),  ("of questions. not of you", "affectionate"),  ("no. that's why i have trouble at parties", "sarcastic"),  ("i knew there were decorations", "sarcastic"),  ("it's an old display bug that has learned to give orders", "guarded"),  ("my public silhouette has pockets", "amused"),  ("you heard a rumor about a rumor", "teasing"),  ("you look like you have a better contract", "teasing")], 'SELENE': [
  ("and most introductions arrive with invoices", "sarcastic"),  ("you are a very poor negotiator", "teasing"),  ("you've obviously never met a good tax designation", "teasing"),  ("how disappointing", "sarcastic"),  ("don't tell my sponsors", 'teasing'),
  ("then let me give you something worth understanding", "flirtatious"),  ("most biographies are", "guarded"),  ("you flatter yourself", "teasing")], 'MILANO': [
  ("one dance. no nondisclosure agreement", "flirtatious"),  ("i can afford one exception", "flirtatious"),  ("and i was meant to be your next acquisition?", "hurt")], 'MARA': [
  ("if you're here to threaten me, take a number", "defiant"),  ("find somebody who enjoys it", "sarcastic"),  ("i've fought in pits with worse lighting", 'resentful'),
  ("i hate it when experience wins arguments", 'resentful')],
 'JEAN-PAUL': [
  ("it isn't a trap if you tell me where the wire is", "flirtatious")], 'REN': [
  ("it says who may read my intentions", "concerned"),  ("what if they take it away from me?", "anxious")],}
# Add specialized expressions to the reusable vocabulary, without requiring unique sprites per character.
EXPRESSIONS.update({'accusatory':('EXP-GLARE','sharp'), 'possessive':('EXP-INTENSE','insistent')})


# Stable character-prefix recognition, also accommodating (V.O.) and (RADIO).
BLOCK=re.compile(r'^\*\*([A-Z][A-Z0-9 .\-\x27/()]{1,50})\*\*\s*$')
INLINE=re.compile(r'\*\*([A-Z][A-Z0-9 .\-\x27/()]{1,40}):\*\*')
BAD={'CHOICE','MATCH','TECHNICAL','ENDING','OUT','IN','IF','ELSE','MUSIC','PERF','BG','STAGING','CHAPTER','SAFE CLUE','NOTE','POSTMATCH','WIN','LOSS','AUTHORITY','INT','EXT','CINEMATIC','BROADCAST','EDITORIAL','DATE'}

def is_speaker(s):
 s=s.strip(); head=s.split('(')[0].strip()
 if head in BAD or len(head)>30 or re.match(r'^\d',head): return False
 if any(x in head for x in ['—',' / ','SCENE','CHOICE','BRANCH','FLAGS','DAY ','NOVEMBER','REVEAL','SETTING','EVIDENCE','NEURAL','FIGHT','OPTIONAL','CONTRACT','AUTHORITATIVE','PLAYER','TOURNAMENT','MODALITY','FORESHADOW','MORAL','IF ','THEN ','END ','NOTES','CUT TO','MATCH ','CUTAWAY','ENDING','PATH','SYSTEM','SAFE CLUE','PHASE','PUBLIC INCIDENT','CARGO LOG','CHAPTER OUT','FINAL IMAGE','LAST IMAGE','RESTRICTED','DEFAULT','ALTERNATE','B1','B2','QUALIFIED','REVIEW','FADE','WE\'RE','ONE MUST FALL','AUDIENCE','SOLO','EXPLOIT','BARGAIN','DISCLOSE','LEAVE']): return False
 return True

def clean(t):
 t=re.sub(r'\[[^]]+\]',' ',t)
 t=re.sub(r'\*\*([^*]+)\*\*',r'\1',t)
 t=re.sub(r'`[^`]+`',' ',t)
 t=re.sub(r'^[>\s]+','',t)
 return t.strip(' \t\r\n"“”')

def emotion_for(speaker,t,near=''):
 t=clean(t); low=t.lower().replace('’',"'")
 if not t: return ('neutral',None,None,0,'empty')
 # Avoid parser artifacts/tags/technical descriptions that aren't character lines.
 if len(t)>440 or len(t)<2: return ('neutral',None,None,0,'format')
 candidates=[]
 for name,regex,wt in RULES:
  if regex.search(low): candidates.append((wt,name,'lexical'))
 # Specific verbs or exclamation help only combined with other text; never exclamation alone.
 if re.search(r'\b(?:please don\x27t|please stay|i beg you)\b',low): candidates.append((5,'vulnerable','lexical'))
 # Scene action context is only considered if explicit delivery word in speaker turn label; otherwise no inference from nearby narrative.
 if near:
  for name,regex in DIRECTION:
   if regex.search(near):
    candidates.append((7 if name not in ('vulnerable',) else 3,name,'explicit direction'))
 if not candidates:
  # Strong evaluative language in dialogue, excluding short routine acknowledgments.
  if len(t)>14 and len(t)<240:
   p,sub=TextBlob(t).sentiment
   terms=low
   if abs(p)>=.37 and sub>=.45:
    if re.search(r'\b(?:ridiculous|absurd|disgusting|terrible|arrogant|fool|idiot|stupid|pathetic|useless|worthless|shameful)\b',terms):
     candidates.append((5,'contemptuous','evaluative language'))
    elif re.search(r'\b(?:impressive|excellent|remarkable|brilliant|beautiful|talented|good fighter|better than|well done|amazing|perfect)\b',terms):
     if re.search(r'\b(?:unfortunately|irritatingly|but|never|do.n.t|not|hate|terribly|sarcastic|a shame)\b',terms) and not re.search(r'\b(?:announcer|broadcast|commentary)\b',speaker.lower()):
      candidates.append((4,'sarcastic','evaluative language'))
     elif re.search(r'\b(?:i|you|your|she|he|they|we)\b',terms):
      candidates.append((4,'teasing' if re.search(r'\b(?:you must have|you really|joke|funny|amusing|charming|good of you)\b',terms) else 'proud','evaluative language'))
    elif re.search(r'\b(?:i feel|feeling|i hope|i wish|i need|i miss|i like|i love|i hate|i appreciate)\b',terms):
     candidates.append((4,'hopeful' if p>0 else 'sad','subjective affect'))
  # Isolated exclamation, especially announcer call, as expressive but keep lower confidence.
  if not candidates and t.endswith('!') and len(t)<120 and not t.startswith(('MATCH','BG')):
   candidates.append((3,'excited','punctuation-only'))
 # Negated emotions should not be performed as their opposite.
 if re.search(r'\b(?:not|never|don\x27t|didn\x27t|won\x27t)\b.{0,40}\b(?:regret|sorry|love|miss)\b',low):
  candidates=[c for c in candidates if c[1] not in ('regretful','affectionate')]
 # Character-specific editorial override, applied only to an exact recognizable utterance.
 for phrase,override in OVERRIDES.get(speaker.split('(')[0].strip().upper(),[]):
  if low.startswith(phrase) and (phrase!='yes.' or low.strip()=='yes.'):
   code,delivery=EXPRESSIONS[override]
   return (override,code,delivery,2,'hand-curated')
 if not candidates and len(t)<160:
  if re.search(r'^(?:why would|why did|what did you|how could you|do you really|you think you|are you seriously|what makes you think)',low):
   candidates.append((3,'suspicious','rhetorical challenge'))
  elif re.search(r'^(?:no[.,!]?\s+(?:i|you|we|it)|i\x27m not your|not this time|i won\x27t)',low):
   candidates.append((3,'defiant','boundary language'))
  elif re.search(r'^(?:thank you|thanks for|i appreciate that|i\x27m glad)',low) and len(t)>14:
   candidates.append((3,'grateful','expressed gratitude'))
 if not candidates: return ('neutral',None,None,0,'no strong cue')
 candidates.sort(key=lambda x:(-x[0],-len(x[1])))
 wt,emo,basis=candidates[0]
 face,delivery=EXPRESSIONS[emo]
 intensity=3 if wt>=7 or (t.endswith('!') and emo in ('angry','threatening','triumphant')) else 2 if wt>=5 else 1
 # Never claim expression reveals unspoken identity/subtext.
 return (emo,face,delivery,intensity,basis)

MUSIC={
'MUS-ARCHIVE':'distorted archival synth and metallic percussion, restrained',
'MUS-GALA':'opulent electro-orchestral pulse, social spectacle',
'MUS-ATHLETIC':'rhythmic electro-percussion, confident athletic motion',
'MUS-ARENA':'driving electronic rock and mechanical percussion, combat intensity',
'MUS-BANTER':'light syncopated futuristic lounge groove, playful',
'MUS-ROMANCE':'warm restrained synth pads and melodic piano, intimate',
'MUS-UNEASE':'low pulsing synth drones, withheld answers',
'MUS-INVESTIGATION':'minimal ticking sequencers and suspense textures',
'MUS-ETHICAL':'dissonant ambient synth, moral unease',
'MUS-CONFRONT':'driving low strings and industrial pulses, personal conflict',
'MUS-GRIEF':'sparse piano, low sustained strings, vulnerable',
'MUS-HOPE':'subdued rising harmony and soft percussion',
'MUS-RESCUE':'urgent rhythmic electronics and high strings, rescue',
'MUS-NOVA':'unsettling polyphonic electronic textures and subbass, autonomous intelligence',
'MUS-FINALE':'hybrid orchestra and industrial electronics, final confrontation',
'MUS-AFTERMATH':'quiet elegiac synth and distant strings',
'MUS-SILENCE':'intentional environmental ambience only',
'MUS-CORPORATE':'clean futuristic ambient pulse, public-facing authority',
'MUS-CLINICAL':'minimal sterile arpeggios and soft electrical hum',
'MUS-GANYMEDE':'vast icy soundscape with slow synth chords',
}

def choose_music(bg,scene,desc):
 c=(scene+' '+desc[:450]).lower(); bg=bg.upper()
 # The real NOVA battle beats take precedence.
 if re.search(r'finale|last stand|executive veto|nova confrontation|last command|one must fall|core destruction|retention latch|gateway',c): return 'MUS-FINALE'
 if 'nova' in bg or re.search(r'containment chamber|composite core|kreissack (?:alive|sacrifice)|nova (?:itself|speaks)',c): return 'MUS-NOVA'
 if re.search(r'rescue|evacuate|emergency|coolant|catastrophe|fire|collapse|containment breach',c) or '@EMERGENCY' in bg: return 'MUS-RESCUE'
 if re.search(r'memorial|epilogue|aftermath|farewell|days? 30|day 30|death|mourn|devroe (?:death|murder)',c): return 'MUS-AFTERMATH' if re.search(r'epilogue|aftermath|day 30|memorial',c) else 'MUS-GRIEF'
 if re.search(r'confrontation|accusation|breakup|break.up|ultimatum|reckoning|argument',c): return 'MUS-CONFRONT'
 if re.search(r'romanc|kiss|intimacy|private night|tender|first date|flirt|dance|pool|after hours',c): return 'MUS-ROMANCE' if re.search(r'romanc|kiss|intimacy|tender|date|dance',c) else 'MUS-BANTER'
 if re.search(r'fight|qualif|quarterfinal|semi.final|championship|combat|sparring|match|arena',c) or 'BG-ARE-MAIN' in bg: return 'MUS-ARENA'
 if re.search(r'investigat|infiltrat|evidence|record|archive|hacking|audit|disclos|forensic|procurement|ledger|testimony|inquiry',c): return 'MUS-INVESTIGATION'
 if re.search(r'very first|anniversary|gala|press|interview|photo|spotlight|publicity',c) or 'BG-SOC-GALA' in bg: return 'MUS-GALA'
 if re.search(r'training|practice|workshop|gym|equipment|calibrat',c): return 'MUS-ATHLETIC'
 if 'BG-LAB' in bg or 'BG-MED' in bg: return 'MUS-CLINICAL'
 if 'BG-COR' in bg or 'BG-WAR' in bg: return 'MUS-CORPORATE'
 if 'BG-EXT-' in bg or 'BG-COL' in bg: return 'MUS-GANYMEDE'
 return 'MUS-UNEASE'

notes=[]; track_rows=[]; dialog_rows=[]; changes=[]; samples=collections.defaultdict(list)
for fileordinal,(protagonist,src) in enumerate(ALL,start=1):
 lines=src.read_text(encoding='utf-8').splitlines(keepends=True)
 # new revision while retaining the original.
 m=re.search(r'_v(\d+)\.(\d+)\.md$',src.name)
 assert m
 newname=src.name[:m.start()]+f'_v{m.group(1)}.{int(m.group(2))+1}.md'
 dest=src.with_name(newname)
 if dest.exists():
  raise RuntimeError(f'Output already exists: {dest}; archive it or move it before regeneration')
 last_scene='UNSPECIFIED'; last_scene_idx=0; speaker_count=0; cue_count=0; scene_count=0; speaker=None; potential_block=False
 out=[]; idx=0; current_bg=''
 # pre-store scene contexts by lookup before first dialogue
 for i,line in enumerate(lines):
  plain=line.rstrip('\n')
  if re.match(r'^#{1,4}\s+\S',plain) and not re.search(r'^# (?:ONE MUST FALL|CHAPTER)',plain,re.I):
   last_scene=plain.strip('# ').strip(); last_scene_idx+=1
  bg_match=re.search(r'\[BG:\s*(BG-[A-Z0-9-]+@[A-Z0-9-]+)',plain)
  if bg_match:
   current_bg=bg_match.group(1)
  if bg_match:
   # Avoid repeated score restarts: this is a palette cue for scene, not a hard restart.
   preview=' '.join(lines[i+1:i+12])
   track=choose_music(current_bg,last_scene,preview)
   id=f'{protagonist.upper().replace("-","_")}-{src.stem[-12:]}-{len(track_rows)+1:04d}'
   out.append(line)
   out.append(f'**[MUSIC: {track} | behavior=palette; continue_same_theme_unless_edited]**\n')
   track_rows.append({'campaign':protagonist,'source_file':str(src.relative_to(ROOT)),'active_file':str(dest.relative_to(ROOT)), 'original_line':i+1,'scene':last_scene,'bg':current_bg,'music':track,'cue_id':id,'certainty':'draft, editable'})
   scene_count+=1
   continue
  block=BLOCK.match(plain.strip())
  if block and is_speaker(block.group(1)):
   # Next non-empty line looks like a dialogue passage (no heading/action tag).
   j=i+1
   while j<len(lines) and not lines[j].strip(): j+=1
   if j<len(lines):
    nexttext=lines[j].strip()
    if nexttext and not nexttext.startswith(('**[','#','---','`','- ','* ')) and not nexttext.startswith('['):
     # Could still be prose underneath a bold heading; speaker names must be credible.
     candidate=block.group(1)
     if len(candidate.split())<=5:
      txt=[]; k=j
      while k<len(lines) and len(txt)<5:
       if not lines[k].strip(): break
       if lines[k].startswith(('##','**[','---','```')): break
       txt.append(lines[k].strip());k+=1
      quote=' '.join(txt)
      context=' '.join(x.strip() for x in lines[max(0,i-3):i])
      # If the stage direction explicitly names the speaker, include it as delivery evidence.
      matched_context=context if re.search(r'\b'+re.escape(candidate.split('(')[0].strip())+r'\b',context,re.I) and not re.search(r'\b(?:MUSIC|PERF)\b',context) else ''
      emotion,face,delivery,intensity,basis=emotion_for(candidate,quote,matched_context)
      speaker_count+=1
      dialog_rows.append({'campaign':protagonist,'file':str(dest.relative_to(ROOT)),'source_line':i+1,'utterance_id':f'{protagonist.upper().replace("-","_")}-F{fileordinal:02d}-D{speaker_count:04d}','speaker':candidate,'dialogue':quote[:280], 'tone':emotion,'expression':face or '', 'delivery':delivery or '','intensity':intensity,'evidence':basis,'review': 'yes' if basis in ('punctuation-only','subjective affect','evaluative language','rhetorical challenge','boundary language','expressed gratitude') else 'no'})
      out.append(line)
      if emotion!='neutral':
       out.append(f'**[PERF: tone={emotion} | expression={face} | delivery={delivery} | intensity={intensity}]**\n')
       cue_count+=1; samples[emotion].append((protagonist,candidate,quote[:110]))
      continue
  # Inline speaker(s) inside narration/dialogue lines. Avoid catching labels of reference metadata inside code fences.
  matches=list(INLINE.finditer(line))
  real=[m for m in matches if is_speaker(m.group(1))]
  if real:
   # Reverse replace per matched span to preserve raw wording.
   altered=line
   for ix,match in reversed(list(enumerate(real))):
    start=match.end();end=real[ix+1].start() if ix+1<len(real) else len(line)
    quote=altered[start:end] if len(real)==1 else line[start:end]
    context=' '.join(x.strip() for x in lines[max(0,i-3):i])
    short_name=match.group(1).split('(')[0].strip()
    matched_context=context if re.search(r'\b'+re.escape(short_name)+r'\b',context,re.I) and not re.search(r'\b(?:MUSIC|PERF)\b',context) else ''
    emo,face,delivery,intens,basis=emotion_for(match.group(1),quote,matched_context)
    speaker_count+=1
    dialog_rows.append({'campaign':protagonist,'file':str(dest.relative_to(ROOT)),'source_line':i+1,'utterance_id':f'{protagonist.upper().replace("-","_")}-F{fileordinal:02d}-D{speaker_count:04d}','speaker':match.group(1),'dialogue':clean(quote)[:280],'tone':emo,'expression':face or '', 'delivery':delivery or '', 'intensity':intens,'evidence':basis,'review':'yes' if basis in ('punctuation-only','subjective affect','evaluative language','rhetorical challenge','boundary language','expressed gratitude') else 'no'})
    if emo!='neutral':
     # Maintain source as in original but insert separate inline cue immediately after speaker marker.
     altered=altered[:match.end()]+f' [PERF: tone={emo} | expression={face} | delivery={delivery} | intensity={intens}]'+altered[match.end():]
     cue_count+=1; samples[emo].append((protagonist,match.group(1),clean(quote)[:110]))
   out.append(altered)
   continue
  out.append(line)
 text=''.join(out)
 assert len(text)>len(''.join(lines))
 dest.write_text('<!-- ACTIVE performance-annotated version. Original wording and background codes preserved; [PERF] and [MUSIC] are editorial, non-canonical production metadata. -->\n'+text,encoding='utf-8')
 changes.append({'campaign':protagonist,'old':str(src.relative_to(ROOT)),'new':str(dest.relative_to(ROOT)),'source_speakers':speaker_count,'expressive_cues':cue_count,'music_cues':scene_count})

DIR=ROOT/'27_Performance_Audio_Registry';DIR.mkdir(exist_ok=True)
for name,fields,records in [ ('dialogue_cues.csv',['campaign','file','source_line','utterance_id','speaker','dialogue','tone','expression','delivery','intensity','evidence','review'],dialog_rows),('scene_music_cues.csv',['campaign','source_file','active_file','original_line','scene','bg','music','cue_id','certainty'],track_rows),('script_revisions.csv',['campaign','old','new','source_speakers','expressive_cues','music_cues'],changes)]:
 with (DIR/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(records)
(DIR/'registry.json').write_text(json.dumps({'expressions':{name:{'expression_code':code,'delivery_default':delivery} for name,(code,delivery) in EXPRESSIONS.items()}, 'music':MUSIC,'script_revisions':changes,'counts':{'utterances':len(dialog_rows),'nonneutral':sum(r['tone']!='neutral' for r in dialog_rows),'music':len(track_rows)}},indent=2,ensure_ascii=False))
print('dialogue',len(dialog_rows),'nonneutral',sum(x['tone']!='neutral' for x in dialog_rows),'music',len(track_rows))
print('cues by emotion',collections.Counter(x['tone'] for x in dialog_rows).most_common(24))
print('per file',*[f'{x["campaign"]}:{x["source_speakers"]}/{x["expressive_cues"]}/{x["music_cues"]}' for x in changes],sep='\n')
print('samples:')
for emo,examples in samples.items():
 print(emo,examples[:2])
