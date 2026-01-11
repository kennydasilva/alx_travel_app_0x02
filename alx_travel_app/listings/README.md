# ALX Travel App 0x01

This project provides CRUD API endpoints for Listings, Bookings and Reviews using Django REST Framework.

## 🚀 API Endpoints

| Resource | Endpoint | Methods |
|----------|----------|---------|
| Listings | /api/listings/ | GET, POST |
| Listings (detail) | /api/listings/<id>/ | GET, PUT, DELETE |
| Bookings | /api/bookings/ | GET, POST |
| Bookings (detail) | /api/bookings/<id>/ | GET, PUT, DELETE |
| Reviews | /api/reviews/ | GET, POST |
| Reviews (detail) | /api/reviews/<id>/ | GET, PUT, DELETE |

## 📄 Documentation

Swagger UI available at:

)

urlpatterns = [
    path('admin/', admi
    
    
    # ALX Travel App

A Django-based travel booking application.

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Seed database: `python manage.py seed`
7. Run server: `python manage.py runserver`

## Models

- **Listing**: Properties available for booking
- **Booking**: Guest reservations
- **Review**: Guest reviews and ratings

## Seeding

The application includes a management command to populate the database with sample data:

```bash
python manage.py seed
