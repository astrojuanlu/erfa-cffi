from numba import njit
from numba.core.typing.cffi_utils import register_module

import _erfa_cffi

from .api import eraEpb as _eraEpb

register_module(_erfa_cffi)


@njit
def eraEpb(dj1, dj2):
    return _eraEpb(dj1, dj2)
