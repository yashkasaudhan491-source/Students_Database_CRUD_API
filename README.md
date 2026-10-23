# Students Database CRUD Application

This is a Python backend application built with FastAPI and SQLite to manage student records via standard CRUD operations.

## Features
* **Create**: Add new student records (POST `/students`).
* **Read**: List all students (GET `/students`) or view a specific student by ID (GET `/students/{student_id}`).
* **Update**: Modify existing student records (PUT `/students/{student_id}`).
* **Delete**: Remove a student record (DELETE `/students/{student_id}`).
* Persistent data storage via SQLite.

## Prerequisites
* Python 3.8+ installed.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd <repository-folder>