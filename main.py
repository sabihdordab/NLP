from Classification import TextClassifier
from CollaborativeFiltering import SongRecommendationSystem
from PreProcessor import TextProcessor


if __name__ == "__main__":
    while True:
        print("\n--- Main Menu ---")
        print("1. Text Classification")
        print("2. Song Recommendation System")
        print("3. Text Processing")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Text Classification ---")
            classifier = TextClassifier()
            classifier.run()
        elif choice == "2":
            print("\n--- Song Recommendation System ---")
            recommender = SongRecommendationSystem()
            recommender.run()
        elif choice == "3":
            print("\n--- Text Processing ---")
            processor = TextProcessor()
            processor.menu()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
