import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv('gold/age_distribution_histograma_g.csv')

selected_team = st.sidebar.selectbox('Select Team:', df['team_id'].unique())

filtered_df = df[df['team_id'] == selected_team]

grouped_df = filtered_df.groupby(['team_id', 'age']).size().reset_index(name='total_players')

chart = alt.Chart(grouped_df).mark_bar().encode(
    alt.X('age:O', title='Age'),
    alt.Y('total_players:Q', title='Total Players'),
    tooltip=['age:O', 'total_players:Q']
).properties(
    title=f'Total Players for Each Age in Team {selected_team}',
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)


