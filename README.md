# User Management API Documentation

Welcome to the User Management API documentation. This API allows you to create, retrieve, update, and delete user records. There are two main endpoints:

1. `CreateUser`: Used for creating new user records via a POST request.
2. `getUser`: Used for retrieving, updating, or deleting user records via GET, PUT, or DELETE requests with ID.

## Table of Contents

1. Installation
2. [API Endpoints](#[api-endpoints](https://hngbackendtask2.onrender.com/api/))
    1. [`CreateUser`]([#createuser-endpoint](https://hngbackendtask2.onrender.com/api/create/))
    2. [`getUser`](#[getuser-endpoint](https://hngbackendtask2.onrender.com/api/user/id/))
2. [Request/Response Formats](#requestresponse-formats)
4. [Usage Examples](#usage-examples)

## 1. Installation
     1. Installation
     Make sure you have Django and Django REST framework installed in your project. If not, you can install them using pip:
     pip install django djangorestframework

    2. Configure Django Settings
    Make sure your Django project is configured properly. Ensure that the INSTALLED_APPS in your settings.py includes your 
    app, and the database is set up.

    4. Create a Model
    You should have a model for the User. Make sure it is defined in your models.py file.

    5. Create a Serializer
    Create a serializer for your User model. The serializer will be used for data validation and 
    serialization/deserialization.

    6. Create Views
    One view for creating user and one for retrieving, updating and deleting user in the Django app's views.py file.

    7. Define URLs
    Define the API URLs in your app's urls.py. You can include them in your project's main URL configuration if needed.

    from django.urls import path
    from . import views

    urlpatterns = [
    path('api/create/', views.CreateUser),
    path('api/user/<int:id>/', views.getUser),
    ]

    8. Run Migrations
    Run database migrations to create the User model table.
    python manage.py makemigrations
    python manage.py migrate

    9. Start the Development Server
    Start the development server to test your API.
    python manage.py runserver


## 2. API Endpoints

### 2.1. `CreateUser` Endpoint

- **Endpoint:** `POST /(https://hngbackendtask2.onrender.com/api/create/)/`
- **Description:** Create a new user record.
- **Request Format:**

  ```json
  Response Format(Success):
  {
    "Message": "User Created",
    "data": {
        "id": 1,
        "name": "Fakorede Olamide"
    }
  Response Format(Error):
  {
    "Message": "User Not Created",
     "data": {
        "name": [
            "This field is required."
        ]
    }

  }
}
  


### 2.2. `getUser` Endpoint
- **Endpoint**: `GET, PUT, DELETE (https://hngbackendtask2.onrender.com/api/user/)`

- **Description**: Retrieve, update, or delete user records based on id.

- **Request Format** (GET):
To retrieve user details by id, make a GET request with the id:
GET https://hngbackendtask2.onrender.com/api/user/id/

- **Request Format** (PUT):
To update user details by id, make a PUT request with the id:
PUT https://hngbackendtask2.onrender.com/api/user/id/

- **Request Format** (DELETE):
To delete a user by id, make a DELETE request with the id:
DELETE https://hngbackendtask2.onrender.com/api/user/id/

## 3. Request/Response Formats:
All API endpoints accept and return data in JSON format.
Request and response bodies should be valid JSON objects.
The API responses follow a consistent format:
Successful responses (status code 201 for creating user and 200 for retrieving user) include a Message and a data field.
Error responses (status code 400) include a Message and an error field.


## 4. Usage Examples:
- **Creating a User**:
  Send a POST request to https://hngbackendtask2.onrender.com/api/create/
 - Example Request:
    Content-Type: application/json
    ```json
    {
    "name": "fakorede olamide",
    }
    ```
- **Retrieving a User**:
  Send a GET request to https://hngbackendtask2.onrender.com/api/user/{id}/ to retrieve a user by their ID.
  - Example Request:
    GET https://hngbackendtask2.onrender.com/api/user/1/

- **Updating a User**:
  Send a PUT request to https://hngbackendtask2.onrender.com/api/user/{id}/ with updated user data in the request body to 
  update a user by their ID.
 - Example Request:
    PUT https://hngbackendtask2.onrender.com/api/user/1/
    Content-Type: application/json
    ```json
    {
    "name": "afeez olamide"
    }
    ```

- **Deleting a User**:
  Send a DELETE request to /api/users/{id}/ to delete a user by their ID.
  - Example Request:
    DELETE https://hngbackendtask2.onrender.com/api/user/1/

This documentation provides an overview of the User Management API, including endpoints, request/response formats, and usage examples
If you have any questions or encounter any issues while using this API, please contact our support team at faccojr00@gmail.com.
Thank you for using our User Management API!





