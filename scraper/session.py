from __future__ import annotations

from contextlib import contextmanager
from typing import Generator, Optional

import requests

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "es-MX,es;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
}


def build_session(headers: Optional[dict[str, str]] = None) -> requests.Session:
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    if headers:
        session.headers.update(headers)
    return session


@contextmanager
def session_scope(headers: Optional[dict[str, str]] = None) -> Generator[requests.Session, None, None]:
    session = build_session(headers=headers)
    try:
        yield session
    finally:
        session.close()
