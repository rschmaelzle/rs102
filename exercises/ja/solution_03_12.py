import json
from spacy.lang.en import English
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/en/capitals.json") as f:
    CAPITALS = json.loads(f.read())

nlp = English()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # すべてのマッチ結果に対して、「GPE」ラベルが付いたスパンを作成しましょう
    matches = matcher(doc)
    doc.ents = [Span(doc, start, end, label="GPE") for match_id, start, end in matches]
    return doc


# パイプラインにコンポーネントを追加しましょう
nlp.add_pipe(countries_component)
print(nlp.pipe_names)

# 国の首都名が入った辞書をスパンのテキストで引くゲッター
get_capital = lambda span: CAPITALS.get(span.text)

# get_capitalをスパンの拡張属性「capital」に登録
Span.set_extension("capital", getter=get_capital)

# テキストを処理し、固有表現テキスト、ラベル、capital属性をプリント
doc = nlp("Czech Republic may help Slovakia protect its airspace")
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])
