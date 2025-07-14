from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('sosthene') == 'ssthn'
    assert shorten('car') == 'cr'
    assert shorten('POPE') == 'PP'
    assert shorten('Gender') == 'Gndr'

if __name__ == "__main__":
    main()