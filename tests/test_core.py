def test_import():
    import importlib
    m = importlib.import_module("causal_sentiment_engine")
    assert m is not None
