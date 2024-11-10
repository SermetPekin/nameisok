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
from fuzzywuzzy import fuzz
import requests

from .types_ import get_url_instance2
from ._globals import THRESHOLD
from .cache import get_cache_content, write_cache


def get_names_fresh():
    u = get_url_instance2()
    url = f'{u.url}/raw/names_.txt'
    print('retrieving packages...')
    try:
        response = requests.get(url)
        response.raise_for_status()
        ns = [line.strip() for line in response.text.splitlines() if line.strip()]
        return ns
    except:
        ...
    return False


def get_existing_packages() -> list | bool:
    name_cache = 'name_3'
    cache_content = get_cache_content(name_cache)
    if cache_content:
        return cache_content

    ns = get_names_fresh()
    if ns:
        write_cache(name_cache, ns)
        return ns
    return False


def check_name_similarity(new_name, existing_packages, threshold=None) -> list[str]:
    if threshold is None:
        threshold = THRESHOLD

    similar_names = []

    existing_packages = [str(x) for x in existing_packages]
    for name in existing_packages:
        similarity_score = fuzz.ratio(new_name.lower(), name.lower())
        if similarity_score >= threshold:
            similar_names.append(name)
    return similar_names
