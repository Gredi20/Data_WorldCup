import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

award_winners = pd.read_csv('silver/award_winners_new.csv')

award_winners['shared'] = pd.to_numeric(award_winners['shared'], errors='coerce')

awards_by_nationality = award_winners.groupby('team_name')['shared'].sum().reset_index(name='total_awards_won')

st.title('Total Awards Won by Nationality')

st.write("Total Awards Won by Nationality:")
st.write(awards_by_nationality)

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(awards_by_nationality['team_name'], awards_by_nationality['total_awards_won'])

ax.set_title('Quantity of Awards Won by State (Nationality)')
ax.set_xlabel('State (Nationality)')
ax.set_ylabel('Number of Awards Won')

ax.set_xticklabels(awards_by_nationality['team_name'], rotation=45, rotation_mode='anchor', ha='right')

st.pyplot(fig)
