📚 Book Manager :- A Django REST API project for managing books with PostgreSQL, fully containerized using Docker and Docker Compose.

🚀 Features :-CRUD APIs for books, 
              PostgreSQL as the database, 
              Environment variables managed via .env, 
              Containerized with Docker (supports docker-compose), 
              Follows best practices with .gitignore and .dockerignore, 

1. API Endpoints (Example):-

POST /books/create/ → Create a book

GET /books/ → List all books

GET /books/{id}/ → Retrieve a single book

PUT /books/{id}/update → Update a book

DELETE /books/{id}/delete → Delete a book

📂 Project Structure:-
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

⚙️ Setup Instructions:-
1️. Clone the Repository:
git clone https://github.com/yourusername/book_manager.git
cd book_manager

2. Create a .env File:-
# Django
SECRET_KEY=your-secret-key
DEBUG=1

# Database
POSTGRES_DB=db_name
POSTGRES_USER=username
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

3. Run with Docker Compose :- docker-compose up --build

4. Apply Migrations :- docker exec -ti django_app python manage.py migrate

5. Create a Superuser :- docker exec -ti django_app python manage.py createsuperuser

6. Access the App :- http://localhost:8000

7. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

8. Install dependencies
pip install -r requirements.txt

9. Apply migrations
python manage.py migrate

10. Run server
python manage.py runserver

11. Enter Django shell :- docker exec -ti django_app python manage.py shell

12. Enter Postgres shell :- docker exec -ti postgres_db psql -U $POSTGRES_USER -d $POSTGRES_DB










