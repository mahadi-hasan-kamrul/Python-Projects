import streamlit as st  # type: ignore
import pandas as pd # type: ignore
import plotly.express as px  # type: ignore #make plots and graphs
import json
import os

st.set_page_config(page_title="Automate Finance Dashboard", page_icon="💰", layout="wide")

category_file = "categories.json"

#we are doing it to store ous categories. So that when we rerun the app, these categories will be there, not wiped away
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": [],
    }
#If we get any json file which has categories then we will load the file to get the categories
if os.path.exists(category_file):
    with open(category_file, "r") as f: #we are opening this in -r read mode
        st.session_state.categories = json.load(f)

def save_categories():
    with open(category_file, "w") as f: #we are opening this in -w write mode
        json.dump(st.session_state.categories, f)

def categorize_transactions(df):
    df["Category"] = "Uncategorized"
    for category, keywords in st.session_state.categories.items(): #getting the dictionary from categories.json
        if category == "Uncategorized" or not keywords:
            continue
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        for idx, row in df.iterrows():
            details = row["Details"].lower().strip()
            if details in lowered_keywords:
                df.at[idx, "Category"] = category
    return df

#with this function we are saving the exiting keywords which are not in the category file in the json file in categories
def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    
    return False

def load_transactions(file):
    try:
        df = pd.read_csv(file) #Reading the uploaded file with pandas
        df.columns = [col.strip() for col in df.columns] #capturing the columns of the file
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float) #adjusting some values
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y") #adjusting the date formate

        #st.write(df) #it will enable you to write in the uploaded file
        return categorize_transactions(df)
    except Exception as e:
        st.error(f"Error Processing File: {str(e)}")
        return None

def main():
    st.title("Automate Finance Dashboard")
    
    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        
        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()#we are creating a new data frame on the base of Debit
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()#we are creating a new data frame on the base of Credit
            st.session_state.debits_df = debits_df.copy()

            #tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"]) #Tabs will help us toggle between debit and credit
            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])
            with tab1:
                #we are creating new category with button and input list
                new_category = st.text_input("New Category Name")
                add_button = st.button("Add Category")
                if add_button and new_category:
                    if new_category not in st.session_state.categories: #we are saving it into session file as a new category
                        st.session_state.categories[new_category] = []
                        save_categories() #it will save categories into categories .json
                        st.rerun()
                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )
                
                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    for idx, row in edited_df.iterrows():
                        new_category = row["Category"]
                        if new_category == st.session_state.debits_df.at[idx, "Category"]:
                            continue
                        details = row["Details"]
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        add_keyword_to_category(new_category, details)

                        #with this we are creating the chart
                st.subheader('Expense Summary')
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)
                
                st.dataframe(
                    category_totals, 
                    column_config={
                     "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED")   
                    },
                    use_container_width=True,
                    hide_index=True
                )
                
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)

            with tab2:
                st.subheader("Payments Summary")
                total_payments = credits_df["Amount"].sum()
                st.metric("Total Payments", f"{total_payments:,.2f} AED")
                st.write(credits_df)

main()