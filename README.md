# # Cloud-based Accounting System

## Project Overview

The **Cloud-based Accounting System** is a web application designed to manage accounting tasks such as invoicing, payroll management, and financial transaction recording. It is built using FastAPI for the backend and Streamlit for the frontend, with a cloud-first approach for scalability and ease of deployment. This system integrates secure user authentication, real-time data updates, and a dynamic user interface to simplify financial operations for businesses.

## Features

- **User Authentication**: Secure user login and registration with role-based access control (Admin, Employee).
- **Invoice Management**: Create, manage, and track invoices including amounts, clients, and due dates.
- **Payroll Management**: Manage employee payroll, including salary generation, deductions, and history.
- **Bank Transaction Recording**: Record and track payments, including linking invoices with bank transactions.
- **Real-Time Data**: The system allows for real-time updates to track the status of invoices, payroll, and transactions.
- **Data Visualization**: Intuitive dashboards to view and analyze financial data.
- **Secure Communication**: All communications between the frontend and backend are encrypted to prevent unauthorized access.

## Tech Stack

- **Backend**:
  - FastAPI: Modern, fast web framework for building APIs with Python 3.7+.
  - SQLAlchemy: ORM for interacting with the SQLite database.
  - Pydantic: Data validation and settings management.
  - Docker: Containerization for easy deployment.
  
- **Frontend**:
  - Streamlit: A tool to create beautiful, interactive web apps for data science and machine learning.

- **Database**:
  - SQLite: A lightweight, serverless, self-contained database for storing accounting records.

- **Authentication**:
  - bcrypt: For hashing passwords securely.
  - JWT (JSON Web Tokens): For secure authentication and token-based access control.

- **Cloud Infrastructure**:
  - Docker and Docker Compose: For containerization and multi-container orchestration.
