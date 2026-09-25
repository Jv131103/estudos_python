import matplotlib.pyplot as plt
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

movies = pd.read_csv("./IA/Sistemas_de_Recomendacao/movies.csv")
ratings = pd.read_csv("./IA/Sistemas_de_Recomendacao/ratings.csv")

final_dataset = ratings.pivot(index='movieId', columns='userId', values='rating')
print(final_dataset.head())

final_dataset.fillna(0, inplace=True)

no_user_voted = ratings.groupby('movieId')['rating'].agg('count')
no_movies_voted = ratings.groupby('userId')['rating'].agg('count')

f, ax = plt.subplots(1, 1, figsize=(16, 4))
plt.scatter(no_user_voted.index, no_user_voted, color='mediumseagreen')
plt.axhline(y=10, color='r')
plt.xlabel('MovieId')
plt.ylabel('No. of users voted')
plt.show()

final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index, :]

f, ax = plt.subplots(1, 1, figsize=(16, 4))
plt.scatter(no_movies_voted.index, no_movies_voted, color='mediumseagreen')
plt.axhline(y=50, color='r')
plt.xlabel('UserId')
plt.ylabel('No. of votes by user')
plt.show()

final_dataset = final_dataset.loc[:, no_movies_voted[no_movies_voted > 50].index]
print(final_dataset)

csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)

knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)


def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies[movies['title'].str.contains(movie_name)]
    if len(movie_list):
        movie_idx = movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId'] == movie_idx].index[0]

        distances , indices = knn.kneighbors(csr_data[movie_idx], n_neighbors=n_movies_to_reccomend + 1)
        rec_movie_indices = sorted(
            zip(indices.flatten().tolist(), distances.flatten().tolist()),
            key=lambda x: x[1],
            reverse=True
        )[1:]
        recommend_frame = []

        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_idx].index
            recommend_frame.append({'Title': movies.iloc[idx]['title'].values[0], 'Distance': val[1]})
        df = pd.DataFrame(recommend_frame, index=range(1, n_movies_to_reccomend + 1))
        return df
    else:
        return "No movies found. Please check your input"


print(get_movie_recommendation("Jurassic Park"))
