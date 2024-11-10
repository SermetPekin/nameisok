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
