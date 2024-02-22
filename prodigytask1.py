import matplotlib.pyplot as plt

# Sample data for categorical variable (e.g., gender distribution)
categories = ['Male', 'Female', 'Non-Binary', 'Prefer not to say']
counts = [300, 350, 50, 20]  # Sample counts for each category

# Create bar chart
plt.bar(categories, counts, color='skyblue')

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender in Population')

# Display the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Sample data for continuous variable (e.g., age distribution)
np.random.seed(0)
ages = np.random.normal(loc=30, scale=10, size=1000)  # Sample ages from a normal distribution

# Create histogram
plt.hist(ages, bins=30, color='lightgreen', edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in Population')

# Display the plot
plt.show()
