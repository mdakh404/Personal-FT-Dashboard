#!/usr/bin/python3
# author: x.com/mdakh404_

import streamlit as st
import pandas as pd

# Streamlit session state initialization
if "incomes" not in st.session_state:
    st.session_state.incomes = None 
if "expenses" not in st.session_state:
    st.session_state.expenses = None  
if "mode" not in st.session_state:
    st.session_state.mode = None     

main_sidebar = st.sidebar.selectbox('Select Appropriate Functionality',
                                    ('Setup', 'Incomes', 'Expenses')
                                    )

if main_sidebar == 'Setup':
    #TODO: edit the help string
    incomes_file = st.file_uploader(label="Upload your income data (CSV or XLS).",
                                    type=["csv", "xls", "xlsx"],
                                    help="Upload your income data in CSV or XLS format. The file size must not exceed 20 MB. \
                                          Make sure the file follows the required structure.", 
                                    width=500     
                                    )
    
    st.markdown(
    """
    <div style="margin-top: 20px; margin-bottom: 20px;">
        <hr>
    </div>
    """,
    unsafe_allow_html=True)

    expenses_file = st.file_uploader(label="Upload your expenses data (CSV or XLS).",
                                     type=["csv", "xls", "xlsx"],
                                     help="Upload your expense data in CSV or XLS format. The file size must not exceed 20 MB. \
                                           Make sure the file follows the required structure.",
                                    width=500      
                                    )
    
    st.markdown(
    """
    <div style="margin-top: 40px; margin-bottom: 60px;">
    </div>
    """,
    unsafe_allow_html=True)

    tracking_mode = st.selectbox("Tracking Mode", ('Monthly', 'Yearly'), width=150)

    st.markdown(
    """
    <div style="margin-bottom: 60px;">
    </div>
    """,
    unsafe_allow_html=True)

    upload_btn = st.button("Upload", type="primary")
    
    if upload_btn:
        if incomes_file is not None:
            st.session_state.incomes = pd.read_csv(incomes_file) if incomes_file.name.endswith('.csv') else pd.read_excel(incomes_file)
        else:
            st.warning("Please upload your income data.")
        if expenses_file is not None:
            st.session_state.expenses = pd.read_csv(expenses_file) if expenses_file.name.endswith('.csv') else pd.read_excel(expenses_file)
        else:
            st.warning("Please upload your expense data.")
        
        st.session_state.mode = tracking_mode
        
elif main_sidebar == 'Incomes':
    if st.session_state.incomes is not None:
        st.dataframe(st.session_state.incomes)
        st.write(st.session_state.mode) # remove this 
    else:
        st.warning("Please upload your income data first.")
        st.write(st.session_state.mode) # remove this 

elif main_sidebar == 'Expenses':
    if st.session_state.expenses is not None:
        st.dataframe(st.session_state.expenses)
        st.write(st.session_state.mode) # remove this 

    else:
        st.warning("Please upload your expense data first.")
        st.write(st.session_state.mode) # remove this 
 
