#!/usr/bin/env python
"""Setup srlinux-pygments."""
from setuptools import setup, find_packages

entry_points = """
[pygments.lexers]
srlinux=srlinux_lexer:SRLinuxLexer
srlinuxmin=srlinux_lexer:SRLinuxLexerMin
"""

setup(
    name="srlinux-pygments",
    version="0.0.1",
    description="Pygments lexer package for SR Linux Network OS configuration files.",
    author="Roman Dodin",
    author_email="dodin.roman@gmail.com",
    url="https://github.com/srl-labs/srlinux-pygments",
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=["Pygments>=2.0.1"],
    zip_safe=True,
    license="MIT License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
)
