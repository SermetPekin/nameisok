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

import requests
from ._result import Result
from .types_ import get_url_instance
from .cache import get_cache_file, get_cache_content, write_cache, write_cache_text


def get_file_for_name(name: str):
    first_letter = name[0].lower()
    u = get_url_instance()
    file_path = f'{u.url}/raw/raw-{first_letter}.txt'
    return file_path


def check_package_name_extra_helper(name: str, text: str):
    ok = name in text
    available_text = 'Available' if not ok else 'Not Available'
    r = Result(ok, 999, available_text)
    return r


def fresh_request_package_name(name):
    file_url = get_file_for_name(name)
    response = requests.get(file_url)
    return response.text


def check_package_name_extra(name: str):
    letter = name.lower()[0]

    cache_name = f'{letter}_cache_partial'
    cache_file = get_cache_file(cache_name)
    if cache_file.exists():
        content_list = get_cache_content(cache_name)
        if content_list:
            text = '\n'.join(content_list)
            return check_package_name_extra_helper(name, text)

    text = fresh_request_package_name(name)
    write_cache_text(cache_name, text)

    return check_package_name_extra_helper(name, text)
