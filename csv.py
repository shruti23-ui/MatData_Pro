import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Streamlit setup
st.set_page_config(page_title="MatData Pro 2.0", layout="wide")
st.title("MatData Pro 2.0")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

# Initialize filtered_df to None or an empty DataFrame
filtered_df = pd.DataFrame()  # Create an empty DataFrame to avoid NameError

if uploaded_file is not None:
    # Read CSV file into DataFrame
    df = pd.read_csv(uploaded_file)

    # Show data preview and basic info
    st.write("Data Preview:")
    st.write(df.head())
    
    st.write("Data Summary:")
    st.write(df.describe())

    # Data cleaning options
    st.sidebar.header("Data Cleaning")
    if st.sidebar.checkbox("Drop Duplicates"):
        df.drop_duplicates(inplace=True)
        st.write("Duplicates dropped")

    if st.sidebar.checkbox("Fill Missing Values"):
        fill_option = st.sidebar.selectbox("Fill with:", ["Mean", "Median", "Mode"])
        if fill_option == "Mean":
            df.fillna(df.mean(), inplace=True)
        elif fill_option == "Median":
            df.fillna(df.median(), inplace=True)
        elif fill_option == "Mode":
            df.fillna(df.mode().iloc[0], inplace=True)
        st.write("Missing values filled with", fill_option)

    # Filter data
    st.write("Filter Data:")
    filter_columns = st.multiselect("Select columns to filter by", df.columns)
    filtered_df = df  # Initialize filtered_df with the original DataFrame

    for col in filter_columns:
        if df[col].dtype == 'object':
            filter_value = st.text_input(f"Enter text for {col} filter")
            if filter_value:
                filtered_df = filtered_df[filtered_df[col].str.contains(filter_value, case=False, na=False)]
        else:
            min_val, max_val = st.slider(f"Select range for {col}", float(df[col].min()), float(df[col].max()), (float(df[col].min()), float(df[col].max())))
            filtered_df = filtered_df[(filtered_df[col] >= min_val) & (filtered_df[col] <= max_val)]

    st.write("Filtered Data:")
    st.write(filtered_df)

    # Ensure that filtered_df is defined before proceeding
    if not filtered_df.empty:
        # Column selection for visualizations
        st.sidebar.header("Visualizations")
        columns = filtered_df.columns

        # Histogram
        st.sidebar.subheader("Histogram")
        hist_column = st.sidebar.selectbox("Select a column for histogram", columns)
        if hist_column:
            st.write(f"Histogram of {hist_column}")
            fig, ax = plt.subplots()
            sns.histplot(filtered_df[hist_column], kde=True, ax=ax)
            st.pyplot(fig)

        # Bar plot
        st.sidebar.subheader("Bar Plot")
        bar_column = st.sidebar.selectbox("Select a column for bar plot", columns)
        if bar_column:
            st.write(f"Bar Plot of {bar_column}")
            fig, ax = plt.subplots()
            filtered_df[bar_column].value_counts().plot(kind='bar', ax=ax, color='skyblue')
            st.pyplot(fig)

        # Scatter plot
        st.sidebar.subheader("Scatter Plot")
        x_col = st.sidebar.selectbox("Select x-axis column", columns)
        y_col = st.sidebar.selectbox("Select y-axis column", columns)
        if x_col and y_col:
            st.write(f"Scatter Plot of {x_col} vs {y_col}")
            fig, ax = plt.subplots()
            sns.scatterplot(x=filtered_df[x_col], y=filtered_df[y_col], ax=ax)
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            st.pyplot(fig)

        # Box plot
        st.sidebar.subheader("Box Plot")
        box_column = st.sidebar.selectbox("Select a column for box plot", columns)
        if box_column:
            st.write(f"Box Plot of {box_column}")
            fig, ax = plt.subplots()
            sns.boxplot(y=filtered_df[box_column], ax=ax)
            st.pyplot(fig)

        # Correlation Heatmap
        st.write("Correlation Heatmap:")
        corr = filtered_df.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

        # Save heatmap image for download
        heatmap_img_data = BytesIO()
        plt.savefig(heatmap_img_data, format='png')
        heatmap_img_data.seek(0)  # Reset the buffer to the beginning

        # Download option for heatmap image
        st.download_button(
            label="Download Heatmap Image",
            data=heatmap_img_data,
            file_name="correlation_heatmap.png",
            mime="image/png"
        )

        # Download options
        st.write("Download Processed Data:")
        download_option = st.selectbox("Select file format", ["CSV", "Excel"])
        if download_option == "CSV":
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(label="Download CSV", data=csv, file_name="processed_data.csv", mime="text/csv")
        else:
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:  # Use openpyxl instead of xlsxwriter
                filtered_df.to_excel(writer, index=False, sheet_name="Sheet1")
            output.seek(0)
            st.download_button(label="Download Excel", data=output, file_name="processed_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.warning("No data available after filtering.")
else:
    st.info("Upload a CSV file to get started.")
 # type: ignore
