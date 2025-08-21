📚 Book Manager :-

A Django REST API project for managing books, with PostgreSQL as the database.
The project is fully containerized with Docker and Docker Compose, making setup and deployment seamless.

🚀 Features :-

CRUD APIs for managing books

PostgreSQL as the database

Environment variables managed via .env

Containerized with Docker (supports docker-compose)

Clean project structure with .gitignore and .dockerignore

Follows Django best practices

📂 Project Structure :-

book_manager/

│── BookApp/              # Django app (models, views, serializers, urls)

│── book_manager/         # Project settings and root urls

│── requirements.txt      # Python dependencies

│── Dockerfile            # Docker image setup

│── docker-compose.yml    # Multi-container setup

│── .env                  # Environment variables (DB credentials, secret key, etc.)

│── .gitignore

│── .dockerignore

│── README.md             # Project documentation


🔗 API Endpoints :- 

| Method | Endpoint              | Description     |
| ------ | --------------------- | --------------- |
| POST   | `/books/create/`      | Create a book   |
| GET    | `/books/`             | List all books  |
| GET    | `/books/{id}/`        | Retrieve a book |
| PUT    | `/books/{id}/update/` | Update a book   |
| DELETE | `/books/{id}/delete/` | Delete a book   |


⚙️ Setup Instructions:-

1️⃣ Clone the Repository :- 

git clone https://github.com/yourusername/book_manager.git
cd book_manager

2️⃣ Create .env File :-  Inside the project root (book_manager/), create a .env file with the following content:

# Django
SECRET_KEY=your-secret-key
DEBUG=1

# Database
POSTGRES_DB=book_db
POSTGRES_USER=book_user
POSTGRES_PASSWORD=book_password
POSTGRES_HOST=db
POSTGRES_PORT=5432


3️⃣ Run with Docker Compose :- Build and start the containers:

docker-compose up --build

This starts:

Django app (container name: django_app)

PostgreSQL database (container name: postgres_db)

4️⃣ Apply Migrations :- Run database migrations inside the Django container:

docker exec -it django_app python manage.py migrate


5️⃣ Create Superuser :- 

docker exec -it django_app python manage.py createsuperuser


6️⃣ Access the Application

API root: http://localhost:8000

Django Admin: http://localhost:8000/admin

🛠 Development without Docker (Optional) 

If you prefer running locally without Docker:

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver


🐚 Useful Commands on powershell :- 

# Enter Django shell inside container
docker exec -it django_app python manage.py shell

# Enter Postgres shell
docker exec -it postgres_db psql -U book_user -d book_db

# See running containers
docker ps

# Stop containers
docker-compose down

# Restart containers
docker-compose up --build



