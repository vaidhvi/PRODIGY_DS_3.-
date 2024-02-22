import pandas as pd

# Load the traffic accident data
accident_data = pd.read_csv('traffic_accidents.csv')

# Display the first few rows of the dataset to understand its structure
print(accident_data.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the distribution of accidents by time of day
plt.figure(figsize=(10, 6))
sns.histplot(data=accident_data, x='Hour', bins=24, kde=True, color='skyblue')
plt.title('Distribution of Accidents by Time of Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

# Visualize the distribution of accidents by weather conditions
plt.figure(figsize=(10, 6))
sns.countplot(data=accident_data, x='Weather_Condition', order=accident_data['Weather_Condition'].value_counts().index[:10], palette='viridis')
plt.title('Distribution of Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Visualize the distribution of accidents by road conditions
plt.figure(figsize=(10, 6))
sns.countplot(data=accident_data, x='Road_Conditions', order=accident_data['Road_Conditions'].value_counts().index[:10], palette='magma')
plt.title('Distribution of Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()


import folium

# Create a map centered around the average latitude and longitude of accidents
accident_map = folium.Map(location=[accident_data['Latitude'].mean(), accident_data['Longitude'].mean()], zoom_start=10)

# Add markers for each accident location
for index, row in accident_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(accident_map)

# Display the map
accident_map.save('accident_hotspots.html')


import folium

# Create a map centered around the average latitude and longitude of accidents
accident_map = folium.Map(location=[accident_data['Latitude'].mean(), accident_data['Longitude'].mean()], zoom_start=10)

# Add markers for each accident location
for index, row in accident_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(accident_map)

# Display the map
accident_map.save('accident_hotspots.html')

# Visualize the distribution of accidents by contributing factors
plt.figure(figsize=(10, 6))
sns.countplot(data=accident_data, y='Contributing_Factor', order=accident_data['Contributing_Factor'].value_counts().index[:10], palette='rocket')
plt.title('Distribution of Accidents by Contributing Factors')
plt.xlabel('Number of Accidents')
plt.ylabel('Contributing Factor')
plt.show()

