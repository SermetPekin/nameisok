[![Python Package](https://github.com/SermetPekin/nameisok/actions/workflows/python-package.yml/badge.svg)](https://github.com/SermetPekin/nameisok/actions/workflows/python-package.yml)[![PyPI](https://img.shields.io/pypi/v/nameisok)](https://img.shields.io/pypi/v/nameisok) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/nameisok)](https://pypi.org/project/nameisok/) 

# nameisok

**nameisok** is a Python package that checks the availability of package names on PyPI. This tool is especially useful for developers looking to publish new packages and wanting to ensure their desired name is unique.

## Installation

To install **nameisok**, simply run:

```bash
pip install nameisok
```


```bash
nameisok example,my_package,nameisok


```

```plaintext
❌ `example` is already taken.
🎉 Wow! `my_package` is available!
❌ `nameisok` is already taken.

```
```bash
nameisok pandas 
```

```plaintext
  ❌ `pandas` is already taken.

```

```bash
nameisok darling 
```
```plaintext
. 🎉 Wow! `darling` is available!
```




