[![Python Package](https://github.com/SermetPekin/nameisok/actions/workflows/python-package.yml/badge.svg?2)](https://github.com/SermetPekin/nameisok/actions/workflows/python-package.yml)[![PyPI](https://img.shields.io/pypi/v/nameisok)](https://img.shields.io/pypi/v/nameisok) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/nameisok)](https://pypi.org/project/nameisok/?2) ![PyPI Downloads](https://static.pepy.tech/badge/nameisok/?2)

nameisok is a Python package that helps developers check the availability of package names on PyPI, taking it one step further with enhanced functionality. This tool is perfect for anyone looking to publish new packages and wanting to avoid name conflicts or similar names that could cause confusion.
Key Features

- PyPI Availability Check: Quickly checks PyPI to see if a package name is available for registration.
- BigQuery Database Check: Uses the PyPI dataset on Google BigQuery for additional verification of package name availability.
- Similarity Check: Detects names that are too similar to existing packages, based on a customizable similarity threshold, preventing potential naming conflicts.

Installation

To install nameisok, simply run:


```bash
pip install nameisok
```

Check Multiple Names
```bash
nameisok example,my_package,nameisok


```
Output 

```plaintext
❌ `example` is already taken.
🎉 Wow! `my_package` is available!
❌ `nameisok` is already taken.

```

### Check a Single Name

You can also check just one name at a time:

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

### Similarity Warnings

When a name is not only taken but also too similar to existing packages, you'll see a warning:

```bash
nameisok numpyyy
```


```plaintext
⚠️ `numpyyy` is very similar to `numpy`, `numpy-extensions`
❌ `numpyyy` is too similar to an existing package.
```
