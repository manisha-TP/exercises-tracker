# exercises-tracker

A full-stack MERN (MongoDB, Express, React, Node.js) application for tracking exercises.

## Features

- Create, read, update, and delete exercises
- User management
- Track exercise description, duration, and date
- Responsive web interface

## Prerequisites

- Node.js (v14 or higher)
- MongoDB (running locally or connection string)
- npm or yarn

## Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Update the `.env` file with your MongoDB connection string:
```
MONGODB_URI=mongodb://localhost:27017/exercises-tracker
PORT=5000
```

5. Start the backend server:
```bash
npm start
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## Usage

1. Make sure MongoDB is running
2. Start the backend server (runs on port 5000)
3. Start the frontend development server (runs on port 3000)
4. Open your browser and navigate to `http://localhost:3000`
5. Create a user first before adding exercises
6. Add, edit, and delete exercises as needed

## API Endpoints

### Users
- `GET /users` - Get all users
- `POST /users/add` - Create a new user

### Exercises
- `GET /exercises` - Get all exercises
- `GET /exercises/:id` - Get a specific exercise
- `POST /exercises/add` - Create a new exercise
- `POST /exercises/update/:id` - Update an exercise
- `DELETE /exercises/:id` - Delete an exercise

## Tech Stack

**Backend:**
- Node.js
- Express.js
- MongoDB with Mongoose
- CORS

**Frontend:**
- React
- React Router
- Axios
- Bootstrap
- React DatePicker