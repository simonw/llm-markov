from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="llm-markov",
    description="Plugin for LLM adding a Markov chain generating model",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/llm-markov",
    project_urls={
        "Issues": "https://github.com/simonw/llm-markov/issues",
        "CI": "https://github.com/simonw/llm-markov/actions",
        "Changelog": "https://github.com/simonw/llm-markov/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=["License :: OSI Approved :: Apache Software License"],
    version=VERSION,
    packages=["llm_markov"],
    entry_points={"llm": ["llm_markov = llm_markov"]},
    install_requires=["llm>=0.5"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
