from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime

# Function to create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password_hash=user.password_hash,
        role="employee"  # Default role or use your business logic for roles
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Function to get a user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

# Function to get a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Function to get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Function to create a new invoice
def create_invoice(db: Session, invoice: schemas.InvoiceCreate, user_id: int):
    db_invoice = models.Invoice(
        user_id=user_id,
        client_name=invoice.client_name,
        amount=invoice.amount,
        due_date=invoice.due_date,
        status=invoice.status or "pending",  # Default status if none provided
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

# Function to get all invoices for a user
def get_invoices_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).filter(models.Invoice.user_id == user_id).offset(skip).limit(limit).all()

# Function to get all invoices
def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).offset(skip).limit(limit).all()

# Function to create a payroll
def create_payroll(db: Session, payroll: schemas.PayrollCreate, employee_id: int):
    db_payroll = models.Payroll(
        employee_id=employee_id,
        salary_amount=payroll.salary_amount,
        month=payroll.month,
        status=payroll.status or "generated",  # Default status if none provided
    )
    db.add(db_payroll)
    db.commit()
    db.refresh(db_payroll)
    return db_payroll

# Function to get all payrolls for an employee
def get_payrolls_by_employee(db: Session, employee_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Payroll).filter(models.Payroll.employee_id == employee_id).offset(skip).limit(limit).all()

# Function to get all payrolls
def get_payrolls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payroll).offset(skip).limit(limit).all()

# Function to create a bank transaction
def create_bank_transaction(db: Session, transaction: schemas.BankTransactionCreate, invoice_id: int):
    db_transaction = models.BankTransaction(
        invoice_id=invoice_id,
        transaction_date=transaction.transaction_date or datetime.utcnow(),  # Default to current timestamp if none provided
        amount=transaction.amount,
        bank_name=transaction.bank_name,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

# Function to get all bank transactions for an invoice
def get_bank_transactions_by_invoice(db: Session, invoice_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.BankTransaction).filter(models.BankTransaction.invoice_id == invoice_id).offset(skip).limit(limit).all()

# Function to get all bank transactions
def get_bank_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BankTransaction).offset(skip).limit(limit).all()

