nameisok
========

.. image:: https://github.com/SermetPekin/nameisok/actions/workflows/python-package.yml/badge.svg?2
   :target: https://github.com/SermetPekin/nameisok/actions/workflows/python-package.yml
.. image:: https://img.shields.io/pypi/v/nameisok
   :target: https://pypi.org/project/nameisok/
.. image:: https://static.pepy.tech/badge/nameisok?2

**nameisok** is a Python package designed to help developers check the availability of package names on PyPI, with added features to ensure your package name is unique and avoids potential conflicts. This tool is ideal for developers looking to publish new packages with confidence.

Key Features
------------

- **PyPI Availability Check**: Quickly checks PyPI to see if a package name is available for registration.
- **BigQuery Database Check**: Verifies package name availability using the PyPI dataset on Google BigQuery.
- **Similarity Check**: Detects names that are too similar to existing packages, based on a customizable similarity threshold, to prevent naming conflicts.

Installation
------------

To install `nameisok`, simply run:

.. code-block:: bash

    pip install nameisok

Usage
-----

**Check Multiple Names**

You can check the availability of multiple package names at once:

.. code-block:: bash

    nameisok example,my_package,nameisok

**Sample Output**

.. code-block:: text

    ❌ `example` is already taken.
    🎉 Wow! `my_package` is available!
    ❌ `nameisok` is already taken.

**Check a Single Name**

To check the availability of a single package name:

.. code-block:: bash

    nameisok pandas

**Sample Output**

.. code-block:: text

    ❌ `pandas` is already taken.

For an available name:

.. code-block:: bash

    nameisok darling

.. code-block:: text

    🎉 Wow! `darling` is available!

**Similarity Warnings**

When a name is taken and similar to existing packages, a warning is displayed:

.. code-block:: bash

    nameisok numpyyy

**Sample Output**

.. code-block:: text

    ⚠️ `numpyyy` is very similar to `numpy`, `numpy-extensions`
    ❌ `numpyyy` is too similar to an existing package.

License
-------

This project is licensed under the MIT License.

