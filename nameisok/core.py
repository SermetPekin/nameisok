import requests

from ._result import Result
from .c_check import check_package_name_extra


def get_check_url(p_name: str) -> str:  # test ok
    # url = f"https://pypi.org/project/{p_name}/"
    url = f"https://pypi.org/simple/{p_name}/"
    return url


def get_request_eval_result(url: str) -> Result:
    req = requests.get(url)  # not testing this part [requests]
    return eval_req(req.status_code, requests.codes.ok)  # test ok


def eval_req(status_code: int, ok_code: int = requests.codes.ok) -> Result:  # test ok
    ok = status_code == ok_code
    available_text = 'Available' if not ok else 'Not Available'
    r = Result(ok, status_code, available_text)
    return r


def get_status_package(p_name: str) -> Result:
    url = get_check_url(p_name)  # test ok
    result = get_request_eval_result(url)  # auto testing partly ok
    if not result.success:
        try:
            result = check_package_name_extra(p_name)
        except:
            ... # we will try to check from bigquery source

    return result


def show_status_console(package_name: str, taken: bool) -> None:  # test ok
    if taken:
        template = f"\n  ❌ `{package_name}` is already taken."
    else:
        template = f"\n. 🎉 Wow! `{package_name}` is available!"
    print(template)


def action_get_status_package(package_name: str) -> bool:
    r = get_status_package(package_name)
    show_status_console(package_name, r.success)
    return not r.success


def get_status_package_cli(package_name: str, action=None) -> bool:  # test ok
    if action is None:
        action = action_get_status_package
    if ',' in package_name:
        results = []
        for p in package_name.split(','):
            res = action(p)
            results.append(res)
        return all(results)
    result = action(package_name)
    return result
