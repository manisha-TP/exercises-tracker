# 🏋️‍♂️ Exercise Tracker Web Application

A comprehensive web application for tracking workouts, managing exercises, and monitoring fitness progress built with Flask and Bootstrap.

![Exercise Tracker](https://img.shields.io/badge/Flask-3.1.2-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple)
![Python](https://img.shields.io/badge/Python-3.7+-green)

## ✨ Features

### 📊 **Dashboard**
- Real-time workout statistics and analytics
- Quick action buttons for common tasks
- Recent workouts overview with details
- Muscle group distribution charts
- Motivational quotes and progress indicators
- Weekly/Monthly/Quarterly progress tracking

### 💪 **Exercise Management**
- Pre-populated exercise library with sample exercises
- Add custom exercises with detailed information:
  - **Exercise Name** (e.g., Push-ups, Squats, Running)
  - **Category** (Strength, Cardio, Core, Flexibility, Sports)
  - **Muscle Group** (Chest, Back, Arms, Legs, Core, Full Body)
  - **Equipment** (Dumbbells, Barbell, None, etc.)
  - **Difficulty Level** (Beginner, Intermediate, Advanced)
  - **Step-by-step Instructions**
- Real-time search and filter functionality
- Exercise preview while creating

### 🎯 **Workout Tracking**
- **Real-time workout timer** with live duration tracking
- Comprehensive exercise logging:
  - **Sets**: Number of sets performed
  - **Reps**: Repetitions per set (comma-separated: "10,12,10")
  - **Weight**: Weight used in kg (comma-separated: "20,22.5,20")
  - **Duration**: Time-based exercises in minutes
  - **Distance**: For cardio exercises in kilometers
  - **Notes**: Personal observations and feelings
- Session management and auto-save
- Exercise selection from library or quick add

### 📈 **Progress Analytics**
- Multiple time period analysis (7, 30, 90 days)
- Visual charts and statistics using Chart.js
- Muscle group distribution analysis
- Achievement system with milestone badges
- Detailed progress reports and trends
- Workout frequency tracking

### 🗂️ **Workout History**
- Complete workout history with pagination
- Detailed workout breakdowns
- Set-by-set analysis tables
- Exercise performance tracking over time
- Searchable and filterable history

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/exercise-tracker.git
   cd exercise-tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r exercise_requirements.txt
   ```

3. **Run the application:**
   ```bash
   python exercise_tracker_app.py
   ```

4. **Open your browser:**
   Go to `http://localhost:5000`

## 📱 User Interface

### Modern Design Features
- **Responsive Bootstrap 5 interface** - Works on desktop, tablet, and mobile
- **Gradient backgrounds and smooth animations**
- **Color-coded exercise categories** for easy identification
- **Interactive charts and progress bars**
- **Real-time updates and live search**
- **Modal dialogs for detailed input**
- **Toast notifications for user feedback**

### Navigation Structure
- **Dashboard**: Overview and quick actions
- **Exercises**: Browse and manage exercise library
- **New Workout**: Start and track workout sessions
- **Workouts**: View workout history
- **Progress**: Detailed analytics and reports

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Charts**: Chart.js for data visualization
- **Icons**: Font Awesome icons
- **Data Storage**: JSON files (easily upgradeable to database)
- **Deployment**: Compatible with Vercel, Heroku, PythonAnywhere

## 📋 How to Use

### Adding Exercises
1. Go to **Exercises** → **Add New Exercise**
2. Fill in exercise details (name, category, muscle group, etc.)
3. Add instructions and equipment requirements
4. Save to exercise library

### Starting a Workout
1. Click **Start Workout** from dashboard
2. Search and add exercises from library
3. Log sets, reps, weight for each exercise
4. Add workout notes
5. Finish workout to save session

### Tracking Progress
1. Visit **Progress** tab
2. View statistics for different time periods
3. Analyze muscle group distribution
4. Check achievement milestones
5. Export or share progress reports

## 📊 Sample Data

The application comes pre-loaded with sample exercises:

### Strength Training
- **Push-ups** (Chest, Bodyweight)
- **Squats** (Legs, Bodyweight)
- **Deadlifts** (Back, Barbell)
- **Bench Press** (Chest, Barbell)

### Cardio
- **Running** (Full Body, None)
- **Cycling** (Legs, Bike)
- **Jump Rope** (Full Body, Jump Rope)

### Core
- **Plank** (Core, None)
- **Sit-ups** (Core, None)
- **Russian Twists** (Core, None)

## 🎯 Key Features

### Workout Input Fields
- **Exercise Selection**: Choose from library or add custom
- **Sets Tracking**: Number of sets completed
- **Repetitions**: Track reps per set with flexibility
- **Weight Progression**: Monitor weight increases over time
- **Time Tracking**: Duration for cardio and timed exercises
- **Distance Logging**: For running, cycling, swimming
- **Personal Notes**: Observations, form notes, feelings

### Analytics & Reports
- **Workout Frequency**: Track consistency over time
- **Volume Progression**: Monitor total weight lifted
- **Muscle Group Balance**: Ensure balanced training
- **Achievement Badges**: Milestone celebrations
- **Visual Charts**: Easy-to-understand progress graphs

## 🌐 Deployment

### Local Development
```bash
python exercise_tracker_app.py
# Visit http://localhost:5000
```

### Vercel Deployment
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow deployment prompts

### Heroku Deployment
1. Create `Procfile`: `web: python exercise_tracker_app.py`
2. Push to Heroku git repository
3. Set environment variables if needed

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] **Database Integration** (PostgreSQL/MongoDB)
- [ ] **User Authentication** and profiles
- [ ] **Social Features** (share workouts, follow friends)
- [ ] **Mobile App** (React Native/Flutter)
- [ ] **Nutrition Tracking** integration
- [ ] **Workout Plans** and programs
- [ ] **Exercise Video Tutorials**
- [ ] **Wearable Device Integration**
- [ ] **Advanced Analytics** and AI insights
- [ ] **Offline Mode** with data sync

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/exercise-tracker/issues) page
2. Create a new issue with detailed description
3. Include screenshots if applicable

---

**Built with ❤️ for fitness enthusiasts and developers!**

*Start your fitness journey today with comprehensive workout tracking and progress analytics.*