import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    'title': [
        'Inception', 'The Matrix', 'Interstellar', 'The Prestige', 'The Dark Knight'
    ],
    'description': [
        'A thief who steals corporate secrets through dream-sharing technology.',
        'A hacker learns about the reality and fights in a computer simulation.',
        'A team travels through space to ensure humanity’s survival.',
        'Two magicians compete to create the ultimate illusion.',
        'Batman fights crime in Gotham City against the Joker.'
    ]
}

df = pd.DataFrame(data)

# Convert descriptions to feature vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Calculate cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# Recommend similar movies
def recommend(title, n=3):
    if title not in df['title'].values:
        print("Movie not found.")
        return
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    print(f"\nRecommendations for '{title}':")
    for i, score in sim_scores:
        print(f"- {df.iloc[i]['title']} (score: {score:.2f})")

# Example
recommend("Inception")