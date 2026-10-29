# Genera la web estática de MJCStudio (portada, privacidad y soporte) en 4 idiomas.
import os
OUT = os.path.join(os.path.dirname(__file__), 'docs')
LANGS = ['es', 'en', 'fr', 'de']
UPDATED = {'es': 'Última actualización: 29 de octubre de 2026', 'en': 'Last updated: 29 October 2026',
           'fr': 'Dernière mise à jour : 29 octobre 2026', 'de': 'Letzte Aktualisierung: 29. Oktober 2026'}
MENU = {'home': {'es': 'Inicio', 'en': 'Home', 'fr': 'Accueil', 'de': 'Start'},
        'priv': {'es': 'Privacidad', 'en': 'Privacy', 'fr': 'Confidentialité', 'de': 'Datenschutz'},
        'sup': {'es': 'Soporte', 'en': 'Support', 'fr': 'Assistance', 'de': 'Support'}}
TITLES = {'home': {'es': 'MJCStudio · Apps para aprender y jugar', 'en': 'MJCStudio · Apps to learn and play',
                   'fr': 'MJCStudio · Applis pour apprendre et jouer', 'de': 'MJCStudio · Apps zum Lernen und Spielen'},
          'priv': {'es': 'Política de privacidad · MJCStudio', 'en': 'Privacy policy · MJCStudio',
                   'fr': 'Politique de confidentialité · MJCStudio', 'de': 'Datenschutzerklärung · MJCStudio'},
          'sup': {'es': 'Soporte · MJCStudio', 'en': 'Support · MJCStudio', 'fr': 'Assistance · MJCStudio', 'de': 'Support · MJCStudio'}}


def L(d, tag='div'):
    return ''.join(f'<{tag} data-l="{l}" lang="{l}">{d[l]}</{tag}>' for l in LANGS)


def page(key, root, body):
    links = [('home', root), ('priv', root + 'privacidad/'), ('sup', root + 'soporte/')]
    menu = ''.join(f'<a href="{h}"{" class=on" if k == key else ""}>' + ''.join(
        f'<span data-l="{l}">{MENU[k][l]}</span>' for l in LANGS) + '</a>' for k, h in links)
    metas = ''.join(f'<meta name="t-{l}" content="{TITLES[key][l]}">' for l in LANGS)
    foot = L({'es': '© 2026 MJCStudio · Desarrollador independiente · España',
              'en': '© 2026 MJCStudio · Independent developer · Spain',
              'fr': '© 2026 MJCStudio · Développeur indépendant · Espagne',
              'de': '© 2026 MJCStudio · Unabhängiger Entwickler · Spanien'}, 'span')
    return f'''<!doctype html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLES[key]['es']}</title>
{metas}
<meta name="description" content="MJCStudio: Rondalia (juegos en grupo) y Lexpedition (vocabulario para exámenes de idiomas).">
<link rel="icon" href="{root}favicon.png">
<link rel="apple-touch-icon" href="{root}img/apple-touch-icon.png">
<link rel="stylesheet" href="{root}site.css">
</head>
<body>
<header><div class="wrap" style="max-width:860px;margin:0 auto">
<a class="logo" href="{root}"><img src="{root}img/mjcstudio.png" alt="MJCStudio" height="64"></a>
<nav class="langs" aria-label="Idioma / Language"><button data-set="es">ES</button><button data-set="en">EN</button><button data-set="fr">FR</button><button data-set="de">DE</button></nav>
</div><div class="wrap" style="max-width:860px;margin:0 auto;padding:0"><nav class="menu">{menu}</nav></div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">{foot} · <a href="{root}privacidad/">{''.join(f'<span data-l="{l}">{MENU["priv"][l]}</span>' for l in LANGS)}</a> · <a href="{root}soporte/">{''.join(f'<span data-l="{l}">{MENU["sup"][l]}</span>' for l in LANGS)}</a></div></footer>
<script src="{root}lang.js"></script>
</body>
</html>
'''


# ---------- PORTADA ----------
home = {
'es': '''<h1>Apps para aprender y jugar</h1>
<p class="lead">Somos MJCStudio, un pequeño estudio independiente. Hacemos apps sencillas, sin anuncios y sin recoger datos, aptas para toda la familia.</p>
<div class="apps">
<div class="app"><img src="img/rondalia.png" alt=""><div><h3>Rondalia</h3><p>Juegos para jugar en grupo con un solo móvil: preguntas, palabra prohibida, abecedario, mímica, banderas y más. Para todas las edades, sin internet.</p><span class="tag">Próximamente en Google Play y App Store</span></div></div>
<div class="app"><img src="img/lexpedition.png" alt=""><div><h3>Lexpedition</h3><p>Aprende el vocabulario difícil de los exámenes de idiomas (niveles A1–C2) navegando en una expedición: verbos con partícula, expresiones y colocaciones.</p><span class="tag">Próximamente en Google Play y App Store</span></div></div>
</div>
<h2>Nuestro compromiso</h2>
<ul><li>Sin anuncios.</li><li>Sin cuentas ni registro.</li><li>No recogemos datos personales: todo se guarda en tu móvil.</li><li>Compra única opcional, sin suscripciones.</li></ul>
<p>¿Dudas o ideas? Escríbenos a <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>''',
'en': '''<h1>Apps to learn and play together</h1>
<p class="lead">We are MJCStudio, a small independent studio. We make simple, family-friendly apps with no ads and no data collection.</p>
<div class="apps">
<div class="app"><img src="img/rondalia.png" alt=""><div><h3>Rondalia</h3><p>Party games for a group with just one phone: trivia, forbidden word, alphabet, charades, flags and more. For all ages, works offline.</p><span class="tag">Coming soon to Google Play and the App Store</span></div></div>
<div class="app"><img src="img/lexpedition.png" alt=""><div><h3>Lexpedition</h3><p>Learn the tricky vocabulary of language exams (levels A1–C2) on a sailing expedition: phrasal verbs, idioms and collocations.</p><span class="tag">Coming soon to Google Play and the App Store</span></div></div>
</div>
<h2>Our promise</h2>
<ul><li>No ads.</li><li>No accounts or sign-up.</li><li>We don't collect personal data: everything stays on your device.</li><li>Optional one-time purchase, no subscriptions.</li></ul>
<p>Questions or ideas? Write to <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>''',
'fr': '''<h1>Des applis pour apprendre et jouer en famille</h1>
<p class="lead">Nous sommes MJCStudio, un petit studio indépendant. Nous créons des applis simples, sans publicité et sans collecte de données, pour toute la famille.</p>
<div class="apps">
<div class="app"><img src="img/rondalia.png" alt=""><div><h3>Rondalia</h3><p>Des jeux à plusieurs avec un seul téléphone : questions, mot interdit, abécédaire, mime, drapeaux et plus encore. Pour tous les âges, sans internet.</p><span class="tag">Bientôt sur Google Play et l'App Store</span></div></div>
<div class="app"><img src="img/lexpedition.png" alt=""><div><h3>Lexpedition</h3><p>Apprends le vocabulaire difficile des examens de langues (niveaux A1–C2) au fil d'une expédition en mer : verbes à particule, expressions et collocations.</p><span class="tag">Bientôt sur Google Play et l'App Store</span></div></div>
</div>
<h2>Notre engagement</h2>
<ul><li>Pas de publicité.</li><li>Pas de compte ni d'inscription.</li><li>Aucune donnée personnelle collectée : tout reste sur ton appareil.</li><li>Achat unique facultatif, sans abonnement.</li></ul>
<p>Une question, une idée ? Écris-nous à <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>''',
'de': '''<h1>Apps zum Lernen und gemeinsamen Spielen</h1>
<p class="lead">Wir sind MJCStudio, ein kleines unabhängiges Studio. Wir machen einfache, familienfreundliche Apps ohne Werbung und ohne Datensammlung.</p>
<div class="apps">
<div class="app"><img src="img/rondalia.png" alt=""><div><h3>Rondalia</h3><p>Gruppenspiele mit nur einem Handy: Quizfragen, verbotenes Wort, ABC-Spiel, Pantomime, Flaggen und mehr. Für jedes Alter, ohne Internet.</p><span class="tag">Bald bei Google Play und im App Store</span></div></div>
<div class="app"><img src="img/lexpedition.png" alt=""><div><h3>Lexpedition</h3><p>Lerne den schwierigen Wortschatz von Sprachprüfungen (Niveaus A1–C2) auf einer Segelexpedition: Partikelverben, Redewendungen und Kollokationen.</p><span class="tag">Bald bei Google Play und im App Store</span></div></div>
</div>
<h2>Unser Versprechen</h2>
<ul><li>Keine Werbung.</li><li>Kein Konto, keine Anmeldung.</li><li>Wir sammeln keine personenbezogenen Daten: Alles bleibt auf deinem Gerät.</li><li>Optionaler Einmalkauf, kein Abo.</li></ul>
<p>Fragen oder Ideen? Schreib uns an <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>'''}

# ---------- PRIVACIDAD ----------
priv = {
'es': '''<h1>Política de privacidad</h1>
<p class="updated">{u}</p>
<div class="box"><p>Esta política se aplica a las apps de <strong>MJCStudio</strong> en Google Play y App Store: <strong>Rondalia</strong> y <strong>Lexpedition</strong>. En pocas palabras: <strong>no recogemos datos personales</strong>, no mostramos anuncios y no usamos herramientas de seguimiento.</p></div>
<h2>1. Responsable</h2>
<p>MJCStudio, desarrollador independiente con sede en España. Contacto: <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>
<h2>2. Qué datos tratamos</h2>
<ul>
<li><strong>Ninguno en nuestros servidores.</strong> Las apps no tienen cuentas ni registro y no envían información a MJCStudio ni a terceros.</li>
<li><strong>Datos guardados solo en tu dispositivo:</strong> los nombres o apodos que escribas para los jugadores o perfiles (y, si lo indicas, su año de nacimiento para ajustar la dificultad), puntuaciones, progreso, ajustes (idioma, tema, sonido) y si has desbloqueado la versión completa. Se guardan en la memoria local de la app y nunca salen del móvil o tableta. Puedes borrarlos desde los ajustes de la app o desinstalándola.</li>
<li><strong>Sin publicidad, sin analítica y sin seguimiento.</strong> No usamos cookies, identificadores publicitarios ni servicios de estadísticas. El único componente de terceros es el sistema de compras de la tienda (Google Play Billing o StoreKit de Apple).</li>
<li><strong>Permisos:</strong> las apps no piden acceso a la cámara, el micrófono, la ubicación, los contactos ni las fotos.</li>
</ul>
<h2>3. Compras</h2>
<p>Las compras dentro de la app (compra única para desbloquear el contenido completo) las gestionan <strong>Google Play</strong> o el <strong>App Store de Apple</strong>. MJCStudio no recibe tus datos de pago; la tienda solo confirma a la app que la compra existe para desbloquear el contenido. Consulta también la política de privacidad de Google o Apple.</p>
<h2>4. Si nos escribes</h2>
<p>Si usas «Escríbenos» o «Enviar comentarios», se abre tu aplicación de correo con un mensaje que puede incluir la versión de la app, el idioma y el modelo del dispositivo, para ayudarnos a resolver el problema. Tú decides si lo envías. Usamos tu dirección de correo y tu mensaje solo para responderte y los borramos cuando ya no son necesarios, o antes si nos lo pides.</p>
<h2>5. Menores</h2>
<p>Las apps son aptas para menores. No recogemos datos de niños. Los enlaces externos (correo, ficha de la tienda) y las compras están protegidos por una pregunta para adultos.</p>
<h2>6. Tus derechos</h2>
<p>Como no guardamos datos tuyos, normalmente no hay nada que consultar ni borrar en nuestro lado. Si nos has escrito, puedes pedir el acceso o la eliminación de ese correo en <a href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>. También puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">www.aepd.es</a>).</p>
<h2>7. Cambios</h2>
<p>Si cambiamos esta política, publicaremos la nueva versión en esta página con su fecha.</p>''',
'en': '''<h1>Privacy policy</h1>
<p class="updated">{u}</p>
<div class="box"><p>This policy applies to <strong>MJCStudio</strong>'s apps on Google Play and the App Store: <strong>Rondalia</strong> and <strong>Lexpedition</strong>. In short: <strong>we do not collect personal data</strong>, we show no ads and we use no tracking tools.</p></div>
<h2>1. Who we are</h2>
<p>MJCStudio, an independent developer based in Spain. Contact: <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>
<h2>2. What data we process</h2>
<ul>
<li><strong>None on our servers.</strong> The apps have no accounts or sign-up and send no information to MJCStudio or to third parties.</li>
<li><strong>Data stored only on your device:</strong> the names or nicknames you type for players or profiles (and, if you add it, their birth year to adjust difficulty), scores, progress, settings (language, theme, sound) and whether you have unlocked the full version. They are kept in the app's local storage and never leave your phone or tablet. You can delete them from the app settings or by uninstalling the app.</li>
<li><strong>No ads, no analytics and no tracking.</strong> We use no cookies, advertising identifiers or statistics services. The only third-party component is the store's purchase system (Google Play Billing or Apple StoreKit).</li>
<li><strong>Permissions:</strong> the apps do not ask for access to your camera, microphone, location, contacts or photos.</li>
</ul>
<h2>3. Purchases</h2>
<p>In-app purchases (a one-time purchase to unlock the full content) are handled by <strong>Google Play</strong> or <strong>Apple's App Store</strong>. MJCStudio never receives your payment details; the store only tells the app that the purchase exists so it can unlock the content. Please also see Google's or Apple's privacy policy.</p>
<h2>4. If you write to us</h2>
<p>If you use "Write to us" or "Send feedback", your email app opens with a message that may include the app version, language and device model, to help us solve the problem. You decide whether to send it. We use your email address and message only to reply and delete them when no longer needed, or sooner if you ask.</p>
<h2>5. Children</h2>
<p>The apps are suitable for children. We do not collect data from children. External links (email, store page) and purchases are protected by a question for adults.</p>
<h2>6. Your rights</h2>
<p>As we keep no data about you, there is normally nothing to access or delete on our side. If you have written to us, you can ask for access to or deletion of that email at <a href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>. You may also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es">www.aepd.es</a>) or your local authority.</p>
<h2>7. Changes</h2>
<p>If we change this policy, we will publish the new version on this page with its date.</p>''',
'fr': '''<h1>Politique de confidentialité</h1>
<p class="updated">{u}</p>
<div class="box"><p>Cette politique s'applique aux applis de <strong>MJCStudio</strong> sur Google Play et l'App Store : <strong>Rondalia</strong> et <strong>Lexpedition</strong>. En bref : <strong>nous ne collectons aucune donnée personnelle</strong>, nous n'affichons pas de publicité et n'utilisons aucun outil de suivi.</p></div>
<h2>1. Responsable</h2>
<p>MJCStudio, développeur indépendant basé en Espagne. Contact : <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>
<h2>2. Données traitées</h2>
<ul>
<li><strong>Aucune sur nos serveurs.</strong> Les applis n'ont ni compte ni inscription et n'envoient aucune information à MJCStudio ni à des tiers.</li>
<li><strong>Données enregistrées uniquement sur ton appareil :</strong> les noms ou pseudos saisis pour les joueurs ou profils (et, si tu l'indiques, leur année de naissance pour adapter la difficulté), les scores, la progression, les réglages (langue, thème, son) et le déblocage éventuel de la version complète. Ils restent dans le stockage local de l'appli et ne quittent jamais ton téléphone ou ta tablette. Tu peux les effacer depuis les réglages de l'appli ou en la désinstallant.</li>
<li><strong>Ni publicité, ni statistiques, ni suivi.</strong> Pas de cookies, d'identifiants publicitaires ni de services d'analyse. Le seul composant tiers est le système d'achat de la boutique (Google Play Billing ou StoreKit d'Apple).</li>
<li><strong>Autorisations :</strong> les applis ne demandent pas l'accès à l'appareil photo, au micro, à la localisation, aux contacts ni aux photos.</li>
</ul>
<h2>3. Achats</h2>
<p>Les achats intégrés (achat unique pour débloquer tout le contenu) sont gérés par <strong>Google Play</strong> ou l'<strong>App Store d'Apple</strong>. MJCStudio ne reçoit jamais tes données de paiement ; la boutique indique seulement à l'appli que l'achat existe afin de débloquer le contenu. Consulte aussi la politique de confidentialité de Google ou d'Apple.</p>
<h2>4. Si tu nous écris</h2>
<p>Avec « Écris-nous » ou « Envoyer un avis », ton appli de messagerie s'ouvre avec un message pouvant contenir la version de l'appli, la langue et le modèle de l'appareil, pour nous aider à résoudre le problème. Tu choisis de l'envoyer ou non. Nous utilisons ton adresse e-mail et ton message uniquement pour te répondre et les supprimons quand ils ne sont plus nécessaires, ou avant si tu le demandes.</p>
<h2>5. Enfants</h2>
<p>Les applis conviennent aux enfants. Nous ne collectons aucune donnée sur les enfants. Les liens externes (e-mail, page de la boutique) et les achats sont protégés par une question réservée aux adultes.</p>
<h2>6. Tes droits</h2>
<p>Comme nous ne conservons aucune donnée te concernant, il n'y a en général rien à consulter ni à effacer de notre côté. Si tu nous as écrit, tu peux demander l'accès à cet e-mail ou sa suppression à <a href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>. Tu peux aussi saisir l'autorité espagnole de protection des données (<a href="https://www.aepd.es">www.aepd.es</a>) ou la CNIL.</p>
<h2>7. Modifications</h2>
<p>Si nous modifions cette politique, nous publierons la nouvelle version sur cette page avec sa date.</p>''',
'de': '''<h1>Datenschutzerklärung</h1>
<p class="updated">{u}</p>
<div class="box"><p>Diese Erklärung gilt für die Apps von <strong>MJCStudio</strong> bei Google Play und im App Store: <strong>Rondalia</strong> und <strong>Lexpedition</strong>. Kurz gesagt: <strong>Wir erheben keine personenbezogenen Daten</strong>, zeigen keine Werbung und nutzen keine Tracking-Tools.</p></div>
<h2>1. Verantwortlicher</h2>
<p>MJCStudio, unabhängiger Entwickler mit Sitz in Spanien. Kontakt: <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a>.</p>
<h2>2. Welche Daten verarbeitet werden</h2>
<ul>
<li><strong>Keine auf unseren Servern.</strong> Die Apps haben kein Konto und keine Anmeldung und senden keine Informationen an MJCStudio oder Dritte.</li>
<li><strong>Nur auf deinem Gerät gespeicherte Daten:</strong> die Namen oder Spitznamen, die du für Spieler oder Profile eingibst (und, falls angegeben, ihr Geburtsjahr für den Schwierigkeitsgrad), Punkte, Fortschritt, Einstellungen (Sprache, Design, Ton) und ob du die Vollversion freigeschaltet hast. Sie liegen im lokalen Speicher der App und verlassen dein Handy oder Tablet nie. Du kannst sie in den Einstellungen der App oder durch Deinstallieren löschen.</li>
<li><strong>Keine Werbung, keine Analyse und kein Tracking.</strong> Keine Cookies, keine Werbe-IDs und keine Statistikdienste. Einziger Drittanbieter-Baustein ist das Kaufsystem des Stores (Google Play Billing oder StoreKit von Apple).</li>
<li><strong>Berechtigungen:</strong> Die Apps fragen nicht nach Zugriff auf Kamera, Mikrofon, Standort, Kontakte oder Fotos.</li>
</ul>
<h2>3. Käufe</h2>
<p>In-App-Käufe (ein Einmalkauf zum Freischalten aller Inhalte) werden von <strong>Google Play</strong> oder dem <strong>App Store von Apple</strong> abgewickelt. MJCStudio erhält niemals deine Zahlungsdaten; der Store teilt der App nur mit, dass der Kauf besteht, damit die Inhalte freigeschaltet werden. Bitte beachte auch die Datenschutzerklärung von Google bzw. Apple.</p>
<h2>4. Wenn du uns schreibst</h2>
<p>Über „Schreib uns“ oder „Feedback senden“ öffnet sich deine E-Mail-App mit einer Nachricht, die App-Version, Sprache und Gerätemodell enthalten kann, damit wir das Problem lösen können. Du entscheidest, ob du sie sendest. Deine E-Mail-Adresse und Nachricht nutzen wir nur für die Antwort und löschen sie, wenn sie nicht mehr gebraucht werden, oder früher auf Wunsch.</p>
<h2>5. Kinder</h2>
<p>Die Apps sind für Kinder geeignet. Wir erheben keine Daten von Kindern. Externe Links (E-Mail, Store-Seite) und Käufe sind durch eine Frage für Erwachsene geschützt.</p>
<h2>6. Deine Rechte</h2>
<p>Da wir keine Daten über dich speichern, gibt es bei uns normalerweise nichts einzusehen oder zu löschen. Wenn du uns geschrieben hast, kannst du Auskunft über diese E-Mail oder ihre Löschung unter <a href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a> verlangen. Du kannst dich auch bei der spanischen Datenschutzbehörde (<a href="https://www.aepd.es">www.aepd.es</a>) oder deiner örtlichen Aufsichtsbehörde beschweren.</p>
<h2>7. Änderungen</h2>
<p>Wenn wir diese Erklärung ändern, veröffentlichen wir die neue Fassung mit Datum auf dieser Seite.</p>'''}
priv = {l: v.replace('{u}', UPDATED[l]) for l, v in priv.items()}

# ---------- SOPORTE ----------
sup = {
'es': '''<h1>Soporte</h1>
<p class="lead">¿Algo no funciona, tienes una idea o quieres avisarnos de una pregunta con un error? Escríbenos y te respondemos lo antes posible.</p>
<div class="box">
<p>General: <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a><br>
Rondalia: <a class="mail" href="mailto:rondalia@mjcstudio.com">rondalia@mjcstudio.com</a><br>
Lexpedition: <a class="mail" href="mailto:lexpedition@mjcstudio.com">lexpedition@mjcstudio.com</a></p>
<p>Si puedes, indica la app, su versión (está en Ajustes › Acerca de) y el modelo de tu móvil.</p></div>
<h2>Preguntas frecuentes</h2>
<p><strong>He cambiado de móvil, ¿cómo recupero la compra?</strong><br>Entra en Ajustes de la app y pulsa «Restaurar compra» con la misma cuenta de Google o Apple con la que compraste.</p>
<p><strong>¿Cómo cambio el idioma?</strong><br>En Ajustes › Idioma. La primera vez la app usa el idioma de tu móvil.</p>
<p><strong>¿Cómo borro mis datos?</strong><br>Todo se guarda solo en tu dispositivo. Puedes borrarlo desde los ajustes de la app o desinstalándola. Más detalles en la <a href="../privacidad/">política de privacidad</a>.</p>
<p><strong>¿Necesito internet?</strong><br>No para jugar o estudiar. Solo para comprar o restaurar la compra.</p>''',
'en': '''<h1>Support</h1>
<p class="lead">Something not working, an idea, or a question with a mistake? Write to us and we'll reply as soon as we can.</p>
<div class="box">
<p>General: <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a><br>
Rondalia: <a class="mail" href="mailto:rondalia@mjcstudio.com">rondalia@mjcstudio.com</a><br>
Lexpedition: <a class="mail" href="mailto:lexpedition@mjcstudio.com">lexpedition@mjcstudio.com</a></p>
<p>If you can, tell us the app, its version (in Settings › About) and your device model.</p></div>
<h2>FAQ</h2>
<p><strong>I changed phones. How do I get my purchase back?</strong><br>Open the app's Settings and tap "Restore purchase" with the same Google or Apple account you used to buy.</p>
<p><strong>How do I change the language?</strong><br>In Settings › Language. The first time, the app uses your phone's language.</p>
<p><strong>How do I delete my data?</strong><br>Everything is stored only on your device. You can delete it from the app settings or by uninstalling the app. More in the <a href="../privacidad/">privacy policy</a>.</p>
<p><strong>Do I need internet?</strong><br>Not to play or study. Only to buy or restore the purchase.</p>''',
'fr': '''<h1>Assistance</h1>
<p class="lead">Un souci, une idée ou une question avec une erreur ? Écris-nous, nous répondons dès que possible.</p>
<div class="box">
<p>Général : <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a><br>
Rondalia : <a class="mail" href="mailto:rondalia@mjcstudio.com">rondalia@mjcstudio.com</a><br>
Lexpedition : <a class="mail" href="mailto:lexpedition@mjcstudio.com">lexpedition@mjcstudio.com</a></p>
<p>Si possible, indique l'appli, sa version (dans Réglages › À propos) et le modèle de ton appareil.</p></div>
<h2>Questions fréquentes</h2>
<p><strong>J'ai changé de téléphone, comment récupérer mon achat ?</strong><br>Ouvre les Réglages de l'appli et touche « Restaurer l'achat » avec le même compte Google ou Apple que lors de l'achat.</p>
<p><strong>Comment changer la langue ?</strong><br>Dans Réglages › Langue. La première fois, l'appli utilise la langue de ton téléphone.</p>
<p><strong>Comment effacer mes données ?</strong><br>Tout est enregistré uniquement sur ton appareil. Tu peux l'effacer depuis les réglages de l'appli ou en la désinstallant. Plus d'infos dans la <a href="../privacidad/">politique de confidentialité</a>.</p>
<p><strong>Faut-il internet ?</strong><br>Non pour jouer ou étudier. Seulement pour acheter ou restaurer l'achat.</p>''',
'de': '''<h1>Support</h1>
<p class="lead">Etwas funktioniert nicht, du hast eine Idee oder einen Fehler in einer Frage gefunden? Schreib uns, wir antworten so schnell wie möglich.</p>
<div class="box">
<p>Allgemein: <a class="mail" href="mailto:soporte@mjcstudio.com">soporte@mjcstudio.com</a><br>
Rondalia: <a class="mail" href="mailto:rondalia@mjcstudio.com">rondalia@mjcstudio.com</a><br>
Lexpedition: <a class="mail" href="mailto:lexpedition@mjcstudio.com">lexpedition@mjcstudio.com</a></p>
<p>Wenn möglich, nenne die App, ihre Version (unter Einstellungen › Über) und dein Gerätemodell.</p></div>
<h2>Häufige Fragen</h2>
<p><strong>Ich habe ein neues Handy. Wie bekomme ich meinen Kauf zurück?</strong><br>Öffne die Einstellungen der App und tippe auf „Kauf wiederherstellen“, mit demselben Google- oder Apple-Konto wie beim Kauf.</p>
<p><strong>Wie ändere ich die Sprache?</strong><br>Unter Einstellungen › Sprache. Beim ersten Start nutzt die App die Sprache deines Handys.</p>
<p><strong>Wie lösche ich meine Daten?</strong><br>Alles wird nur auf deinem Gerät gespeichert. Du kannst es in den Einstellungen der App oder durch Deinstallieren löschen. Mehr dazu in der <a href="../privacidad/">Datenschutzerklärung</a>.</p>
<p><strong>Brauche ich Internet?</strong><br>Nicht zum Spielen oder Lernen. Nur zum Kaufen oder Wiederherstellen.</p>'''}

import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from home_mk import home
for key, root, content, path in [('home', './', home, 'index.html'), ('priv', '../', priv, 'privacidad/index.html'),
                                 ('sup', '../', sup, 'soporte/index.html')]:
    body = L({l: content[l].replace('src="img/', f'src="{root}img/') for l in LANGS})
    open(os.path.join(OUT, path), 'w', encoding='utf-8').write(page(key, root, body))
print('ok')
