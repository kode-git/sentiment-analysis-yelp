
import pandas as pd

# data paths
business_json_path = 'yelp_dataset/yelp_academic_dataset_business.json'
review_json_path =  'yelp_dataset/yelp_academic_dataset_review.json'

# loading business_json
df_b = pd.read_json(business_json_path, lines=True) # business_json dataframe
df_c = df_b.columns.values # business_json columns

# Cleaning business_json
# 1 = open, 0 = closed, we need to maintain only the open business because the closed one are irrelevant
df_b = df_b[df_b['is_open'] == 1]

# Drop not used columns: hours, is_open, 'review_count'
df_b = df_b.drop(['hours', 'is_open', 'review_count'], axis=1)


df_categories = df_b.assign(categories=df_b.categories.str.split(', ')).explode('categories')

# Taking only restaurants from the business_json
df_restaurants = df_categories[df_categories['categories'].str.contains('Restaurants', na=False)]


