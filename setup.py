from setuptools import setup
from Cython.Build import cythonize
import numpy

packages=['sentence2vec']

setup(
    name = "sentence2vec",
    version = 1.0,
    author = "klb3713",
    author_email = "klbgyx7@gmail.com",
    url = "http://klb3713",
    install_requires = ["scipy", "six", "gensim"],
    include_dirs = [numpy.get_include(), "sentence2vec"],
    ext_modules = cythonize("word2vec_inner.pyx"),
    packages = packages
)
