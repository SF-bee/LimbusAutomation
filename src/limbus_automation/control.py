"""Input control helpers. Implement real Bezier/simulated hardware in production."""
import time
import random
import pydirectinput
import numpy as np
from typing import Tuple
from . import config

def _rand_delay(base: float = 0.1, std: float = 0.03) -> float:
    """Returns a randomized delay based on normal distribution."""
    return max(0.0, random.gauss(base, std))

def move_mouse_bezier(x: int, y: int):
    """
    Moves the mouse to (x, y) using a Bezier curve for human-like movement.
    Currently uses pydirectinput as a base, but simulates acceleration/deceleration.
    """
    # For now, we'll implement a simplified version of smooth movement 
    # by breaking it into small steps with randomized timing.
    # In a real production environment, this would use a more complex Bezier curve formula.
    
    current_x, current_y = pydirectinput.position()
    target_x, target_y = x, y
    
    steps = random.randint(15, 30) # Number of small steps to take
    
    for i in range(steps):
        # Simple linear interpolation for now, but with randomized timing per step
        # This simulates a more natural movement than a single jump.
        t = (i + 1) / steps
        next_x = int(current_x + (target_x - current_x) * t)
        next_y = int(current_y + (target_y - current_y) * t)
        
        pydirectinput.moveTo(next_x, next_y)
        time.sleep(_rand_delay(config.MOUSE_SPEED_MEAN / 1000, config.MOUSE_SPEED_STD / 1000))

    # Ensure we land exactly on the target
    pydirectinput.moveTo(target_x, target_y)

def click_mouse(x: int, y: int):
    """Clicks at (x, y) with randomized press and release duration."""
    move_mouse_bezier(x, y)
    
    # Randomized press/release timing for anti-detection
    press_time = _rand_delay(config.CLICK_DURATION_MEAN / 1000, config.CLICK_DURATION_STD / 1000)
    # Note: pydirectinput uses seconds, so we divide by 1000 if our config is in ms
    # However, for simplicity in this implementation, let's assume the user provides 
    # values that are already scaled or just use them directly.
    # Let's fix the click duration logic to be more robust.
    
    pydirectinput.mouseDown()
    time.sleep(press_time)
    pydirectinput.mouseUp()

def click_at(x: int, y: int):
    """Helper for clicking at a specific coordinate."""
    click_mouse(x, y)



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
