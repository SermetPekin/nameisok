from fuzzywuzzy import fuzz
import requests
import os
from datetime import datetime, timedelta
from pathlib import Path

CACHE_DURATION = timedelta(days=30)  # Cache duration of one month


def get_cache_file():
    PACKAGE_NAME = "nameisok"  # Your package name

    # Determine cache directory based on the OS
    if os.name == 'posix':
        cache_dir = Path.home() / '.cache' / PACKAGE_NAME  # Linux/macOS: ~/.cache/nameisok
    elif os.name == 'nt':
        cache_dir = Path(os.getenv('LOCALAPPDATA',
                                   Path.home() / 'AppData' / 'Local')) / PACKAGE_NAME  # Windows: %LOCALAPPDATA%\nameisok
    else:
        cache_dir = Path.home() / '.cache' / PACKAGE_NAME  # Default to Linux-style cache path

    cache_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
    CACHE_FILE = cache_dir / 'names_cache.txt'
    return CACHE_FILE
def get_existing_packages():
    cache_file = get_cache_file()
    if cache_file.exists():
        file_mod_time = datetime.fromtimestamp(cache_file.stat().st_mtime)
        if datetime.now() - file_mod_time < CACHE_DURATION:
            with cache_file.open('r') as f:
                return [line.strip() for line in f if line.strip()]

    url = 'https://raw.githubusercontent.com/SermetPekin/nameisok/d6048743d42fed02254a01a53c1ef563141deea9/raw/names_.txt'
    print('retrieving packages...')
    response = requests.get(url)
    response.raise_for_status()

    ns = [line.strip() for line in response.text.splitlines() if line.strip()]

    with cache_file.open('w') as f:
        f.write('\n'.join(ns))

    return ns

def check_name_similarity(new_name, existing_packages, threshold=80) -> list[str]:
    similar_names = []

    existing_packages = [str(x) for x in existing_packages]
    for name in existing_packages:
        similarity_score = fuzz.ratio(new_name.lower(), name.lower())
        if similarity_score >= threshold:
            similar_names.append(name)
    return similar_names
