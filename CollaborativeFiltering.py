import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import lil_matrix
import pandas as pd

class SongRecommendationSystem:
    def __init__(self, file_path="Dataset/Collaborative Filtering/Songs Dataset Truncated.csv", limit=10000):
        self.file_path = file_path
        self.limit = limit
        self.data = self.load_data()
        self.users, self.songs, self.user_to_idx, self.song_to_idx = self.create_mappings()
        self.num_users = len(self.users)
        self.num_songs = len(self.songs)
        self.utility_matrix = self.build_utility_matrix()
        self.mean_centered_matrix, self.user_means = self.center_matrix()
        self.similarity_matrix = cosine_similarity(self.mean_centered_matrix)

    def load_data(self):
        df = pd.read_csv(self.file_path, nrows=self.limit)
        df.columns = ['user_id', 'song_id', 'rating']
        return df

    def create_mappings(self):
        """
        Creates index mappings for user IDs and song IDs to optimize matrix operations.
        For example:
        If user_ids are [1001, 1008] and song_ids are ['S55', 'S42']:
        - user_to_idx will be {1001: 0, 1008: 1}
        - song_to_idx will be {'S55': 0, 'S42': 1}
        """
        users = sorted(self.data['user_id'].unique())
        songs = sorted(self.data['song_id'].unique())
        user_to_idx = {user: idx for idx, user in enumerate(users)}
        song_to_idx = {song: idx for idx, song in enumerate(songs)}
        return users, songs, user_to_idx, song_to_idx

    def build_utility_matrix(self):
        matrix = lil_matrix((self.num_users, self.num_songs), dtype=np.float32)
        for _, row in self.data.iterrows():
            user_idx = self.user_to_idx[row['user_id']]
            song_idx = self.song_to_idx[row['song_id']]
            matrix[user_idx, song_idx] = row['rating']
        return matrix.tocsr()

    def center_matrix(self):
        # For each user, the mean of their valid (non-zero) ratings is calculated and subtracted from all of their ratings.
        # The formula used is:
        #   centered_rating(u, i) = rating(u, i) - mean(u)
        # Where:
        #   - rating(u, i) is the rating given by user 'u' for song 'i',
        #   - mean(u) is the average rating of user 'u' for all the songs they rated,
        #   - centered_rating(u, i) is the user's rating for song 'i' after subtracting their average rating.
        # This centers the ratings for each user around zero.
        mean_centered = self.utility_matrix.copy().astype(np.float32)
        user_means = np.zeros(self.num_users, dtype=np.float32)

        for i in range(self.num_users):
            ratings = self.utility_matrix[i].toarray().flatten()
            valid_ratings = ratings[ratings != 0]

            if valid_ratings.size > 0:
                mean = valid_ratings.mean()
                user_means[i] = mean
                for j in range(len(ratings)):
                    if ratings[j] != 0:
                        mean_centered[i, j] -= mean

        return mean_centered, user_means

    def get_similar_users(self, user_idx, top_n=3):
        similarities = self.similarity_matrix[user_idx]
        similar_users = sorted([(idx, sim) for idx, sim in enumerate(similarities)], key=lambda x: x[1], reverse=True)
        return [(self.users[idx], sim) for idx, sim in similar_users[1:top_n + 1]]

    def recommend_for_user(self, user_id, k):
        user_idx = self.user_to_idx.get(user_id)
        if user_idx is None:
            print(f"User {user_id} not found.")
            return

        user_ratings = self.mean_centered_matrix[user_idx].toarray().flatten()
        top_similar_users = self.get_similar_users(user_idx, top_n=k)

        print(f"Top {k} similar users to {user_id}:")
        for similar_user, sim in top_similar_users:
            print(f"User {similar_user}: Similarity = {sim:.4f}")

        unrated_songs = [idx for idx, rating in enumerate(user_ratings) if rating == 0]
        predicted_ratings = []

        for song_idx in unrated_songs:
            weighted_sum = 0
            total_similarity = 0

            for similar_user, sim in top_similar_users:
                similar_user_idx = self.user_to_idx[similar_user]
                similar_ratings = self.mean_centered_matrix[similar_user_idx].toarray().flatten()

                if similar_ratings[song_idx] != 0:
                    weighted_sum += sim * similar_ratings[song_idx]
                    total_similarity += sim

            if total_similarity > 0:
                predicted_score = weighted_sum / total_similarity
                predicted_ratings.append((self.songs[song_idx], predicted_score))

        predicted_ratings.sort(key=lambda x: x[1], reverse=True)

        print(f"\nPredicted ratings for {user_id}:")
        for song, score in predicted_ratings:
            print(f"Song {song}: Predicted Rating = {score:.4f}")

    def run(self):
        try:
            user_id = int(input("Enter your user ID: "))
            k = int(input("How many similar users would you like to consider? "))
            self.recommend_for_user(user_id, k)
        except ValueError:
            print("Please enter valid numeric values.")

if __name__ == "__main__":
    recommender = SongRecommendationSystem()
    recommender.run()
