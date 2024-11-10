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
from .c_check import check_package_name_extra
from .similar import get_existing_packages, check_name_similarity


def get_check_url(p_name: str) -> str:  # test ok
    """
    https://pypi.org/project/{p_name}/
    https://pypi.org/simple/{p_name}/
    """
    url = f"https://pypi.org/simple/{p_name}/"
    return url


def get_request_eval_result(url: str) -> Result:
    req = requests.get(url)  # not testing this part [requests]
    return eval_req(req.status_code, requests.codes.ok)  # test ok


def eval_req(status_code: int, ok_code: int = requests.codes.ok) -> Result:  # test ok
    exists = status_code == ok_code
    available_text = 'Available' if not exists else 'Not Available'
    r = Result(exists, status_code, available_text)
    return r


def get_status_package(p_name: str) -> Result:
    url = get_check_url(p_name)  # test ok
    result = get_request_eval_result(url)  # auto testing partly ok
    if not result.exists:
        result = check_package_name_extra(p_name)
    return result


def extra_checks_if_available(p_name) -> None:
    print('Similarity check begins...')
    check_similarity(p_name)


def show_status_console_available(package_name: str) -> None:  # test ok

    template = f"\n. 🎉 Wow! `{package_name}` is available!"
    print(template)


def show_status_console_taken(package_name: str) -> None:  # test ok
    template = f"\n  ❌ `{package_name}` is already taken."
    print(template)


def show_status_similar_exists(package_name: str, similar_names: list) -> None:  # test ok
    if similar_names:
        print(
            f" ❌ Unfortunately, the name '{package_name}' is too similar to existing projects: {', '.join(similar_names)}")
    else:
        print(f"I have good news 🎉 the name '{package_name}' is available and sufficiently unique.")


def check_similarity(new_package_name):
    ep = get_existing_packages()
    if not ep:
        import warnings
        msg = 'Similarity check failed.'
        warnings.warn(msg)
        return False

    similar_names = check_name_similarity(new_package_name, ep)
    return similar_names


def action_get_status_package(package_name: str) -> bool | None:
    r = get_status_package(package_name)
    if r.exists:  # pypi + database was checked
        show_status_console_taken(package_name)
        return not r.exists
    print(f'First check passed for `{package_name}` 🎉. Now I will check similar packages.')
    # similarity check
    similar_names = check_similarity(package_name)
    if similar_names is False:
        return

    show_status_similar_exists(package_name, similar_names)
    return not similar_names.__len__() > 0


def get_status_package_cli(package_name: str, action=None) -> bool | list[bool]:  # test ok
    if action is None:
        action = action_get_status_package
    if ',' in package_name:
        results = []
        for p in package_name.split(','):
            res = action(p)
            results.append(res)
        return results
    result = action(package_name)
    return result
