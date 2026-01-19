# Quick Start Guide

## Running the Application

### Start all services with Docker Compose

```bash
# Build and start all services
docker compose up --build

# Or run in detached mode
docker compose up -d --build
```

### Access the Services

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **MongoDB**: localhost:27017

### Stop Services

```bash
# Stop all services
docker compose down

# Stop and remove volumes (clean slate)
docker compose down -v
```

## Development Workflow

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Worker Development
```bash
cd worker
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python worker.py
```

## Database Selection

### Using MongoDB (Default)
No changes needed - MongoDB is configured by default.

### Switching to PostgreSQL
1. Edit `docker-compose.yml`:
   - Comment out the `mongodb` service
   - Uncomment the `postgres` service and `postgres_data` volume
2. Update environment variables in backend:
   - Change `DATABASE_URL` to use PostgreSQL connection string
3. Restart services:
   ```bash
   docker compose down -v
   docker compose up --build
   ```

## Troubleshooting

### Port Already in Use
If you get a port conflict error:
```bash
# Check what's using the port
lsof -i :5173  # or :8000, :27017

# Kill the process or change port in docker-compose.yml
```

### Database Connection Issues
```bash
# Check if database is running
docker compose ps

# View database logs
docker compose logs mongodb
# or
docker compose logs postgres
```

### Rebuild from Scratch
```bash
# Stop everything and remove all data
docker compose down -v

# Remove all images
docker compose down --rmi all

# Rebuild and start
docker compose up --build
```
