# mspaint

[![test](https://github.com/enveda/mspaint/actions/workflows/test.yml/badge.svg)](https://github.com/enveda/mspaint/actions/workflows/test.yml)

> multi-engine painting of Mass Spec data

[Example notebook](./notebooks/example.ipynb)

## Development

#### Setup
```shell
git clone https://github.com/enveda/mspaint.git
poetry install --with dev,test
poetry run pre-commit install
```

#### Contribution

```shell
git checkout -b <relevant-sounding-branch-name>
# make meaningful contributions
poetry run pytest
# open a PR
```
