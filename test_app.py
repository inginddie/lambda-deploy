from app import es_primo

def test_es_primo():
    assert es_primo(3) is True
    assert es_primo(4) is False
    assert es_primo(14) is False
    assert es_primo(90) is False