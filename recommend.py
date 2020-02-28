import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

##Step 1: Read CVS File
df = pd.read_csv("movie_dataset.csv")
# print(df.columns)

## step2: Select Features
features = ['keywords', 'cast', 'genres', 'director']

# step3: Create a column in DF which combines all selected features

def combine_features(row):
    try:
        return row['keywords'] +" "+row['cast']+" "+row['genres']+" "+row['director']
    except:
        print("Error: ", row)

df['combined_features'] = df.apply(combine_features, axis=1)
print(df['combined_features'].head())

##Step 4: Create count matrix from this new combined column


##Step 5: Compute the cosine Similarity on the count_matrix

movie_user_likes = "Avatar"