import requests
from requests import Response
from typing import Optional


def hit_url(url: str) -> Optional[Response]:
    """
        hits the API endpoint and returns response if successful
    """
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response
