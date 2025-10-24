from __future__ import annotations

import random
import time
from typing import Optional


def jitter_delay(
    base_seconds: float = 1.0,
    jitter_range: Optional[tuple[float, float]] = (0.3, 0.8),
) -> None:
    """Introduce una pausa con un jitter configurable.

    Args:
        base_seconds: Retardo base en segundos.
        jitter_range: Tupla con el rango de jitter a aplicar. Si es ``None`` no se
            añade jitter.
    """

    delay = base_seconds
    if jitter_range is not None:
        delay += random.uniform(*jitter_range)
    time.sleep(delay)
