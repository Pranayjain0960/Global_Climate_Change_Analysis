import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:/Users/hp/Downloads/global_temp.csv")
print(df.head())
print(df.shape)
#info
print(df.info())

# description:-
print(df.describe())

# Drop rows with missing values
df = df.dropna(subset=['year', 'co2', 'temperature_change_from_ghg'])

# Convert year to integer
df['year'] = df['year'].astype(int)

# Lineplot for temperature over years

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='temperature_change_from_ghg', color='tomato')
plt.title('Global Temperature Change from GHG Over Years')
plt.xlabel('Year')
plt.ylabel('Temperature Change (°C)')
plt.grid(True)
plt.show()

# insights:-The lineplot shows how the global temperature change attributed to greenhouse gases (GHG) has evolved from past years up to recent years.

# Scatterplot of CO2 vs temperature

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='co2', y='temperature_change_from_ghg', hue='year', palette='coolwarm')
plt.title('CO2 Emissions vs. Temperature Change from GHG')
plt.xlabel('CO2 Emissions (Million Tons)')
plt.ylabel('Temperature Change (°C)')
plt.show()

# insight:- The scatterplot shows individual data points of CO2 emissions versus temperature change, with points colored by year.

# Correlation

correlation = df['co2'].corr(df['temperature_change_from_ghg'])
print(f"Correlation between CO2 and Temperature Change: {correlation:.2f}")

# insight:- The correlation coefficient is 0.97 which means that there is strong positive relationship between CO2 and Temperature change.

# Correlation heatmap:- 

plt.figure(figsize=(6, 4))
sns.heatmap(df[['co2', 'temperature_change_from_ghg']].corr(), annot=True, cmap='YlGnBu')
plt.title("Correlation Heatmap")
plt.show()

# insight:- This heatmap confirms the numerical correlation, making it easy to see how strongly these two variables are related.