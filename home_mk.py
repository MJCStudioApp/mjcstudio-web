# Textos de marketing de la portada (es, en, fr, de)

# Logo de Rondalia (sin fondo, con la rota en el centro): sustituye al emoji 🎡 de la nota del nombre
ROTA = '<svg class="rota-ico" viewBox="0 0 512 512" width="22" height="22" aria-hidden="true" focusable="false"><circle cx="256" cy="106" r="52" fill="#3B63F5"/><circle cx="385.9" cy="181" r="52" fill="#0FA595"/><circle cx="385.9" cy="331" r="52" fill="#F2A516"/><circle cx="256" cy="406" r="52" fill="#F2692E"/><circle cx="126.1" cy="331" r="52" fill="#F0437E"/><circle cx="126.1" cy="181" r="52" fill="#7351F0"/><circle cx="256" cy="256" r="74" fill="#EFE6D2"/><circle cx="256" cy="256" r="63.6" fill="none" stroke="#A4471F" stroke-width="9.2"/><circle cx="256" cy="256" r="50.3" fill="none" stroke="#A4471F" stroke-width="3.3"/><g stroke="#A4471F" stroke-width="6.6" stroke-linecap="round"><line x1="315.2" y1="256" x2="196.8" y2="256"/><line x1="297.9" y1="297.9" x2="214.1" y2="214.1"/><line x1="256" y1="315.2" x2="256" y2="196.8"/><line x1="214.1" y1="297.9" x2="297.9" y2="214.1"/></g><circle cx="256" cy="256" r="14.8" fill="#EFE6D2" stroke="#A4471F" stroke-width="7.9"/></svg>'

def block(t, lg):
    shots = lambda *p: '<div class="shots">' + ''.join(f'<img src="img/{a}-{lg}.jpg" alt="{alt}" loading="lazy" width="270" height="436">' for a, alt in p) + '</div>'
    feats = lambda items: '<div class="feats">' + ''.join(f'<div class="feat"><span class="fi">{i}</span><div><strong>{h}</strong><br>{d}</div></div>' for i, h, d in items) + '</div>'
    def beta(app, mail, cls):
        b = BETA[lg]
        return (f'<div class="beta"><h3>🧪 {b["h"]}</h3><p>{b["p"].format(mail=f'<a href="mailto:{mail}">{mail}</a>')}</p>'
                f'<div class="cta"><a class="btn {cls}" href="https://play.google.com/store/apps/details?id=com.mjcstudio.{app}" rel="noopener">{b["and"]}</a>'
                f'<a class="btn ghost" href="https://play.google.com/apps/testing/com.mjcstudio.{app}" rel="noopener">{b["web"]}</a></div>'
                f'<p class="small">{b["n"]}</p></div>')
    def store(aid, cls):
        b = STORE[lg]
        cc = {'es': 'es', 'en': 'us', 'fr': 'fr', 'de': 'de', 'pt': 'pt'}[lg]
        return (f'<div class="store"><h3>📱 {b["h"]}</h3><p>{b["p"]}</p>'
                f'<div class="cta"><a class="btn {cls}" href="https://apps.apple.com/{cc}/app/id{aid}" rel="noopener">{b["b"]}</a></div></div>')
    chips = lambda items: '<div class="chips">' + ''.join(f'<span>{c}</span>' for c in items) + '</div>'
    return f'''<section class="hero">
<h1>{t['h1']}</h1>
<p class="lead">{t['lead']}</p>
<div class="cta"><a class="btn r" href="#rondalia-{lg}">{t['b1']}</a><a class="btn l" href="#lexpedition-{lg}">{t['b2']}</a></div>
</section>

<section class="appsec" id="rondalia-{lg}">
<div class="apphead"><img src="img/rondalia.png" alt="" width="72" height="72"><div><h2>Rondalia</h2><p class="kicker">{t['r_k']}</p></div></div>
<p>{t['r_p']}</p>
<h3 class="modes-h">{t['r_mh']}</h3>
<div class="modes">{feats(t['r_m'])}</div>
{feats(t['r_f'])}
{shots(('ron-inicio', t['r_a1']), ('ron-verdad', t['r_a3']), ('ron-abecedario', t['r_a2']))}
<h3>{t['r_gh']}</h3>
{chips(t['r_g'])}
<p class="note">{t['r_n']}</p>
<p class="note">{ROTA} {ORIGIN[lg]}</p>
<p class="note">{FOLLOW[lg]['r']} <a href="https://x.com/Rondalia" rel="noopener">𝕏 @Rondalia</a> · <a href="https://www.instagram.com/rondalia.app/" rel="noopener">📷 rondalia.app</a></p>
{store('6829351479', 'r')}
{beta('rondalia', 'rondalia@mjcstudio.com', 'r')}
</section>

<section class="appsec" id="lexpedition-{lg}">
<div class="apphead"><img src="img/lexpedition.png" alt="" width="72" height="72"><div><h2>Lexpedition</h2><p class="kicker">{t['l_k']}</p></div></div>
<p>{t['l_p']}</p>
{chips(t['l_langs'])}
{feats(t['l_f'])}
{shots(('lex-usuarios', t['l_a3']), ('lex-carta', t['l_a1']), ('lex-progreso', t['l_a2']))}
<p class="note">{t['l_n']}</p>
{store('6829351766', 'l')}
{beta('lexpedition', 'lexpedition@mjcstudio.com', 'l')}
</section>

<section class="promise">
<h2>{t['c_h']}</h2>
<ul>{''.join(f'<li>{x}</li>' for x in t['c'])}</ul>
<p>{t['mail']} <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a></p>
<p>{FOLLOW[lg]['p']} <a href="https://x.com/MJCStudioApp" rel="noopener">𝕏 @MJCStudioApp</a> · <a href="https://www.instagram.com/mjcstudio.app/" rel="noopener">📷 mjcstudio.app</a> · <a href="https://x.com/Rondalia" rel="noopener">𝕏 @Rondalia</a> · <a href="https://www.instagram.com/rondalia.app/" rel="noopener">📷 rondalia.app</a></p>
</section>

<section class="idea">
<h2>💡 {IDEA[lg]['h']}</h2>
<p>{IDEA[lg]['p']}</p>
<div class="cta"><a class="btn ghost" href="mailto:soporte@mjcstudio.com?subject={IDEA[lg]['s']}">{IDEA[lg]['b']}</a></div>
</section>'''


ORIGIN = {
 'es': '<strong>¿Por qué «Rondalia»?</strong> Viene de «ronda»: jugar por turnos, en corro. Y la «o» del logo es una <em>rota</em>, una rueda de juego que los antiguos romanos grababan en las escaleras de foros y templos para jugar en grupo. Casi dos mil años después, la idea sigue siendo la misma: un tablero, varios jugadores y cada uno en su turno.',
 'en': '<strong>Why “Rondalia”?</strong> It comes from the Spanish “ronda”, a round: playing in turns, sitting in a circle. And the “o” in the logo is a <em>rota</em>, a game wheel the ancient Romans carved into the steps of forums and temples to play together. Nearly two thousand years later, the idea is the same: one board, several players, everyone taking turns.',
 'fr': '<strong>Pourquoi « Rondalia » ?</strong> Le nom vient de l’espagnol « ronda », la ronde : jouer chacun son tour, en cercle. Et le « o » du logo est une <em>rota</em>, une roue de jeu que les Romains gravaient sur les marches des forums et des temples pour jouer ensemble. Près de deux mille ans plus tard, l’idée reste la même : un plateau, plusieurs joueurs, chacun son tour.',
 'de': '<strong>Warum „Rondalia“?</strong> Der Name kommt vom spanischen „ronda“, der Runde: reihum spielen, im Kreis. Und das „o“ im Logo ist eine <em>Rota</em>, ein Spielrad, das die alten Römer in die Stufen von Foren und Tempeln ritzten, um gemeinsam zu spielen. Fast zweitausend Jahre später ist die Idee dieselbe: ein Spielbrett, mehrere Spieler, alle reihum.',
 'pt': '<strong>Porquê «Rondalia»?</strong> Vem de «ronda», a roda: jogar à vez, em círculo. E o «o» do logótipo é uma <em>rota</em>, uma roda de jogo que os antigos romanos gravavam nos degraus dos fóruns e templos para jogar em conjunto. Quase dois mil anos depois, a ideia é a mesma: um tabuleiro, vários jogadores e cada um na sua vez.',
}

FOLLOW = {
 'es': dict(p='Síguenos en X e Instagram para conocer las novedades:', r='Novedades, juegos nuevos y sets de temporada en'),
 'en': dict(p='Follow us on X and Instagram for news:', r='News, new games and seasonal sets on'),
 'fr': dict(p='Suis-nous sur X et Instagram pour les nouveautés :', r='Nouveautés, nouveaux jeux et sets de saison sur'),
 'de': dict(p='Folge uns auf X und Instagram für Neuigkeiten:', r='Neuigkeiten, neue Spiele und Saison-Sets auf'),
 'pt': dict(p='Segue-nos no X e no Instagram para saberes as novidades:', r='Novidades, jogos novos e coleções da época em'),
}

IDEA = {
 'es': dict(h='Sugiere una app', p='¿Echas en falta alguna app para aprender o jugar? Cuéntanos tu idea: leemos todas las propuestas.', b='Enviar mi idea', s='Idea%20para%20una%20app'),
 'en': dict(h='Suggest an app', p='Is there an app for learning or playing that you wish existed? Tell us your idea: we read every suggestion.', b='Send my idea', s='App%20idea'),
 'fr': dict(h='Propose une appli', p="Il te manque une appli pour apprendre ou jouer ? Raconte-nous ton idée : nous lisons toutes les propositions.", b='Envoyer mon idée', s='Id%C3%A9e%20d%27appli'),
 'de': dict(h='App vorschlagen', p='Fehlt dir eine App zum Lernen oder Spielen? Erzähl uns deine Idee – wir lesen jeden Vorschlag.', b='Idee senden', s='App-Idee'),
 'pt': dict(h='Sugere uma app', p='Falta-te alguma app para aprender ou jogar? Conta-nos a tua ideia: lemos todas as sugestões.', b='Enviar a minha ideia', s='Ideia%20para%20uma%20app'),
}

STORE = {
 'es': dict(h='Descárgala en iPhone y iPad', p='Ya está en la App Store: gratis y completa, sin anuncios.', b='Descargar en la App Store'),
 'en': dict(h='Get it on iPhone and iPad', p='Now on the App Store: free and complete, with no ads.', b='Download on the App Store'),
 'fr': dict(h='Télécharge-la sur iPhone et iPad', p="Disponible sur l'App Store : gratuite et complète, sans pub.", b="Télécharger sur l'App Store"),
 'de': dict(h='Lade sie auf iPhone und iPad', p='Jetzt im App Store: kostenlos und komplett, ohne Werbung.', b='Im App Store laden'),
 'pt': dict(h='Descarrega-a no iPhone e iPad', p='Já está na App Store: grátis e completa, sem anúncios.', b='Descarregar na App Store'),
}

BETA = {
 'es': dict(h='Prueba la beta en Android', p='Estamos en prueba cerrada en Google Play. 1) Escríbenos a {mail} con el Gmail que usas en tu móvil Android y te añadimos. 2) Únete con uno de estos enlaces y descárgala.', **{'and': 'Unirse desde el móvil Android', 'web': 'Unirse desde la web'}, n='Solo para móviles Android con Google Play. Usa la misma cuenta de Gmail que nos diste.'),
 'en': dict(h='Try the beta on Android', p="We're in a closed test on Google Play. 1) Email {mail} with the Gmail you use on your Android phone and we'll add you. 2) Join with one of these links and download it.", **{'and': 'Join on your Android phone', 'web': 'Join on the web'}, n='Android phones with Google Play only. Use the same Gmail account you gave us.'),
 'fr': dict(h='Teste la bêta sur Android', p="Nous sommes en test fermé sur Google Play. 1) Écris-nous à {mail} avec le Gmail de ton téléphone Android et nous t'ajoutons. 2) Rejoins le test avec l'un de ces liens et télécharge l'appli.", **{'and': 'Rejoindre sur Android', 'web': 'Rejoindre sur le web'}, n='Uniquement pour les téléphones Android avec Google Play. Utilise le même compte Gmail.'),
 'de': dict(h='Teste die Beta auf Android', p='Wir sind im geschlossenen Test bei Google Play. 1) Schreib uns an {mail} mit dem Gmail-Konto deines Android-Handys, dann fügen wir dich hinzu. 2) Tritt über einen dieser Links bei und lade die App herunter.', **{'and': 'Auf dem Android-Handy beitreten', 'web': 'Im Web beitreten'}, n='Nur für Android-Handys mit Google Play. Verwende dasselbe Gmail-Konto.'),
 'pt': dict(h='Experimenta a beta no Android', p='Estamos em teste fechado no Google Play. 1) Escreve-nos para {mail} com o Gmail que usas no teu telemóvel Android e adicionamos-te. 2) Junta-te com uma destas ligações e descarrega a app.', **{'and': 'Juntar-me no telemóvel Android', 'web': 'Juntar-me na web'}, n='Só para telemóveis Android com Google Play. Usa a mesma conta Gmail que nos deste.'),
}

T = {}
T['es'] = dict(
 h1='Apps para aprender y jugar',
 lead='Somos MJCStudio, un pequeño estudio independiente de desarrollo de software y aplicaciones, con sede en España. Todo empezó como un hobby en casa, en familia. Hacemos apps cuidadas, sin anuncios y sin recoger datos, para pasar buenos ratos juntos y aprender sin darse cuenta.',
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Momentos de calidad que caben en un móvil',
 r_p='Cualquier rato es bueno para jugar juntos: la sobremesa, un viaje en coche, la espera en un restaurante, una tarde de lluvia o una reunión con amigos. Saca el móvil y empieza la partida, en familia, con amigos o tú solo. Un solo móvil que se va pasando, o una tableta en el centro de la mesa, sin internet, sin cuentas y sin que nadie tenga que leer instrucciones: abuelos, padres y peques juegan juntos, cada uno a su nivel.',
 r_f=[('👨‍👩‍👧‍👦', 'Cada uno a su nivel', 'Cuatro niveles de dificultad, del 1 al 4. En la misma partida, el peque recibe su pregunta y el abuelo la suya.'),
      ('🎲', 'Más de 15 juegos, un solo marcador', 'Desde preguntas y mímica hasta el abecedario, banderas o palabra prohibida. Cambiad de juego cuando queráis o dejad que «La rueda elige» decida en cada turno: el marcador suma los puntos de todos. ¿No sabéis a qué jugar? «Ayúdame a elegir» os propone juegos con tres preguntas rápidas.'),
      ('🎡', 'La rueda elige', '¿Sin ganas de decidir? Gira la rueda y toca un juego distinto en cada turno, por rondas. Tú eliges cuáles entran, y la rueda suena como una ruleta.'),
      ('🤝', 'Nuevo: todos juntos', '¿Con niños pequeños o sin ganas de competir? Elegid «Todos juntos»: un solo equipo, sin nombres, con el nivel que queráis. Responded entre todos y superad el reto: 20 aciertos antes de 5 fallos.'),
      ('👥', 'Todos los que seáis', 'Guarda hasta 50 jugadores y jugad todos a la vez, sin límite por juego. En las partidas grandes, El despistado tiene varios despistados que se descubren ronda a ronda.'),
      ('✈️', 'Sin internet', 'En el coche, en el avión, en la playa o en el pueblo sin cobertura: Rondalia no necesita conexión ni gasta datos. Todo va dentro de la app.'),
      ('📺', 'También en la tele', 'Duplica la pantalla del móvil o la tableta en la tele y jugad todos viéndola en grande.'),
      ('⚔️', 'Duelo para dos', '¿Sois dos? En Palabrea, Cálculo, Adivina el número y Llega al número jugáis a la vez con la pantalla dividida, cada uno con el reto de su nivel. Gana quien sume más puntos.'),
      ('📚', 'Más de 6.000 retos', 'Más de 2.000 preguntas por idioma, cientos de palabras, mímicas y categorías, y todo el contenido revisado para que sea apto para niños. En Ajustes ves cuánto contenido tiene cada juego.'),
      ('🧒', 'También para jugar solo', 'Preguntas, Abecedario, Letra al vuelo, Palabrea, Adivina la palabra, Cálculo, Banderas, Adivina el número y Llega al número sirven para practicar y aprender con un solo jugador. Con el reto de partida y tu récord de aciertos seguidos, siempre hay algo que superar.'),
      ('🏆', 'Marcador y turnos', 'La app lleva los puntos, los turnos y el tiempo, para que vosotros solo os preocupéis de pasarlo bien, en familia o con amigos.'),
      ('💬', 'Para conoceros mejor', 'No todo es competir: ¿Qué prefieres?, Conocernos e Historia encadenada abren conversaciones para descubrir gustos, recuerdos y anécdotas de los demás.'),
      ('🌱', 'Siempre creciendo', 'Rondalia se actualiza con frecuencia: juegos nuevos, más preguntas y sets gratis para las fechas especiales del año, con su propio estilo visual. La app te avisa de cada versión nueva y te cuenta sus novedades, y desde ella puedes sugerirnos juegos.')],
 r_a1='Pantalla de inicio de Rondalia', r_a2='Juego del Abecedario en Rondalia',
 r_gh='Los juegos',
 r_g=['❓ Preguntas', '🤐 Palabra prohibida', '🔤 Abecedario', '🎭 Mímica', '🚩 Banderas', '➗ Cálculo', '🔢 Adivina el número', '🎯 Llega al número', '⚡ Letra al vuelo', '🔠 Palabrea', '🎈 Adivina la palabra', '🤔 ¿Qué elegiría?', '🤷 El despistado', '⚖️ ¿Qué prefieres?', '💬 Conocernos', '📖 Historia encadenada', '🔐 Descifra el código'],
 r_n='En español, inglés, francés, alemán y portugués, con preguntas adaptadas a cada país. Edición de lanzamiento: ahora gratis y completa, sin compras. Descárgala ahora y tenla completa para siempre.',
 l_k='Rumbo fijo: aprobar tu examen',
 l_p='Lexpedition convierte la preparación de tu examen oficial de idiomas en una travesía por el mar, y el puerto de destino es el aprobado. Cada lección es una isla que conquistar y cada expresión que dominas es una milla menos hasta la meta. Con cinco o diez minutos al día llegarás al examen con el vocabulario que más se resiste.',
 l_langs=['🇬🇧 Inglés', '🇩🇪 Alemán', '🇫🇷 Francés', '🇪🇸 Español', 'Niveles A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Cuatro idiomas para estudiar', 'Prepara inglés, alemán, francés o español, del nivel A1 al C2 del Marco Común Europeo (inglés, desde A2). Puedes estudiar varios a la vez.'),
      ('🧩', 'Lo que más cuesta', 'Verbos con partícula o preposición (phrasal verbs, trennbare Verben…), expresiones idiomáticas y colocaciones, con frases de ejemplo reales.'),
      ('🗺️', 'Una carta de navegación', 'Elige tu rumbo entre islas misteriosas, despeja la niebla y planta tu bandera. Asciende de Grumete a Almirante.'),
      ('🧠', 'Repaso inteligente', 'Tarjetas, elegir la partícula, completar huecos y unir parejas, con repetición espaciada para que no se olvide lo aprendido.'),
      ('🌱', 'Motivación diaria', 'Test diario con nota, racha, meta de XP, misiones e insignias. Ideal para crear el hábito.'),
      ('✈️', 'Sin conexión', 'En el metro, en el avión o donde no haya cobertura: Lexpedition funciona sin internet y sin gastar datos. Todo el vocabulario va dentro de la app.'),
      ('🗣️', 'En tu idioma', 'La app habla español, inglés, francés o alemán, y los significados pueden salir traducidos a tu idioma o como definición.')],
 l_a1='Carta de navegación de Lexpedition', l_a2='Progreso, rango y récords en Lexpedition',
 l_n='Para cualquier edad: desde niños que preparan su primer certificado hasta adultos. Funciona en móvil y tableta, con varios perfiles en el mismo dispositivo. Edición de lanzamiento: ahora gratis y completa, con los cuatro idiomas y todos los niveles. Descárgala ahora y tenla completa para siempre.',
 c_h='Características',
 c=['Sin anuncios.', 'Sin cuentas ni registro.', 'Funcionan sin conexión: sin datos móviles ni cobertura.', 'Para móvil y tableta: Android, iPhone y iPad.', 'No recogemos datos personales: todo se guarda en tu dispositivo.', 'Aptas para menores: compras y enlaces protegidos con una pregunta para adultos.', 'Compra única opcional, sin suscripciones.'],
 mail='¿Dudas o ideas? Escríbenos a')
T['en'] = dict(
 h1='Apps to learn and play',
 lead="We are MJCStudio, a small independent software and app development studio based in Spain. It all started as a hobby at home, as a family. We make carefully crafted apps with no ads and no data collection, for great times together and learning without noticing.",
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Quality time that fits in one phone',
 r_p="Any moment is a good moment to play together: after a meal, on a car trip, waiting at a restaurant, on a rainy afternoon or with friends. Bring out your phone and start playing, with family, with friends or on your own. One phone passed around, or a tablet in the middle of the table, no internet, no accounts and no rules to read: grandparents, parents and kids play together, each at their own level.",
 r_f=[('👨‍👩‍👧‍👦', 'Everyone at their level', 'Four difficulty levels, from 1 to 4. In the same game, the little one gets their question and grandpa gets his.'),
      ('🎲', 'More than 15 games, one scoreboard', 'From quiz and charades to the alphabet wheel, flags or forbidden words. Switch games whenever you like or let “Spin the wheel” decide each turn: the scoreboard adds up the points from all of them. Not sure what to play? “Help me choose” asks three quick questions and suggests games.'),
      ('🎡', 'The wheel picks', 'Tired of deciding? Spin the wheel and get a different game every turn, in rounds. You choose which games go in, and the wheel clicks like a roulette.'),
      ('🤝', 'New: all together', 'Playing with young kids, or just not in the mood to compete? Choose “All together”: one team, no names, at the level you pick. Answer together and beat the challenge: 20 correct answers before 5 misses.'),
      ('👥', 'Everyone can play', 'Save up to 50 players and play all together, with no limit per game. In big games, The Clueless One has several clueless ones, found round by round.'),
      ('✈️', 'No internet needed', 'In the car, on a plane, at the beach or anywhere without signal: Rondalia needs no connection and uses no data. Everything is built into the app.'),
      ('📺', 'On the TV too', 'Mirror your phone or tablet screen to the TV and everyone plays on the big screen.'),
      ('⚔️', 'A duel for two', 'Just the two of you? In Wordsmithing, Mental Math, Guess the Number and Reach the Number you play at the same time on a split screen, each with a challenge at your own level. Whoever scores more points wins.'),
      ('📚', 'More than 6,000 challenges', 'Over 2,000 questions per language, hundreds of words, charades and categories, all checked to be child-friendly. Settings shows how much content each game has.'),
      ('🧒', 'Solo play too', 'Quiz, Alphabet Wheel, Letter Rush, Wordsmithing, Guess the Word, Mental Math, Flags, Guess the Number and Reach the Number are great for practising and learning on your own. With the game challenge and your record of correct answers in a row, there\'s always something to beat.'),
      ('🏆', 'Scores and turns', 'The app keeps the score, turns and time, so all you have to do is have fun, with family or friends.'),
      ('💬', 'Get to know each other better', 'It is not all about winning: Would You Rather?, Get to Know You and Story Chain spark conversations to discover the tastes, memories and stories of the people around you.'),
      ('🌱', 'Always growing', 'Rondalia is updated often: new games, more questions and free sets for special times of the year, each with its own visual style. The app lets you know about each new version and what is new, and you can suggest games from it.')],
 r_a1='Rondalia home screen', r_a2='Alphabet Wheel in Rondalia',
 r_gh='The games',
 r_g=['❓ Quiz', '🤐 Forbidden Words', '🔤 Alphabet Wheel', '🎭 Charades', '🚩 Flags', '➗ Mental Math', '🔢 Guess the Number', '🎯 Reach the Number', '⚡ Letter Rush', '🔠 Wordsmithing', '🎈 Guess the Word', '🤔 What Would They Pick?', '🤷 The Clueless One', '⚖️ Would You Rather?', '💬 Get to Know You', '📖 Story Chain', '🔐 Codeburst'],
 r_n='In English, Spanish, French, German and Portuguese, with questions adapted to each country. Launch edition: free and complete right now, no purchases. Download it now and keep the full version forever.',
 l_k='Set your course for passing your exam',
 l_p='Lexpedition turns preparing for your official language exam into a voyage across the sea, and the destination port is a pass. Each lesson is an island to conquer and every expression you master is one mile closer to the goal. With five or ten minutes a day you will reach exam day with the vocabulary that resists the most.',
 l_langs=['🇬🇧 English', '🇩🇪 German', '🇫🇷 French', '🇪🇸 Spanish', 'Levels A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Four languages to study', 'Prepare English, German, French or Spanish, from A1 to C2 of the Common European Framework (English from A2). You can study several at once.'),
      ('🧩', 'The hard stuff', 'Phrasal verbs, verbs with prepositions (trennbare Verben…), idioms and collocations, with real example sentences.'),
      ('🗺️', 'A sea chart', 'Choose your course among mystery islands, clear the fog and plant your flag. Rise from Deckhand to Admiral.'),
      ('🧠', 'Smart review', 'Flashcards, pick the particle, fill the gaps and match pairs, with spaced repetition so you don\'t forget.'),
      ('🌱', 'Daily motivation', 'Daily test with a score, streaks, XP goal, missions and badges. Perfect to build the habit.'),
      ('✈️', 'Study offline', 'On the train, on a plane or anywhere without signal: Lexpedition works without internet and uses no data. All the vocabulary is built into the app.'),
      ('🗣️', 'In your language', 'The app speaks English, Spanish, French or German, and meanings can be shown as translations or definitions.')],
 l_a1='Lexpedition sea chart', l_a2='Progress, rank and records in Lexpedition',
 l_n='For every age: from children preparing their first certificate to adults. Works on phones and tablets, with several profiles on the same device. Launch edition: free and complete right now, with all four languages and every level. Download it now and keep the full version forever.',
 c_h='Features',
 c=['No ads.', 'No accounts or sign-up.', 'They work offline: no mobile data or signal needed.', 'For phones and tablets: Android, iPhone and iPad.', "We don't collect personal data: everything stays on your device.", 'Child-friendly: purchases and links are protected by a question for adults.', 'Optional one-time purchase, no subscriptions.'],
 mail='Questions or ideas? Write to')
T['fr'] = dict(
 h1='Des applis pour apprendre et jouer',
 lead="Nous sommes MJCStudio, un petit studio indépendant de développement de logiciels et d'applications, basé en Espagne. Tout a commencé comme un passe-temps à la maison, en famille. Nous créons des applis soignées, sans publicité et sans collecte de données, pour passer de bons moments ensemble et apprendre sans s'en rendre compte.",
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Des moments de qualité qui tiennent dans un téléphone',
 r_p="Tous les moments sont bons pour jouer ensemble : après le repas, en voiture, en attendant au restaurant, un après-midi de pluie ou entre amis. Sors ton téléphone et la partie commence, en famille, entre amis ou en solo. Un seul téléphone qui passe de main en main, ou une tablette au centre de la table, sans internet, sans compte et sans règles à lire : grands-parents, parents et enfants jouent ensemble, chacun à son niveau.",
 r_f=[('👨‍👩‍👧‍👦', 'Chacun à son niveau', 'Quatre niveaux de difficulté, de 1 à 4. Dans la même partie, le petit a sa question et le grand-père la sienne.'),
      ('🎲', 'Plus de 15 jeux, un seul score', 'Du quiz et du mime à la roue de l\'alphabet, aux drapeaux ou aux mots interdits. Changez de jeu quand vous voulez ou laissez « La roue décide » choisir à chaque tour : le tableau des scores additionne tous les points. Vous ne savez pas à quoi jouer ? « Aide-moi à choisir » pose trois questions rapides et vous propose des jeux.'),
      ('🎡', 'La roue décide', 'Pas envie de choisir ? Lancez la roue : un jeu différent à chaque tour, par manches. Vous choisissez les jeux en lice, et la roue cliquette comme une roulette.'),
      ('🤝', 'Nouveau : tous ensemble', 'Avec de jeunes enfants ou sans envie de compétition ? Choisissez « Tous ensemble » : une seule équipe, sans prénoms, au niveau de votre choix. Répondez ensemble et relevez le défi : 20 bonnes réponses avant 5 erreurs.'),
      ('👥', 'Autant de joueurs que vous voulez', 'Enregistre jusqu\'à 50 joueurs et jouez tous ensemble, sans limite par jeu. Dans les grandes parties, Le Distrait compte plusieurs distraits, démasqués manche après manche.'),
      ('✈️', 'Sans internet', 'En voiture, en avion, à la plage ou à la campagne sans réseau : Rondalia fonctionne sans connexion et sans consommer de données. Tout est déjà dans l\'appli.'),
      ('📺', 'Aussi sur la télé', 'Duplique l\'écran du téléphone ou de la tablette sur la télé et jouez tous en grand.'),
      ('⚔️', 'Un duel à deux', 'Vous êtes deux ? Dans Motine, Calcul mental, Devine le nombre et Atteins le nombre, jouez en même temps sur écran partagé, chacun avec un défi à son niveau. Le plus de points gagne.'),
      ('📚', 'Plus de 6 000 défis', 'Plus de 2 000 questions par langue, des centaines de mots, de mimes et de catégories, tout vérifié pour convenir aux enfants. Les Réglages montrent le contenu de chaque jeu.'),
      ('🧒', 'Aussi pour jouer seul', 'Quiz, Roue de l\'alphabet, Lettre éclair, Motine, Devine le mot, Calcul mental, Drapeaux, Devine le nombre et Atteins le nombre permettent de s\'entraîner et d\'apprendre en solo. Avec le défi de partie et ton record de bonnes réponses d\'affilée, il y a toujours quelque chose à battre.'),
      ('🏆', 'Score et tours', 'L\'appli compte les points, les tours et le temps : vous n\'avez plus qu\'à vous amuser, en famille ou entre amis.'),
      ('💬', 'Pour mieux se connaître', 'Il n\'y a pas que la compétition : Tu préfères ?, Faisons connaissance et Histoire à la chaîne lancent des conversations pour découvrir les goûts, les souvenirs et les anecdotes des autres.'),
      ('🌱', 'Toujours plus riche', 'Rondalia est mise à jour souvent : nouveaux jeux, plus de questions et packs gratuits pour les moments forts de l\'année, chacun avec son propre style visuel. L\'appli te prévient à chaque nouvelle version et te présente ses nouveautés, et tu peux nous y proposer des jeux.')],
 r_a1="Écran d'accueil de Rondalia", r_a2="Roue de l'alphabet dans Rondalia",
 r_gh='Les jeux',
 r_g=['❓ Quiz', '🤐 Mots interdits', "🔤 Roue de l'alphabet", '🎭 Mime', '🚩 Drapeaux', '➗ Calcul mental', '🔢 Devine le nombre', '🎯 Atteins le nombre', '⚡ Lettre éclair', '🔠 Motine', '🎈 Devine le mot', '🤔 Devine son choix', '🤷 Le Distrait', '⚖️ Tu préfères ?', '💬 Faisons connaissance', '📖 Histoire à la chaîne', '🔐 Le code caché'],
 r_n="En français, espagnol, anglais, allemand et portugais, avec des questions adaptées à chaque pays. Édition de lancement : gratuite et complète en ce moment, sans achat. Télécharge-la maintenant et garde la version complète pour toujours.",
 l_k='Cap sur la réussite de ton examen',
 l_p="Lexpedition transforme la préparation de ton examen officiel de langue en une traversée en mer, et le port d'arrivée, c'est la réussite. Chaque leçon est une île à conquérir et chaque expression maîtrisée est un mille de moins vers le but. Avec cinq ou dix minutes par jour, tu arriveras à l'examen avec le vocabulaire qui résiste le plus.",
 l_langs=['🇬🇧 Anglais', '🇩🇪 Allemand', '🇫🇷 Français', '🇪🇸 Espagnol', 'Niveaux A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Quatre langues à étudier', 'Prépare l\'anglais, l\'allemand, le français ou l\'espagnol, du niveau A1 au C2 du Cadre européen commun (anglais à partir du A2). Tu peux en étudier plusieurs.'),
      ('🧩', 'Ce qui coûte le plus', 'Verbes à particule ou à préposition (phrasal verbs, trennbare Verben…), expressions idiomatiques et collocations, avec de vraies phrases d\'exemple.'),
      ('🗺️', 'Une carte marine', 'Choisis ton cap parmi des îles mystérieuses, dissipe le brouillard et plante ton drapeau. Grimpe de Mousse à Amiral.'),
      ('🧠', 'Révision intelligente', 'Cartes, choix de la particule, textes à trous et paires, avec répétition espacée pour ne pas oublier.'),
      ('🌱', 'Motivation quotidienne', 'Test du jour noté, série, objectif d\'XP, missions et badges. Idéal pour prendre l\'habitude.'),
      ('✈️', 'Hors connexion', 'Dans le métro, en avion ou sans réseau : Lexpedition fonctionne sans internet et ne consomme pas de données. Tout le vocabulaire est déjà dans l\'appli.'),
      ('🗣️', 'Dans ta langue', 'L\'appli parle français, espagnol, anglais ou allemand, et les sens s\'affichent en traduction ou en définition.')],
 l_a1='Carte marine de Lexpedition', l_a2='Progrès, grade et records dans Lexpedition',
 l_n="Pour tous les âges : des enfants qui préparent leur premier diplôme aux adultes. Fonctionne sur téléphone et tablette, avec plusieurs profils sur le même appareil. Édition de lancement : gratuite et complète en ce moment, avec les quatre langues et tous les niveaux. Télécharge-la maintenant et garde la version complète pour toujours.",
 c_h='Caractéristiques',
 c=['Pas de publicité.', 'Pas de compte ni d\'inscription.', 'Elles fonctionnent hors connexion : ni données mobiles ni réseau.', 'Pour téléphone et tablette : Android, iPhone et iPad.', 'Aucune donnée personnelle collectée : tout reste sur ton appareil.', 'Adapté aux enfants : achats et liens protégés par une question pour adultes.', 'Achat unique facultatif, sans abonnement.'],
 mail='Une question, une idée ? Écris-nous à')
T['de'] = dict(
 h1='Apps zum Lernen und Spielen',
 lead='Wir sind MJCStudio, ein kleines unabhängiges Studio für Software- und App-Entwicklung aus Spanien. Alles begann als Hobby zu Hause, in der Familie. Wir machen liebevoll gestaltete Apps ohne Werbung und ohne Datensammlung – für schöne Stunden miteinander und Lernen ganz nebenbei.',
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Wertvolle gemeinsame Momente, die in ein Handy passen',
 r_p='Jeder Moment ist gut, um gemeinsam zu spielen: nach dem Essen, auf der Autofahrt, beim Warten im Restaurant, an einem Regennachmittag oder mit Freunden. Handy raus – und los geht\'s, mit der Familie, mit Freunden oder allein. Ein Handy, das herumgereicht wird, oder ein Tablet in der Mitte des Tisches, ohne Internet, ohne Konto und ohne Anleitung lesen: Großeltern, Eltern und Kinder spielen zusammen, jeder auf seinem Niveau.',
 r_f=[('👨‍👩‍👧‍👦', 'Jeder auf seinem Niveau', 'Vier Schwierigkeitsstufen, von 1 bis 4. Im selben Spiel bekommt das Kind seine Frage und der Opa seine.'),
      ('🎲', 'Über 15 Spiele, eine Punktetabelle', 'Von Quiz und Pantomime bis Buchstabenrad, Flaggen oder verbotene Wörter. Wechselt das Spiel, wann ihr wollt, oder lasst „Das Rad entscheidet“ in jeder Runde wählen: Die Punktetabelle zählt alles zusammen. Ihr wisst nicht, was ihr spielen sollt? „Hilf mir wählen“ stellt drei kurze Fragen und schlägt Spiele vor.'),
      ('🎡', 'Das Rad entscheidet', 'Keine Lust zu entscheiden? Dreht das Rad und bekommt in jeder Runde ein anderes Spiel. Ihr wählt, welche Spiele dabei sind, und das Rad klickt wie ein Roulette.'),
      ('🤝', 'Neu: alle zusammen', 'Mit kleinen Kindern oder einfach ohne Lust auf Wettkampf? Wählt „Alle zusammen“: ein Team, ohne Namen, auf der Stufe, die ihr wollt. Antwortet gemeinsam und schafft die Herausforderung: 20 richtige Antworten vor 5 Fehlern.'),
      ('👥', 'Alle spielen mit', 'Speichere bis zu 50 Spieler und spielt alle zusammen, ohne Begrenzung pro Spiel. In großen Runden gibt es bei Der Ahnungslose mehrere Ahnungslose, die Runde für Runde entlarvt werden.'),
      ('✈️', 'Ohne Internet', 'Im Auto, im Flugzeug, am Strand oder im Funkloch: Rondalia braucht keine Verbindung und kein Datenvolumen. Alles steckt schon in der App.'),
      ('📺', 'Auch auf dem Fernseher', 'Spiegle den Bildschirm von Handy oder Tablet auf den Fernseher und alle spielen auf dem großen Bildschirm.'),
      ('⚔️', 'Duell zu zweit', 'Nur ihr zwei? In Wörteln, Kopfrechnen, Zahlenraten und Triff die Zahl spielt ihr gleichzeitig auf geteiltem Bildschirm, jeder mit einer Aufgabe auf seinem Niveau. Wer mehr Punkte holt, gewinnt.'),
      ('📚', 'Über 6.000 Aufgaben', 'Über 2.000 Fragen pro Sprache, Hunderte Wörter, Pantomimen und Kategorien – alles kindgerecht geprüft. In den Einstellungen siehst du, wie viel Inhalt jedes Spiel hat.'),
      ('🧒', 'Auch allein spielbar', 'Quiz, Buchstabenrad, Buchstabenblitz, Wörteln, Wörterraten, Kopfrechnen, Flaggen, Zahlenraten und Triff die Zahl eignen sich zum Üben und Lernen mit nur einem Spieler. Mit der Herausforderung und deinem Rekord an richtigen Antworten in Folge gibt es immer etwas zu schlagen.'),
      ('🏆', 'Punkte und Runden', 'Die App zählt Punkte, Runden und Zeit – ihr müsst nur noch Spaß haben, mit der Familie oder mit Freunden.'),
      ('💬', 'Einander besser kennenlernen', 'Es geht nicht nur ums Gewinnen: Was wäre dir lieber?, Kennenlernen und Kettengeschichte bringen Gespräche in Gang, in denen ihr Vorlieben, Erinnerungen und Anekdoten der anderen entdeckt.'),
      ('🌱', 'Wächst ständig', 'Rondalia wird regelmäßig aktualisiert: neue Spiele, mehr Fragen und kostenlose Pakete für besondere Zeiten im Jahr, jeweils mit eigenem Stil. Die App sagt dir bei jeder neuen Version Bescheid und zeigt, was neu ist, und du kannst uns darin Spiele vorschlagen.')],
 r_a1='Startbildschirm von Rondalia', r_a2='Buchstabenrad in Rondalia',
 r_gh='Die Spiele',
 r_g=['❓ Quiz', '🤐 Verbotene Wörter', '🔤 Buchstabenrad', '🎭 Pantomime', '🚩 Flaggen', '➗ Kopfrechnen', '🔢 Zahlenraten', '🎯 Triff die Zahl', '⚡ Buchstabenblitz', '🔠 Wörteln', '🎈 Wörterraten', '🤔 Rate die Wahl', '🤷 Der Ahnungslose', '⚖️ Was wäre dir lieber?', '💬 Kennenlernen', '📖 Kettengeschichte', '🔐 Code-Detektiv'],
 r_n='Auf Deutsch, Spanisch, Englisch, Französisch und Portugiesisch, mit Fragen für jedes Land. Launch-Edition: aktuell kostenlos und komplett, ohne Käufe. Jetzt herunterladen und die Vollversion für immer behalten.',
 l_k='Kurs auf deine bestandene Prüfung',
 l_p='Lexpedition macht aus der Vorbereitung auf deine offizielle Sprachprüfung eine Reise übers Meer – und der Zielhafen ist das Bestehen. Jede Lektion ist eine Insel, die du eroberst, und jeder Ausdruck, den du beherrschst, ist eine Seemeile näher am Ziel. Mit fünf bis zehn Minuten am Tag gehst du mit genau dem Wortschatz in die Prüfung, der am schwersten fällt.',
 l_langs=['🇬🇧 Englisch', '🇩🇪 Deutsch', '🇫🇷 Französisch', '🇪🇸 Spanisch', 'Niveaus A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Vier Sprachen zum Lernen', 'Bereite dich auf Englisch, Deutsch, Französisch oder Spanisch vor, von A1 bis C2 des Gemeinsamen Europäischen Referenzrahmens (Englisch ab A2). Auch mehrere gleichzeitig.'),
      ('🧩', 'Das, was am schwersten fällt', 'Partikelverben und Verben mit Präposition (phrasal verbs, trennbare Verben…), Redewendungen und Kollokationen, mit echten Beispielsätzen.'),
      ('🗺️', 'Eine Seekarte', 'Wähle deinen Kurs zwischen geheimnisvollen Inseln, vertreibe den Nebel und hisse deine Flagge. Steige vom Schiffsjungen zum Admiral auf.'),
      ('🧠', 'Kluges Wiederholen', 'Karteikarten, Partikel wählen, Lücken füllen und Paare bilden – mit verteilter Wiederholung, damit nichts vergessen wird.'),
      ('🌱', 'Tägliche Motivation', 'Tagestest mit Note, Serie, XP-Ziel, Missionen und Abzeichen. Ideal, um dranzubleiben.'),
      ('✈️', 'Offline lernen', 'In der U-Bahn, im Flugzeug oder im Funkloch: Lexpedition funktioniert ohne Internet und verbraucht kein Datenvolumen. Der ganze Wortschatz steckt schon in der App.'),
      ('🗣️', 'In deiner Sprache', 'Die App spricht Deutsch, Spanisch, Englisch oder Französisch, und Bedeutungen erscheinen als Übersetzung oder Definition.')],
 l_a1='Seekarte in Lexpedition', l_a2='Fortschritt, Rang und Rekorde in Lexpedition',
 l_n='Für jedes Alter: von Kindern vor ihrem ersten Zertifikat bis zu Erwachsenen. Läuft auf Handy und Tablet, mit mehreren Profilen auf einem Gerät. Launch-Edition: aktuell kostenlos und komplett, mit allen vier Sprachen und allen Niveaus. Jetzt herunterladen und die Vollversion für immer behalten.',
 c_h='Funktionen',
 c=['Keine Werbung.', 'Für Handy und Tablet: Android, iPhone und iPad.', 'Kein Konto, keine Anmeldung.', 'Funktionieren offline: ohne mobile Daten und ohne Netz.', 'Wir sammeln keine personenbezogenen Daten: Alles bleibt auf deinem Gerät.', 'Kindgerecht: Käufe und Links sind durch eine Frage für Erwachsene geschützt.', 'Optionaler Einmalkauf, kein Abo.'],
 mail='Fragen oder Ideen? Schreib uns an')

T['pt'] = dict(
 h1='Apps para aprender e jogar',
 lead='Somos a MJCStudio, um pequeno estúdio independente de desenvolvimento de software e aplicações, sediado em Espanha. Tudo começou como um passatempo em casa, em família. Fazemos apps cuidadas, sem anúncios e sem recolher dados, para passar bons momentos juntos e aprender sem dar por isso.',
 b1='🎲 Rondalia', b2='⛵ Lexpedition',
 r_k='Momentos que valem a pena, num só telemóvel',
 r_p='Qualquer momento é bom para jogar juntos: depois do jantar, numa viagem de carro, à espera num restaurante, numa tarde de chuva ou com amigos. Pega no telemóvel e começa a partida, em família, com amigos ou sozinho. Um só telemóvel que vai passando de mão em mão, ou um tablet no centro da mesa, sem internet, sem contas e sem ninguém ter de ler instruções: avós, pais e pequenos jogam juntos, cada um ao seu nível.',
 r_f=[('👨‍👩‍👧‍👦', 'Cada um ao seu nível', 'Quatro níveis de dificuldade, do 1 ao 4. Na mesma partida, o pequeno recebe a sua pergunta e o avô a dele.'),
      ('🎲', 'Mais de 15 jogos, uma só pontuação', 'Das perguntas e da mímica ao abecedário, às bandeiras ou à palavra proibida. Mudem de jogo quando quiserem ou deixem que «A roda escolhe» decida em cada vez: a pontuação soma os pontos de todos. Não sabem a que jogar? «Ajuda-me a escolher» faz três perguntas rápidas e propõe jogos.'),
      ('🎡', 'A roda escolhe', 'Sem vontade de decidir? Rodem a roda e calha um jogo diferente em cada vez, por rondas. Vocês escolhem quais entram, e a roda soa como uma roleta.'),
      ('🤝', 'Novo: todos juntos', 'Com crianças pequenas ou sem vontade de competir? Escolham «Todos juntos»: uma só equipa, sem nomes, no nível que quiserem. Respondam juntos e superem o desafio: 20 respostas certas antes de 5 falhas.'),
      ('👥', 'Todos os que forem', 'Guarda até 50 jogadores e joguem todos juntos, sem limite por jogo. Nas partidas grandes, O distraído tem vários distraídos, que se descobrem ronda a ronda.'),
      ('✈️', 'Sem internet', 'No carro, no avião, na praia ou na aldeia sem rede: a Rondalia não precisa de ligação nem gasta dados. Está tudo dentro da app.'),
      ('📺', 'Também na televisão', 'Espelha o ecrã do telemóvel ou do tablet na televisão e joguem todos em grande.'),
      ('⚔️', 'Duelo a dois', 'São dois? Na Palavreia, no Cálculo, no Adivinha o número e no Chega ao número jogam ao mesmo tempo com o ecrã dividido, cada um com o desafio do seu nível. Ganha quem somar mais pontos.'),
      ('📚', 'Mais de 6000 desafios', 'Mais de 2000 perguntas por idioma, adaptadas a Portugal, centenas de palavras, mímicas e categorias, e todo o conteúdo revisto para ser adequado a crianças. Nas Definições vês quanto conteúdo tem cada jogo.'),
      ('🧒', 'Também para jogar sozinho', 'Perguntas, Abecedário, Letra a voar, Palavreia, Adivinha a palavra, Cálculo, Bandeiras, Adivinha o número e Chega ao número servem para praticar e aprender com um só jogador. Com o desafio de partida e o teu recorde de respostas certas seguidas, há sempre algo para superar.'),
      ('🏆', 'Pontuação e vezes', 'A app conta os pontos, as vezes e o tempo, para que vocês só tenham de se divertir, em família ou com amigos.'),
      ('💬', 'Para se conhecerem melhor', 'Nem tudo é competir: O que preferes?, Conhecermo-nos e História encadeada abrem conversas para descobrir gostos, memórias e histórias dos outros.'),
      ('🌱', 'Sempre a crescer', 'A Rondalia é atualizada com frequência: jogos novos, mais perguntas e coleções grátis para as datas especiais do ano, com o seu próprio estilo visual. A app avisa-te de cada versão nova e conta-te as novidades, e podes sugerir-nos jogos a partir dela.')],
 r_a1='Ecrã inicial da Rondalia', r_a2='Jogo do Abecedário na Rondalia',
 r_gh='Os jogos',
 r_g=['❓ Perguntas', '🤐 Palavra proibida', '🔤 Abecedário', '🎭 Mímica', '🚩 Bandeiras', '➗ Cálculo', '🔢 Adivinha o número', '🎯 Chega ao número', '⚡ Letra a voar', '🔠 Palavreia', '🎈 Adivinha a palavra', '🤔 O que escolheria?', '🤷 O distraído', '⚖️ O que preferes?', '💬 Conhecermo-nos', '📖 História encadeada', '🔐 Decifra o código'],
 r_n='Em português, espanhol, inglês, francês e alemão, com perguntas adaptadas a cada país. Edição de lançamento: agora grátis e completa, sem compras. Descarrega-a já e fica com ela completa para sempre.',
 l_k='Rumo certo: passar no teu exame',
 l_p='A Lexpedition transforma a preparação do teu exame oficial de línguas numa travessia pelo mar, e o porto de chegada é a aprovação. Cada lição é uma ilha para conquistar e cada expressão que dominas é uma milha a menos até à meta. Com cinco ou dez minutos por dia, chegarás ao exame com o vocabulário que mais resiste.',
 l_langs=['🇬🇧 Inglês', '🇩🇪 Alemão', '🇫🇷 Francês', '🇪🇸 Espanhol', 'Níveis A1 · A2 · B1 · B2 · C1 · C2'],
 l_f=[('🌍', 'Quatro línguas para estudar', 'Prepara inglês, alemão, francês ou espanhol, do nível A1 ao C2 do Quadro Europeu Comum de Referência (inglês a partir do A2). Podes estudar várias ao mesmo tempo.'),
      ('🧩', 'O que mais custa', 'Verbos com partícula ou preposição (phrasal verbs, trennbare Verben…), expressões idiomáticas e colocações, com frases de exemplo reais.'),
      ('🗺️', 'Uma carta de navegação', 'Escolhe o teu rumo entre ilhas misteriosas, dissipa o nevoeiro e planta a tua bandeira. Sobe de Grumete a Almirante.'),
      ('🧠', 'Revisão inteligente', 'Cartões, escolher a partícula, completar espaços e juntar pares, com repetição espaçada para não esqueceres o que aprendeste.'),
      ('🌱', 'Motivação diária', 'Teste diário com nota, sequência, meta de XP, missões e medalhas. Ideal para criar o hábito.'),
      ('✈️', 'Sem ligação', 'No metro, no avião ou onde não haja rede: a Lexpedition funciona sem internet e sem gastar dados. Todo o vocabulário está dentro da app.'),
      ('🗣️', 'Na tua língua', 'A app está em espanhol, inglês, francês ou alemão, e os significados podem aparecer traduzidos ou como definição.')],
 l_a1='Carta de navegação da Lexpedition', l_a2='Progresso, posto e recordes na Lexpedition',
 l_n='Para qualquer idade: de crianças que preparam o primeiro certificado a adultos. Funciona no telemóvel e no tablet, com vários perfis no mesmo dispositivo. Edição de lançamento: agora grátis e completa, com as quatro línguas e todos os níveis. Descarrega-a já e fica com ela completa para sempre.',
 c_h='Características',
 c=['Sem anúncios.', 'Sem contas nem registo.', 'Funcionam sem ligação: sem dados móveis nem rede.', 'Para telemóvel e tablet: Android, iPhone e iPad.', 'Não recolhemos dados pessoais: tudo fica guardado no teu dispositivo.', 'Adequadas a menores: compras e ligações protegidas com uma pergunta para adultos.', 'Compra única opcional, sem subscrições.'],
 mail='Dúvidas ou ideias? Escreve-nos para')



# 6.25: cinco formas (Solo, Duelo, Todos contra todos, Todos juntos, Por equipos)
# 6.16: las cuatro formas de jugar, juntas y arriba (antes repartidas entre «Nuevo: todos juntos», «Todos los que seáis», «Duelo para dos» y «También para jugar solo»)
MODES4 = {
 'es': ('5 formas de jugar, en la misma app', [
   ('👤', 'Solo', 'Para practicar o pasar el rato: Preguntas, Banderas, Cálculo, Palabrea, Adivina la palabra y más, con tu récord de aciertos seguidos y retos con vidas.'),
   ('⚔️', 'Duelo para dos', 'Pantalla dividida, cada uno en su lado y a su nivel: pulsador en Preguntas y Banderas (responde quien pulse antes), una palabra para cada uno en Adivina la palabra, y Cálculo, Palabrea, Adivina el número y Llega al número. Gana quien sume más.'),
   ('🏆', 'Todos contra todos', 'De 3 en adelante, cada uno con sus puntos y sin límite por juego: guarda hasta 50 jugadores y jugad por turnos o todos a la vez, con un solo marcador. En las partidas grandes, El despistado tiene varios despistados.'),
   ('👥', 'Todos juntos', '¿Con niños pequeños o sin ganas de competir? Un solo equipo, sin nombres: ganáis o perdéis juntos contra un reto, como 20 aciertos antes de 5 fallos. Y si sois dos, Palabra prohibida y Mímica se juegan en equipo.'),
   ('🆚', 'Por equipos', 'Equipo contra equipo: 2 o más equipos, del tamaño que queráis. Se turnan los equipos y, dentro de cada uno, sus jugadores; los puntos son del equipo. Con 2 equipos, también en duelo.')]),
 'en': ('5 ways to play, in one app', [
   ('👤', 'Solo', 'To practise or pass the time: Quiz, Flags, Mental Math, Wordsmithing, Guess the Word and more, with your record of correct answers in a row and challenges with lives.'),
   ('⚔️', 'A duel for two', 'Split screen, each on your own side and at your own level: a buzzer in Quiz and Flags (whoever buzzes first answers), a word each in Guess the Word, plus Mental Math, Wordsmithing, Guess the Number and Reach the Number. The higher score wins.'),
   ('🏆', 'Free-for-all', '3 or more, each with their own points and no limit per game: save up to 50 players and play taking turns or all at once, with one scoreboard. In big games, The Clueless One has several clueless players.'),
   ('👥', 'All together', 'Playing with little ones or not in the mood to compete? One team, no names: you win or lose together against a challenge, such as 20 right before 5 wrong. And with two of you, Forbidden Words and Charades are played as a team.'),
   ('🆚', 'Teams', 'Team against team: 2 or more teams, any size you like. Teams take turns and, within each team, so do its players; points go to the team. With 2 teams, you can also duel.')]),
 'fr': ('5 façons de jouer, dans la même appli', [
   ('👤', 'Solo', 'Pour s’entraîner ou passer le temps : Quiz, Drapeaux, Calcul mental, Motine, Devine le mot et plus encore, avec ton record de bonnes réponses d’affilée et des défis avec des vies.'),
   ('⚔️', 'Un duel à deux', 'Écran partagé, chacun de son côté et à son niveau : un buzzer au Quiz et aux Drapeaux (le premier qui appuie répond), un mot chacun à Devine le mot, et aussi Calcul mental, Motine, Devine le nombre et Atteins le nombre. Le meilleur score gagne.'),
   ('🏆', 'Chacun pour soi', 'À partir de 3, chacun ses points et sans limite par jeu : enregistre jusqu’à 50 joueurs et jouez à tour de rôle ou tous en même temps, avec un seul tableau des scores. Dans les grandes parties, Le Distrait a plusieurs distraits.'),
   ('👥', 'Tous ensemble', 'Avec de jeunes enfants ou sans envie de compétition ? Une seule équipe, sans prénoms : vous gagnez ou perdez ensemble face à un défi, comme 20 bonnes réponses avant 5 erreurs. Et à deux, Mots interdits et Mime se jouent en équipe.'),
   ('🆚', 'En équipes', 'Équipe contre équipe : 2 équipes ou plus, de la taille que vous voulez. Les équipes jouent à tour de rôle et, dans chaque équipe, ses joueurs aussi ; les points vont à l’équipe. À 2 équipes, aussi en duel.')]),
 'de': ('5 Arten zu spielen, in einer App', [
   ('👤', 'Allein', 'Zum Üben oder Zeitvertreib: Quiz, Flaggen, Kopfrechnen, Wörteln, Wörterraten und mehr, mit deinem Rekord an richtigen Antworten in Folge und Herausforderungen mit Leben.'),
   ('⚔️', 'Duell zu zweit', 'Geteilter Bildschirm, jeder auf seiner Seite und seiner Stufe: Buzzer bei Quiz und Flaggen (wer zuerst drückt, antwortet), ein eigenes Wort bei Wörterraten, dazu Kopfrechnen, Wörteln, Zahlenraten und Triff die Zahl. Wer mehr Punkte hat, gewinnt.'),
   ('🏆', 'Jeder gegen jeden', 'Ab 3, jeder mit seinen Punkten und ohne Grenze pro Spiel: Speichere bis zu 50 Spieler und spielt reihum oder alle gleichzeitig, mit einer Punktetabelle. In großen Runden hat Der Ahnungslose mehrere Ahnungslose.'),
   ('👥', 'Alle zusammen', 'Mit kleinen Kindern oder ohne Lust auf Wettkampf? Ein Team, ohne Namen: Ihr gewinnt oder verliert gemeinsam gegen eine Herausforderung, etwa 20 richtige vor 5 Fehlern. Und zu zweit spielt ihr Verbotene Wörter und Pantomime im Team.'),
   ('🆚', 'In Teams', 'Team gegen Team: 2 oder mehr Teams, so groß ihr wollt. Die Teams sind abwechselnd dran und in jedem Team reihum seine Spieler; die Punkte gehen ans Team. Mit 2 Teams auch als Duell.')]),
 'pt': ('5 formas de jogar, na mesma app', [
   ('👤', 'Sozinho', 'Para praticar ou passar o tempo: Perguntas, Bandeiras, Cálculo, Palavreia, Adivinha a palavra e mais, com o teu recorde de respostas certas seguidas e desafios com vidas.'),
   ('⚔️', 'Duelo a dois', 'Ecrã dividido, cada um no seu lado e no seu nível: botão de resposta em Perguntas e Bandeiras (responde quem carregar primeiro), uma palavra para cada um em Adivinha a palavra, e ainda Cálculo, Palavreia, Adivinha o número e Chega ao número. Ganha quem somar mais.'),
   ('🏆', 'Todos contra todos', 'A partir de 3, cada um com os seus pontos e sem limite por jogo: guarda até 50 jogadores e joguem à vez ou todos ao mesmo tempo, com uma só pontuação. Nas partidas grandes, há vários distraídos.'),
   ('👥', 'Todos juntos', 'Com crianças pequenas ou sem vontade de competir? Uma só equipa, sem nomes: ganham ou perdem juntos contra um desafio, como 20 certas antes de 5 falhas. E se forem dois, Palavra proibida e Mímica jogam-se em equipa.'),
   ('🆚', 'Por equipas', 'Equipa contra equipa: 2 ou mais equipas, do tamanho que quiserem. As equipas jogam à vez e, dentro de cada uma, os seus jogadores; os pontos são da equipa. Com 2 equipas, também em duelo.')])}
for _lg, (_h, _m) in MODES4.items():
    T[_lg]['r_mh'] = _h; T[_lg]['r_m'] = _m
    T[_lg]['r_f'] = [f for f in T[_lg]['r_f'] if f[0] not in ('🤝', '👥', '⚔️', '🧒')]

# 6.26 / 9.5: juego nuevo en Rondalia y varios usuarios, a la vista, en Lexpedition
NEW626 = {'es': {'chip': '⚡ ¿Verdad o broma?', 'nf': ('⚡', 'Nuevo: ¿Verdad o broma?', 'Una pregunta y dos respuestas, una lógica y otra disparatada: toca la lógica antes de que se acabe el tiempo. Solo, en grupo o en duelo, cada uno a su nivel.'), 'a3r': '¿Verdad o broma? en duelo, con la pantalla dividida', 'a3l': '«¿Quién va a estudiar?»: varios usuarios en Lexpedition', 'lf': ('👨\u200d👩\u200d👧', 'Una app, varios alumnos', 'Un usuario para cada persona de casa, cada uno con su idioma, su nivel, su progreso, su racha y sus ajustes. Al abrir la app eliges quién va a estudiar. Todo en el mismo móvil o tableta, sin cuentas ni registro.'), 'lp': ' Y sirve para toda la familia: cada persona estudia con su propio usuario.', 'duel': ('Adivina el número y Llega al número. Gana quien sume más.', 'Adivina el número, Llega al número y ¿Verdad o broma? Gana quien sume más.')}, 'en': {'chip': '⚡ Truth or Bluff', 'nf': ('⚡', 'New: Truth or Bluff', 'One question, two answers, one sensible and one silly: tap the sensible one before time runs out. Solo, in a group or in a duel, each at their own level.'), 'a3r': 'Truth or Bluff duel on a split screen', 'a3l': '“Who is studying?”: several users in Lexpedition', 'lf': ('👨\u200d👩\u200d👧', 'One app, several learners', 'A user for everyone at home, each with their own language, level, progress, streak and settings. When you open the app, pick who is studying. All on the same phone or tablet, with no accounts or sign-up.'), 'lp': ' And it works for the whole family: everyone studies with their own user.', 'duel': ('Guess the Number and Reach the Number. The higher score wins.', 'Guess the Number, Reach the Number and Truth or Bluff. The higher score wins.')}, 'fr': {'chip': '⚡ Vrai ou farfelu ?', 'nf': ('⚡', 'Nouveau : Vrai ou farfelu ?', 'Une question, deux réponses, l’une logique et l’autre farfelue : touche la logique avant la fin du temps. Seul, à plusieurs ou en duel, chacun à son niveau.'), 'a3r': 'Vrai ou farfelu ? en duel sur écran partagé', 'a3l': 'Choix de l’utilisateur : plusieurs élèves dans Lexpedition', 'lf': ('👨\u200d👩\u200d👧', 'Une appli, plusieurs élèves', 'Un utilisateur pour chaque personne à la maison, chacun avec sa langue, son niveau, ses progrès, sa série et ses réglages. À l’ouverture, tu choisis qui va étudier. Le tout sur le même téléphone ou la même tablette, sans compte ni inscription.'), 'lp': ' Et elle sert à toute la famille : chacun étudie avec son propre utilisateur.', 'duel': ('Devine le nombre et Atteins le nombre. Le meilleur score gagne.', 'Devine le nombre, Atteins le nombre et Vrai ou farfelu ? Le meilleur score gagne.')}, 'de': {'chip': '⚡ Echt oder Quatsch?', 'nf': ('⚡', 'Neu: Echt oder Quatsch?', 'Eine Frage, zwei Antworten, eine sinnvolle und eine verrückte: Tippe die sinnvolle, bevor die Zeit abläuft. Allein, in der Runde oder im Duell, jeder auf seiner Stufe.'), 'a3r': 'Echt oder Quatsch? im Duell auf geteiltem Bildschirm', 'a3l': 'Nutzerauswahl: mehrere Lernende in Lexpedition', 'lf': ('👨\u200d👩\u200d👧', 'Eine App, mehrere Lernende', 'Ein Nutzer für jede Person zu Hause, jeder mit eigener Sprache, eigenem Niveau, Fortschritt, eigener Serie und eigenen Einstellungen. Beim Öffnen wählst du, wer lernt. Alles auf demselben Handy oder Tablet, ohne Konto.'), 'lp': ' Und sie passt für die ganze Familie: Jeder lernt mit seinem eigenen Nutzer.', 'duel': ('Zahlenraten und Triff die Zahl. Wer mehr Punkte hat, gewinnt.', 'Zahlenraten, Triff die Zahl und Echt oder Quatsch? Wer mehr Punkte hat, gewinnt.')}, 'pt': {'chip': '⚡ Verdade ou disparate?', 'nf': ('⚡', 'Novo: Verdade ou disparate?', 'Uma pergunta e duas respostas, uma lógica e outra disparatada: toca na lógica antes de o tempo acabar. Sozinho, em grupo ou em duelo, cada um no seu nível.'), 'a3r': 'Verdade ou disparate? em duelo, com o ecrã dividido', 'a3l': 'Escolha do utilizador: vários alunos na Lexpedition', 'lf': ('👨\u200d👩\u200d👧', 'Uma app, vários alunos', 'Um utilizador para cada pessoa lá de casa, cada um com a sua língua, o seu nível, progresso, série e definições. Ao abrir a app escolhes quem vai estudar. Tudo no mesmo telemóvel ou tablet, sem contas nem registo.'), 'lp': ' E serve para toda a família: cada pessoa estuda com o seu próprio utilizador.', 'duel': ('Adivinha o número e Chega ao número. Ganha quem somar mais.', 'Adivinha o número, Chega ao número e Verdade ou disparate? Ganha quem somar mais.')}}
for _lg, _d in NEW626.items():
    _t = T[_lg]
    _t['r_g'] = _t['r_g'] + [_d['chip']]
    _i = next(i for i, f in enumerate(_t['r_f']) if f[0] == '🎡')
    _t['r_f'] = _t['r_f'][:_i + 1] + [_d['nf']] + _t['r_f'][_i + 1:]
    _t['r_a3'] = _d['a3r']; _t['l_a3'] = _d['a3l']
    _t['l_f'] = [_d['lf']] + _t['l_f']
    _t['l_p'] += _d['lp']
    _a, _b = _d['duel']
    _m = [(i, h, x.replace(_a, _b)) for i, h, x in _t['r_m']]
    assert _m != list(_t['r_m']), 'duelo sin cambiar: ' + _lg
    _t['r_m'] = _m

home = {l: block(T[l], l) for l in T}
