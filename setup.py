#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["fire"]

test_requirements = ["pytest", "tox"]
dev_requirements = [
    "pip",
    "bumpversion",
    "flake8",
    "tox",
    "coverage",
    "Sphinx",
] + test_requirements

setup(
    author="Tomer Keren",
    author_email="tomer.keren.dev@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Like str.split, but for video",
    entry_points={"console_scripts": ["vid_split=vid_split.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="vid_split",
    name="vid_split",
    packages=find_packages(include=["vid_split"], exclude=["tests"]),
    extras_require={
        "test": test_requirements,
        "dev": test_requirements + ["pre-commit"],
    },
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Tadaboody/vid_split",
    version="0.1.0",
    zip_safe=False,
)
