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
from dataclasses import dataclass


@dataclass
class Result:
    success: bool
    code: int
    value: str


def get_check_url(p_name: str) -> str:  # test ok
    url = f"https://pypi.org/project/{p_name}/"
    return url


def get_request_eval_result(url: str) -> Result:
    req = requests.get(url)  # not testing this part [requests]
    return eval_req(req.status_code, requests.codes.ok)  # test ok


def eval_req(status_code: int, ok_code: int) -> Result:  # test ok
    ok = status_code == ok_code
    available_text = 'Available' if not ok else 'Not Available'
    r = Result(ok, status_code, available_text)
    return r


def get_status_package(p_name: str) -> Result:
    url = get_check_url(p_name)  # test ok
    return get_request_eval_result(url)  # auto testing partly ok


def show_status_console(package_name: str, taken: bool) -> None:  # test ok
    if taken:
        template = f"\n  ❌ `{package_name}` is already taken."
    else:
        template = f"\n. 🎉 Wow! `{package_name}` is available!"
    print(template)


def action_get_status_package(package_name: str) -> None:
    r = get_status_package(package_name)
    show_status_console(package_name, r.success)


def get_status_package_cli(package_name: str, action=None) -> None:  # test ok
    if action is None:
        action = action_get_status_package
    if ',' in package_name:
        for p in package_name.split(','):
            action(p)
        return
    action(package_name)
