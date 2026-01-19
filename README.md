# Go-to-class-ai

An AI-powered class management system built with modern web technologies and Docker.

## Architecture

This project follows a microservices architecture using Docker Compose:

```
Docker Compose
├── frontend (Vite + React)
├── backend (FastAPI)
├── database (MongoDB or Postgres)
└── worker / scheduler (optional)
```

## Tech Stack

- **Frontend**: Vite + React (Port 5173)
- **Backend**: FastAPI (Port 8000)
- **Database**: MongoDB (Port 27017) or PostgreSQL (Port 5432)
- **Worker**: Python-based scheduler for background tasks

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:
```bash
git clone https://github.com/DunsinK/Go-to-class-ai.git
cd Go-to-class-ai
```

2. Start all services:
```bash
docker-compose up --build
```

3. Access the application:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Development

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Worker
```bash
cd worker
pip install -r requirements.txt
python worker.py
```

## Project Structure

```
.
├── frontend/           # Vite + React frontend
│   ├── src/           # React source files
│   ├── Dockerfile     # Frontend Docker configuration
│   └── package.json   # Node dependencies
├── backend/           # FastAPI backend
│   ├── main.py       # FastAPI application
│   ├── requirements.txt
│   └── Dockerfile    # Backend Docker configuration
├── database/         # Database initialization scripts
│   ├── mongodb/      # MongoDB init scripts
│   └── postgres/     # PostgreSQL init scripts
├── worker/           # Background task scheduler
│   ├── worker.py     # Scheduler implementation
│   ├── requirements.txt
│   └── Dockerfile    # Worker Docker configuration
└── docker-compose.yml # Docker Compose configuration
```

## Database Options

The project supports both MongoDB and PostgreSQL:

- **MongoDB** (default): NoSQL database, great for flexible schemas
- **PostgreSQL**: Relational database, uncomment in docker-compose.yml to use

## Environment Variables

Copy the example environment files and configure as needed:
```bash
cp frontend/.env.example frontend/.env
cp backend/.env.example backend/.env
```

## License

MIT