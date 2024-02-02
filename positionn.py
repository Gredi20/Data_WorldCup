import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

award_winners = pd.read_csv('silver/award_winners_new.csv')
squads = pd.read_csv('silver/squads_new.csv')

merged_data = pd.merge(award_winners, squads, on='player_id', how='inner')

position_award_data = merged_data[['position_name', 'award_name']]

st.title('Total Awards for Each Position')

st.write("Merged Data:")
st.write(merged_data.head())

st.write("\nExtracted Data:")
st.write(position_award_data.head())

position_awards_count = position_award_data.groupby(['position_name', 'award_name']).size().reset_index(name='total_awards_count')

st.write("\nTotal Awards Count by Position and Award:")
st.write(position_awards_count)

fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='position_name', y='total_awards_count', hue='award_name', data=position_awards_count, ax=ax)
ax.set_title('Total Awards for Each Position and Award')
ax.set_xlabel('Position Name')
ax.set_ylabel('Total Number of Awards')
ax.legend(title='Award Name', bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(fig)
