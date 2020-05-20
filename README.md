# ERFA CFFI wrapper

## Proof of concept

```bash
$ C_INCLUDE_PATH=$(pwd)/../erfa/src/ LIBRARY_PATH=$(pwd)/../erfa/src/.libs/ python erfa_wrapper.py
$ LD_LIBRARY_PATH=$(pwd)/../erfa/src/.libs/ python -c "from _erfa_cffi import lib; print(lib.eraEpb(2415019.8135, 30103.18648))"
```

To run the tests:

```bash
$ PYTHONPATH=$(pwd) LD_LIBRARY_PATH=$(pwd)/../erfa/src/.libs/ pytest
```
