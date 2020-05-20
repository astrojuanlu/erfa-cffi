import pytest

from erfa_cffi import eraEpb


def test_epb():
    # https://github.com/liberfa/erfa/blob/a3a02dc8e05f9e53ae49f1c6deb6cf16b15b7ab5/src/t_erfa_c.c#L3323-L3346
    epb = eraEpb(2415019.8135, 30103.18648)

    assert epb == pytest.approx(1982.418424159278580, abs=1e-12)
