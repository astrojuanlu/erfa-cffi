from setuptools import setup

setup(
    cffi_modules=["src/_cffi_build/build_wrapper.py:ffi"],
)
