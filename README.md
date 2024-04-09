
# Fitness trainers' schedule managing

Application purpose is a managing fitness trainers' schedule.
The project containd backend part of the application

Stack used: Django REST Framework, Docker

Database: PostgreSQL 14

## API Reference
The API endpoints of apps listed below

#### Bookings

```http
GET /bookings/bookings/

POST /bookings/bookings/

GET /bookings/bookings/{id}/

PUT /bookings/bookings/{id}/

PATCH /bookings/bookings/{id}/

DELETE /bookings/bookings/{id}/  
```
#### Gyms

```http
GET /gyms/gyms/

POST /gyms/gyms/

GET /gyms/gyms/{id}/

PUT /gyms/gyms/{id}/

PATCH /gyms/gyms/{id}/

DELETE /gyms/gyms/{id}/
```
#### Schedules

```http
GET /schedules/schedules/

POST /schedules/schedules/

GET /schedules/schedules/{id}/

PUT /schedules/schedules/{id}/

PATCH /schedules/schedules/{id}/

DELETE /schedules/schedules/{id}/
```
#### Trainers

```http
GET /trainers/trainers/

POST /trainers/trainers/

GET /trainers/trainers/{id}/

PUT /trainers/trainers/{id}/

PATCH /trainers/trainers/{id}/

DELETE /trainers/trainers/{id}/

```
#### Users

```http
GET /users/users/

POST /users/users/

GET /users/users/{id}/

PUT /users/users/{id}/

PATCH /users/users/{id}/

DELETE /users/users/{id}/

```