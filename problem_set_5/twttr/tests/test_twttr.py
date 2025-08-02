import pytest
from twttr import shorten

def test_shorten_up():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('SOSTHENE') == 'SSTHN'
    assert shorten('CARA') == 'CR'
    assert shorten('POPE') == 'PP'
    assert shorten('GENDER') == 'GNDR'


def test_shorten_lw():
    assert shorten('twitter') == 'twttr'
    assert shorten('sosthene') == 'ssthn'
    assert shorten('car') == 'cr'
    assert shorten('pope') == 'pp'
    assert shorten('gender') == 'gndr'

def test_shorten_pn():
    assert shorten('hello, name') == 'hll, nm'
    assert shorten('hello, name, surname') == 'hll, nm, srnm'
    assert shorten('who?') == 'wh?'
    assert shorten("CS50's 1st problem") == "CS50's 1st prblm"
    assert shorten('!,.?') == '!,.?'

def test_shorten_num():
    with pytest.raises(TypeError):
        shorten(123)
    with pytest.raises(TypeError):
        shorten(1.23)
    with pytest.raises(TypeError):
        shorten(0)