import pandas as pd
import streamlit as st
import plotly.express as px

team_stats = pd.read_csv('gold/pie_chart_pjesa2_g.csv')

def main():
    st.title('Wins, Draws, and Losses by Team')

    selected_team_id = st.selectbox('Select Team by Team ID:', team_stats['team_id'].unique())

    selected_team_df = team_stats[team_stats['team_id'] == selected_team_id]

    fig = px.pie(selected_team_df, names=['wins', 'draws', 'losses'], values=[selected_team_df.iloc[0, selected_team_df.columns.get_loc('wins')], selected_team_df.iloc[0, selected_team_df.columns.get_loc('draws')], selected_team_df.iloc[0, selected_team_df.columns.get_loc('losses')]],
                 title=f'Wins, Draws, and Losses for Team {selected_team_id}')

    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
