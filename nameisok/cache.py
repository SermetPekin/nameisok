"""
MIT License

Copyright (c) 2024 Sermet Pekin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from datetime import datetime, timedelta
from pathlib import Path
from ._globals import PACKAGE_NAME, CACHE_DURATION
import warnings


def warn(msg):
    warnings.warn(msg)


def get_cache_file(name='names_cache_') -> Path:
    if os.name == 'posix':
        cache_dir = Path.home() / '.cache' / PACKAGE_NAME  # Linux/macOS: ~/.cache/nameisok
    elif os.name == 'nt':
        cache_dir = Path(os.getenv('LOCALAPPDATA',
                                   Path.home() / 'AppData' / 'Local')) / PACKAGE_NAME  # Windows: %LOCALAPPDATA%\nameisok
    else:
        cache_dir = Path.home() / '.cache' / PACKAGE_NAME  # Default to Linux-style cache path

    cache_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
    return cache_dir / f'{name}.txt'


def cache_still_valid(name):
    cache_file = get_cache_file(name)
    file_mod_time = datetime.fromtimestamp(cache_file.stat().st_mtime)
    return datetime.now() - file_mod_time < CACHE_DURATION


def cache_file_exists(name):
    return get_cache_file(name).exists()


def cache_file_to_list(name) -> list | bool:
    cache_file = get_cache_file(name)

    with cache_file.open('r') as f:
        return [line.strip() for line in f if line.strip()]


def get_cache_content(name: str) -> bool | list[str]:
    if not cache_file_exists(name):
        return False
    if not cache_still_valid(name):
        return False

    try:
        liste = cache_file_to_list(name)
        return liste
    except:
        warn(f'reading cache content for {name} failed.')

    return False


def write_cache(name: str, list_: list) -> None:
    cache_file = get_cache_file(name)
    try:
        with cache_file.open('w') as f:
            f.write('\n'.join(list_))

    except:
        ...


def write_cache_text(name: str, text: str) -> None:
    cache_file = get_cache_file(name)
    try:
        with cache_file.open('w') as f:
            f.write(text)

    except:
        ...
