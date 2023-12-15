import streamlit as st
import pandas as pd
import plotly.express as px

# Data Loading
@st.cache_data
def load_data():
    data = pd.read_csv('../data/Real_Estate_Sales_2001-2020_GL.csv')
    # Drop rows with null values
    data = data.dropna()
    # Find the index of the row with the highest 'Sale Amount'
    max_sale_index = data['Sale Amount'].idxmax()

    # Remove the row with the highest 'Sale Amount'
    data = data.drop(max_sale_index)
    return data

# Explore Data
def explore_data(data):
    st.header('Real Estate Data Analysis')
    
    # Filters and exploration
    st.subheader('Data Exploration')
    selected_property_type = st.selectbox('Select Property Type', data['Property Type'].unique())
    filtered_data = data[data['Property Type'] == selected_property_type]

    # Filter by Sale Amount
    sale_amount_min = st.slider('Minimum Sale Amount', min_value=int(data['Sale Amount'].min()), max_value=int(data['Sale Amount'].max()))
    sale_amount_max = st.slider('Maximum Sale Amount', min_value=sale_amount_min, max_value=int(data['Sale Amount'].max()))
    filtered_data = filtered_data[(filtered_data['Sale Amount'] >= sale_amount_min) & (filtered_data['Sale Amount'] <= sale_amount_max)]
    
    st.subheader('Filtered Data')
    st.write(f'Data for {selected_property_type} with Sale Amount between ${sale_amount_min} and ${sale_amount_max}:')
    st.dataframe(filtered_data)

    # Data visualizations
    st.subheader('Data Visualizations')
    st.plotly_chart(px.scatter(filtered_data, x='Assessed Value', y='Sale Amount', title='Assessed Value vs. Sale Amount'))
    
# Unique Data
def unique_data(data):
    st.header('Unique Data')
    st.write('Here are the unique values, data types, and potential values for each column in the dataset.')

    unique_info_df = pd.DataFrame(columns=['Column Name', 'Data Type', 'Definition', 'Potential Values'])
    for column in data.columns:
        data_type = data[column].dtype
        definition = ''
        potential_values = ', '.join(map(str, data[column].unique()[:5]))
        unique_info_df = unique_info_df.append({'Column Name': column, 'Data Type': data_type,
                                                'Definition': definition, 'Potential Values': potential_values}, ignore_index=True)

    st.dataframe(unique_info_df)

# Dynamic Plotting
def dynamic_plotting(data):
    st.header('Dynamic Plotting')
    st.write('Select X and Y columns to create a plot. Choose the plot type and customize your visualization.')

    x_column = st.selectbox('Select X-axis column:', data.columns)
    y_column = st.selectbox('Select Y-axis column:', data.columns)
    
    plot_type = st.selectbox('Select Plot Type:', ['Scatter', 'Line', 'Bar', 'Histogram'])

    if st.button('Create Plot'):
        if plot_type == 'Scatter':
            fig = px.scatter(data, x=x_column, y=y_column, title=f'{x_column} vs. {y_column}')
        elif plot_type == 'Line':
            fig = px.line(data, x=x_column, y=y_column, title=f'{x_column} vs. {y_column}')
        elif plot_type == 'Bar':
            fig = px.bar(data, x=x_column, y=y_column, title=f'{x_column} vs. {y_column}')
        elif plot_type == 'Histogram':
            num_bins = st.slider('Number of Bins', min_value=5, max_value=50, value=20)
            fig = px.histogram(data, x=x_column, y=y_column, nbins=num_bins, title=f'{x_column} vs. {y_column}')
        
        st.plotly_chart(fig)

        # Download the plot as an image
        if st.button('Download Plot as PNG'):
            fig.write_image('scatter_plot.png')
            st.markdown('[Download Plot](scatter_plot.png)')

# Main Application
def main():
    st.set_page_config(page_title='Real Estate Data Analysis', page_icon='✅')
    st.title('Real Estate Data Analysis')
    data = load_data()
    page = st.sidebar.selectbox('Select Page', ['Data Exploration', 'Unique Data', 'Dynamic Plotting'])
    
    if page == 'Data Exploration':
        explore_data(data)
    elif page == 'Unique Data':
        unique_data(data)
    elif page == 'Dynamic Plotting':
        dynamic_plotting(data)

if __name__ == '__main__':
    main()
