import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Streamlit setup
st.set_page_config(page_title="MatData Pro", layout="wide")
st.title("MatData Pro")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV file into DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Show the first few rows of the dataframe
    st.write("Data Preview:")
    st.write(df.head())

    # Show basic information about the dataframe
    st.write("Data Summary:")
    st.write(df.describe())

    # Filter data
    st.write("Filter Data:")
    filter_column = st.selectbox("Select a column to filter", df.columns)
    filter_value = st.text_input(f"Enter value for {filter_column}")
    if filter_value:
        filtered_df = df[df[filter_column].astype(str).str.contains(filter_value, na=False)]
        st.write(f"Filtered Data:")
        st.write(filtered_df)
    else:
        filtered_df = df

    # Column selection for visualizations
    columns = filtered_df.columns

    # Generate and display a histogram of a selected column
    column = st.selectbox("Select a column for histogram", columns)
    if column:
        st.write(f"Histogram of {column}")
        fig, ax = plt.subplots()
        filtered_df[column].hist(ax=ax)
        st.pyplot(fig)
    
    # Generate and display a bar plot of a selected column
    bar_column = st.selectbox("Select a column for bar plot", columns)
    if bar_column:
        st.write(f"Bar Plot of {bar_column}")
        fig, ax = plt.subplots()
        filtered_df[bar_column].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    # Generate and display a scatter plot of selected columns
    x_col = st.selectbox("Select x-axis column for scatter plot", columns)
    y_col = st.selectbox("Select y-axis column for scatter plot", columns)
    if x_col and y_col:
        st.write(f"Scatter Plot of {x_col} vs {y_col}")
        fig, ax = plt.subplots()
        ax.scatter(filtered_df[x_col], filtered_df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)

    # Generate and display a correlation heatmap
    st.write("Correlation Heatmap:")
    corr = filtered_df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Download processed data
    st.write("Download Processed Data:")
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )
else:
    st.info("Upload a CSV file to get started.")
