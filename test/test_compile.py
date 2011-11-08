


def test_compile():
    try:
        import tiddlywebplugins.jsonp
        assert True
    except ImportError, exc:
        assert False, exc
