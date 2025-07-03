import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import hashlib

st.set_page_config(
    page_title="CGBank - Coimbatore Trusted Banking Partner",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2a5298;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .account-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .transaction-item {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2a5298 0%, #1e3c72 100%);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'users' not in st.session_state:
    st.session_state.users = {
        'Rahul': {
            'password': hashlib.md5('password123'.encode()).hexdigest(),
            'name': 'Rahul',
            'account_number': '1234567890',
            'balance': 15750.50,
            'account_type': 'Savings'
        },
        'cravin': {
            'password': hashlib.md5('mypassword'.encode()).hexdigest(),
            'name': 'cravin',
            'account_number': '0987654321',
            'balance': 8320.75,
            'account_type': 'Checking'
        }
    }

if 'transactions' not in st.session_state:
    st.session_state.transactions = []
    for i in range(20):
        transaction = {
            'date': datetime.now() - timedelta(days=random.randint(1, 30)),
            'description': random.choice(['ATM Withdrawal', 'MEESHO BILL', 'Salary Credit', 'HDB/FINANCE', ' Rahul Transfer', 'CAR Credit']),
            'amount': round(random.uniform(-500, 1000), 2),
            'balance': round(random.uniform(1000, 20000), 2)
        }
        st.session_state.transactions.append(transaction)
 
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
 
def login_page():
    st.markdown("""
    <div class="main-header">
        <h1>🏦 CGBank</h1>
        <h3>Coimbatore Trusted Banking Partner</h3>
        <h4>Secure • Reliable • Innovative</h4>
        <p>174/2 Avinasi road,Annai statue,Coimbatore-641029</p>
        <p>Contact:+91-63820-74060</p>
        <p>Email:Cgbankcbe@gmail.com</p>
        <h5>Welcome to CGBank! Your trusted partner in banking services.We are committed to providing you with secure and innovative banking</h5> 
        <p>HELPLINE:1800-123-4506</p>
    </div>
    """, unsafe_allow_html=True)
   
    col1, col2, col3 = st.columns([1, 2, 1])
   
    with col2:
        st.markdown("###  Login to Your Account")
       
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Login", use_container_width=True)
           
            if submitted:
                if username in st.session_state.users:
                    if st.session_state.users[username]['password'] == hash_password(password):
                        st.session_state.logged_in = True
                        st.session_state.current_user = username
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid password!")
                else:
                    st.error("Username not found!")
       
        st.markdown("---")
        st.markdown("**DEMO ACCOUNTS:**")
        st.info("Username: Sowandarya, Password: password123")
        st.info("Username: Ayush, Password: mypassword")
 
def dashboard():
    user = st.session_state.users[st.session_state.current_user]
    st.markdown(f"""
    <div class="main-header">
        <h1>Welcome back, {user['name']}! 👋</h1>
        <p>Account: {user['account_number']} | {user['account_type']} Account</p>
    </div>
    """, unsafe_allow_html=True)
   
    col1, col2, col3, col4, col5= st.columns(5)
   
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #2a5298;">💰 Account Balance</h3>
            <h2 style="color: #28a745;">₹""" + f"{user['balance']:,.2f}" + """</h2>
        </div>
        """, unsafe_allow_html=True)
   
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #2a5298;">📊 This Month</h3>
            <h2 style="color: #17a2b8;">₹2,340.50</h2>
            <p style="color: #28a745;">↑ +12.5%</p>
        </div>
        """, unsafe_allow_html=True)
   
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #2a5298;">💳 Available Credit</h3>
            <h2 style="color: #6f42c1;">₹5,000.00</h2>
        </div>
        """, unsafe_allow_html=True)
   
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #2a5298;">🎯 Savings Goal</h3>
            <h2 style="color: #fd7e14;">75%</h2>
            <p>₹15,000 / ₹20,000</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col5:
        st.markdown("""
         <div class="metric-card">
            <h3 style="color: #2a5298;">About bank</h3>
            <h2 style="color: #fd7e14;">75%</h2>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")            
                    
   
    st.markdown("### ⚡ Quick Actions")
    col1, col2, col3, col4 , col5 = st.columns(5)
   
    with col1:
        if st.button("💸 Transfer Money", key="dashboard_transfer", use_container_width=True):
            st.session_state.page = "transfer"
            st.rerun()
   
    with col2:
        if st.button("💰 Pay Bills", key="dashboard_bills", use_container_width=True):
            st.session_state.page = "bills"
            st.rerun()
   
    with col3:
        if st.button("📊 View Statements", key="dashboard_statements", use_container_width=True):
            st.session_state.page = "statements"
            st.rerun()
   
    with col4:
        if st.button("🎯 Set Goals", key="dashboard_goals", use_container_width=True):
            st.session_state.page = "goals"
            st.rerun()
    with col5:
        if st.button("  About",key="dashboard_about",use_container_width=True):
            st.session_state.page="about"
            st.rerun()

    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("### 📈 Spending Overview")
        # Generate sample spending data
        categories = ['Food', 'Travel', 'Movie', 'Bills', 'Shopping', 'Healthcare']
        amounts = [450, 320, 180, 890, 260, 120]
       
        fig = px.pie(values=amounts, names=categories, title="Monthly Spending by Category")
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
   
    with col2:
        st.markdown("### 📊 Account Balance Trend")
        dates = [datetime.now() - timedelta(days=i) for i in range(30, 0, -1)]
        balances = [user['balance'] + random.uniform(-1000, 1000) for _ in dates]
       
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=balances, mode='lines+markers', name='Balance'))
        fig.update_layout(title="30-Day Balance History", xaxis_title="Date", yaxis_title="Balance (₹)")
        st.plotly_chart(fig, use_container_width=True)
 
def transactions_page():
    st.markdown("### 📋 Recent Transactions")
   
    col1, col2, col3 = st.columns(3)
    with col1:
        date_filter = st.date_input("From Date", value=datetime.now() - timedelta(days=30))
    with col2:
        amount_filter = st.selectbox("Amount Range", ["All", "< ₹100", "₹100 - ₹500", "> ₹500"])
    with col3:
        type_filter = st.selectbox("Transaction Type", ["All", "Credit", "Debit"])
   
    for i, transaction in enumerate(st.session_state.transactions[:10]):
        color = "#28a745" if transaction['amount'] > 0 else "#dc3545"
        sign = "+" if transaction['amount'] > 0 else ""
       
        st.markdown(f"""
        <div class="transaction-item">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h4 style="margin: 0; color: #2a5298;">{transaction['description']}</h4>
                    <p style="margin: 0; color: #6c757d; font-size: 0.9em;">{transaction['date'].strftime('%Y-%m-%d %H:%M')}</p>
                </div>
                <div style="text-align: right;">
                    <h3 style="margin: 0; color: {color};">{sign}₹{abs(transaction['amount']):,.2f}</h3>
                    <p style="margin: 0; color: #6c757d; font-size: 0.9em;">Balance: ₹{transaction['balance']:,.2f}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
 
def transfer_page():
    st.markdown("### 💸 Transfer Money")
   
    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("#### Transfer Details")
        with st.form("transfer_form"):
            recipient = st.text_input("Recipient Account", placeholder="Enter account number")
            amount = st.number_input("Amount (₹)", min_value=0.01, step=0.01)
            description = st.text_input("Description (Optional)", placeholder="What's this for?")
            submitted = st.form_submit_button("Transfer", use_container_width=True)
           
            if submitted:
                if amount > 0 and recipient:
                    st.success(f"Transfer of ₹{amount:,.2f} to {recipient} initiated successfully!")
                    new_transaction = {
                        'date': datetime.now(),
                        'description': f'Transfer to {recipient}',
                        'amount': -amount,
                        'balance': st.session_state.users[st.session_state.current_user]['balance'] - amount
                    }
                    st.session_state.transactions.insert(0, new_transaction)
                    st.session_state.users[st.session_state.current_user]['balance'] -= amount
                else:
                    st.error("Please enter valid transfer details!")
   
    with col2:
        st.markdown("#### Recent Recipients")
        recent_recipients = ["cravin (0987654321)", "rahul (1122334455)", "karthik (5566778899)"]
        for i, recipient in enumerate(recent_recipients):
            if st.button(f"📤 {recipient}", key=f"recipient_{i}", use_container_width=True):
                st.info(f"Selected: {recipient}")
 
def bills_page():
    st.markdown("### 💰 Pay Bills")
   
    bills = [
        {"name": "WATER BILL", "amount": 1156.78, "due": "2025-06-25", "status": "Due Soon"},
        {"name": "Airtel Recharge", "amount": 328.99, "due": "2025-06-28", "status": "Upcoming"},
        {"name": "LIC HOUSING/FINANCE", "amount": 17450.50, "due": "2025-07-01", "status": "Upcoming"},
    
    ]
   
    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("#### Upcoming Bills")
        for i, bill in enumerate(bills):
            status_color = "#ffc107" if bill["status"] == "Due Soon" else "#28a745"
            st.markdown(f"""
            <div class="transaction-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0;">{bill['name']}</h4>
                        <p style="margin: 0; color: #6c757d;">Due: {bill['due']}</p>
                    </div>
                    <div style="text-align: right;">
                        <h4 style="margin: 0; color: #dc3545;">₹{bill['amount']:,.2f}</h4>
                        <span style="color: {status_color}; font-size: 0.8em;">{bill['status']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
           
            if st.button(f"Pay ₹{bill['amount']:,.2f}", key=f"pay_bill_{i}", use_container_width=True):
                st.success(f"Payment of ₹{bill['amount']:,.2f} for {bill['name']} processed successfully!")
   
    with col2:
        st.markdown("#### Pay New Bill")
        with st.form("bill_form"):
            biller = st.selectbox("Select Biller", ["Electricity Company", "Water Department", "Gas Company", "Internet Provider", "Other"])
            if biller == "Other":
                custom_biller = st.text_input("Enter Biller Name")
            account_num = st.text_input("Account Number")
            bill_amount = st.number_input("Amount (₹)", min_value=0.01, step=0.01)
            submitted = st.form_submit_button("Pay Bill", use_container_width=True)
           
            if submitted and bill_amount > 0:
                st.success(f"Bill payment of ₹{bill_amount:,.2f} processed successfully!")
def About_page():
       st.markdown("#### About")
       about=["""1. KYC Compliance (Know Your Customer)
Mandatory under AML (Anti-Money Laundering) laws.

Requires:

Proof of Identity (e.g., Aadhaar, Passport, Driving License)

Proof of Address

Recent Photograph

2. Minimum Balance Requirement
Some savings accounts require a minimum monthly balance.

Non-maintenance may attract charges.

3. Transaction Limits
Daily withdrawal and transfer limits (especially for online banking, ATMs).

Regulated by RBI (India) or FDIC/FinCEN (US), etc.

4. Interest Rates and Charges
Banks must disclose:

Interest on savings/current/fixed accounts

Loan interest rates

Processing fees, penalties, etc.

5. Confidentiality and Privacy
Customer data is protected under banking secrecy laws.

Banks cannot share your financial data without consent, except with authorized authorities.

6. Account Monitoring and Reporting
Suspicious activity is reported to authorities (e.g., FIU-IND in India, FinCEN in the US).

Large transactions (over ₹10 lakh or $10,000) may be reported automatically.

7. Dormant Accounts
Accounts inactive for over 2 years may be marked dormant.

Requires re-KYC or written request to reactivate.

8. No Discrimination
Banks cannot discriminate based on caste, religion, gender, age, or economic status.

📝 Steps to Open a Bank Account
🔹 Step 1: Choose the Type of Account
Savings Account

Current Account (for business)

Fixed Deposit / Recurring Deposit

Student or Senior Citizen Accounts

🔹 Step 2: Visit the Bank or Apply Online
Most banks offer online applications via their websites or mobile apps.

You may also visit a nearby branch.

🔹 Step 3: Fill the Account Opening Form
Provide personal details, nominee information, and select services (ATM, internet banking, cheque book, etc.).

🔹 Step 4: Submit KYC Documents
ID Proof (e.g., Aadhaar, Passport)

Address Proof (Utility bill, Aadhaar, etc.)

Photographs

PAN Card (mandatory for Indian accounts)

🔹 Step 5: Initial Deposit
Some accounts require an initial deposit to open the account (e.g., ₹500 or $50).

Zero-balance accounts like Jan Dhan Yojana in India don't need this.

🔹 Step 6: Verification
Bank will verify documents and your identity.

May involve a quick in-person or video KYC.

🔹 Step 7: Receive Welcome Kit
Includes: passbook, debit card, cheque book, and customer ID.

You'll also get login credentials for online banking."""

]
def logout():
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.session_state.page = "dashboard"
    st.rerun()
 
def main():
    if not st.session_state.logged_in:
        login_page()
    else:

        with st.sidebar:
            st.markdown("### 🏦 CGBank Navigation")
           
            if st.button("🏠 Dashboard", key="sidebar_dashboard", use_container_width=True):
                st.session_state.page = "dashboard"
                st.rerun()
           
            if st.button("📋 Transactions", key="sidebar_transactions", use_container_width=True):
                st.session_state.page = "transactions"
                st.rerun()
           
            if st.button("💸 Transfer", key="sidebar_transfer", use_container_width=True):
                st.session_state.page = "transfer"
                st.rerun()
           
            if st.button("💰 Pay Bills", key="sidebar_bills", use_container_width=True):
                st.session_state.page = "bills"
                st.rerun()
            if st.button("About", key="sidebar_about", use_container_width=True):
                st.session_state.page = "about"
                st.rerun()
            st.markdown("---")
           
            user = st.session_state.users[st.session_state.current_user]
            st.markdown(f"**Login UserName:** {user['name']}")
            st.markdown(f"**Account Number:** {user['account_number']}")
           
            if st.button("🚪 Logout", key="sidebar_logout", use_container_width=True):
                logout()
       
        if 'page' not in st.session_state:
            st.session_state.page = "dashboard"
       
        if st.session_state.page == "dashboard":
            dashboard()
        elif st.session_state.page == "transactions":
            transactions_page()
        elif st.session_state.page == "transfer":
            transfer_page()
        elif st.session_state.page == "bills":
            bills_page()
 
if __name__ == "__main__":
    main()