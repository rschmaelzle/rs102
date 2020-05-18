def test():
    assert Span.has_extension("wikipedia_url"), "スパンに拡張属性を登録しましたか？"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "ゲッターを登録しましたか？"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "get_wikipedia_urlをゲッターとして登録しましたか？"
    assert "(ent.text, ent._.wikipedia_url)" in __solution__, "カスタム属性にアクセスしましたか？"
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://en.wikipedia.org/w/index.php?search=David_Bowie"
    ), "ゲッター属性の値が誤っているようです"

    __msg__.good(
        "Nice！モデルによって予測された固有表現を使って、Wikipedia URLを生成し、カスタム属性に追加するコンポーネントを作成しました。"
        "リンクを開いたらどうなるか、試して見ましょう！"
    )
