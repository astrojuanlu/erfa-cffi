import os

from cffi import FFI

FFI_BUILDER_PATH = os.path.dirname(os.path.abspath(__file__))
ERFA_SRC = os.path.relpath(os.path.join(FFI_BUILDER_PATH, os.pardir, os.pardir, "liberfa", "src"))

# get all of the .c files in the liberfa/erfa/src directory
# https://github.com/liberfa/pyerfa/blob/master/setup.py
erfafns = os.listdir(ERFA_SRC)
sources = []
sources.extend([os.path.join(ERFA_SRC, fn)
                for fn in erfafns
                if fn.endswith('.c') and not fn.startswith('t_')])

ffi = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffi.cdef(
    """
    double eraEpb(double dj1, double dj2);
"""
)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffi.set_source(
    "_erfa_cffi",
    """
    #include "erfa.h"
""",
    sources=sources,
    include_dirs=[ERFA_SRC],
    # libraries=["erfa"],  # Only if liberfa is externally available
    libraries=[],
)


if __name__ == "__main__":
    ffi.compile(verbose=True)
