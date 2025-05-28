# Getting Started

Follow the instructions below to set up and run your FastAPI project.

## Prerequisites

Ensure you have the following installed:

- Python >= 3.10  
- PostgreSQL  
- Redis  

## Project Setup

### 1. Clone the project repository:

```bash
git clone https://github.com/jod35/fastapi-beyond-CRUD.git
```

### 2. Navigate to the project directory:

```bash
cd fastapi-beyond-CRUD/
```

### 3. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

### 4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set up environment variables by copying the example configuration:

```bash
cp .env.example .env
```

### 6. Run database migrations to initialize the database schema:

```bash
alembic upgrade head
```
