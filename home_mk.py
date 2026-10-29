# Textos de marketing de la portada (es, en, fr, de)

def block(t, lg):
    shots = lambda a, b, alt1, alt2: (f'<div class="shots"><img src="img/{a}-{lg}.jpg" alt="{alt1}" loading="lazy" width="270" height="436">'
                                      f'<img src="img/{b}-{lg}.jpg" alt="{alt2}" loading="lazy" width="270" height="436"></div>')
    feats = lambda items: '<div class="feats">' + ''.join(f'<div class="feat"><span class="fi">{i}</span><div><strong>{h}</strong><br>{d}</div></div>' for i, h, d in items) + '</div>'
    chips = lambda items: '<div class="chips">' + ''.join(f'<span>{c}</span>' for c in items) + '</div>'
    return f'''<section class="hero">
<h1>{t['h1']}</h1>
<p class="lead">{t['lead']}</p>
<div class="cta"><a class="btn r" href="#rondalia-{lg}">{t['b1']}</a><a class="btn l" href="#lexpedition-{lg}">{t['b2']}</a></div>
</section>

<section class="appsec" id="rondalia-{lg}">
<div class="apphead"><img src="img/rondalia.png" alt="" width="72" height="72"><div><h2>Rondalia</h2><p class="kicker">{t['r_k']}</p></div></div>
<p>{t['r_p']}</p>
{feats(t['r_f'])}
{shots('ron-inicio', 'ron-abecedario', t['r_a1'], t['r_a2'])}
<h3>{t['r_gh']}</h3>
{chips(t['r_g'])}
<p class="note">{t['r_n']}</p>
</section>

<section class="appsec" id="lexpedition-{lg}">
<div class="apphead"><img src="img/lexpedition.png" alt="" width="72" height="72"><div><h2>Lexpedition</h2><p class="kicker">{t['l_k']}</p></div></div>
<p>{t['l_p']}</p>
{chips(t['l_langs'])}
{feats(t['l_f'])}
{shots('lex-carta', 'lex-progreso', t['l_a1'], t['l_a2'])}
<p class="note">{t['l_n']}</p>
</section>

<section class="promise">
<h2>{t['c_h']}</h2>
<ul>{''.join(f'<li>{x}</li>' for x in t['c'])}</ul>
<p>{t['mail']} <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a></p>
</section>'''


T = {}
T['es'] = dict(
 h1='Apps para aprender y jugar en familia',
 lead='Somos MJCStudio, un pequeño estudio independiente de Sevilla. Hacemos apps cuidadas, sin anuncios y sin recoger datos, para pasar buenos ratos juntos y aprender sin darse cuenta.',
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Momentos de calidad que caben en un móvil',
 r_p='Cualquier rato es bueno para jugar juntos: la sobremesa, un viaje en coche, la espera en un restaurante, una tarde de lluvia o una reunión con amigos. Saca el móvil y empieza la partida. Un solo móvil que se va pasando, sin internet, sin cuentas y sin que nadie tenga que leer instrucciones: abuelos, padres y peques juegan juntos, cada uno a su nivel.',
 r_f=[('👨‍👩‍👧‍👦', 'Cada uno a su nivel', 'Cuatro grupos de edad (5–7, 8–11, 12–15 y 16+). En la misma partida, el peque recibe su pregunta y el abuelo la suya.'),
      ('🎲', '11 juegos en una app', 'Desde preguntas y mímica hasta el abecedario, banderas o palabra prohibida. Siempre hay uno que apetece.'),
      ('📚', 'Miles de preguntas', 'Más de 2.000 preguntas por idioma, cientos de palabras y mímicas, y todo el contenido revisado para que sea apto para niños.'),
      ('🧒', 'También para jugar solo', 'Preguntas, Abecedario, Cálculo, Banderas y Adivina el número sirven para practicar y aprender con un solo jugador.'),
      ('🏆', 'Marcador y turnos', 'La app lleva los puntos, los turnos y el tiempo, para que vosotros solo os preocupéis de reír.'),
      ('🎃', 'Sorpresas de temporada', 'Set de Halloween gratis: preguntas, palabras y mímicas, y un estilo visual con calderos de bruja, murciélagos y telarañas.')],
 r_a1='Pantalla de inicio de Rondalia', r_a2='Juego del Abecedario en Rondalia',
 r_gh='Los juegos',
 r_g=['❓ Preguntas', '🤐 Palabra prohibida', '🔤 Abecedario', '🎭 Mímica', '🚩 Banderas', '➗ Cálculo', '🔢 Adivina el número', '🤷 El despistado', '⚖️ ¿Qué prefieres?', '💬 Conocernos', '📖 Historia encadenada'],
 r_n='En español, inglés, francés y alemán, con preguntas adaptadas a cada país. Gratis para empezar; una única compra desbloquea todo, sin suscripciones.',
 l_k='Rumbo fijo: aprobar tu examen',
 l_p='Lexpedition convierte la preparación de tu examen oficial de idiomas en una travesía por el mar, y el puerto de destino es el aprobado. Cada lección es una isla que conquistar y cada expresión que dominas es una milla menos hasta la meta. Con cinco o diez minutos al día llegarás al examen con el vocabulario que más se resiste.',
 l_langs=['🇬🇧 Inglés', '🇩🇪 Alemán', '🇫🇷 Francés', '🇪🇸 Español', 'Niveles A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Cuatro idiomas para estudiar', 'Prepara inglés, alemán, francés o español, del nivel A1 al C2 del Marco Común Europeo. Puedes estudiar varios a la vez.'),
      ('🧩', 'Lo que más cuesta', 'Verbos con partícula o preposición (phrasal verbs, trennbare Verben…), expresiones idiomáticas y colocaciones, con frases de ejemplo reales.'),
      ('🗺️', 'Una carta de navegación', 'Elige tu rumbo entre islas misteriosas, despeja la niebla y planta tu bandera. Asciende de Grumete a Almirante.'),
      ('🧠', 'Repaso inteligente', 'Tarjetas, elegir la partícula, completar huecos y unir parejas, con repetición espaciada para que no se olvide lo aprendido.'),
      ('🔥', 'Motivación diaria', 'Test diario con nota, racha, meta de XP, misiones e insignias. Ideal para crear el hábito.'),
      ('🗣️', 'En tu idioma', 'La app habla español, inglés, francés o alemán, y los significados pueden salir traducidos a tu idioma o como definición.')],
 l_a1='Carta de navegación de Lexpedition', l_a2='Progreso, rango y récords en Lexpedition',
 l_n='Para cualquier edad: desde niños que preparan su primer certificado hasta adultos. Varios perfiles en el mismo móvil. Gratis en todos los niveles: el Test diario y las 3 primeras islas de cada nivel; cada idioma completo se desbloquea con una compra única.',
 c_h='Nuestro compromiso',
 c=['Sin anuncios, nunca.', 'Sin cuentas ni registro.', 'No recogemos datos personales: todo se guarda en tu móvil.', 'Aptas para menores: compras y enlaces protegidos con una pregunta para adultos.', 'Compra única opcional, sin suscripciones.'],
 mail='¿Dudas o ideas? Escríbenos a')
T['en'] = dict(
 h1='Apps to learn and play together',
 lead="We are MJCStudio, a small independent studio from Seville, Spain. We make carefully crafted apps with no ads and no data collection, for great times together and learning without noticing.",
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Quality time that fits in one phone',
 r_p="Any moment is a good moment to play together: after a meal, on a car trip, waiting at a restaurant, on a rainy afternoon or with friends. Bring out your phone and start playing. One phone passed around, no internet, no accounts and no rules to read: grandparents, parents and kids play together, each at their own level.",
 r_f=[('👨‍👩‍👧‍👦', 'Everyone at their level', 'Four age groups (5–7, 8–11, 12–15 and 16+). In the same game, the little one gets their question and grandpa gets his.'),
      ('🎲', '11 games in one app', 'From quiz and charades to the alphabet wheel, flags or forbidden words. There is always one you feel like playing.'),
      ('📚', 'Thousands of questions', 'Over 2,000 questions per language, hundreds of words and charades, all checked to be child-friendly.'),
      ('🧒', 'Solo play too', 'Quiz, Alphabet Wheel, Mental Math, Flags and Guess the Number are great for practising and learning on your own.'),
      ('🏆', 'Scores and turns', 'The app keeps the score, turns and time, so all you have to do is laugh.'),
      ('🎃', 'Seasonal surprises', 'A free Halloween set: questions, words and charades, plus a visual style with witch cauldrons, bats and cobwebs.')],
 r_a1='Rondalia home screen', r_a2='Alphabet Wheel in Rondalia',
 r_gh='The games',
 r_g=['❓ Quiz', '🤐 Forbidden Words', '🔤 Alphabet Wheel', '🎭 Charades', '🚩 Flags', '➗ Mental Math', '🔢 Guess the Number', '🤷 The Clueless One', '⚖️ Would You Rather?', '💬 Get to Know You', '📖 Story Chain'],
 r_n='In English, Spanish, French and German, with questions adapted to each country. Free to start; a single purchase unlocks everything, no subscriptions.',
 l_k='Set your course for passing your exam',
 l_p='Lexpedition turns preparing for your official language exam into a voyage across the sea, and the destination port is a pass. Each lesson is an island to conquer and every expression you master is one mile closer to the goal. With five or ten minutes a day you will reach exam day with the vocabulary that resists the most.',
 l_langs=['🇬🇧 English', '🇩🇪 German', '🇫🇷 French', '🇪🇸 Spanish', 'Levels A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Four languages to study', 'Prepare English, German, French or Spanish, from A1 to C2 of the Common European Framework. You can study several at once.'),
      ('🧩', 'The hard stuff', 'Phrasal verbs, verbs with prepositions (trennbare Verben…), idioms and collocations, with real example sentences.'),
      ('🗺️', 'A sea chart', 'Choose your course among mystery islands, clear the fog and plant your flag. Rise from Deckhand to Admiral.'),
      ('🧠', 'Smart review', 'Flashcards, pick the particle, fill the gaps and match pairs, with spaced repetition so you don\'t forget.'),
      ('🔥', 'Daily motivation', 'Daily test with a score, streaks, XP goal, missions and badges. Perfect to build the habit.'),
      ('🗣️', 'In your language', 'The app speaks English, Spanish, French or German, and meanings can be shown as translations or definitions.')],
 l_a1='Lexpedition sea chart', l_a2='Progress, rank and records in Lexpedition',
 l_n='For every age: from children preparing their first certificate to adults. Several profiles on the same device. Free at every level: the Daily test and the first 3 islands of each level; each full language is unlocked with a one-time purchase.',
 c_h='Our promise',
 c=['No ads, ever.', 'No accounts or sign-up.', "We don't collect personal data: everything stays on your device.", 'Child-friendly: purchases and links are protected by a question for adults.', 'Optional one-time purchase, no subscriptions.'],
 mail='Questions or ideas? Write to')
T['fr'] = dict(
 h1='Des applis pour apprendre et jouer en famille',
 lead="Nous sommes MJCStudio, un petit studio indépendant de Séville. Nous créons des applis soignées, sans publicité et sans collecte de données, pour passer de bons moments ensemble et apprendre sans s'en rendre compte.",
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Des moments de qualité qui tiennent dans un téléphone',
 r_p="Tous les moments sont bons pour jouer ensemble : après le repas, en voiture, en attendant au restaurant, un après-midi de pluie ou entre amis. Sors ton téléphone et la partie commence. Un seul téléphone qui passe de main en main, sans internet, sans compte et sans règles à lire : grands-parents, parents et enfants jouent ensemble, chacun à son niveau.",
 r_f=[('👨‍👩‍👧‍👦', 'Chacun à son niveau', 'Quatre tranches d\'âge (5–7, 8–11, 12–15 et 16+). Dans la même partie, le petit a sa question et le grand-père la sienne.'),
      ('🎲', '11 jeux dans une appli', 'Du quiz et du mime à la roue de l\'alphabet, aux drapeaux ou aux mots interdits. Il y en a toujours un qui fait envie.'),
      ('📚', 'Des milliers de questions', 'Plus de 2 000 questions par langue, des centaines de mots et de mimes, tout vérifié pour convenir aux enfants.'),
      ('🧒', 'Aussi pour jouer seul', 'Quiz, Roue de l\'alphabet, Calcul mental, Drapeaux et Devine le nombre permettent de s\'entraîner et d\'apprendre en solo.'),
      ('🏆', 'Score et tours', 'L\'appli compte les points, les tours et le temps : vous n\'avez plus qu\'à rire.'),
      ('🎃', 'Surprises de saison', 'Un pack Halloween gratuit : questions, mots et mimes, et un style visuel avec chaudrons de sorcière, chauves-souris et toiles d\'araignée.')],
 r_a1="Écran d'accueil de Rondalia", r_a2="Roue de l'alphabet dans Rondalia",
 r_gh='Les jeux',
 r_g=['❓ Quiz', '🤐 Mots interdits', "🔤 Roue de l'alphabet", '🎭 Mime', '🚩 Drapeaux', '➗ Calcul mental', '🔢 Devine le nombre', '🤷 Le Distrait', '⚖️ Tu préfères ?', '💬 Faisons connaissance', '📖 Histoire à la chaîne'],
 r_n="En français, espagnol, anglais et allemand, avec des questions adaptées à chaque pays. Gratuit pour commencer ; un achat unique débloque tout, sans abonnement.",
 l_k='Cap sur la réussite de ton examen',
 l_p="Lexpedition transforme la préparation de ton examen officiel de langue en une traversée en mer, et le port d'arrivée, c'est la réussite. Chaque leçon est une île à conquérir et chaque expression maîtrisée est un mille de moins vers le but. Avec cinq ou dix minutes par jour, tu arriveras à l'examen avec le vocabulaire qui résiste le plus.",
 l_langs=['🇬🇧 Anglais', '🇩🇪 Allemand', '🇫🇷 Français', '🇪🇸 Espagnol', 'Niveaux A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Quatre langues à étudier', 'Prépare l\'anglais, l\'allemand, le français ou l\'espagnol, du niveau A1 au C2 du Cadre européen commun. Tu peux en étudier plusieurs.'),
      ('🧩', 'Ce qui coûte le plus', 'Verbes à particule ou à préposition (phrasal verbs, trennbare Verben…), expressions idiomatiques et collocations, avec de vraies phrases d\'exemple.'),
      ('🗺️', 'Une carte marine', 'Choisis ton cap parmi des îles mystérieuses, dissipe le brouillard et plante ton drapeau. Grimpe de Mousse à Amiral.'),
      ('🧠', 'Révision intelligente', 'Cartes, choix de la particule, textes à trous et paires, avec répétition espacée pour ne pas oublier.'),
      ('🔥', 'Motivation quotidienne', 'Test du jour noté, série, objectif d\'XP, missions et badges. Idéal pour prendre l\'habitude.'),
      ('🗣️', 'Dans ta langue', 'L\'appli parle français, espagnol, anglais ou allemand, et les sens s\'affichent en traduction ou en définition.')],
 l_a1='Carte marine de Lexpedition', l_a2='Progrès, grade et records dans Lexpedition',
 l_n="Pour tous les âges : des enfants qui préparent leur premier diplôme aux adultes. Plusieurs profils sur le même appareil. Gratuit à chaque niveau : le Test du jour et les 3 premières îles de chaque niveau ; chaque langue complète se débloque par un achat unique.",
 c_h='Notre engagement',
 c=['Pas de publicité, jamais.', 'Pas de compte ni d\'inscription.', 'Aucune donnée personnelle collectée : tout reste sur ton appareil.', 'Adapté aux enfants : achats et liens protégés par une question pour adultes.', 'Achat unique facultatif, sans abonnement.'],
 mail='Une question, une idée ? Écris-nous à')
T['de'] = dict(
 h1='Apps zum Lernen und gemeinsamen Spielen',
 lead='Wir sind MJCStudio, ein kleines unabhängiges Studio aus Sevilla. Wir machen liebevoll gestaltete Apps ohne Werbung und ohne Datensammlung – für schöne Stunden miteinander und Lernen ganz nebenbei.',
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Wertvolle gemeinsame Momente, die in ein Handy passen',
 r_p='Jeder Moment ist gut, um gemeinsam zu spielen: nach dem Essen, auf der Autofahrt, beim Warten im Restaurant, an einem Regennachmittag oder mit Freunden. Handy raus – und los geht\'s. Ein Handy, das herumgereicht wird, ohne Internet, ohne Konto und ohne Anleitung lesen: Großeltern, Eltern und Kinder spielen zusammen, jeder auf seinem Niveau.',
 r_f=[('👨‍👩‍👧‍👦', 'Jeder auf seinem Niveau', 'Vier Altersgruppen (5–7, 8–11, 12–15 und 16+). Im selben Spiel bekommt das Kind seine Frage und der Opa seine.'),
      ('🎲', '11 Spiele in einer App', 'Von Quiz und Pantomime bis Buchstabenrad, Flaggen oder verbotene Wörter. Irgendeins passt immer.'),
      ('📚', 'Tausende Fragen', 'Über 2.000 Fragen pro Sprache, Hunderte Wörter und Pantomimen – alles kindgerecht geprüft.'),
      ('🧒', 'Auch allein spielbar', 'Quiz, Buchstabenrad, Kopfrechnen, Flaggen und Zahlenraten eignen sich zum Üben und Lernen mit nur einem Spieler.'),
      ('🏆', 'Punkte und Runden', 'Die App zählt Punkte, Runden und Zeit – ihr müsst nur noch lachen.'),
      ('🎃', 'Saison-Überraschungen', 'Ein kostenloses Halloween-Paket: Fragen, Wörter und Pantomimen, dazu ein Stil mit Hexenkesseln, Fledermäusen und Spinnweben.')],
 r_a1='Startbildschirm von Rondalia', r_a2='Buchstabenrad in Rondalia',
 r_gh='Die Spiele',
 r_g=['❓ Quiz', '🤐 Verbotene Wörter', '🔤 Buchstabenrad', '🎭 Pantomime', '🚩 Flaggen', '➗ Kopfrechnen', '🔢 Zahlenraten', '🤷 Der Ahnungslose', '⚖️ Was wäre dir lieber?', '💬 Kennenlernen', '📖 Kettengeschichte'],
 r_n='Auf Deutsch, Spanisch, Englisch und Französisch, mit Fragen für jedes Land. Kostenlos starten; ein einziger Kauf schaltet alles frei, ohne Abo.',
 l_k='Kurs auf deine bestandene Prüfung',
 l_p='Lexpedition macht aus der Vorbereitung auf deine offizielle Sprachprüfung eine Reise übers Meer – und der Zielhafen ist das Bestehen. Jede Lektion ist eine Insel, die du eroberst, und jeder Ausdruck, den du beherrschst, ist eine Seemeile näher am Ziel. Mit fünf bis zehn Minuten am Tag gehst du mit genau dem Wortschatz in die Prüfung, der am schwersten fällt.',
 l_langs=['🇬🇧 Englisch', '🇩🇪 Deutsch', '🇫🇷 Französisch', '🇪🇸 Spanisch', 'Niveaus A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Vier Sprachen zum Lernen', 'Bereite dich auf Englisch, Deutsch, Französisch oder Spanisch vor, von A1 bis C2 des Gemeinsamen Europäischen Referenzrahmens. Auch mehrere gleichzeitig.'),
      ('🧩', 'Das, was am schwersten fällt', 'Partikelverben und Verben mit Präposition (phrasal verbs, trennbare Verben…), Redewendungen und Kollokationen, mit echten Beispielsätzen.'),
      ('🗺️', 'Eine Seekarte', 'Wähle deinen Kurs zwischen geheimnisvollen Inseln, vertreibe den Nebel und hisse deine Flagge. Steige vom Schiffsjungen zum Admiral auf.'),
      ('🧠', 'Kluges Wiederholen', 'Karteikarten, Partikel wählen, Lücken füllen und Paare bilden – mit verteilter Wiederholung, damit nichts vergessen wird.'),
      ('🔥', 'Tägliche Motivation', 'Tagestest mit Note, Serie, XP-Ziel, Missionen und Abzeichen. Ideal, um dranzubleiben.'),
      ('🗣️', 'In deiner Sprache', 'Die App spricht Deutsch, Spanisch, Englisch oder Französisch, und Bedeutungen erscheinen als Übersetzung oder Definition.')],
 l_a1='Seekarte in Lexpedition', l_a2='Fortschritt, Rang und Rekorde in Lexpedition',
 l_n='Für jedes Alter: von Kindern vor ihrem ersten Zertifikat bis zu Erwachsenen. Mehrere Profile auf einem Gerät. Kostenlos auf jedem Niveau: der Tagestest und die ersten 3 Inseln jedes Niveaus; jede Sprache wird mit einem Einmalkauf komplett freigeschaltet.',
 c_h='Unser Versprechen',
 c=['Keine Werbung, niemals.', 'Kein Konto, keine Anmeldung.', 'Wir sammeln keine personenbezogenen Daten: Alles bleibt auf deinem Gerät.', 'Kindgerecht: Käufe und Links sind durch eine Frage für Erwachsene geschützt.', 'Optionaler Einmalkauf, kein Abo.'],
 mail='Fragen oder Ideen? Schreib uns an')

home = {l: block(T[l], l) for l in T}
