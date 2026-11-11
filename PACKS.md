# Packs de Rondalia (descargables)

Carpeta `docs/packs/`: la app la lee desde `https://mjcstudio.com/packs/`. Solo contiene **datos** (JSON con textos y colores): nunca código.
Estrategia y reglas de contenido: documento `PACKS-Rondalia.md` del proyecto.

## Ficheros

- `catalog.json`: la lista de packs. La app la pide al abrir la pestaña Packs (como mucho cada 12 h).
- `<id>/<idioma>.json`: el contenido de un pack en un idioma (`es`, `en`, `fr`, `de`, `pt`).

## catalog.json

```json
{
 "v": 1,
 "places": { "es-an": { "es": "Andalucía", "en": "Andalusia", "fr": "Andalousie", "de": "Andalusien", "pt": "Andaluzia" } },
 "packs": [ {
   "id": "andalucia",            // minúsculas, números y guiones; 2-40 caracteres; no se cambia nunca
   "ver": 1,                     // subir al corregir el contenido
   "ico": "💃",                  // un emoji
   "theme": "lugares",           // fiestas | historia | personajes | lengua | cocina | deportes | arte | lugares | otros
   "place": ["eu", "es", "es-an"], // de lo más amplio a lo más concreto; ["world"] si es de todo el mundo
   "langs": ["es"],              // idiomas en los que existe <id>/<idioma>.json
   "free": true,                 // la app solo muestra los gratis
   "season": ["12-01", "01-06"], // opcional: mes-día de inicio y fin
   "n": { "trivia": 24, "tabu": 10, "mimica": 8 },
   "kb": 6,                      // tamaño aproximado del fichero
   "name": { "es": "Andalucía", "en": "Andalusia" },
   "desc": { "es": "De la Alhambra a Doñana…" },
   "skin": {                     // opcional: solo estos 8 colores, en hexadecimal de 6 cifras
     "light": { "--accent": "#B3261E", "--bg": "#FBF6EC", "--soft": "#F3E7D3" },
     "dark":  { "--accent": "#FF8A5B", "--bg": "#1F1712", "--surface": "#2B211A" }
   }
 } ]
}
```

Colores admitidos en `skin`: `--bg`, `--surface`, `--ink`, `--muted`, `--line`, `--track`, `--soft`, `--accent`. Comprobar el contraste AA (4,5:1) del texto sobre el fondo y del blanco sobre el acento, en claro y en oscuro.

## <id>/<idioma>.json

```json
{
 "id": "andalucia", "v": 1, "lang": "es",
 "trivia": [ { "cat": "geo", "lv": 1, "p": "¿Cuál es la capital de Andalucía?", "r": "Sevilla" } ],
 "tabu":   [ { "lv": 1, "w": "Flamenco", "f": ["baile", "guitarra", "palmas", "cante"] } ],
 "mimica": [ { "lv": 1, "cat": "Acción", "t": "bailar sevillanas" } ]
}
```

- `cat` de trivia: `geo`, `ent`, `his`, `art`, `cie`, `dep` (las seis categorías de Preguntas). Repartir entre varias.
- `lv`: 1 (5-7 años), 2 (8-11), 3 (12-15), 4 (16 o más). Intentar que haya de todos los niveles.
- `tabu`: de 3 a 5 palabras prohibidas. Las palabras de una sola palabra y de 4 a 12 letras sirven también para Adivina la palabra.
- Límites que aplica la app: pregunta 300 caracteres, respuesta 160, palabra 40, mímica 80; fichero de 800 KB como máximo.

## Publicar un pack

1. Crear `<id>/<idioma>.json` y añadir el pack a `catalog.json`.
2. Comprobar que los dos ficheros son JSON válido y que `n` coincide con lo que hay.
3. Subir a `main`: GitHub Pages lo publica y la app lo ve sin versión nueva.

`andalucia` es un **borrador de ejemplo** (24 preguntas, 10 palabras, 8 mímicas): revisar el contenido antes de publicarlo.
