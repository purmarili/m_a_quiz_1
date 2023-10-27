import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file
df = pd.read_csv('to_spotify_songs.csv')

# 2. Extract desired rows and columns
# Let's assume you want rows from index 5 to 10 for the columns "daily_rank" and "weekly_movement"
subset_df = df.loc[5:10, ['daily_rank', 'weekly_movement']]

# 3. Assign indexing to a specific column
# Setting "daily_rank" as the index
df.set_index('daily_rank', inplace=True)

# 4. Create a filter based on 2 parameters
# Filtering where daily_rank is less than 20 and weekly_movement is greater than 0
filtered_df = df[(df.index < 20) & (df['weekly_movement'] > 0)]

# 5. Sort the table using 2 parameters
# Sorting by 'daily_rank' in ascending order and 'weekly_movement' in descending order
sorted_df = df.sort_values(['daily_rank', 'weekly_movement'], ascending=[True, False])

# 6. Use statistical functions
mean_val = df['weekly_movement'].mean()
std_val = df['weekly_movement'].std()
median_val = df['weekly_movement'].median()
min_val = df['weekly_movement'].min()
max_val = df['weekly_movement'].max()

# 7. Build 2 different types of graphs
# Bar chart for weekly_movement distribution
df['weekly_movement'].value_counts().plot(kind='bar')
plt.title('Distribution of Weekly Movement')
plt.show()

# Line chart for daily rank vs weekly movement
df.reset_index(inplace=True)
plt.plot(df['daily_rank'], df['weekly_movement'], marker='o')
plt.title('Daily Rank vs Weekly Movement')
plt.xlabel('Daily Rank')
plt.ylabel('Weekly Movement')
plt.show()
