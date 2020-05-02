

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("gene.py"),
    extra_compile_args=["-O3"] 
)

