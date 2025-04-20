from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default="employee")
    created_at = Column(DateTime, default=datetime.utcnow)  # Automatically set timestamp on creation

    invoices = relationship("Invoice", back_populates="user")  # Establishing the relationship with Invoice
    payrolls = relationship("Payroll", back_populates="employee")  # Establishing the relationship with Payroll

class Invoice(Base):
    __tablename__ = "invoices"
    invoice_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    client_name = Column(String)
    amount = Column(DECIMAL(10, 2))
    due_date = Column(DateTime)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)  # Automatically set timestamp on creation

    user = relationship("User", back_populates="invoices")  # Establishing the relationship with User
    bank_transactions = relationship("BankTransaction", back_populates="invoice")  # Relationship with BankTransaction

class Payroll(Base):
    __tablename__ = "payrolls"
    payroll_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.user_id"))
    salary_amount = Column(DECIMAL(10, 2))
    month = Column(String)
    status = Column(String, default="generated")
    created_at = Column(DateTime, default=datetime.utcnow)  # Automatically set timestamp on creation

    employee = relationship("User", back_populates="payrolls")  # Relationship with User

class BankTransaction(Base):
    __tablename__ = "bank_transactions"
    transaction_id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.invoice_id"))
    transaction_date = Column(DateTime, default=datetime.utcnow)  # Automatically set timestamp on creation
    amount = Column(DECIMAL(10, 2))
    bank_name = Column(String)

    invoice = relationship("Invoice", back_populates="bank_transactions")  # Relationship with Invoice

