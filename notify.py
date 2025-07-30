# notify.py --- Sound alert for price threshold
# This module provides functionality to play a sound alert when the price
# of a cryptocurrency crosses predefined thresholds.
import os

def sound_alert():
    """
    Plays a system sound or voice alert when threshold is triggered.
    On macOS, uses 'say'. On Windows, could use winsound.
    """
    try:
        os.system("say 'Bitcoin alert triggered!'")  # macOS
    except Exception as e:
        print(f"🔇 Sound alert failed: {e}")
