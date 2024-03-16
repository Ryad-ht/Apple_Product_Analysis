import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##### Price Analysis #########################################################

# Load the data
apple_products = pd.read_csv('apple_products.csv')
# Calculate the discount amount
apple_products['Discount_Amount'] = apple_products['Mrp'] - apple_products['Sale Price']
# Plot the distribution of discount amounts
plt.figure(figsize=(10, 6))
apple_products['Discount_Amount'].hist(bins=50)
plt.title('Distribution of Discount Amounts')
plt.xlabel('Discount Amount')
plt.ylabel('Frequency')
plt.show()

##### Rating and Review Analysis #############################################

# Explore the relationship between sale price and star rating
sns.scatterplot(x='Sale Price', y='Star Rating', data=apple_products)
plt.title('Sale Price vs Star Rating')
plt.show()
# Explore the relationship between sale price and number of reviews
sns.scatterplot(x='Sale Price', y='Number Of Reviews', data=apple_products)
plt.title('Sale Price vs Number Of Reviews')
plt.show()

##### Discount Impact Study #################################################

# Investigate if higher discounts correlate with better ratings
sns.scatterplot(x='Discount_Percentage', y='Star Rating', data=apple_products)
plt.title('Discount Percentage vs Star Rating')
plt.show()
# Investigate if higher discounts correlate with more reviews
sns.scatterplot(x='Discount_Percentage', y='Number Of Reviews', data=apple_products)
plt.title('Discount Percentage vs Number Of Reviews')
plt.show()

##### Product Popularity #####################################################

# Assess which products are most popular based on the number of ratings
top_rated_products = apple_products.sort_values('Number Of Ratings', ascending=False).head(10)
sns.barplot(x='Number Of Ratings', y='Product Name', data=top_rated_products)
plt.title('Top 10 Most Rated Products')
plt.show()

##### Memory Configuration ###################################################

# Analyze pricing trends across different RAM configurations
sns.boxplot(x='Ram', y='Sale Price', data=apple_products)
plt.title('Sale Price by RAM Configuration')
plt.show()

##### Temporal Trends ###################################################

# Convert Sale_Date to datetime
apple_products['Sale_Date'] = pd.to_datetime(apple_products['Sale_Date'])
# Group data by month or year depending on the data
apple_products['Year'] = apple_products['Sale_Date'].dt.year
yearly_trends = apple_products.groupby('Year').agg({'Sale Price': 'mean', 'Number Of Ratings': 'sum'})
# Plot the trends over time
yearly_trends['Sale Price'].plot(title='Average Sale Price Over Time', ylabel='Average Sale Price')
plt.show()
yearly_trends['Number Of Ratings'].plot(title='Total Number of Ratings Over Time', ylabel='Number Of Ratings')
plt.show()
