# FastAPI MySQL Docker Project

This API is built using python fastapi and it interacts with the database using sqlachemy client. `dockerfile` and `docker-compose.yml` file are given and used to run both api and the database.

## Features

- **Create Employee**: Add a new employee with a name and salary.
- **Update Employee**: Update an employee's details.
- **Delete Employee**: Remove an employee record.
- **MySQL Integration**: Uses MySQL as the database to store employee records.
- **Dockerized**: Easily set up and run using Docker and Docker Compose.

## Project Structure

```
main.py               # Main FastAPI application
requirements.txt      # Project dependencies
.env                  # Environment variables
.env.sample           # Sample environment file with variable names
Dockerfile            # Dockerfile for the FastAPI app
docker-compose.yml    # Docker Compose configuration
```

## Prerequisites
- **Python 3.x**
- **Docker**
- **Docker Compose**

## Setting Up Environment Variables

1. **Copy `.env.sample` to `.env`**:


2. **Edit `.env`** and fill in the required values:

   ```env
   DATABASE_URL=mysql+mysqlconnector://<user>:<your_password>@db:3306/employees_db
   DB_HOST=db
   DB_USER=<user>
   MYSQL_ROOT_PASSWORD=<your_password>
   DB_NAME=employees_db
   ```

   Replace `<user>` and `<your_password>` with your chosen user and its password for MySQL.

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd fast_api_task
   ```

2. **Build and Start the Application**:

   Use Docker Compose to build and start the containers:
   **Note:** Incase if the below command doesn't work make sure to run along with sudo.

   ```bash
   docker compose up --build
   ```

3. **Access the API**:

   Once the containers are running, the FastAPI application will be accessible at `http://localhost:8000`.

## API Endpoints

- **Create Employee**: `POST /employees/`
  - **Body**: `{ "employee_name": "John Doe", "employee_salary": 50000 }`
  - **Response** :` {
      "id": 1,
      "employee_name": "John Doe",
      "employee_salary": 50000
    }`
- **Update Employee**: `PUT /employees/`
  - **Body**: `{ "id": 1, "employee_name": "Jane Doe", "employee_salary": 55000 }`
  - **Request Body**:`{
      "id": 1,
      "employee_name": "Jane Doe",
      "employee_salary": 60000
    }`
- **Delete Employee**: `DELETE /employees/{employee_id}`
  - **Response**: `    {
      "detail": "Employee deleted"
    }`

## Stopping the Application

To stop the application, run:

```bash
docker compose down
```
