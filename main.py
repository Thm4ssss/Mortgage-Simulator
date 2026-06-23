import streamlit as st 
import src.functions as func 

st.title('Loan Repayment Simulator')

#Input Data Section
st.write('### Loan Conditions')
col1,col2=st.columns(2)
amount=col1.number_input("Amount borrowed (in €)",min_value=0,value=40000,step=1000)
interest_rate=col2.number_input("Interest rate (in %)",min_value=0.01,value=2.0,step=0.01)
loan_term=col1.number_input('Loan term (in years)',min_value=0,value=10)
deferred=col2.number_input('Deferred (in years)',min_value=0,value=0,max_value=loan_term-1)

#Compute and display repayment values
st.write('### Repayment Simulation')

##Compute values
monthly_rate=(interest_rate/100)/12
repayment_period=loan_term-deferred
monthly_repayment=func.monthly_payment(amount,monthly_rate,repayment_period*12)
deferred_monthly=func.deferred_monthly_payment(amount,monthly_rate,deferred)

total_deferred=func.total_deferred_amount(deferred*12,deferred_monthly)
total_payments=monthly_repayment*repayment_period*12+total_deferred
total_interests=total_payments-amount

##Display values
col1,col2=st.columns(2)
col1.metric('Monthly Repayments',f"{monthly_repayment:.1f}€",border=True)
col2.metric('Monthly Repayments Deferred Period',f"{deferred_monthly:.1f}€",border=True)
col1.metric('Total Payments',f"{total_payments:.1f}€",border=True)
col2.metric('Total Interests',f"{total_interests:.1f}€",border=True)