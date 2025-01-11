import os
import json
import math

class TextClassifier:
    def __init__(self):
        self.project_dir = "Dataset/Classification-Train And Test"
        self.result_dir = "Result/Classification"

        # Define classes based on dataset folders
        self.classes = ['Comp.graphics', 'rec.autos', 'sci.electronics', 'soc.religion.christian', 'talk.politics.mideast'] 

        
        self.class_data = {} # Dictionary to store classes information
        self.unique_words = set()  # Unique vocabulary
        self.total_vocab_size = 0  # Total size of the vocabulary

    def load_dataset(self):
        total_documents = 0
        for class_name in self.classes:
            path = os.path.join(self.project_dir, class_name)
            files_list = os.listdir(path)

            self.class_data[class_name] = {
                "word_count": 0,  # Total words in this class 
                "prior_probability": 0.0,  # Prior probability of the class
                # Formula: P(class) = (Number of documents in class) / (Total number of documents)

                "word_frequencies": {},  # Word frequency : count of each word in the class
                }

            for file in files_list:
                if file == "test":
                    continue
                if file.endswith('.txt'):
                    with open(os.path.join(path, file), 'r') as txt_file:
                        words = txt_file.read().split()
                        # Update word count and frequencies for this class
                        self.class_data[class_name]["word_count"] += len(words)
                        for word in words:
                            self.class_data[class_name]["word_frequencies"][word] = (
                                self.class_data[class_name]["word_frequencies"].get(word, 0) + 1
                            )
                        self.unique_words.update(words)
                        total_documents += 1

        # Calculate prior probabilities for each class
        for class_name in self.classes:
            path = os.path.join(self.project_dir, class_name)
            files_list = os.listdir(path)
            document_count = len(files_list) - 1  # Exclude the "test" folder
            self.class_data[class_name]["prior_probability"] = document_count / total_documents

        self.total_vocab_size = len(self.unique_words)

    def save_statistics(self):
        """
        Saves the statistics including the unique vocabulary, class probabilities,
        and word distributions for each class to files.
        """
        dictionary_path = os.path.join(self.result_dir, 'dictionary.txt')
        with open(dictionary_path, 'w') as dictionary_file:
            dictionary_file.write('\n'.join(self.unique_words))
            dictionary_file.write(f'\n{self.total_vocab_size}')

        # Save class data (probabilities and word distributions)
        class_data_path = os.path.join(self.result_dir, 'class_data.json')
        with open(class_data_path, 'w') as data_file:
            json.dump(self.class_data, data_file, indent=2)

    def classify_test_files(self):
        """
        Classifies the test files using the Naive Bayes formula and calculates accuracy.

        Formula used:
        P(class|document) = log(P(class)) + sum(log(P(word|class)))
        where:
        - P(class) is the prior probability of the class
        - P(word|class) = (frequency_of_word_in_class + 1) / (total_words_in_class + vocab_size) ...Laplace smoothing
        """
        classification_results = {}
        total_tests = 0 #for calculating accuracy
        correct_predictions = 0 #for calculating accuracy

        for test_class in self.classes:
            test_path = os.path.join(self.project_dir, test_class, 'test')
            test_files = os.listdir(test_path)
            for test_file in test_files:
                total_tests += 1
                file_class_probs = {} # Dictionary to store probabilities for each class for this test_file
                with open(os.path.join(test_path, test_file), 'r') as file:
                    test_words = file.read().split()
                for class_name in self.classes:
                    class_info = self.class_data[class_name]
                    # Start with log of prior probability
                    class_prob = math.log(class_info["prior_probability"]) # log(P(class))
                    # Add log probabilities for each word in the test file
                    #P(word∣class)= (frequency_of_word_in_class+1)/(total_words_in_class+vocab_size)
                    for word in test_words:
                        if word in class_info["word_frequencies"]:
                            word_freq = class_info["word_frequencies"][word] + 1
                        else:
                            word_freq = 1

                        class_prob += math.log(word_freq / (class_info["word_count"] + self.total_vocab_size)) # log(P(word|class))

                    file_class_probs[class_name] = class_prob

                
                predicted_class = sorted(file_class_probs.items(), key=lambda x: x[1], reverse=True)[0][0]
                correct_predictions += int(predicted_class == test_class)

                
                classification_results[test_file] = {
                    "predicted_class": predicted_class,
                    "actual_class": test_class,
                    "probabilities": file_class_probs,
                }

        
        results_path = os.path.join(self.result_dir, 'classification_results.txt')
        with open(results_path, 'w') as results_file:
            json.dump(classification_results, results_file, indent=2)

        
        accuracy = correct_predictions / total_tests
        print(f"Accuracy: {accuracy:.2%}")

