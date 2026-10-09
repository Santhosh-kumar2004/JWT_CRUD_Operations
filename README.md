# JWT CRUD Operations using FastAPI

## About the Project

This is a simple Employee Management API built using FastAPI and PostgreSQL.

This project helps us to learn how to create APIs, connect a database, register users, log in users, and protect APIs using JWT authentication.

Users can register and log in to the application. After successful login, they can use the employee APIs with a valid access token.

This project is useful for beginners who want to learn FastAPI, PostgreSQL, CRUD operations, and JWT authentication.

## Features

* User registration
* User login
* Password hashing
* JWT token generation
* JWT token verification
* Add employee details
* Get all employee details
* Get one employee by ID
* Update employee details
* Delete employee details
* PostgreSQL database connection
* API testing using Swagger UI

## Technologies Used

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Psycopg2
* JWT Authentication
* Passlib and Bcrypt
* Python-dotenv
* Uvicorn
* Swagger UI

## What is CRUD?

CRUD means four basic operations used to manage data.

* **Create:** Add new employee details.
* **Read:** Get employee details.
* **Update:** Change existing employee details.
* **Delete:** Remove employee details.

## What is JWT Authentication?

JWT means JSON Web Token.

It is used to check whether a user has a valid login token before accessing protected APIs.

The authentication process works like this:

1. A new user registers with a username and password.
2. The password is stored as a hash in the database.
3. The user logs in with the correct username and password.
4. The application creates a JWT access token.
5. The user sends the token when accessing protected APIs.
6. The application checks the token.
7. If the token is valid, the API can continue processing the request.

If the token is missing, invalid, or expired, the API returns an authentication error.

## Project Requirements

Before running this project, install the following:

* Python 3.10 or above
* PostgreSQL
* VS Code or another Python editor
* Git
* Basic knowledge of Python and SQL

## Project Setup

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/Santhosh-kumar2004/JWT_CRUD_Operations.git
```

Go inside the project folder:

```bash
cd JWT_CRUD_Operations
```

### Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If you use Command Prompt, run:

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install the Required Packages

Install all packages from the requirements file:

```bash
pip install -r requirements.txt
```

The requirements file contains the packages needed for the project.

### Step 4: Create a PostgreSQL Database

Open PostgreSQL using pgAdmin or the PostgreSQL terminal.

Create a database:

```sql
CREATE DATABASE employee_db;
```

Use the database name in your database connection settings.

Make sure PostgreSQL is running before starting the application.

### Step 5: Configure the Environment Variables

Create a file named `.env` in the project root folder.

Add the following values:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/employee_db
SECURITY_KEY=replace_with_a_long_random_secret
ALGORITHM=HS256
EXPIRE_MINUTES=30
```

Replace `your_password` with your PostgreSQL password.

Use your project's actual database variable name if it is different from `DATABASE_URL`.

**Important:**

* Keep your `.env` file private.
* Do not upload your real database password or secret key to GitHub.
* Use a strong, random secret key.
* The secret key and algorithm must remain the same when creating and verifying tokens.

### Step 6: Run the Application

If the FastAPI application file is `app/main.py`, run:

```bash
uvicorn app.main:app --reload
```

If your main application file is in another location, use the correct Python module path.

After starting the server, open:

http://127.0.0.1:8000/docs

This opens Swagger UI, where you can test the APIs.

## API Endpoints

The following endpoints are used in this project.

### 1. User Registration

**Method:** POST

**Endpoint:**

```text
/register
```

This API creates a new user account.

Example request body:

```json
{
  "User_Name": "testuser",
  "User_Password": "YourPassword123"
}
```

Use the exact field names defined in the `UserCreate` schema.

The password is hashed before it is stored in the database.

### 2. User Login

**Method:** POST

**Endpoint:**

```text
/login
```

Enter your username and password using the form fields provided by Swagger UI.

If the login details are correct, the API returns an access token.

Example response:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

The actual response depends on the login route implementation.

### 3. Get All Employees

**Method:** GET

**Endpoint:**

```text
/employees
```

This API returns the employee records from the database.

You can also use the optional `limit` parameter.

Example:

```text
/employees?limit=5
```

This requests up to five employee records.

### 4. Get One Employee

**Method:** GET

**Endpoint:**

```text
/employee/{employee_id}
```

This API returns one employee using the employee ID.

Example:

```text
/employee/1
```

Replace `1` with the required employee ID.

### 5. Add an Employee

**Method:** POST

**Endpoint:**

```text
/add
```

This API adds a new employee to the database.

Example request body:

```json
{
  "Employee_Name": "Santhosh",
  "Employee_Age": 22,
  "Employee_Gender": "Male",
  "Employee_Email": "santhosh@example.com",
  "Employee_Phone": "9876543210"
}
```

Use the exact field types and validation rules defined in your `EmployeeAdd` schema.

### 6. Update an Employee

**Method:** PUT

**Endpoint:**

```text
/update/{employee_id}
```

This API updates an existing employee.

Example:

```text
/update/1
```

Provide the employee ID and the request body required by the `EmployeeUpdate` schema.

### 7. Delete an Employee

**Method:** DELETE

**Endpoint:**

```text
/delete/{employee_id}
```

This API deletes an employee from the database.

Example:

```text
/delete/1
```

Replace `1` with the employee ID you want to delete.

**Note:** Employee endpoints require a valid JWT token.

## How to Test JWT Authentication in Swagger UI

Follow these steps to test the protected APIs.

1. Start the FastAPI application.
2. Open `http://127.0.0.1:8000/docs`.
3. Use the `/register` endpoint to create a user.
4. Use the `/login` endpoint to verify the username and password.
5. Click the **Authorize** button in Swagger UI.
6. Enter your username and password in the OAuth2 form.
7. Click Authorize and then Close.
8. Execute a protected employee endpoint.
9. If authentication succeeds, the API processes your request.

Swagger UI obtains and sends the token automatically when OAuth2 is configured correctly.

You do not normally need to paste the token manually into the OAuth2 username/password form.

## Common Errors

### 401 Unauthorized

This means the request could not pass authentication.

Possible reasons:

* The token is missing.
* The token is invalid.
* The token has expired.
* The secret key used to verify the token does not match.

**Solution:** Log in again and authorize Swagger UI with a new token.

### 404 Not Found

This means the requested employee was not found, or the URL does not match an existing route.

**Solution:** Check the employee ID and endpoint URL.

### Database Connection Error

This can happen when PostgreSQL is not running or the connection details are incorrect.

**Solution:** Check the database name, username, password, port, and connection URL.

### Module Not Found

This can happen if the required packages are not installed or the application is started using the wrong module path.

**Solution:** Activate the virtual environment, install the requirements, and check the Uvicorn command.

## Important Notes

* Do not share your database password or secret key.
* Do not commit your `.env` file to GitHub.
* Use a valid access token for protected APIs.
* An expired token must be replaced with a new token.
* This is a learning project. Review the security settings before using it in a real application.

## Learning Outcomes

By working with this project, beginners can learn:

* How to build REST APIs using FastAPI.
* How to connect FastAPI with PostgreSQL.
* How to use SQLAlchemy for database operations.
* How to implement CRUD operations.
* How to hash and verify passwords.
* How to create and verify JWT tokens.
* How to protect APIs using authentication.
* How to test APIs using Swagger UI.

## Author

**SANTHOSHKUMAR N**

GitHub: https://github.com/Santhosh-kumar2004

## Conclusion

This project is a simple example of building an employee management API with database operations and JWT authentication.

You can clone the repository, install the required packages, configure your PostgreSQL database, and run the application to learn how the different parts work together.
