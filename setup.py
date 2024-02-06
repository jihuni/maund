from setuptools import setup, find_packages
setup(
    name = "MAUND",
    scripts=[
        'bin/maund.py',
    ],
    packages=find_packages(exclude=['bin']),
    install_requires=[
        "pandas==1.3.5",
        "python-Levenshtein",
    ],
    version = "0.5.1",
    description = "Miseq analysis program",
    )


