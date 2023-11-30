import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv('yoyo_cleaned_data.csv')

st.title("Yoyo Data Application")
st.write("The yoyo data found in this application was scraped from yoyoexperts webiste of current string trick yoyos for sale. Note that the underlying dataset is not comprehensive.")

show_names = st.checkbox("Show All Yoyo Names")
if show_names:
    st.write("List of Yoyo Names (Click to Expand):")
    st.write(df['name'].tolist())

selected_name = st.text_input('Enter a yoyo name', 'Pragma') # Default is John
name_df = df[df['name'] == selected_name]

if name_df.empty:
    st.write('Name not found')
else:
    # Scatter plot for all yoyos of the same brand
    brand_name = name_df['brand'].iloc[0]  # Assuming there's only one brand for the selected yoyo
    brand_df = df[df['brand'] == brand_name]
    fig = px.scatter(brand_df, x='price', y='weight in grams',
                     color_discrete_sequence=px.colors.qualitative.Set1,
                     title=f'Price vs Weight Plot for {selected_name} and All {brand_name} Brand Yoyos')

    # Scatter plot for the selected yoyo (overlay)
    if not name_df.empty:
        fig.add_trace(px.scatter(name_df, x='price', y='weight in grams').data[0])

    # Display the combined scatter plot
    st.plotly_chart(fig)

    st.write(f"### Yoyo Specs:")

    st.write(f"# {selected_name}")


    specs_order = ['description', 'price', 'brand', 'weight in grams', 'bearing size',
        'response', 'material group', 'designed in', 'made in',
        'machined in', 'released', 'diameter mm', 'width mm', 'gap width mm']

    for spec in specs_order:
        if spec in name_df.columns and not pd.isna(name_df[spec].iloc[0]):
            st.write(f"**{spec.capitalize()}:** {name_df[spec].iloc[0]}")


    show_table = st.checkbox("Show Full Table")
    if show_table:
        st.write(f"# Full Table")
        st.table(name_df)