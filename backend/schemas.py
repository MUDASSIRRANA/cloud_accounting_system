from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User schema
class UserBase(BaseModel):
    full_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models

# Invoice schema
class InvoiceCreate(BaseModel):
    client_name: str
    amount: float
    due_date: datetime
    status: Optional[str] = "pending"  # Default to "pending" if not provided

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models

class Invoice(InvoiceCreate):
    invoice_id: int
    created_at: datetime

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models

# Payroll schema
class PayrollCreate(BaseModel):
    salary_amount: float
    month: str
    status: Optional[str] = "generated"  # Default to "generated" if not provided

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models

class Payroll(PayrollCreate):
    payroll_id: int
    employee_id: int

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models

# Bank Transaction schema
class BankTransactionCreate(BaseModel):
    transaction_date: Optional[datetime] = datetime.utcnow()  # Default to current timestamp if not provided
    amount: float
    bank_name: str

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models

class BankTransaction(BankTransactionCreate):
    transaction_id: int
    invoice_id: int

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models
