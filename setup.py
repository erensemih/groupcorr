from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='groupcorr',
    version='0.1.0',
    url="https://github.com/erensemih/groupcorr",
    author="Semih Eren",
    author_email="19semiheren97@gmail.com",
    description="Correlation Importance Among Different Groups",
    keywords="feature importance selection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)