from numba import njit, vectorize
from numba.core.typing.cffi_utils import register_module
from numba.types import float64

import _erfa_cffi

from .api import eraEpb as _eraEpb

register_module(_erfa_cffi)


@njit
def eraEpb(dj1, dj2):
    return _eraEpb(dj1, dj2)


@vectorize([float64(float64, float64)])
def eraEpb_v(dj1, dj2):
    return _eraEpb(dj1, dj2)
