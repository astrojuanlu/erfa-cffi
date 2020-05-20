from cffi import FFI

ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef(
    """
    double eraEpb(double dj1, double dj2);
"""
)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source(
    "_erfa_cffi",
    """
    #include "erfa.h"
""",
    libraries=["erfa"],
)  # library name, for the linker


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
