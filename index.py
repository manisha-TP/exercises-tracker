import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from exercise_tracker_app import app

# Initialize sample data for Vercel
from exercise_tracker_app import init_sample_exercises
init_sample_exercises()

# Vercel entry point
app = app