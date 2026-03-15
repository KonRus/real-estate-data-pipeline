import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch(url: str):

    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()

    return r.text