from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()
DB = "test.db"

# User model
class User(BaseModel):
    full_name: str
    email: str
    password: str

# Invoice model
class Invoice(BaseModel):
    user_id: int
    client_name: str
    amount: float
    due_date: str
    status: str

# Payroll model
class Payroll(BaseModel):
    employee_id: int
    salary_amount: float
    month: str
    status: str

# Transaction model
class BankTransaction(BaseModel):
    invoice_id: int
    transaction_date: str
    amount: float
    bank_name: str

# === USERS ===
@app.get("/users/")
def get_users():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT user_id, full_name, email FROM users")
        rows = cur.fetchall()
        return [{"user_id": r[0], "full_name": r[1], "email": r[2]} for r in rows]

@app.post("/users/")
def create_user(user: User):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (full_name, email, password_hash, role, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
            (user.full_name, user.email, user.password, 'employee')
        )
        con.commit()
        return {"message": "User created"}

# === INVOICES ===
@app.get("/invoices/")
def get_invoices():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT invoice_id, user_id, client_name, amount, due_date, status FROM invoices")
        rows = cur.fetchall()
        return [{"invoice_id": r[0], "user_id": r[1], "client_name": r[2], "amount": r[3], "due_date": r[4], "status": r[5]} for r in rows]

@app.post("/invoices/")
def create_invoice(invoice: Invoice):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO invoices (user_id, client_name, amount, due_date, status, created_at) VALUES (?, ?, ?, ?, ?, datetime('now'))",
            (invoice.user_id, invoice.client_name, invoice.amount, invoice.due_date, invoice.status)
        )
        con.commit()
        return {"message": "Invoice created"}

# === PAYROLLS ===
@app.get("/payrolls/")
def get_payrolls():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT payroll_id, employee_id, salary_amount, month, status FROM payrolls")
        rows = cur.fetchall()
        return [{"payroll_id": r[0], "user_id": r[1], "salary": r[2], "month": r[3], "status": r[4]} for r in rows]

@app.post("/payrolls/")
def create_payroll(payroll: Payroll):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO payrolls (employee_id, salary_amount, month, status) VALUES (?, ?, ?, ?)",
            (payroll.employee_id, payroll.salary_amount, payroll.month, payroll.status)
        )
        con.commit()
        return {"message": "Payroll entry added"}

# === BANK TRANSACTIONS ===
@app.get("/transactions/")
def get_transactions():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT transaction_id, invoice_id, transaction_date, amount, bank_name FROM bank_transactions")
        rows = cur.fetchall()
        return [{"transaction_id": r[0], "user_id": r[1], "date": r[2], "amount": r[3], "bank": r[4]} for r in rows]

@app.post("/transactions/")
def create_transaction(tx: BankTransaction):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO bank_transactions (invoice_id, transaction_date, amount, bank_name) VALUES (?, ?, ?, ?)",
            (tx.invoice_id, tx.transaction_date, tx.amount, tx.bank_name)
        )
        con.commit()
        return {"message": "Transaction added"}
# === DELETE USERS ===
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        con.commit()
        return {"message": "User deleted"}

# === DELETE INVOICES ===
@app.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM invoices WHERE invoice_id = ?", (invoice_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Invoice not found")
        con.commit()
        return {"message": "Invoice deleted"}

# === DELETE PAYROLLS ===
@app.delete("/payrolls/{payroll_id}")
def delete_payroll(payroll_id: int):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM payrolls WHERE payroll_id = ?", (payroll_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Payroll not found")
        con.commit()
        return {"message": "Payroll deleted"}

# === DELETE BANK TRANSACTIONS ===
@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM bank_transactions WHERE transaction_id = ?", (transaction_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Transaction not found")
        con.commit()
        return {"message": "Transaction deleted"}
