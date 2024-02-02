import pandas as pd
import streamlit as st
import plotly.express as px


result_df = pd.read_csv('gold/pie_chart_pjesa1_g.csv')

result_df['percentage_goals'] = result_df['total_goals'] / result_df['total_goals'].sum() * 100

def main():
    st.title('Percentage of Goals by Position')

    st.table(result_df[['position', 'total_goals']])

    fig = px.pie(result_df, names='position', values='percentage_goals', title='Percentage of Goals by Position')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
