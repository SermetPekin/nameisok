import requests
from ._result import Result


def get_file_for_name(name):
    first_letter = name[0].lower()
    file_path = f'https://raw.githubusercontent.com/SermetPekin/nameisok/680f11c457858a058ad81bda819008cb341d3bd2/raw/raw-{first_letter}.txt'
    return file_path


def check_package_name_extra(name):
    file_url = get_file_for_name(name)
    response = requests.get(file_url)
    ok = name in response.text
    available_text = 'Available' if not ok else 'Not Available'
    r = Result(ok, 999, available_text)
    return r
