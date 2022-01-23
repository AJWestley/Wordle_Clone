from random import choice

class Word:

    TOTALLY_WRONG = 0
    WRONG_PLACE = 1
    CORRECT = 2
    EMPTY = 3
    INPUT_KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']
    ROWS = 6
    COLUMNS = 5

    WORDS = ('PZAZZ', 'JAZZY', 'BUZZY', 'FUZZY', 'FIZZY', 'WHIZZ', 'DIZZY', 'FRIZZ', 'MEZZO', 'PIZZA', 'WIZZO', 'JACKY',
             'JEEZE', 'JUMPY', 'JAMMY', 'JIMMY', 'JIFFY', 'JUNKY', 'QUACK', 'QUICK', 'ZAPPY', 'ZIPPY', 'JACKS', 'JOCKS',
             'JUMBO', 'JUMPS', 'QUAKY', 'JAGGY', 'JERKY', 'JIGGY', 'JIVEY', 'JOKEY', 'JUICY', 'JUKED', 'JUNKS', 'KLUTZ',
             'BOOZY', 'CRAZY', 'FUZED', 'GIZMO', 'HIJAB', 'JIVED', 'JOKED', 'JUKES', 'MIXUP', 'QUAKE', 'QUARK', 'QUIRK',
             'QUALM', 'UNZIP', 'WOOZY', 'AFFIX', 'BANJO', 'BLAZE', 'BLITZ', 'BURQA', 'CHUCK', 'EQUIP', 'FJORD', 'FUJIS',
             'FUZES', 'JAKES', 'JAPAN', 'JAWED', 'JELLY', 'JENNY', 'JERKS', 'JEWEL', 'JIVER', 'JIVES', 'JOKER', 'JOKES',
             'JOLLY', 'JUBES', 'JUDGE', 'JUICE', 'KAZOO', 'KICKY', 'MUCKY', 'OXBOW', 'PIQUE', 'PLAZA', 'QUBIT', 'QUIPS',
             'VISOR', 'WALTZ', 'YUCKY', 'ZINCS', 'AMAZE', 'BOOZE', 'BRAZE', 'BUMPY', 'CHECK', 'CHICK', 'CHUFF', 'CHUMP',
             'CLUCK', 'COCKY', 'CRAZE', 'CUBBY', 'CUPPY', 'DJINN', 'DOOZY', 'EJECT', 'EMOJI', 'ENJOY', 'FRITZ', 'FROZE',
             'GANJA', 'GAUZE', 'GAZED', 'GLAZE', 'GLITZ', 'HAZED', 'HAZEL', 'JEEPS', 'JOHNS', 'JOLTY', 'JOYED', 'KNACK',
             'KNICK', 'KNOCK', 'MAJOR', 'MAZES', 'MICKY', 'MUMMY', 'PECKY', 'PICKY', 'PLUCK', 'PRIZE', 'PROXY', 'PUFFY',
             'PUMPY', 'PUPPY', 'PYGMY', 'QUAYS', 'QUELL', 'QUERY', 'QUILL', 'SPAZA', 'TOPAZ', 'UNBOX', 'UNFIX', 'UNMIX',
             'VEXED', 'VIXEN', 'WACKY', 'WAZOO', 'WHACK', 'WHUMP', 'ZEBRA', 'ZINGS', 'ZOOMS', 'AGAZE', 'AMUCK', 'AXMEN',
             'AXMAN', 'BEAUX', 'BLACK', 'BLOCK', 'BLUFF', 'BOBBY', 'BOXED', 'BUCKO', 'BUCKS', 'BULKY', 'CHAMP', 'CHIMP',
             'CHOMP', 'CHIMP', 'CHUNK', 'CLACK', 'CLICK', 'CLOCK', 'CLUMP', 'CODEX', 'COMFY', 'DAZED', 'DIVVY', 'DOZED',
             'DOZEN', 'DUCKY', 'EXCEL', 'EXPEL', 'FAXED', 'FELIX', 'FIXED', 'FLACK', 'FLECK', 'FLICK', 'FLOCK', 'FLUFF',
             'FLYBY', 'FOXED', 'FUNKY', 'GAWKY', 'GAZER', 'GAZES', 'GRAZE', 'GUMMY', 'GUPPY', 'HACKY', 'HAZES', 'HERTZ',
             'HUBBY', 'HUFFY', 'HUMPH', 'HUMPY', 'INBOX', 'INFIX', 'JADED', 'JAUNT', 'JELLO', 'JERRY', 'JESSY', 'JETTY',
             'JILLS', 'JOEYS', 'JOULE', 'JUDAS', 'JUDOS', 'JULIA', 'KICKS', 'KINKY', 'LAZED', 'LUCKY', 'MIXED', 'MOMMY',
             'MUCKS', 'NINJA', 'NYMPH', 'PEPPY', 'PIXEL', 'PLACK', 'PLUMB', 'POMMY', 'POPPY', 'PUCKS', 'PUNKY', 'QUADS',
             'QUAIL', 'QUEEN', 'QUEUE', 'QUILT', 'QUINS', 'SQUAD', 'SQUID', 'VEXER', 'VEXES', 'WAXED', 'WEBBY', 'WHIFF',
             'WHOMP', 'WIMPY', 'YUMMY', 'ZESTY', 'ZITTY', 'ZONED', 'ZOOTY', 'ABACK', 'ADOZE', 'AQUAS', 'AXING', 'AXIOM',
             'AZURE', 'BACKS', 'BLIMP', 'BOXER', 'BOXES', 'BRICK', 'BUFFS', 'BUGGY', 'BUMPS', 'BUNCH', 'BYWAY', 'CHALK',
             'CHEWY', 'CLAMP', 'CLIFF', 'CLIMB', 'CLUNK', 'COCKS', 'CRACK', 'CRUMB', 'CUBIC', 'CUFFS', 'CUPPA', 'CURVY',
             'DAZES', 'DOJOS', 'DOZER', 'DOZES', 'DUMMY', 'DUMPY', 'EXACT', 'EXAMS', 'EXECS', 'EXPAT', 'FAXES', 'FIXER',
             'FIXES', 'FLAKY', 'FLUNK', 'FOXES', 'FRACK', 'FROCK', 'GABBY', 'GLYPH', 'GUNKY', 'HAPPY', 'HELIX', 'HEXED',
             'HOPPY', 'HIPPY', 'HOBBY', 'HULKY', 'HUNKY', 'JADES', 'JAILS', 'JANES', 'JARLS', 'JEANS', 'JOINS', 'JOINT',
             'JOLTS', 'JONES', 'JOUST', 'JUROR', 'JUSTS', 'KAYAK', 'KEBAB', 'KHAKI', 'LAZES', 'LUMPY', 'MAXES', 'MILKY',
             'MIXES', 'MOCKS', 'MOXIE', 'MULCH', 'MUMBO', 'MUMPS', 'MUNCH', 'MURKY', 'MUSKY', 'OOZED', 'OZONE', 'PACKS',
             'PICKS', 'PINKY', 'POPUP', 'PRICK', 'PSYCH', 'PUBIC', 'PUFFS', 'PUMPS', 'PUNCH', 'QUART', 'QUASI', 'QUEER',
             'QUEST', 'QUIET', 'QUITE', 'QUITS', 'QUOTA', 'QUOTE', 'RAZED', 'REFIX', 'REMIX', 'REWAX', 'SAVVY', 'SCUFF',
             'SHUCK', 'SIZED', 'SKIMP', 'SKULK', 'SKUNK', 'SMACK', 'SPECK', 'SQUAT', 'SUCKY', 'TOXIC', 'VAMPS', 'VOUCH',
             'WACKO', 'WACKS', 'WAXER', 'WAXES', 'WHICH', 'WICKS', 'WONKY', 'WRACK', 'WRECK', 'YAPPY', 'ZONER', 'ZONES',
             'ANNEX', 'APPLY', 'AXLED', 'BAGGY', 'BARKY', 'BEAKY', 'BEBOP', 'BELCH', 'BENCH', 'BICEP', 'BIMBO', 'BLANK',
             'BLINK', 'BOGGY', 'BOMBS', 'BULKS', 'BUNKS', 'BUTCH', 'BYLAW', 'CAKEY', 'CAMPS', 'CHEEK', 'CHOKE', 'CHIVE',
             'CHUBS', 'CHUMS', 'CLANK', 'CLINK', 'CLONK', 'COMBO', 'COMBS', 'COMIC', 'COMMA', 'CONCH', 'CRAMP', 'CRIMP',
             'CRUNK', 'CYCAD', 'DEBBY', 'DUCKS', 'EXUDE', 'EXULT', 'FAFFS', 'FANCY', 'FAWNY', 'FEMME', 'FIGGY', 'FINCH',
             'FLAMY', 'FLANK', 'FLUKE', 'FOGGY', 'FUNKS', 'GAWKS', 'GECKO', 'GRUFF', 'GRUMP', 'GULCH', 'GYPSY', 'HACKS',
             'HANKY', 'HAVOC', 'HAWKS', 'HEXER', 'HEXES', 'HUFFS', 'HUMPS', 'HUNCH', 'HUSKY', 'IMPLY', 'INDEX', 'JEERS',
             'JESSE', 'JESTS', 'KINKS', 'KIRBY', 'KNAVE', 'KNOWN', 'KONKS', 'LIPPY', 'LOBBY', 'LUCKS', 'LYNCH', 'MACAW',
             'MAMBA', 'MIFFS', 'MIMIC', 'MINCY', 'MOMMA', 'NAPPY', 'NEXUS', 'NIPPY', 'OOZES', 'PEAKY', 'PEGGY', 'PERKY',
             'PERVY', 'PESKY', 'PIGGY', 'PIMPS', 'PINCH', 'PLANK', 'PLONK', 'POKEY', 'POPPA', 'PORKY', 'POUCH', 'PUDGY',
             'PUKED', 'PUNKS', 'RAZER', 'RAZES', 'RAZOR', 'REDUX', 'ROCKY', 'SCAMP', 'SCOFF', 'SEIZE', 'SHACK', 'SHOCK',
             'SIXTH', 'SIXTY', 'SIZES', 'SNUCK', 'SMOKY', 'SPIKY', 'SPUNK', 'SWAMP', 'TACKY', 'THICK', 'THUMB', 'THUMP',
             'TUBBY', 'TUMMY', 'TZARS', 'UNSEX', 'VALVE', 'VIVID', 'VODKA', 'WAVEY', 'WENCH', 'WHELM', 'WHELP', 'WHISK',
             'WIMPS', 'XENON', 'YACKS', 'YOLKY', 'ZESTS', 'ABBEY', 'ALBUM', 'AWFUL', 'AXLES', 'BAKED', 'BANKS', 'BATCH',
             'BEACH', 'BEAMY', 'BEEFY', 'BIKED', 'BIRCH', 'BITCH', 'BLEAK', 'BLOKE', 'BLOWN', 'BLUBS', 'BLURB', 'BOINK',
             'BONKS', 'BOTCH', 'BOUGH', 'BRINK', 'BUDDY', 'BULBS', 'BULLY', 'BUNNY', 'BURKA', 'BUSHY', 'BUSKS', 'CACHE',
             'CAKED', 'CAVED', 'CATCH', 'CHAFE', 'CHAPS', 'CHARM', 'CHASM', 'CHEAP', 'CHEEP', 'CHEFS', 'CHEMO', 'CHEWS',
             'CHIEF', 'CHIME', 'CHING', 'CHIPS', 'CHIRP', 'CHOPS', 'CHOWS', 'CHUGS', 'CIVIL', 'CLERK', 'CLOAK', 'CLOVE',
             'CLOWN', 'CLUBS', 'CLUNG', 'COACH', 'CONKS', 'COTCH', 'COUGH', 'COVEN', 'CRANK', 'CRYPT', 'CUBED', 'CUMIN',
             'CUPID', 'CURVE', 'CUSHY', 'CYBER', 'DECKS', 'DETOX', 'DICKS', 'DINKY', 'DOCKS', 'DUMBO', 'DUMPS', 'DUMBS',
             'DUSKY', 'DYKED', 'EMPTY', 'EPOCH', 'EVOKE', 'EXALT', 'EXILE', 'FAKED', 'FETCH', 'FIFTH', 'FIFTY', 'FLAKE',
             'FLASK', 'FLOWN', 'FLUME', 'FLUNG', 'FOAMY', 'FOLKS', 'FRANK', 'FULLY', 'FUMED', 'FUNNY', 'GAFFS', 'GAMMA',
             'GEEKY', 'GEMMA', 'GLOWY', 'GLUGG', 'GRAVY', 'HEAVY', 'HEMPS', 'HIPPO', 'HOKEY', 'HOWDY', 'HULKS', 'HUNKS',
             'HYMNS', 'HYPED', 'KAPUT', 'KELLY', 'KELPS', 'KIOSK', 'KNIFE', 'KNOBS', 'KNOWS', 'LACKA', 'LANKY', 'LATEX',
             'LAYBY', 'LEXIS', 'LICKS', 'LOCKS', 'LOCUM', 'LUMPS', 'LUNCH', 'MACHO', 'MAGIC', 'MAGMA', 'MANGY', 'MARCH',
             'MATCH', 'MAUVE', 'MAYBE', 'MERCH', 'MERCY', 'MIKED', 'MILKS', 'MITCH', 'MOCHA', 'MONKS', 'MUCUS', 'MUDDY',
             'MURKS', 'MUSHY', 'MUSKS', 'NECKS', 'NICKS', 'NUMBS', 'OHMIC', 'PARCH', 'PATCH', 'PAVED', 'PEACH', 'PERCH',
             'PHONY', 'PIKED', 'PINKS', 'PINUP', 'PITCH', 'PLUME', 'PLUMS', 'POACH', 'POKED', 'POLKA', 'POOCH', 'POOFY',
             'POOPY', 'PORCH', 'PRANK', 'PRICY', 'PUKES', 'PULPS', 'PUNNY', 'PUPIL', 'PUSHY', 'RELAX', 'RUGBY', 'SEXED',
             'SHAKY', 'SLACK', 'SLICK', 'SNACK', 'SNICK', 'SNUFF', 'SOPPY', 'SPANK', 'SPICY', 'STUCK', 'SUCKS', 'SULKY',
             'TABBY', 'TAFFY', 'TAMMY', 'TAXED', 'THUNK', 'TIKKA', 'TOFFY', 'TOMMY', 'TOXIN', 'TRUCK', 'TUCKS', 'TUXES',
             'UNCAP', 'UPPED', 'VAPID', 'VENOM', 'VIBED', 'VICED', 'VINYL', 'VOCAL', 'WAKEN', 'VOWED', 'VOWEL', 'WALKS',
             'WATCH', 'WAVED', 'WEDGY', 'WEEPY', 'WHARF', 'WHIMS', 'WHINY', 'WHIPS', 'WINKS', 'WITCH', 'WIVED', 'WOKEN',
             'WORMY', 'WOVEN', 'YAWNY', 'ABOVE', 'AMBLE', 'AMPED', 'AMPLE', 'APPAL', 'APPLE', 'ASKEW', 'AWAKE', 'AWOKE',
             'BABEL', 'BACON', 'BADDY', 'BADLY', 'BAKER', 'BAKES', 'BALDY', 'BALMS', 'BARKS', 'BASKS', 'BAWLS', 'BEAKS',
             'BEGUN', 'BELLY', 'BELOW', 'BENDY', 'BENNY', 'BIBLE', 'BIKER', 'BIKES', 'BILLY', 'BIPED', 'BLABS', 'BLAME',
             'BLEEP', 'BLING', 'BLIPS', 'BLOBS', 'BLOOM', 'BLOOP', 'BLOWS', 'BLUEY', 'BLUSH', 'BOGEY', 'BONNY', 'BOOGY',
             'BOOKS', 'BOWED', 'BOWEL', 'BOWLS', 'BRAKE', 'BRAVO', 'BRAWL', 'BRAWN', 'BREAK', 'BRISK', 'BROKE', 'BROOK',
             'BROWN', 'BUDGE', 'BUGLE', 'BULGE', 'BUNDU', 'BURLY', 'BURPS', 'CABIN', 'CABLE', 'CADDY', 'CAKES', 'CALMS',
             'CAMEL', 'CANDY', 'CARVE', 'CAVES', 'CAWED', 'CELEB', 'CHILD', 'CHILL', 'CHURN', 'CLAIM', 'CLAMS', 'CLANG',
             'CLAPS', 'CLASP', 'CLAWS', 'CLEFS', 'CLEFT', 'CLING', 'CLIPS', 'COBLE', 'CODEC', 'COKES', 'COOKS', 'COPED',
             'COUPE', 'COVER', 'COVES', 'COVET', 'COWLS', 'CRAVE', 'CRAWL', 'CREAK', 'CREEK', 'CROOK', 'CROWD', 'CROWN',
             'CUBES', 'CURBS', 'CURLY', 'CUSPS', 'DEBUG', 'DECAF', 'DIMLY', 'DOGGY', 'DORKY', 'DRUNK', 'DUNKS', 'DUTCH',
             'DWARF', 'DWEEB', 'EBBED', 'EBIKE', 'EBOOK', 'ELBOW', 'EMBED', 'ENVOY', 'EVICT', 'EXEAT', 'EXERT', 'EXIST',
             'EXITS', 'EXTRA', 'FABLE', 'FACED', 'FAKER', 'FAKES', 'FAMED', 'FAWNS', 'FECAL', 'FEMUR', 'FENCE', 'FEVER',
             'FIGHT', 'FILMS', 'FISHY', 'FIVES', 'FLAME', 'FLAPS', 'FLAWS', 'FLING', 'FLIPS', 'FLOPS', 'FLOWS', 'FLUSH',
             'FOCAL', 'FOCUS', 'FOGEY', 'FOLLY', 'FORKS', 'FORUM', 'FOWLS', 'FREAK', 'FRISK', 'FROWN', 'FUDGE', 'FUGAL',
             'FUGUE', 'FUMER', 'FUMES', 'FUNGI', 'GAVEL', 'GIVEN', 'GLOVE', 'GNAWN', 'GOOFY', 'GOOPY', 'GRAPH', 'GUAVA',
             'GULFS', 'GULLY', 'GULPS', 'HAIKU', 'HALVE', 'HANKS', 'HARPY', 'HATCH', 'HAVEN', 'HEFTY', 'HIKED', 'HITCH',
             'HONKS', 'HUMAN', 'HUMID', 'HUMUS', 'HUSKS', 'HYPER', 'HYPES', 'IMBUE', 'ITCHY', 'KARMA', 'KEEPS', 'KEYED',
             'KINGS', 'KIWIS', 'KUDUS', 'KYLES', 'KYLIE', 'LAMBS', 'LAMPS', 'LAYUP', 'LEAKY', 'LEMMA', 'LIMBO', 'LIMBS',
             'LIMPS', 'LOOKY', 'LOVEY', 'LOWLY', 'LURCH', 'MACED', 'MACON', 'MADAM', 'MADLY', 'MAKER', 'MANIC', 'MANLY',
             'MARKS', 'MAPLE', 'MASKS', 'MEDIC', 'MEWED', 'MIGHT', 'MIKES', 'MIMED', 'MINCE', 'MODEM', 'MOLDY', 'MOLLY',
             'MOPED', 'MOVIE', 'MOWED', 'MUSIC', 'MYTHS', 'NAGGY', 'NANCY', 'NEWLY', 'NUKED', 'OCCUR', 'OFFED', 'OPIUM',
             'PACED', 'PADDY', 'PALMS', 'PANIC', 'PARKA', 'PARKS', 'PAVER', 'PAVES', 'PAWED', 'PAWNS', 'PEAKS', 'PECAN',
             'PEEVE', 'PENCE', 'PENNY', 'PERKS', 'PERVS', 'PHAGE', 'PIKES', 'PIPED', 'PIVOT', 'PLACE', 'PLEBS', 'PLOWS',
             'PLUGS', 'PLUSH', 'POKER', 'POKES', 'POLLY', 'PORKS', 'PRAWN', 'PROVE', 'PROWL', 'PSALM', 'PUMAS', 'PUPAE',
             'PYLON', 'RACKS', 'RHYME', 'ROCKS', 'RUMBA', 'SACKS', 'SCALP', 'SCOWL', 'SCRUB', 'SCRUM', 'SCUBA', 'SCUMS',
             'SEXES', 'SHANK', 'SHOWY', 'SHYLY', 'SILKY', 'SIXES', 'SKEWS', 'SKIMS', 'SKIPS', 'SKULL', 'SLUNK', 'SMIRK',
             'SMOKE', 'TRICK', 'SNIFF', 'SOCKS', 'SOPHY', 'SPARK', 'SPAWN', 'SPEAK', 'SPIKE', 'SPOKE', 'SPOOK', 'STACK',
             'STICK', 'STOCK', 'STUFF', 'STUMP', 'SWUNG', 'TACKS', 'TAXES', 'TAXIS', 'TEXAS', 'TEXTS', 'THANK', 'THINK',
             'THYME', 'TICKS', 'TRUMP', 'TWEAK', 'UMBRA', 'UNHIP', 'UNIFY', 'UNPEG', 'UPPER', 'UVULA', 'VAGUE', 'VEGAN',
             'VEINY', 'VERBS', 'VIBES', 'VICAR', 'VICES', 'VIEWS', 'VIPER', 'VLOGS', 'VOICE', 'VOMIT', 'VROOM', 'WAKER',
             'WAKES', 'WALLY', 'WASHY', 'WAVER', 'WAVES', 'WEAVE', 'WEEKS', 'WEIGH', 'WIDOW', 'WIKIS', 'WILLY', 'WINCE',
             'WINDY', 'BOOBY', 'WIPED', 'WIVES', 'WOMAN', 'WOMEN', 'WORKS', 'WOWED', 'WREAK', 'WRUNG', 'YACHT', 'YANKS',
             'YOLKS', 'ABEAM', 'ACHED', 'ACIDY', 'AGLOW', 'ALPHA', 'AMBER', 'AMONG', 'ANVIL', 'APTLY', 'BABES', 'BADGE',
             'BAGEL', 'BANGS', 'BARBS', 'BARFS', 'BASIC', 'BEADY', 'BEAMS', 'BEEFS', 'BEEPS', 'BEGAN', 'BEGIN', 'BEING',
             'BINGE', 'BIOME', 'BIRDY', 'BLAND', 'BLEND', 'BLIND', 'BLOND', 'BLUED', 'BLUNT', 'BOGUS', 'BOING', 'BONEY',
             'BONGO', 'BOOBS', 'BOOMS', 'BOSOM', 'BOUND', 'BOWER', 'BRACE', 'BREWS', 'BRIBE', 'BRIEF', 'BRING', 'BROOM',
             'BROWS', 'BRUSH', 'BUILD', 'BULLS', 'BUOYS', 'BUSTY', 'BUYER', 'CACAO', 'CACTI', 'CAFES', 'CAGED', 'CAMEO',
             'CAPER', 'CAPES', 'CARBS', 'CARPS', 'CHADS', 'CHAIN', 'CHANT', 'CHINA', 'CHORD', 'CHUTE', 'CLASH', 'CLOGS',
             'CLOTH', 'CLOUD', 'CLUED', 'COBRA', 'COCOA', 'COMAS', 'COMET', 'CONGA', 'COOPS', 'COPES', 'COPSE', 'CORNY',
             'CORPS', 'COULD', 'COWER', 'CRABS', 'CRAFT', 'COUTH', 'CRAMS', 'CRAPS', 'CREAM', 'CREEP', 'CREMA', 'CREPE',
             'CREPT', 'CREWS', 'CRIBS', 'CRIME', 'CRISP', 'CROPS', 'CROWS', 'CRUSH', 'CULLS', 'CUTEY', 'CURRY', 'CYANS',
             'DEBAG', 'DECAY', 'DECOY', 'DEFOG', 'DEIFY', 'DELVE', 'DEPTH', 'DEVIL', 'DICEY', 'DINGY', 'DITCH', 'DIVED',
             'DODGY', 'DOPEY', 'DOUGH', 'DRANK', 'DRINK', 'DRYLY', 'DUFUS', 'DUKES', 'DUNCE', 'DUSKS', 'DUVET', 'DWELL',
             'DYING', 'EBONY', 'EMBER', 'ENEMY', 'EPICS', 'EVERY', 'FACES', 'FACET', 'FACTS', 'FANGS', 'FARCE', 'FARMS',
             'FECES', 'FEIGN', 'FEWER', 'FIBRE', 'FILTH', 'FIRMS', 'FLAGS', 'FLASH', 'FLESH', 'FLAYS', 'FLOGS', 'FLUID',
             'FLYER', 'FOAMS', 'FONDU', 'FOODY', 'FORCE', 'FORMS', 'FOUND', 'FRAME', 'FUNDS', 'FURRY', 'FUSSY', 'GABLE',
             'GALLY', 'GALOP', 'GAMED', 'GAPED', 'GAUDY', 'GEEKS', 'GHOUL', 'GIDDY', 'GINNY', 'GIVER', 'GIVES', 'GLAMS',
             'GLOBE', 'GLOBS', 'GLOOM', 'GLOOP', 'GLOWS', 'GLUEY', 'GNAWS', 'GNOME', 'GODLY', 'GOLEM', 'GOLFS', 'GOLLY',
             'GOWNS', 'GRAVE', 'GREEK', 'GROUP', 'GROVE', 'GROWL', 'GROWN', 'GRUBS', 'GULAG', 'HAKES', 'HANDY', 'HEAVE',
             'HELMS', 'HELPS', 'HENCE', 'HIGHS', 'HIKER', 'HIKES', 'HIVES', 'HILLY', 'HOCUS', 'HOLLY', 'HOMED', 'HOOKS',
             'HOPED', 'HOVER', 'HOWLS', 'ICILY', 'ICING', 'INKED', 'IVORY', 'KERRY', 'KILLS', 'KILNS', 'KINDS', 'KISSY',
             'KITTY', 'KNEAD', 'KNEEL', 'KNELT', 'KUDOS', 'LATCH', 'LAUGH', 'LEECH', 'LEAFY', 'LEFTY', 'LEVEL', 'LIKED',
             'LIKEN', 'LIMEY', 'LINKS', 'LIVED', 'LIVEN', 'LIVID', 'LOGIC', 'LOOPY', 'LOVED', 'LUBED', 'LUCID', 'LUPUS',
             'LURKS', 'LYCRA', 'LYRIC', 'MACES', 'MACRO', 'MAFIA', 'MAIMS', 'MAMAS', 'MANGA', 'MANGE', 'MANGO', 'MAYAN',
             'MEANY', 'MEMES', 'MEMOS', 'MEOWS', 'MICRO', 'MIMES', 'MINTY', 'MONEY', 'MONTH', 'MOODY', 'MOPES', 'MOUND',
             'MOUTH', 'MUSTY', 'NACHO', 'NAKED', 'NAVAL', 'NAVEL', 'NICHE', 'NIFTY', 'NOTCH', 'NUKES', 'OFFER', 'OPTIC',
             'OVARY', 'OWING', 'PACER', 'PACES', 'PACTS', 'PAGAN', 'PAGED', 'PANSY', 'PANTY', 'PAPER', 'PARMA', 'PAYED',
             'PEACE', 'PERPS', 'PHONE', 'PIECE', 'IPIER', 'PIPES', 'PIPET', 'PLAYS', 'POEMS', 'PONGS', 'POOFS', 'POOPS',
             'POPES', 'POUND', 'POWER', 'PRAMS', 'PRICE', 'PRIME', 'PREPS', 'PRISM', 'PROBE', 'PROMS', 'PROOF', 'PROPS',
             'PULLS', 'PURGE', 'RALPH', 'RAMPS', 'RANCH', 'REBUY', 'RECAP', 'REPLY', 'RISKY', 'ROWDY', 'RUNUP', 'SAGGY',
             'SAMBA', 'SAUCY', 'SCABS', 'SCAMS', 'SCARF', 'SCOOP', 'SCOPE', 'SCRAM', 'SCRAP', 'SCREW', 'SHAKE', 'SHARK',
             'SHAVE', 'SHAWL', 'SHELF', 'SHIVS', 'SHOOK', 'SHOVE', 'SHOWN', 'SHRUB', 'SKILL', 'SLINK', 'SLYLY', 'SMUSH',
             'SNOWY', 'SOGGY', 'SPACE', 'SPASM', 'SPECS', 'SPERM', 'SPEWS', 'SPICE', 'SPOOF', 'STAFF', 'STAMP', 'STIFF',
             'STOMP', 'STUNK', 'SUNUP', 'SWABS', 'SWAPS', 'SWARM', 'SWEEP', 'SWEPT', 'SWIFT', 'SWIMS', 'SWING', 'SWIPE',
             'SWOOP', 'SYNCS', 'SYRUP', 'TEMPO', 'TEMPT', 'THIGH', 'TOMBS', 'TOPIC', 'TOUCH', 'TRAMP', 'TRUNK', 'TWERP',
             'TWICE', 'TYPED', 'UNBAN', 'UNCLE', 'UNCUT', 'UNFED', 'UNPIN', 'VALID', 'VALUE', 'VAULT', 'VEGAS', 'VENUE',
             'VENUS', 'VERGE', 'VIGOR', 'VILLA', 'VINED', 'VIRGO', 'WAFTS', 'WAGED', 'WAGON', 'WARMS', 'WARPS', 'WASPS',
             'WEDGE', 'WEEPS', 'WELSH', 'WHALE', 'WHEEL', 'WHILE', 'WHINE', 'WHIRL', 'WHOLE', 'WIDTH', 'WINGS', 'WIPES',
             'WISPS', 'WOOFS', 'WOOLY', 'WOOPS', 'WORMS', 'WOULD', 'WOUND', 'WRAPS', 'WRING', 'WRONG', 'YAWNS', 'YELPS',
             'YIKES', 'YOKES', 'YOUNG', 'ABYSS', 'ACHES', 'ADLIB', 'ADMIN', 'AGAPE', 'AGING', 'AGONY', 'ALIKE', 'ALIVE',
             'ALLOW', 'AMITY', 'ANGRY', 'ASKED', 'AVAIL', 'AVIAN', 'AVOID', 'AWAYS', 'AWNED', 'BALDS', 'BALLS', 'BANDS',
             'BARGE', 'BARRY', 'BATHS', 'BATTY', 'BEGET', 'BEGOT', 'BELLS', 'BENDS', 'BERRY', 'BIDED', 'BIGOT', 'BILLS',
             'BINDS', 'BIRTH', 'BITTY', 'BLADE', 'BLEED', 'BLUER', 'BLUES', 'BLOOD', 'BLURS', 'BLURT', 'BOLDS', 'BONDS',
             'BONED', 'BONUS', 'BOOTH', 'BOOTY', 'BOSSY', 'BRAGS', 'BRAND', 'BRASH', 'BRAYS', 'BROTH', 'BRUNT', 'BUILT',
             'BURNS', 'BURNT', 'BYTES', 'CAGES', 'CALLS', 'CANAL', 'CANED', 'CANON', 'CARGO', 'CARRY', 'CATTY', 'CELLO',
             'CELLS', 'CHAIR', 'CHAOS', 'CHART', 'CHASE', 'CHATS', 'CHEAT', 'CHEER', 'CHESS', 'CHEST', 'CHOIR', 'CHORE',
             'CHOSE', 'CIGAR', 'CLANS', 'CLEAN', 'CLONE', 'CLOUT', 'CLUES', 'CODED', 'COLDS', 'COLON', 'CONDO', 'CORGI',
             'COUNT', 'CRASH', 'CRUDE', 'CRUEL', 'CRIER', 'CULTS', 'CURLS', 'CYSTS', 'DADDY', 'DAGGA', 'DANCE', 'DANDY',
             'DAWNS', 'DECAL', 'DEMON', 'DENIM', 'DESKS', 'DICED', 'DOLLY', 'DOMED', 'DORKS', 'DOUBT', 'DOVES', 'DOWNS',
             'DRAWN', 'DRIVE', 'DROVE', 'DROWN', 'DRUMS', 'DUCTS', 'EGGED', 'ELEGY', 'ELVES', 'ETHIC', 'EVADE', 'EVENS',
             'EVENT', 'EVILS', 'EYING', 'FADED', 'FAIRY', 'FAITH', 'FALLS', 'FATTY', 'FAULT', 'FAUNA', 'FELLA', 'FELLS',
             'FELON', 'FENDS', 'FERRY', 'FEUDS', 'FIELD', 'FIEND', 'FIERY', 'FILED', 'FILLS', 'FINAL', 'FINDS', 'FINED',
             'FLAIL', 'FLINT', 'FLOOD', 'FLOUR', 'FLUTE', 'FOLDS', 'FORGE', 'FORTH', 'FORTY', 'FOOTY', 'FORGO', 'FOYER',
             'FRAUD', 'FRESH', 'FRILL', 'FROGS', 'FROTH', 'FRYER', 'FUELS', 'FURLS', 'GAGED', 'GAMER', 'GAMES', 'GANGS',
             'GAPES', 'GASPS', 'GAUGE', 'GERMS', 'GIFTS', 'GIRLY', 'GISMO', 'GLAND', 'GLORY', 'GLUED', 'GLUON', 'GNASH',
             'GOING', 'GONGS', 'GOODY', 'GOOFS', 'GOUGE', 'GRABS', 'GRACE', 'GRAFT', 'GRAMS', 'GRAPE', 'GRASP', 'GRIEF',
             'GRIME', 'GRIPE', 'GRIPS', 'GROOM', 'GROPE', 'GROWS', 'GUILD', 'GULLS', 'GUTSY', 'GYRAL', 'HABIT', 'HANGS',
             'HARDY', 'HARPS', 'HEAPS', 'HEDGE', 'HENRY', 'HERBS', 'HINGE', 'HOBOS', 'HOMES', 'HOMIE', 'HONEY', 'HOODY',
             'HOOFS', 'HOOPS', 'HOPES', 'HORNY', 'HOTLY', 'HOUND', 'HULLS', 'HURRY', 'HYDRA', 'HYDRO', 'HYENA', 'IMAGE',
             'INPUT', 'KILTS', 'KITED', 'KNEES', 'KNITS', 'KNOTS', 'KOALA', 'LABEL', 'LACED', 'LAKES', 'LANCE', 'LAPEL',
             'LARKS', 'LARVA', 'LAWED', 'LAWNS', 'LEAKS', 'LEAVE', 'LEEKS', 'LEMON', 'LEMUR', 'LEVER', 'LIGHT', 'LIKES',
             'LILAC', 'LIVER', 'LIVES', 'LLAMA', 'LOCAL', 'LOLLY', 'LOOKS', 'LOVER', 'LOVES', 'LUNGE', 'LUNGS', 'MAGES',
             'MALLS', 'MARRY', 'MARSH', 'MATHS', 'MAYOR', 'MEATY', 'MEDAL', 'MELON', 'MENDS', 'MENUS', 'MERGE', 'MERRY',
             'MESSY', 'MINDS', 'MINED', 'MINUS', 'MISTY', 'MODEL', 'MOSEY', 'MOTHS', 'MOULT', 'MOUNT', 'MOURN', 'MUONS',
             'MURAL', 'MUSED', 'MUTED', 'NAIVE', 'NAMED', 'NANNY', 'NARKS', 'NEIGH', 'NERVE', 'NEVER', 'NIGHT', 'NINNY',
             'NOBLE', 'NOMAD', 'NOVAE', 'NUDGE', 'NYLON', 'OAKED', 'OAKEN', 'OBEYS', 'ODDLY', 'OINKS', 'OLIVE', 'OMEGA',
             'OUNCE', 'OVALS', 'OVENS', 'OWNED', 'PAGER', 'PAGES', 'PANDA', 'PANEL', 'PARRY', 'PARTY', 'PASTY', 'PATHS',
             'PATTY', 'PAYER', 'PAYEE', 'PEDAL', 'PENNE', 'PETTY', 'PHASE', 'PHOTO', 'PILED', 'PILLS', 'PINED', 'PLAIN',
             'PLANE', 'PLANS', 'PLANT', 'PLEAD', 'POGOS', 'POLED', 'POLLS', 'PONDS', 'POTTY', 'PRAYS', 'PREYS', 'PROUD',
             'PRUNE', 'PULSE', 'PUNTS', 'PYRES', 'RAKED', 'RANKS', 'RASPY', 'RAVED', 'RAVEN', 'REACH', 'REFRY', 'REHAB',
             'REPAY', 'REPEG', 'REVEL', 'RIVAL', 'ROACH', 'ROOMY', 'ROUGH', 'RUNIC', 'RUNNY', 'RUSKS', 'SALVE', 'SALVO',
             'SAVED', 'SCARY', 'SCOLD', 'SEVEN', 'SHAFT', 'SHAME', 'SHAMS', 'SHAPE', 'SHEEP', 'SHIFT', 'SHIPS', 'SHOPS',
             'SHOWS', 'SHREW', 'SHRUG', 'SHUSH', 'SILKS', 'SINKS', 'SKIDS', 'SKINS', 'SLEEK', 'SLUMS', 'SLUNG', 'SLURP',
             'SMALL', 'SMASH', 'SMELL', 'SMITH', 'SMOGS', 'SNAKE', 'SNARK', 'SNEAK', 'SOAPY', 'SOFTY', 'SOLVE', 'SPAYS',
             'SPELL', 'SPEND', 'SPILL', 'SPRAY', 'SPRIG', 'SPUDS', 'STALK', 'STANK', 'STINK', 'SUAVE', 'SUNNY', 'SWAYS',
             'SWELL', 'SWISH', 'SYNTH', 'TAKEN', 'TALKS', 'TANKS', 'TEACH', 'TECHS', 'THAWS', 'THEFT', 'THEME', 'THIEF',
             'THING', 'THONG', 'THREW', 'THROW', 'THROB', 'THUGS', 'TIPSY', 'TOKEN', 'TORCH', 'TOUGH', 'TULIP', 'TUNIC',
             'TUSKS', 'TWIGS', 'TYING', 'TYPES', 'TYPOS', 'ULCER', 'UNFIT', 'URBAN', 'USURP', 'VAILS', 'VALET', 'VALOR',
             'VENTS', 'VIALS', 'VIDEO', 'VINES', 'VIOLA', 'VIRAL', 'VIRUS', 'VITAL', 'VOIDS', 'VOLTS', 'VOTED', 'WADED',
             'WAGER', 'WAGES', 'WALLS', 'WANDS', 'WANED', 'WEARY', 'WELDS', 'WELLS', 'WHATS', 'WHEAT', 'WHERE', 'WHIRR',
             'WHITE', 'WHORE', 'WHOSE', 'WIELD', 'WILDS', 'WILLS', 'WINDS', 'WITTY', 'WOOSH', 'WORLD', 'WORRY', 'WORTH',
             'WRATH', 'YOUTH', 'ABIDE', 'ABLER', 'ABLES', 'ABODE', 'ABOUT', 'ABUSE', 'ACIDS', 'ACORN', 'ACTED', 'ACUTE',
             'ADAPT', 'ADEPT', 'ADMIT', 'ADOPT', 'AGGRO', 'AHOLD', 'AIMED', 'ALARM', 'ALIBI', 'ALIGN', 'ALLEY', 'ALLOY',
             'ALOFT', 'ALONG', 'ALOOF', 'AMENS', 'AMUSE', 'ANGEL', 'ANGLE', 'ANIME', 'ANNOY', 'ANNUL', 'ANTIC', 'APRON',
             'ARMED', 'ASKER', 'AUNTY', 'AVAST', 'AVERT', 'AWARD', 'BAILS', 'BALES', 'BANES', 'BARDS', 'BARON', 'BASED',
             'BASIL', 'BASIN', 'BATED', 'BATON', 'BEADS', 'BEANS', 'BEARD', 'BELTS', 'BIDES', 'BIRDS', 'BISON', 'BLARE',
             'BLAST', 'BLEAT', 'BLESS', 'BLISS', 'BLOAT', 'BLOTS', 'BOARD', 'BOILS', 'BOLTS', 'BONES', 'BOOED', 'BOONS',
             'BORED', 'BORNE', 'BOSON', 'BOUTS', 'BRAID', 'BRAIL', 'BRAIN', 'BREAD', 'BREED', 'BRIDE', 'BROAD', 'BROOD',
             'BRUTE', 'BURST', 'BUSTS', 'BUTTS', 'CADET', 'CAINS', 'CANES', 'CANOE', 'CARDS', 'CARED', 'CAROL', 'CAUSE',
             'CEDAR', 'CENTS', 'CIDER', 'CITED', 'CLASS', 'CLEAR', 'CLEAT', 'CLOTS', 'COALS', 'COILS', 'COINS', 'COLTS',
             'CONES', 'COOED', 'COOLS', 'CORAL', 'COURT', 'CRANE', 'CREED', 'CRIED', 'CRUST', 'CURES', 'CURIO', 'CURSE',
             'CUTER', 'DAILY', 'DAMES', 'DEBTS', 'DECOR', 'DEEMS', 'DEEPS', 'DEFER', 'DELAY', 'DEMOS', 'DEPOT', 'DICER',
             'DICES', 'DIMES', 'DINGS', 'DISCO', 'DISCS', 'DODGE', 'DOING', 'DOMES', 'DONGA', 'DOOMS', 'DORMS', 'DRABS',
             'DRAFT', 'DRAMA', 'DRAPE', 'DRAWS', 'DREAM', 'DRIFT', 'DRIPS', 'DROOP', 'DROPS', 'DRUGS', 'DULLS', 'DUSTY',
             'EDGED', 'EIGHT', 'ELECT', 'ELOPE', 'EMAIL', 'ENACT', 'ERUPT', 'FADES', 'FAILS', 'FAINT', 'FALSE', 'FARED',
             'FATAL', 'FATED', 'FEEDS', 'FEELS', 'FELTS', 'FERAL', 'FERNS', 'FETAL', 'FETUS', 'FILES', 'FILER', 'FINES',
             'FIRED', 'FLAIR', 'FLARE', 'FLATS', 'FLEAS', 'FLEES', 'FLEET', 'FLIER', 'FLIES', 'FLIRT', 'FLOAT', 'FLOOR',
             'FLORA', 'FLOSS', 'FOALS', 'FOILS', 'FOLIO', 'FONTS', 'FOODS', 'FOOLS', 'FOURS', 'FRAIL', 'FREED', 'FRIED',
             'FRONT', 'FRUIT', 'FUSES', 'GAGES', 'GAUNT', 'GHAST', 'GHOST', 'GILLS', 'GLADE', 'GLEAN', 'GLIDE', 'GLINT',
             'GLUES', 'GNARL', 'GOLDS', 'GOOEY', 'GORGE', 'GOTHS', 'GOURD', 'GRAND', 'GREYS', 'GRILL', 'GRIND', 'GRUNT',
             'GUARD', 'GUIDE', 'GUILT', 'HAIRY', 'HALLS', 'HANDS', 'HARSH', 'HASTY', 'HAULS', 'HAUNT', 'HEATH', 'HELLO',
             'HELLS', 'HILLS', 'HOLDS', 'HONED', 'HOTTY', 'HULAS', 'HUNTS', 'HURLS', 'ICONS', 'IDIOM', 'INEPT', 'INFER',
             'KARAT', 'KITES', 'LACES', 'LAPSE', 'LAYED', 'LEAPS', 'LEDGE', 'LEFTS', 'LEGAL', 'LEPER', 'LIFTS', 'LIMES',
             'LIMIT', 'LINGO', 'LISPS', 'LOBES', 'LODGE', 'LOFTS', 'LOGIN', 'LOOMS', 'LOONY', 'LOOPS', 'LOUSY', 'LOWER',
             'LOYAL', 'MAIDS', 'MAILS', 'MAINS', 'MALTS', 'MANES', 'MANOR', 'MATED', 'MASON', 'MEALS', 'MEANS', 'MELTS',
             'MESON', 'METAL', 'MEDIA', 'MIDST', 'MILES', 'MINER', 'MINES', 'MINOR', 'MINTS', 'MOANS', 'MODES', 'MOLAR',
             'MOLES', 'MOODS', 'MOOED', 'MOONS', 'MORAL', 'MORON', 'MOTEL', 'MOUSE', 'MUTES', 'NAMES', 'NEEDY', 'NERDY',
             'NEWER', 'NICER', 'NIECE', 'NINTH', 'NORMS', 'NUTTY', 'OCEAN', 'OFTEN', 'OMENS', 'OPENS', 'OPTED', 'OVERT',
             'OWNER', 'PANTS', 'PAINS', 'PAINT', 'PALER', 'PALES', 'PANES', 'PAROL', 'PAUSE', 'PEARL', 'PEELS', 'PELTS',
             'PENIS', 'PERIL', 'PETAL', 'PIANO', 'PILOT', 'PINES', 'PINTS', 'PLATE', 'PLEAS', 'PLIER', 'PLOTS', 'POINT',
             'POLAR', 'POLES', 'POLIO', 'POOLS', 'POSED', 'POURS', 'POUTS', 'PRIDE', 'PRIED', 'PRINT', 'PRODS', 'PRONE',
             'PUREE', 'PURER', 'PURRS', 'PURSE', 'PUTTS', 'RABID', 'RACED', 'RAKES', 'RAMEN', 'RAPED', 'RAPID', 'RAVES',
             'REALM', 'REBEL', 'RECON', 'REEKS', 'REFED', 'RENEW', 'REPEL', 'RIFLE', 'RIGHT', 'RIPEN', 'RISKS', 'RIVER',
             'RIVET', 'ROBED', 'ROBIN', 'ROMAN', 'ROPED', 'ROVER', 'ROWED', 'RUNGS', 'SADLY', 'SALLY', 'SANDY', 'SAUCE',
             'SAVER', 'SAVES', 'SAWED', 'SCALE', 'SCANS', 'SCENE', 'SCENT', 'SCONE', 'SCORN', 'SCOUR', 'SCOUT', 'SEEKS',
             'SERUM', 'SERVE', 'SETUP', 'SEVER', 'SEWED', 'SHAGS', 'SHALL', 'SHELL', 'SHUNT', 'SHYER', 'SIEVE', 'SIGHS',
             'SIGHT', 'SILLY', 'SINCE', 'SINEW', 'SIRUP', 'SITUP', 'SKATE', 'SKEET', 'SKIES', 'SKITS', 'SLABS', 'SLAMS',
             'SLAPS', 'SLEEP', 'SLEPT', 'SLIME', 'SLING', 'SLIPS', 'SLOBS', 'SLOOP', 'SLOPE', 'SLOWS', 'SLUGS', 'SMELT',
             'SMILE', 'SNAPS', 'SNIPE', 'SNIPS', 'SNOBS', 'SNOOP', 'SNOWS', 'SOAKS', 'SONIC', 'SOUPS', 'SPADE', 'SPANS',
             'SPEED', 'SPELT', 'SPENT', 'SPIED', 'SPINE', 'SPLAT', 'SPLIT', 'SPOIL', 'SPOON', 'SPOUT', 'SPURT', 'STAVE',
             'STEAK', 'STOKE', 'STORK', 'STOVE', 'STUBS', 'STUDY', 'STUNG', 'SUPER', 'SURFS', 'SWANS', 'SWINE', 'SWORD',
             'SWORN', 'TABLE', 'TAKER', 'TAKES', 'TALLY', 'TAMED', 'TAPED', 'TEDDY', 'TELLY', 'TEPID', 'THUDS', 'TIGHT',
             'TIMED', 'TIMID', 'TONIC', 'TOWED', 'TOWEL', 'TOWNS', 'TROVE', 'TRUCE', 'TRULY', 'TUBAS', 'TUBES', 'TUMOR',
             'TURBO', 'TURFS', 'TWEED', 'TWINE', 'TWINS', 'TWIRL', 'UNDID', 'UNDUE', 'UNITY', 'UPSET', 'URGED', 'USING',
             'VEERS', 'VERSE', 'VESTS', 'VISAS', 'VISIT', 'VISOR', 'VOTER', 'VOTES', 'WADES', 'WANES', 'WARDS', 'WARNS',
             'WEANS', 'WEEDS', 'WEIRD', 'WIDER', 'WINES', 'WIRED', 'WOODS', 'WOOED', 'WOOLS', 'WORDS', 'YELLS', 'YIELD',
             'YODEL', 'YOYOS', 'ABORT', 'ACRES', 'ACTOR', 'ADDED', 'ADULT', 'AFIRE', 'AFOOT', 'AFORE', 'AFTER', 'AGAIN',
             'AGENT', 'AGILE', 'AHEAD', 'ALGAE', 'ALOUD', 'AMASS', 'AMISS', 'ANGER', 'ANGST', 'APART', 'ARBOR', 'ARGON',
             'AROMA', 'ARROW', 'ASHED', 'ATOMS', 'ATTIC', 'AWAIT', 'AWARE', 'BAITS', 'BASES', 'BASIS', 'BATES', 'BEARS',
             'BEAST', 'BEATS', 'BEERS', 'BEETS', 'BERET', 'BESTS', 'BETAS', 'BITER', 'BOAST', 'BOATS', 'BOOST', 'BOOTS',
             'BORES', 'BRASS', 'BRATS', 'CARER', 'CARTS', 'CASES', 'CASTS', 'CATER', 'CEASE', 'CITES', 'COAST', 'COATS',
             'CORES', 'COSTS', 'CRATE', 'CREST', 'CRIER', 'CRIES', 'CRITS', 'CROSS', 'DAIRY', 'DAISY', 'DAUNT', 'DEARY',
             'DEATH', 'DEITY', 'DIARY', 'DIGIT', 'DIRTY', 'DOLLS', 'DONUT', 'DOTTY', 'DRAGS', 'DRILL', 'DRUID', 'DRYER',
             'DUALS', 'DUDES', 'DUELS', 'DUNES', 'EAGLE', 'EARLY', 'EDGES', 'ELUDE', 'EMITS', 'EMOTE', 'ENDED', 'ENTRY',
             'ERECT', 'FAIRS', 'FARES', 'FARTS', 'FASTS', 'FATES', 'FEARS', 'FEAST', 'FEATS', 'FESTS', 'FIRES', 'FIRST',
             'FISTS', 'FORTE', 'FORTS', 'FREER', 'FREES', 'FRETS', 'FRIAR', 'FRIES', 'FROST', 'GAINS', 'GATED', 'GENES',
             'GENIE', 'GENRE', 'GENTS', 'GEODE', 'GEOID', 'GIANT', 'GIRLS', 'GLARE', 'GLASS', 'GLOAT', 'GLOSS', 'GOALS',
             'GOODS', 'GOONS', 'GRADE', 'GRAIL', 'GRAIN', 'GRANT', 'GREED', 'GREEN', 'GRIDS', 'GRINS', 'GROAN', 'GROIN',
             'GROUT', 'GUESS', 'GUEST', 'HAILS', 'HALOS', 'HALTS', 'HATED', 'HEADS', 'HEALS', 'HEARD', 'HEEDS', 'HEELS',
             'HERDS', 'HERON', 'HIDES', 'HINTS', 'HIRED', 'HOARD', 'HOLES', 'HONES', 'HOODS', 'HORDE', 'HORNS', 'HOSED',
             'HOTEL', 'HOURS', 'HOUSE', 'HURTS', 'IDLED', 'IGLOO', 'INGOT', 'IRONY', 'ITEMS', 'LADEN', 'LADLE', 'LAGER',
             'LANDS', 'LARGE', 'LAYER', 'LEASH', 'LEGIT', 'LENDS', 'LIEGE', 'LOGOS', 'LOLLS', 'LORRY', 'LUNAR', 'LURED',
             'LYRES', 'MARES', 'MASTS', 'MATES', 'MEATS', 'MEETS', 'MERIT', 'METER', 'METRE', 'METRO', 'MISER', 'MISTS',
             'MITES', 'MOATS', 'MOIST', 'MOOSE', 'MORSE', 'MOTOR', 'MOTTO', 'NASTY', 'NOISY', 'NORTH', 'NOUNS', 'NUDES',
             'OBESE', 'OBOES', 'OCTET', 'OMITS', 'OPERA', 'ORBIT', 'ORGAN', 'OSCAR', 'PAIRS', 'PARIS', 'PARSE', 'PARTS',
             'PASTA', 'PASTE', 'PASTS', 'PATIO', 'PEARS', 'PEERS', 'PESTO', 'PESTS', 'PIERS', 'POETS', 'POISE', 'PORTS',
             'POSER', 'POSES', 'PRESS', 'PRIES', 'PRIOR', 'RACER', 'RACES', 'RAFTS', 'RAGED', 'RANGE', 'RAPES', 'RASPS',
             'REACT', 'READY', 'REAPS', 'REARM', 'REDRY', 'REDYE', 'REEFS', 'REFER', 'REFIT', 'REFIT', 'REGAL', 'REIGN',
             'RELAY', 'RHINO', 'RICES', 'RIDGE', 'RIFTS', 'RIGID', 'RINGS', 'RIPER', 'ROAMS', 'ROBOT', 'ROGUE', 'ROMEO',
             'ROOFS', 'ROOMS', 'ROPES', 'ROUGE', 'ROUND', 'ROWER', 'ROYAL', 'SABRE', 'SAFER', 'SALTY', 'SCARE', 'SCARS',
             'SCOOT', 'SCORE', 'SEAMS', 'SEEDY', 'SEEMS', 'SEEPS', 'SEGUE', 'SEPIA', 'SEWER', 'SHADE', 'SHARD', 'SHEDS',
             'SHEEN', 'SHINE', 'SHINS', 'SHOAL', 'SHOED', 'SHONE', 'SHOUT', 'SHRED', 'SIFTS', 'SIGIL', 'SIGNS', 'SINGE',
             'SINGS', 'SLASH', 'SLAYS', 'SLOSH', 'SLOTH', 'SLYER', 'SMART', 'SMEAR', 'SMITE', 'SMOTE', 'SNAGS', 'SOAPS',
             'SOBER', 'SOFAS', 'SONGS', 'SOUND', 'SOUTH', 'SPARE', 'SPARS', 'SPATS', 'SPEAR', 'SPIRE', 'SPITE', 'SPITS',
             'SPORE', 'SPORT', 'SPOTS', 'SPREE', 'STABS', 'STEAM', 'STEEP', 'STEMS', 'STEPS', 'STEWS', 'STING', 'STOIC',
             'STOOP', 'STOPS', 'STORM', 'STOWS', 'STRAP', 'STRAW', 'STRIP', 'STYLE', 'SUGAR', 'SURGE', 'SUSHI', 'SWATS',
             'SWEAR', 'SWEAT', 'SWEET', 'SWISS', 'SWORE', 'TABOO', 'TACOS', 'TAMER', 'TAMES', 'TANGO', 'TAPER', 'TAPES',
             'TAPIR', 'TARDY', 'TARPS', 'TEAMS', 'TENTH', 'TERMS', 'THINS', 'THIRD', 'TIBIA', 'TIMER', 'TIMES', 'TINGE',
             'TODAY', 'TOMES', 'TONGA', 'TONGS', 'TOTEM', 'TOWER', 'TOYED', 'TRACE', 'TRAMS', 'TRAPS', 'TRIBE', 'TRIMS',
             'TRIPE', 'TRIPS', 'TROOP', 'TROPE', 'TRUTH', 'TUNED', 'TWEET', 'TWIST', 'UDDER', 'UNDER', 'UNION', 'UNLIT',
             'UNTIL', 'URGES', 'USAGE', 'USHER', 'USUAL', 'WAIST', 'WAITS', 'WARTS', 'WARES', 'WASTE', 'WATER', 'WATTS',
             'WEARS', 'WIRES', 'WISER', 'WORSE', 'WORST', 'WRIST', 'WRITE', 'WROTE', 'YARDS', 'YEARN', 'YOURS', 'ADORN',
             'ADDER', 'AEGIS', 'AGATE', 'AGREE', 'AIDED', 'AILED', 'ALIEN', 'ALINE', 'ALLOT', 'ALONE', 'ALURE', 'ARRAY',
             'ARTSY', 'ASHES', 'AUDIO', 'AUDIT', 'AUNTS', 'AURAL', 'DARED', 'DATED', 'DEALS', 'DEALT', 'DEANS', 'DEEDS',
             'DELTA', 'DENSE', 'DENTS', 'DIALS', 'DIANA', 'DINER', 'DINES', 'DOLES', 'DONOR', 'DOSED', 'DOTED', 'DOUSE',
             'DRAIN', 'DREAD', 'DRIED', 'DROID', 'DRONE', 'DROOL', 'DUETS', 'DUSTS', 'EAGER', 'EARTH', 'ELDER', 'ENROL',
             'ENSUE', 'GEARS', 'ESSAY', 'ETHER', 'ETHOS', 'ETUDE', 'GATES', 'GEESE', 'GOATS', 'GOERS', 'GOOSE', 'GRASS',
             'GRATE', 'GREAT', 'GREET', 'GRITS', 'GROSS', 'HAIRS', 'HARES', 'HASTE', 'HATER', 'HATES', 'HEARS', 'HEART',
             'HEATS', 'HEIRS', 'HEIST', 'HEROS', 'HIRES', 'HOIST', 'HOOTS', 'HORSE', 'HOSES', 'HOSTS', 'IDEAL', 'IDLES',
             'IDOLS', 'INDIE', 'INLET', 'INNER', 'INTEL', 'LANES', 'LEADS', 'LEANS', 'LEANT', 'LEARN', 'LENSE', 'LINER',
             'LINES', 'LIONS', 'LOADS', 'LONES', 'LOINS', 'LONER', 'LOONS', 'LORDS', 'LOTUS', 'LOUSE', 'LURES', 'LUSTS',
             'LUTES', 'NAILS', 'NASAL', 'NATAL', 'NEEDS', 'NERDS', 'NINES', 'NODES', 'NOONS', 'NOSED', 'NOTED', 'NURSE',
             'OATHS', 'ODOUR', 'OGRES', 'OILED', 'OLDER', 'ONION', 'OTHER', 'OUTDO', 'OUTED', 'RAGES', 'REDID', 'RENAL',
             'RERUN', 'RESAY', 'RETAG', 'RETRY', 'RILED', 'ROGER', 'ROLLS', 'RONDO', 'RUDER', 'RUINS', 'RULER', 'RULES',
             'RUNES', 'RUNTS', 'RURAL', 'SAGES', 'SALAD', 'SALON', 'SANDS', 'SARGE', 'SASSY', 'SATYR', 'SAUNA', 'SAYER',
             'SEDAN', 'SELLS', 'SENDS', 'SHARE', 'SHEAR', 'SHEER', 'SHEET', 'SHIRT', 'SHITS', 'SHOES', 'SHOOT', 'SHORE',
             'SHORT', 'SHOTS', 'SIDED', 'SIEGE', 'SINUS', 'SISSY', 'SLAIN', 'SLANT', 'SLEDS', 'SLIDE', 'SLURS', 'SNAIL',
             'SNARL', 'SNIDE', 'SNOUT', 'SOLID', 'SOOTY', 'SORRY', 'SOULS', 'STAGE', 'STAGS', 'STALL', 'STAND', 'STASH',
             'STAYS', 'STILL', 'STORY', 'STRAY', 'STUDS', 'STUNS', 'STUNT', 'SUEDE', 'TALON', 'TASTY', 'TAUNT', 'TEARY',
             'TEETH', 'TELLS', 'TENDS', 'THEIR', 'THERE', 'THESE', 'THOSE', 'THREE', 'TIDAL', 'TIGER', 'TILDE', 'TITTY',
             'TOGAS', 'TOLLS', 'TONED', 'TONNE', 'TOOTH', 'TRASH', 'TRAYS', 'TREND', 'TRILL', 'TROLL', 'TUNAS', 'TUNER',
             'TUNES', 'TYRES', 'ULTRA', 'UNITE', 'UNITS', 'UNSET', 'UNTIE', 'URINE', 'YEARS', 'YEAST', 'AIRED', 'ALERT',
             'ALIAS', 'ALTAR', 'ALTER', 'ALTOS', 'ARENA', 'ARSON', 'ASIDE', 'ATLAS', 'ATONE', 'AURAS', 'DARES', 'DARTS',
             'DATES', 'DEARS', 'DEERS', 'DETER', 'DIETS', 'DIRER', 'DIRTS', 'DOERS', 'DOORS', 'DOSES', 'DOTES', 'DREAR',
             'DRESS', 'DRIER', 'DRIES', 'EARED', 'EARNS', 'EATEN', 'EDITS', 'ELITE', 'ENTER', 'EUROS', 'IDEAS', 'IDIOT',
             'INERT', 'INSET', 'IRONS', 'INTRO', 'ISLES', 'ISSUE', 'LAIRS', 'LASER', 'LASSO', 'LASTS', 'LATER', 'LATTE',
             'LEASE', 'LEAST', 'LEERS', 'LIARS', 'LISTS', 'LITRE', 'LOOSE', 'LOOTS', 'LOSER', 'LOSES', 'NEARS', 'NESTS',
             'NITRO', 'NOISE', 'NOOSE', 'NOSES', 'NOTES', 'ONSET', 'ORALS', 'ORDER', 'OUTER', 'OUTRO', 'RADAR', 'RADIO',
             'RAIDS', 'RAILS', 'RAINS', 'RANTS', 'RATED', 'REEDS', 'REELS', 'REINS', 'RELIT', 'RENTS', 'RERAN', 'RESIN',
             'REUSE', 'RIDER', 'RIDES', 'RINSE', 'RISEN', 'ROADS', 'RODEO', 'ROLES', 'ROUTE', 'RUSTS', 'SAILS', 'SAINT',
             'SALES', 'SALSA', 'SALTS', 'SATED', 'SATIN', 'SAUTE', 'SEALS', 'SEEDS', 'SENSE', 'SIDES', 'SILOS', 'SIREN',
             'SLATE', 'SLATS', 'SLEET', 'SLITS', 'SLOTS', 'SNARE', 'SNEER', 'SNOOT', 'SNORE', 'SNORT', 'SOILS', 'SOLAR',
             'SOLES', 'SOLOS', 'SONAR', 'SOURS', 'STAIN', 'STALE', 'STEAD', 'STEAL', 'STEED', 'STEEL', 'STERN', 'STINT',
             'STOLE', 'STONE', 'STOOD', 'STOOL', 'STOUT', 'SUITE', 'SUITS', 'SURER', 'TAILS', 'TAINT', 'TALES', 'TEENS',
             'TENOR', 'TENSE', 'TENTS', 'TESLA', 'TIDES', 'TILES', 'TILTS', 'TINTS', 'TIRED', 'TITAN', 'TITLE', 'TOADS',
             'TOILS', 'TONER', 'TONES', 'TOOLS', 'TOONS', 'TOTAL', 'TOURS', 'TRADE', 'TRAIL', 'TRAIN', 'TRANS', 'TREAD',
             'TRIAD', 'TRIAL', 'TRIED', 'TROUT', 'TRUER', 'TRUST', 'TUTOR', 'USERS', 'UTTER', 'AREAS', 'ARISE', 'AROSE',
             'ARSES', 'ASSES', 'ASSET', 'EASES', 'EATER', 'EERIE', 'ERASE', 'IRATE', 'OASIS', 'OTTER', 'RAISE', 'RARER',
             'RARES', 'RATES', 'RATIO', 'REARS', 'RESAT', 'RESET', 'RESIT', 'RESTS', 'RETRO', 'RIOTS', 'RISER', 'RISES',
             'RITES', 'ROARS', 'ROAST', 'ROOST', 'ROOTS', 'ROSES', 'ROTOR', 'SATED', 'SEARS', 'SEATS', 'SITAR', 'SITES',
             'SOARS', 'SORES', 'SORTS', 'STAIR', 'STARE', 'STARS', 'START', 'STATE', 'STATS', 'STEER', 'STIRS', 'STORE',
             'TARTS', 'TASTE', 'TEARS', 'TEASE', 'TESTS', 'TIERS', 'TIRES', 'TIARA', 'TOAST', 'TOOTS', 'TORSO', 'TRAIT',
             'TREAT', 'TREES', 'TRIES', 'TROTS')

    def __init__(self):
        self.new_puzzle()


    def input(self, letter: str):
        if letter.lower() in self.INPUT_KEYS and self._column_at < 5 and not self.check_correct():
            self._inputs[self._row_at][self._column_at] = letter.upper()
            self._column_at += 1
            return 1
        else:
            return 0

    def backspace(self):
        if self._column_at > 0 and not self.check_correct():
            self._column_at -= 1
            self._inputs[self._row_at][self._column_at] = ''
            return 1
        else:
            return 0

    def confirm_input(self):
        if self._column_at == 5 and not self.check_correct():
            for index, value in enumerate(self._inputs[self._row_at]):
                if value == self._answer[index]:
                    self._check[self._row_at][index] = self.CORRECT
                else:
                    self._check[self._row_at][index] = self.TOTALLY_WRONG
            for index, value in enumerate(self._inputs[self._row_at]):
                if self._check[self._row_at][index] != self.CORRECT:
                    for i, val in enumerate(self._inputs[self._row_at]):
                        if self._check[self._row_at][i] != self.CORRECT and self._inputs[self._row_at][index] == self._answer[i]:
                            self._check[self._row_at][index] = self.WRONG_PLACE
                            break
            self._column_at = 0
            self._row_at = self._row_at + 1
            return 1
        else:
            return 0

    def check_correct(self):
        for i in range(self.ROWS):
            all_true = True
            for j in range(self.COLUMNS):
                if self._check[i][j] != self.CORRECT:
                    all_true = False
            if all_true:
                return True
        return False

    def next_line(self):
        self._row_at += 1
        self._column_at = 0

    def get_checked(self, i, j):
        return self._check[i][j]

    def get_inputs(self):
        return self._inputs

    def get_row_at(self):
        return self._row_at

    def get_answer(self):
        return self._answer

    def get_valid_word(self):
        return ''.join(self._inputs[self._row_at]) in self.WORDS

    def new_puzzle(self):
        self._answer = choice(self.WORDS)
        self._row_at = 0
        self._column_at = 0
        self._check = [[self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY]]
        self._inputs = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''],
                        ['', '', '', '', ''], ['', '', '', '', '']]

    def __str__(self):
        return f"{self._inputs[self._row_at][0]} [{self._check[self._row_at][0]}], {self._inputs[self._row_at][1]} [{self._check[self._row_at][1]}], " \
               f"{self._inputs[self._row_at][2]} [{self._check[self._row_at][2]}], {self._inputs[self._row_at][3]} [{self._check[self._row_at][3]}], " \
               f"{self._inputs[self._row_at][4]} [{self._check[self._row_at][4]}], "

