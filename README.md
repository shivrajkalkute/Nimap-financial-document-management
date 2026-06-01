# Financial Documents Management API

## Overview

Financial Documents Management API is a simple backend application developed using FastAPI and SQLite. The application allows users to upload and manage financial documents through REST APIs.

This project demonstrates fundamental backend development concepts such as API development, database integration, file handling, and document management.

---

## Features

* Upload financial documents
* Store document information in SQLite database
* View uploaded documents
* REST API endpoints using FastAPI
* Automatic API documentation with Swagger UI

---

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## Project Structure

financial-document-management/

├── main.py

├── database.py

├── models.py

├── auth.py

├── requirements.txt

└── README.md

---

## Installation

Clone the repository:

```bash
git clone https://github.com/shivrajkalkute/Nimap-financial-document-management.git
cd Nimap-financial-document-management
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run on:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Available APIs

### Home Endpoint

```http
GET /
```

Returns application status.

### Upload Document

```http
POST /upload-document
```

Uploads a document to the server.

### View Documents

```http
GET /documents
```

Returns all uploaded documents.

---

## Database

The project uses SQLite for storing document information.

Document fields:

* id
* title
* file_path
* uploaded_by

---

## Author

Shivraj Kalkute
