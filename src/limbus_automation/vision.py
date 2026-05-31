"""Minimal vision utilities using OpenCV and Pillow."""
from typing import Optional, Tuple
import cv2
import numpy as np
from PIL import ImageGrab
import os
from . import config

def capture_screen() -> np.ndarray:
    """Capture the whole screen and return BGR numpy array."""
    # Note: ImageGrab.grab() is a bit slow, but works for basic needs.
    # For higher performance, we might consider Win32 API later.
    img = ImageGrab.grab()
    # Convert PIL image to numpy array and then to BGR (OpenCV format)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def get_screen_size() -> Tuple[int, int]:
    """Return the screen resolution from config."""
    return config.SCREEN_WIDTH, config.SCREEN_HEIGHT

    arr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return arr


def find_template(screen: np.ndarray, template_path: str, threshold: float = 0.85) -> Optional[Tuple[int,int,int,int]]:
    """Locate template on screen. Returns bbox (x,y,w,h) or None."""
    tpl = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    if tpl is None:
        return None
    res = cv2.matchTemplate(screen, tpl, cv2.TM_CCOEFF_NORMED)
    minv, maxv, minloc, maxloc = cv2.minMaxLoc(res)
    if maxv >= threshold:
        h, w = tpl.shape[:2]
        x, y = maxloc
        return (x, y, w, h)
    return None
