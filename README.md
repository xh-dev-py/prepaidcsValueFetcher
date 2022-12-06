# prepaidcs-value-fetcher

## Installation
```shell
pip install prepaidcsValueFetcher -U
```

```shell
pip install git+https://github.com/xh-dev-py/prepaidcsValueFetcher
```

```shell
python -m prepaidcsValueFetcher {mobile_no} {password}
```


## Build
```shell
rm -fr dist
python setup.py sdist bdist_wheel
twine upload dist/*
```