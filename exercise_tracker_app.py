"""
Exercise Tracker Web Application
Version: 1.0
Flask web application for tracking workouts and exercises
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import json
import os
from datetime import datetime, timedelta
import uuid
from collections import defaultdict
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

class ExerciseTracker:
    def __init__(self):
        self.exercises_file = "exercises_data.json"
        self.workouts_file = "workouts_data.json"
        self.users_file = "users_data.json"
        self.init_data_files()
    
    def init_data_files(self):
        """Initialize data files if they don't exist"""
        for file_path in [self.exercises_file, self.workouts_file, self.users_file]:
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    json.dump([], f)
    
    def load_data(self, file_path):
        """Load data from JSON file"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return []
    
    def save_data(self, file_path, data):
        """Save data to JSON file"""
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving {file_path}: {e}")
            return False
    
    def add_exercise(self, exercise_data):
        """Add a new exercise to the database"""
        exercises = self.load_data(self.exercises_file)
        exercise = {
            'id': str(uuid.uuid4()),
            'name': exercise_data['name'],
            'category': exercise_data['category'],
            'muscle_group': exercise_data['muscle_group'],
            'equipment': exercise_data.get('equipment', 'None'),
            'instructions': exercise_data.get('instructions', ''),
            'difficulty': exercise_data.get('difficulty', 'Intermediate'),
            'created_at': datetime.now().isoformat()
        }
        exercises.append(exercise)
        self.save_data(self.exercises_file, exercises)
        return exercise
    
    def get_exercises(self, category=None, muscle_group=None):
        """Get exercises with optional filtering"""
        exercises = self.load_data(self.exercises_file)
        
        if category:
            exercises = [ex for ex in exercises if ex['category'].lower() == category.lower()]
        if muscle_group:
            exercises = [ex for ex in exercises if ex['muscle_group'].lower() == muscle_group.lower()]
            
        return exercises
    
    def get_exercise_by_id(self, exercise_id):
        """Get a specific exercise by ID"""
        exercises = self.load_data(self.exercises_file)
        for exercise in exercises:
            if exercise['id'] == exercise_id:
                return exercise
        return None
    
    def log_workout(self, workout_data):
        """Log a workout session"""
        workouts = self.load_data(self.workouts_file)
        workout = {
            'id': str(uuid.uuid4()),
            'user_id': workout_data.get('user_id', 'default'),
            'date': workout_data.get('date', datetime.now().isoformat()),
            'exercises': workout_data['exercises'],  # List of exercise logs
            'duration': workout_data.get('duration', 0),  # In minutes
            'notes': workout_data.get('notes', ''),
            'created_at': datetime.now().isoformat()
        }
        workouts.append(workout)
        self.save_data(self.workouts_file, workouts)
        return workout
    
    def add_exercise_to_workout(self, exercise_log):
        """Add an exercise log to a workout"""
        return {
            'exercise_id': exercise_log['exercise_id'],
            'exercise_name': exercise_log['exercise_name'],
            'sets': exercise_log['sets'],
            'reps': exercise_log.get('reps', []),
            'weight': exercise_log.get('weight', []),
            'duration': exercise_log.get('duration', 0),  # For time-based exercises
            'distance': exercise_log.get('distance', 0),  # For cardio
            'calories': exercise_log.get('calories', 0),
            'notes': exercise_log.get('notes', '')
        }
    
    def get_workouts(self, user_id='default', limit=None, date_from=None, date_to=None):
        """Get workouts with optional filtering"""
        workouts = self.load_data(self.workouts_file)
        user_workouts = [w for w in workouts if w['user_id'] == user_id]
        
        # Filter by date range
        if date_from:
            user_workouts = [w for w in user_workouts if w['date'] >= date_from]
        if date_to:
            user_workouts = [w for w in user_workouts if w['date'] <= date_to]
        
        # Sort by date (newest first)
        user_workouts.sort(key=lambda x: x['date'], reverse=True)
        
        if limit:
            user_workouts = user_workouts[:limit]
            
        return user_workouts
    
    def get_workout_by_id(self, workout_id):
        """Get a specific workout by ID"""
        workouts = self.load_data(self.workouts_file)
        for workout in workouts:
            if workout['id'] == workout_id:
                return workout
        return None
    
    def get_workout_stats(self, user_id='default', days=30):
        """Get workout statistics for the past N days"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        workouts = self.get_workouts(
            user_id=user_id,
            date_from=start_date.isoformat(),
            date_to=end_date.isoformat()
        )
        
        stats = {
            'total_workouts': len(workouts),
            'total_duration': sum(w.get('duration', 0) for w in workouts),
            'total_exercises': sum(len(w.get('exercises', [])) for w in workouts),
            'workout_frequency': len(workouts) / days if days > 0 else 0,
            'muscle_groups_trained': defaultdict(int),
            'exercise_types': defaultdict(int),
            'weekly_workouts': []
        }
        
        # Analyze muscle groups and exercise types
        for workout in workouts:
            for exercise_log in workout.get('exercises', []):
                exercise = self.get_exercise_by_id(exercise_log.get('exercise_id'))
                if exercise:
                    stats['muscle_groups_trained'][exercise['muscle_group']] += 1
                    stats['exercise_types'][exercise['category']] += 1
        
        return stats
    
    def get_exercise_progress(self, user_id='default', exercise_id=None, days=90):
        """Get progress for a specific exercise"""
        workouts = self.get_workouts(user_id=user_id, limit=50)
        progress = []
        
        for workout in workouts:
            for exercise_log in workout.get('exercises', []):
                if exercise_id and exercise_log.get('exercise_id') == exercise_id:
                    progress.append({
                        'date': workout['date'],
                        'sets': exercise_log.get('sets', 0),
                        'reps': exercise_log.get('reps', []),
                        'weight': exercise_log.get('weight', []),
                        'duration': exercise_log.get('duration', 0),
                        'max_weight': max(exercise_log.get('weight', [0])),
                        'total_reps': sum(exercise_log.get('reps', []))
                    })
        
        return sorted(progress, key=lambda x: x['date'])

# Initialize tracker
tracker = ExerciseTracker()

# Pre-populate with sample exercises if database is empty
def init_sample_exercises():
    exercises = tracker.get_exercises()
    if not exercises:
        sample_exercises = [
            {
                'name': 'Push-ups',
                'category': 'Strength',
                'muscle_group': 'Chest',
                'equipment': 'None',
                'instructions': 'Start in plank position, lower body to ground, push back up',
                'difficulty': 'Beginner'
            },
            {
                'name': 'Squats',
                'category': 'Strength',
                'muscle_group': 'Legs',
                'equipment': 'None',
                'instructions': 'Stand with feet hip-width apart, lower hips back and down',
                'difficulty': 'Beginner'
            },
            {
                'name': 'Running',
                'category': 'Cardio',
                'muscle_group': 'Full Body',
                'equipment': 'None',
                'instructions': 'Maintain steady pace, breathe rhythmically',
                'difficulty': 'Intermediate'
            },
            {
                'name': 'Deadlift',
                'category': 'Strength',
                'muscle_group': 'Back',
                'equipment': 'Barbell',
                'instructions': 'Lift barbell from ground to hip level, keep back straight',
                'difficulty': 'Advanced'
            },
            {
                'name': 'Plank',
                'category': 'Core',
                'muscle_group': 'Core',
                'equipment': 'None',
                'instructions': 'Hold plank position, keep body straight',
                'difficulty': 'Intermediate'
            }
        ]
        
        for exercise in sample_exercises:
            tracker.add_exercise(exercise)

# Routes
@app.route('/')
def index():
    """Main dashboard"""
    user_id = session.get('user_id', 'default')
    recent_workouts = tracker.get_workouts(user_id=user_id, limit=5)
    stats = tracker.get_workout_stats(user_id=user_id, days=30)
    
    return render_template('dashboard.html', 
                         recent_workouts=recent_workouts, 
                         stats=stats)

@app.route('/exercises')
def exercises():
    """Exercise library"""
    category = request.args.get('category')
    muscle_group = request.args.get('muscle_group')
    
    exercises = tracker.get_exercises(category=category, muscle_group=muscle_group)
    
    # Get unique categories and muscle groups for filters
    all_exercises = tracker.get_exercises()
    categories = list(set(ex['category'] for ex in all_exercises))
    muscle_groups = list(set(ex['muscle_group'] for ex in all_exercises))
    
    return render_template('exercises.html', 
                         exercises=exercises,
                         categories=categories,
                         muscle_groups=muscle_groups,
                         selected_category=category,
                         selected_muscle_group=muscle_group)

@app.route('/add_exercise', methods=['GET', 'POST'])
def add_exercise():
    """Add new exercise"""
    if request.method == 'POST':
        exercise_data = {
            'name': request.form['name'],
            'category': request.form['category'],
            'muscle_group': request.form['muscle_group'],
            'equipment': request.form.get('equipment', ''),
            'instructions': request.form.get('instructions', ''),
            'difficulty': request.form.get('difficulty', 'Intermediate')
        }
        
        exercise = tracker.add_exercise(exercise_data)
        flash(f'Exercise "{exercise["name"]}" added successfully!', 'success')
        return redirect(url_for('exercises'))
    
    return render_template('add_exercise.html')

@app.route('/workout/new')
def new_workout():
    """Start a new workout"""
    exercises = tracker.get_exercises()
    return render_template('new_workout.html', exercises=exercises)

@app.route('/workout/log', methods=['POST'])
def log_workout():
    """Log a completed workout"""
    try:
        data = request.get_json()
        
        user_id = session.get('user_id', 'default')
        workout_data = {
            'user_id': user_id,
            'exercises': data.get('exercises', []),
            'duration': data.get('duration', 0),
            'notes': data.get('notes', ''),
            'date': data.get('date', datetime.now().isoformat())
        }
        
        workout = tracker.log_workout(workout_data)
        return jsonify({'success': True, 'workout_id': workout['id']})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/workouts')
def workouts():
    """View workout history"""
    user_id = session.get('user_id', 'default')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    all_workouts = tracker.get_workouts(user_id=user_id)
    total_workouts = len(all_workouts)
    
    # Simple pagination
    start = (page - 1) * per_page
    end = start + per_page
    workouts_page = all_workouts[start:end]
    
    has_prev = page > 1
    has_next = end < total_workouts
    
    return render_template('workouts.html', 
                         workouts=workouts_page,
                         has_prev=has_prev,
                         has_next=has_next,
                         prev_num=page-1 if has_prev else None,
                         next_num=page+1 if has_next else None,
                         page=page)

@app.route('/workout/<workout_id>')
def view_workout(workout_id):
    """View specific workout details"""
    workout = tracker.get_workout_by_id(workout_id)
    if not workout:
        flash('Workout not found', 'error')
        return redirect(url_for('workouts'))
    
    # Get exercise details for each logged exercise
    for exercise_log in workout.get('exercises', []):
        exercise = tracker.get_exercise_by_id(exercise_log.get('exercise_id'))
        if exercise:
            exercise_log['exercise_details'] = exercise
    
    return render_template('view_workout.html', workout=workout)

@app.route('/progress')
def progress():
    """View progress and statistics"""
    user_id = session.get('user_id', 'default')
    
    # Get stats for different time periods
    stats_7d = tracker.get_workout_stats(user_id=user_id, days=7)
    stats_30d = tracker.get_workout_stats(user_id=user_id, days=30)
    stats_90d = tracker.get_workout_stats(user_id=user_id, days=90)
    
    return render_template('progress.html',
                         stats_7d=stats_7d,
                         stats_30d=stats_30d,
                         stats_90d=stats_90d)

@app.route('/api/exercise/<exercise_id>/progress')
def exercise_progress(exercise_id):
    """API endpoint for exercise progress data"""
    user_id = session.get('user_id', 'default')
    progress = tracker.get_exercise_progress(user_id=user_id, exercise_id=exercise_id)
    return jsonify(progress)

@app.route('/api/exercises/search')
def search_exercises():
    """API endpoint for exercise search"""
    query = request.args.get('q', '').lower()
    exercises = tracker.get_exercises()
    
    if query:
        filtered_exercises = [
            ex for ex in exercises 
            if query in ex['name'].lower() or 
               query in ex['muscle_group'].lower() or 
               query in ex['category'].lower()
        ]
    else:
        filtered_exercises = exercises
    
    return jsonify(filtered_exercises)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Template filters
@app.template_filter('format_date')
def format_date(date_string):
    """Format ISO date string to readable format"""
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%B %d, %Y at %I:%M %p')
    except:
        return date_string

@app.template_filter('format_duration')
def format_duration(minutes):
    """Format duration in minutes to hours and minutes"""
    if minutes < 60:
        return f"{minutes} min"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m" if mins > 0 else f"{hours}h"

@app.template_filter('safe_sum')
def safe_sum(values):
    """Safely sum a list of values"""
    try:
        return sum(float(v) for v in values if v)
    except:
        return 0

@app.template_filter('safe_max')
def safe_max(values):
    """Safely get max from a list of values"""
    try:
        valid_values = [float(v) for v in values if v]
        return max(valid_values) if valid_values else 0
    except:
        return 0

if __name__ == '__main__':
    # Initialize sample data
    init_sample_exercises()
    
    print("Starting Exercise Tracker Web Application...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)