#! /bin/python

from setuptools import setup, find_packages

setup (
    name="pytchatty",
    packages=find_packages(),
    install_requires=[
        "pytchat",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "pytchatty = pytchatty.main:main"
        ]
    },
    description="just a chat implementation of pytchat library",
    url="https://github.com/rodrigo-sys/pytchatty",
)
