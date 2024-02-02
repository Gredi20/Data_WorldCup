import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('gold/line_chart_g.csv')

selected_team = st.selectbox("Select Team", df['team_id'].unique())

selected_team_df = df[df['team_id'] == selected_team]

fig = px.line(selected_team_df, x='year', y=['goals_for', 'goals_against', 'points'],
              title=f'Stats Over Years for Team {selected_team}',
              labels={'value': 'Stats'},
              line_shape='linear')

st.plotly_chart(fig)
