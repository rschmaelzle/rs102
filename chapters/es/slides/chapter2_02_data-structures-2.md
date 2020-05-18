---
type: slides
---

# Estructuras de datos (2): Doc, Span y Token

Notes: Ahora que lo sabes todo sobre el vocabulario y el string store podemos
estudiar las estructuras de datos más importantes: el `Doc` y sus views el
`Token` y el `Span`.

---

# The Doc object

```python
# Crea un objeto nlp
from spacy.lang.en import English
nlp = English()

# Importa la clase Doc
from spacy.tokens import Doc

# Las palabras y espacios que usaremos para crear el doc
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Crea un doc manualmente
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: El `Doc` es una de las estructuras de datos centrales de spaCy. Es creado
automáticamente cuando procesas un texto con el objeto `nlp`. Pero también
puedes crear un instance manualmente.

Después de crear el objeto `nlp` podemos importar la clase `Doc` desde
`spacy.tokens`.

Aquí estamos creando un doc a partir de tres palabras. Los espacios son una
lista de valores booleanos que indican si una palabra está seguida por un
espacio. Cada token incluye esa información - inclusive el último!

La clase `Doc` recibe tres argumentos: el vocabulario compartido, las palabras y
los espacios.

---

# El objeto Span (1)

<img src="/span_indices.png" width="65%" alt="Illustration of a Span object within a Doc with token indices" />

Notes: Un `Span` es un slice de un Doc que está formado por uno o más tokens. El
`Span` recibe al menos tres argumentos: el doc al que se refiere, el índice de
inicio y el índice del final del span. ¡Recuerda que el índice del final es
excluyente!

---

# El objeto Span (2)

```python
# Importa las clases Doc y Span
from spacy.tokens import Doc, Span

# Las palabras y espacios que usaremos para crear el doc
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Crea un doc manualmente
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Crea un span manualmente
span = Span(doc, 0, 2)

# Crea un span con un label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Añade el span a los doc.ents
doc.ents = [span_with_label]
```

Notes: Para crear un `Span` manualmente también podemos importar la clase desde
`spacy.tokens`. Podemos crear un instance con el doc y los índices de inicio y
final, así como un argumento opcional de label.

Los `doc.ents` son escribibles así que podemos añadir entidades manualmente
sobrescribiendo los con una lista de spans.

---

# Buenas prácticas

- `Doc` y `Span` son muy poderosos y contienen referencias y relaciones de
  palabras y frases
  - **Convertir el resultado a strings lo más tarde posible**
  - **Usar los atributos de los tokens si están disponibles** – por ejemplo,
    `token.i` para el índice del token
- No olvides pasar el `vocab` compartido

Notes: Unos trucos y tips antes de comenzar:

El `Doc` y el `Span` son muy poderosos y optimizados para desempeño. Te dan
acceso a todas las referencias y relaciones de las palabras y las frases.

Si tu aplicación tiene que generar strings asegúrate de que conviertas el doc lo
más tarde posible. Si lo haces demasiado temprano perderás las relaciones entre
los tokens.

Para mantener las cosas consistentes intenta usar los atributos incluidos de los
tokens, siempre que sea posible. Por ejemplo, `token.i` para el índice del
token.

¡Tampoco te olvides de siempre pasar el vocabulario compartido!

---

# ¡Practiquemos!

Notes: Ahora practiquemos esto y creemos algunos docs y spans desde cero.
