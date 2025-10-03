import sys
import os

# Add the parent directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import the Flask app
from exercise_tracker_app import app

# This is the entry point for Vercel
# Vercel will automatically call this Flask app