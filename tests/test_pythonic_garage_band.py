from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Guitarist, Bassist, Drummer


def test_version():
    assert __version__ == '0.1.0'


def test_guitarist_str():
    actual = Guitarist('guitarist', 'guitar').__str__()
    expected = 'I am a guitarist'
    assert actual == expected


def test_bassist_repl():
    actual = Bassist('bassist', 'bass').__repr__()
    expected = 'bassist'
    assert actual == expected


def test_play_solo():
    actual = Drummer('drummer', 'drumm').play_solo()
    expected = 'drummer is playing solo on the drumm'
    assert actual == expected
