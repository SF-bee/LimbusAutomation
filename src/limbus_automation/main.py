"""Entry point for the automation toolkit."""
import time
from .fsm import FSM
from .config import *
from .vision import capture_screen, get_screen_size
from .control import click_at

def main():
    print("LimbusAutomation starting...")
    width, height = get_screen_size()
    print(f"Screen resolution: {width}x{height}")
    
    # For testing purposes, let's just capture a screen and click somewhere
    print("Capturing screenshot for test...")
    screen = capture_screen()
    print(f"Captured screen shape: {screen.shape}")
    
    print("Moving mouse to center and clicking...")
    center_x, center_y = width // 2, height // 2
    click_at(center_x, center_y)
    print("Done.")

if __name__ == '__main__':
    main()

    main()
