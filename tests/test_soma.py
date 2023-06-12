from src.main import soma


def test_soma():
    assert 4 == soma(2, 2)


def test_soma_falha():
    assert 2 == soma(1, 1)
