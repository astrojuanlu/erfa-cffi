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
