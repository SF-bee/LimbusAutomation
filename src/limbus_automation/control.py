"""Input control helpers. Implement real Bezier/simulated hardware in production."""
import time
import random
import pydirectinput
from typing import Tuple


def _rand_delay(base: float = 0.1, std: float = 0.03) -> float:
    return max(0.0, random.gauss(base, std))


def move_mouse_bezier(x: int, y: int, duration: float = 0.4):
    """Placeholder: move mouse with small randomized steps to (x,y)."""
    # NOTE: Replace with true Bezier curve implementation sending scan codes.
    steps = max(3, int(duration / 0.02))
    cx, cy = pydirectinput.position()
    for i in range(1, steps + 1):
        nx = int(cx + (x - cx) * i / steps)
        ny = int(cy + (y - cy) * i / steps)
        pydirectinput.moveTo(nx, ny, duration=0)
        time.sleep(duration / steps + random.uniform(-0.005, 0.005))


def click(x: int, y: int, button: str = 'left'):
    move_mouse_bezier(x, y, duration=0.15)
    time.sleep(_rand_delay(0.05, 0.02))
    pydirectinput.click(x, y, button=button)
    time.sleep(_rand_delay(0.08, 0.03))
