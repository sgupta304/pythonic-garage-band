import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.band import Band
from pythonic_garage_band.members.musician import Musician
from pythonic_garage_band.members.drummer import Drummer
from pythonic_garage_band.members.guitarist import Guitarist
from pythonic_garage_band.members.bassist import Bassist


@pytest.fixture
def rand_band():
    nirvana = Band("Nirvana")
    nirvana.add_band_member([Guitarist("Curt Kobain", "kobain's solo"),
                             Drummer("Dave Grohl", "Grohl's solo"),
                             Bassist("Kris Novoselic", "Kris's solo")])
    return nirvana


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize(
    "musician, musician_name, musician_instrument, musician_solo", [
        (Drummer("Tony", "cats"), "Tony", "drums", "I'm the Drummer, and I'm going to sing cats"),
        (Guitarist("Tony", "cats"), "Tony", "guitar", "I'm the Guitarist, and I'm going to sing cats"),
        (Bassist("Tony", "cats"), "Tony", "base", "I'm the Bassist, and I'm going to sing cats")
    ]
)
def test_drummer_name(musician, musician_name, musician_instrument, musician_solo):
    assert musician.musician_name == musician_name
    assert musician.instrument == musician_instrument
    assert musician.play_solo() == musician_solo


def test_band_str_repr_band_solos(rand_band):
    actual_len = len([Band.to_list()])
    actual = rand_band.play_solos()
    expected = "I'm the Guitarist, and I'm going to sing kobain's solo, I'm the Drummer, and I'm going to sing " \
               "Grohl's solo, I'm the Bassist, and I'm going to sing Kris's solo, "
    assert repr(rand_band) == "Band with Band instance."
    assert str(rand_band) == "We are Band, and our name is Nirvana."
    assert actual == expected
    assert actual_len == 1


def test_abstract_musician():
    with pytest.raises(TypeError):
        Musician(None, None, None)
