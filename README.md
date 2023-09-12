# User Management API Documentation

Welcome to the User Management API documentation. This API allows you to create, retrieve, update, and delete user records. There are two main endpoints:

1. `CreateUser`: Used for creating new user records via a POST request.
2. `getUser`: Used for retrieving, updating, or deleting user records via GET, PUT, or DELETE requests with ID.

## Table of Contents

1. [API Endpoints](#[api-endpoints](https://hngbackendtask2.onrender.com/api/))
    1. [`CreateUser`]([#createuser-endpoint](https://hngbackendtask2.onrender.com/api/create/))
    2. [`getUser`](#[getuser-endpoint](https://hngbackendtask2.onrender.com/api/user/id/))
2. [Request/Response Formats](#requestresponse-formats)
3. [Usage Examples](#usage-examples)

## 1. API Endpoints

### 1.1. `CreateUser` Endpoint

- **Endpoint:** `POST /[CreateUser](https://hngbackendtask2.onrender.com/api/create/)/`
- **Description:** Create a new user record.
- **Request Format:**

  ```json
  {
      "name": "John Doe"
  }
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
  


1.2. getUser Endpoint
Endpoint: GET, PUT, DELETE /user/

Description: Retrieve, update, or delete user records based on id.

Request Format (GET):
To retrieve user details by id, make a GET request with the id:
GET https://hngbackendtask2.onrender.com/api/user/id/

Request Format (PUT):
To update user details by id, make a PUT request with the id:
PUT https://hngbackendtask2.onrender.com/api/user/id/

Request Format (DELETE):
To delete a user by id, make a DELETE request with the id:
DELETE https://hngbackendtask2.onrender.com/api/user/id/

2. Request/Response Formats:
All API endpoints accept and return data in JSON format.
Request and response bodies should be valid JSON objects.

3. Usage Examples:
   
Creating a User
curl -X POST (https://hngbackendtask2.onrender.com/api/create/) -d '{"name": "Fakorede Olamide"}' -H "Content-Type: application/json"

Retrieve user details by ID
curl  -X GET (https://hngbackendtask2.onrender.com/api/user/id/)

Updating user details by ID
curl  -X PUT (https://hngbackendtask2.onrender.com/api/user/id/)

Deleting user detaiols by ID
curl  -X DELETE (https://hngbackendtask2.onrender.com/api/user/id/)

This documentation provides an overview of the User Management API, including endpoints, request/response formats, and usage examples
If you have any questions or encounter any issues while using this API, please contact our support team at support@example.com.
Thank you for using our User Management API!


