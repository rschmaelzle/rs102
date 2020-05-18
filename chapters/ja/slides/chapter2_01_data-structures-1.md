---
type: slides
---

# データ構造(1): VocabとLexemesとStringStore

Notes: Welcome back！さて、いくつかのspaCyのオブジェクトを扱ってみたので、
そろそろspaCyが実際に裏側で何をしているかを学んでいきましょう。

---

# 共有語彙データと文字列ストア (1)

- `Vocab`: 複数のdocに共有されるデータを保存
- メモリを節約するために、spaCyは全ての文字列を**ハッシュ値**に変換しています
- 文字列は一度だけ、`nlp.vocab.strings`を通して`StringStore`に保存されます
- String store: 双方向ルックアップテーブル

```python
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]
```

- ハッシュ値は復号できません。これが、共有語彙データクラスをつかう理由です。

```python
# 対応する文字列をみたことがない場合、エラーとなります
string = nlp.vocab.strings[3197928453018144401]
```

Notes: spaCyは全てのデータをVocabという語彙データベースに保存しています。

これには単語や、タグや固有表現に使われるラベルが含まれます。

メモリを節約するために、全ての文字列はハッシュIDにエンコードされます。
単語が複数回現れた時でも、毎回は保存しません。

代わりに、spaCyはハッシュ関数を使用してIDを生成し、文字列を一度だけ文字列ストアに保存します。
文字列ストアは`nlp.vocab.strings`から使うことができます。

これは双方向のルックアップテーブルです。文字列からハッシュ値を得ることも、その逆も可能です。
内部的には、spaCyはハッシュIDのみを用いてデータのやり取りをしています。

ハッシュIDは直接は復号できません。もし単語が語彙データに含まれていなければ、文字列を復元できません。
ですから、共有語彙データが必要なのです。

---

# 共有語彙データと文字列ストア (2)

- `nlp.vocab.strings`で文字列をハッシュをルックアップしてみます

```python
doc = nlp("I love coffee")
print("hash value:", nlp.vocab.strings["coffee"])
print("string value:", nlp.vocab.strings[3197928453018144401])
```

```out
hash value: 3197928453018144401
string value: coffee
```

- `doc`からも語彙データと文字列ストアにアクセスできます

```python
doc = nlp("I love coffee")
print("hash value:", doc.vocab.strings["coffee"])
```

```out
hash value: 3197928453018144401
```

Notes: 文字列のハッシュを得るためには、`nlp.vocab.strings`をルックアップします。

ハッシュから文字列を得る際は、ハッシュ値をルックアップします。

`Doc`オブジェクトからも語彙データと文字列ストアにアクセスできます。

---

# Lexemes: 語彙素

- `Lexeme`オブジェクトは語彙データの要素（語彙素）

```python
doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]

# 語彙属性をプリント
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
```

```out
coffee 3197928453018144401 True
```

- 単語についての**文脈に依存しない**情報を保存
  - 単語の文字列: `lexeme.text`と`lexeme.orth`(ハッシュ値)
  - `lexeme.is_alpha`等の語彙属性
  - 文脈に依存する品詞タグ、依存関係ラベル、固有表現ラベルは**保持していない**

Notes: Lexemeは文脈に依存しない語彙データベースの要素（語彙素）です。

語彙素は、vocabオブジェクトから文字列やハッシュIDで取得できます。

語彙素もトークンのように、いくつかの属性を提供しています。

語彙素は、単語に関する文脈に依存しない情報を持っています。
たとえば、単語の文字列や、それらがアルファベットのみで構成されているかどうか、などです。

語彙素は、品詞タグや依存関係や固有表現のラベル等、文脈に依存するデータは保持していません。

---

# Vocabとハッシュ値と語彙素

<img src="/vocab_stringstore.png" width="70%" alt="Doc、Vocab、StringStoreにおける'I'と'love'と'coffee'の図解" />

Notes: 一例を示します。

`Doc`は文脈とともに単語を持っています。ここでは、「I」と「love」と「coffee」を品詞タグと依存関係ラベルとともに持っています。

それぞれのトークンは、単語のハッシュ値を持つ語彙素を参照しています。
ハッシュ値から文字列を得るために、spaCyは文字列ストアを用います。

---

# Let's practice!

Notes: ここで紹介したことはどれも抽象的かもしれません。なので、実際に語彙データと文字列ストアを演習でみていきましょう。
