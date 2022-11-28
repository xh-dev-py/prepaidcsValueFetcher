from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='prepaidcsValueFetcher',
    version='0.0.1',
    description='prepaidcs value fetcher',
    py_modules=['prepaidcsValueFetcher'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xh-dev-py/prepaidcsValueFetcher",
    author="xethhung",
    author_email="pypi@xethh.dev",
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    }
)