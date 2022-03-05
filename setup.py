#!/usr/bin/python3

from distutils.core import setup

setup(
    name="solarmax-smt",
    version="0.1",
    description="ibrary/CLI app to display some solarmax-smt data",
    author="Michael Vogt",
    author_email="michael.vogt@gmail.com",
    url="https://github.com/mvo5/solarmax-smt",
    py_modules=["smaxsmt"],
    scripts=["solarmax-smt"],
)
