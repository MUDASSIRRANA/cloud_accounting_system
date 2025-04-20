import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Cloud Accounting System 💼")
menu = st.sidebar.selectbox("Menu", ["Users", "Invoices", "Payrolls", "Bank Transactions"])

# === USERS ===
if menu == "Users":
    st.subheader("👥 Users")

    if st.button("Load Users"):
        res = requests.get(f"{API_URL}/users/")
        if res.status_code == 200:
            for u in res.json():
                st.write(f"ID: {u['user_id']} | Name: {u['full_name']} | Email: {u['email']}")
        else:
            st.error("Failed to load users")

    st.markdown("---")
    st.subheader("➕ Add New User")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create User"):
        res = requests.post(f"{API_URL}/users/", json={
            "full_name": full_name,
            "email": email,
            "password": password
        })
        st.success("User created!" if res.status_code == 200 else "Failed to create user")

    st.markdown("---")
    st.subheader("❌ Delete User")
    user_delete_id = st.text_input("User ID to Delete")
    if st.button("Delete User"):
        res = requests.delete(f"{API_URL}/users/{user_delete_id}")
        st.success("User deleted!" if res.status_code == 200 else "Failed to delete user")

# === INVOICES ===
elif menu == "Invoices":
    st.subheader("📄 Invoices")
    if st.button("Load Invoices"):
        res = requests.get(f"{API_URL}/invoices/")
        if res.status_code == 200:
            for i in res.json():
                st.write(f"ID: {i['invoice_id']} | User: {i['user_id']} | Client: {i['client_name']} | Amount: {i['amount']} | Due: {i['due_date']} | Status: {i['status']}")
        else:
            st.error("Failed to load invoices")

    st.markdown("---")
    st.subheader("➕ Add New Invoice")
    user_id = st.text_input("User ID")
    client_name = st.text_input("Client Name")
    amount = st.number_input("Amount", min_value=0.0)
    due_date = st.text_input("Due Date (YYYY-MM-DD)")
    status = st.selectbox("Status", ["unpaid", "paid", "overdue"])

    if st.button("Create Invoice"):
        res = requests.post(f"{API_URL}/invoices/", json={
            "user_id": int(user_id),
            "client_name": client_name,
            "amount": amount,
            "due_date": due_date,
            "status": status
        })
        st.success("Invoice created!" if res.status_code == 200 else "Failed to create invoice")

    st.markdown("---")
    st.subheader("❌ Delete Invoice")
    invoice_delete_id = st.text_input("Invoice ID to Delete")
    if st.button("Delete Invoice"):
        res = requests.delete(f"{API_URL}/invoices/{invoice_delete_id}")
        st.success("Invoice deleted!" if res.status_code == 200 else "Failed to delete invoice")

# === PAYROLLS ===
elif menu == "Payrolls":
    st.subheader("💰 Payrolls")
    if st.button("Load Payrolls"):
        res = requests.get(f"{API_URL}/payrolls/")
        if res.status_code == 200:
            for p in res.json():
                st.write(f"ID: {p['payroll_id']} | User: {p['user_id']} | Salary: {p['salary']} | Month: {p['month']} | Status: {p['status']}")
        else:
            st.error("Failed to load payrolls")

    st.markdown("---")
    st.subheader("➕ Add New Payroll")
    employee_id = st.text_input("Employee ID")
    salary_amount = st.number_input("Salary Amount", min_value=0.0)
    month = st.text_input("Month")
    status = st.selectbox("Status", ["paid", "unpaid"])

    if st.button("Create Payroll"):
        res = requests.post(f"{API_URL}/payrolls/", json={
            "employee_id": int(employee_id),
            "salary_amount": salary_amount,
            "month": month,
            "status": status
        })
        st.success("Payroll added!" if res.status_code == 200 else "Failed to add payroll")

    st.markdown("---")
    st.subheader("❌ Delete Payroll")
    payroll_delete_id = st.text_input("Payroll ID to Delete")
    if st.button("Delete Payroll"):
        res = requests.delete(f"{API_URL}/payrolls/{payroll_delete_id}")
        st.success("Payroll deleted!" if res.status_code == 200 else "Failed to delete payroll")

# === BANK TRANSACTIONS ===
elif menu == "Bank Transactions":
    st.subheader("🏦 Bank Transactions")
    if st.button("Load Transactions"):
        res = requests.get(f"{API_URL}/transactions/")
        if res.status_code == 200:
            for t in res.json():
                st.write(f"ID: {t['transaction_id']} | Invoice: {t['user_id']} | Date: {t['date']} | Amount: {t['amount']} | Bank: {t['bank']}")
        else:
            st.error("Failed to load transactions")

    st.markdown("---")
    st.subheader("➕ Add New Transaction")
    invoice_id = st.text_input("Invoice ID")
    transaction_date = st.text_input("Transaction Date (YYYY-MM-DD HH:MM:SS)")
    amount = st.number_input("Amount", min_value=0.0)
    bank_name = st.text_input("Bank Name")

    if st.button("Create Transaction"):
        res = requests.post(f"{API_URL}/transactions/", json={
            "invoice_id": int(invoice_id),
            "transaction_date": transaction_date,
            "amount": amount,
            "bank_name": bank_name
        })
        st.success("Transaction added!" if res.status_code == 200 else "Failed to add transaction")

    st.markdown("---")
    st.subheader("❌ Delete Transaction")
    transaction_delete_id = st.text_input("Transaction ID to Delete")
    if st.button("Delete Transaction"):
        res = requests.delete(f"{API_URL}/transactions/{transaction_delete_id}")
        st.success("Transaction deleted!" if res.status_code == 200 else "Failed to delete transaction")
