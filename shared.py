import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

award_winners = pd.read_csv('silver/award_winners_new.csv')

award_winners['year'] = award_winners['tournament_id'].str.extract(r'(\d{4})', expand=False)

shared_award_winners = award_winners[award_winners['shared'] == 1]

shared_awards_count = shared_award_winners.groupby('year').size().reset_index(name='count')

st.title('Shared Awards Count Over Years')

st.write("Shared Awards Count Data:")
st.write(shared_awards_count.head())

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(shared_awards_count['year'], shared_awards_count['count'])

ax.set_title('Quantity of Shared Instances for Each Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Shared Instances')

st.pyplot(fig)
