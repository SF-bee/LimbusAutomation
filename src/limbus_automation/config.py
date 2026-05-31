# Central configuration: change values here, not in logic files

import os

# --- Resolution and Capture Settings ---
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")

# Ensure directories exist
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# --- Vision Settings ---
# Template matching threshold (0.0 to 1.0)
MATCH_THRESHOLD = 0.8

# --- Control Settings (Anti-Detection) ---
# Mouse movement: Bezier curve parameters
# We use a normal distribution for speed/timing variation
MOUSE_SPEED_MEAN = 500  # Average time for a move operation in ms
MOUSE_SPEED_STD = 100   # Standard deviation for timing jitter

# Click duration (how long the mouse button is held down)
CLICK_DURATION_MEAN = 100 # ms
CLICK_DURATION_STD = 30    # ms

# --- Latency Settings ---
# Base delay between actions
BASE_DELAY = 1.5  # seconds
DELAY_VARIATION = 0.5 # max variation in seconds

# Thresholds for specific game states (to be filled as we develop)
STATE_THRESHOLDS = {
    "room_type": 0.7,
    "skill_ready": 0.85,
}

MATCH_CONFIDENCE = 0.85

# Timing (use randomized delays in code)
DEFAULT_ACTION_DELAY = 0.2  # seconds (base)