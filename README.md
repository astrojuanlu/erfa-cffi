# CFFI wrapper for ERFA

## Proof of concept

```bash
$ C_INCLUDE_PATH=$(pwd)/../erfa/src/ LIBRARY_PATH=$(pwd)/../erfa/src/.libs/ pip install -e .
$ LD_LIBRARY_PATH=$(pwd)/../erfa/src/.libs/ python -c "from erfa_cffi import eraEpb; print(eraEpb(2415019.8135, 30103.18648))"
```

To run the tests:

```bash
$ LD_LIBRARY_PATH=$(pwd)/../erfa/src/.libs/ pytest
```

## Informal benchmarks

Preliminary benchmarks show identical running time than Astropy,
with the advantage that erfa_cffi can be used inside numba functions:

```
In [1]: from erfa_cffi.fast import eraEpb as eraEpb_scalar, eraEpb_v

In [2]: import numpy as np

In [3]: dj1 = np.full(10, 2415019.8135)

In [4]: dj2 = 30103.18648

In [5]: eraEpb_v(dj1, dj2)
Out[5]: 
array([1982.41842416, 1982.41842416, 1982.41842416, 1982.41842416,
       1982.41842416, 1982.41842416, 1982.41842416, 1982.41842416,
       1982.41842416, 1982.41842416])

In [6]: %timeit eraEpb_v(dj1, dj2)
822 ns ± 57.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [7]: from astropy._erfa import epb

In [8]: epb(dj1, dj2)
Out[8]: 
array([1982.41842416, 1982.41842416, 1982.41842416, 1982.41842416,
       1982.41842416, 1982.41842416, 1982.41842416, 1982.41842416,
       1982.41842416, 1982.41842416])

In [9]: %timeit epb(dj1, dj2)
817 ns ± 21.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

```
