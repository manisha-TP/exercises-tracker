#!/usr/bin/env python3
"""
Deployment Test Script
Run this to verify your app is ready for deployment
"""

import sys
import os

# Test imports
try:
    from exercise_tracker_app import app
    print("✅ Flask app imports successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

# Test template files
template_files = [
    'exercise_base.html',
    'dashboard.html', 
    'exercises.html',
    'add_exercise.html',
    'new_workout.html',
    'workouts.html',
    'view_workout.html',
    'progress.html',
    '404.html',
    '500.html'
]

missing_templates = []
for template in template_files:
    if not os.path.exists(f'templates/{template}'):
        missing_templates.append(template)

if missing_templates:
    print(f"❌ Missing templates: {missing_templates}")
    sys.exit(1)
else:
    print("✅ All templates found")

# Test configuration files
config_files = ['requirements.txt', 'vercel.json', 'runtime.txt', 'api/index.py']
missing_config = []
for config in config_files:
    if not os.path.exists(config):
        missing_config.append(config)

if missing_config:
    print(f"❌ Missing config files: {missing_config}")
    sys.exit(1)
else:
    print("✅ All config files found")

print("\n🚀 Your app is ready for deployment!")
print("\nDeploy with:")
print("1. Upload to GitHub")
print("2. Connect to Vercel")
print("3. Deploy!")