import re
from nltk.stem import PorterStemmer
import os
import time
class TextProcessor:
    def __init__(self):
        self.text = ""
        self.DEFAULT_FILE_PATH_IN = "Dataset/TextProcessing/61085-0.txt"
        self.lower_pre_processed_text = False
        self.tokenize_method = "standard"

    def load_text(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
                return True
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return False
        except Exception as e:
            print(f"Error loading file: {str(e)}")
            return False
        
    def write_to_file(self, filename, content):
        try:
            if not content.strip():
                print("Warning: No content to write to file.")
                return
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Results saved to '{filename}'")
        except Exception as e:
            print(f"Error writing to file: {str(e)}")



    def tokenize(self, method="standard"):
        text = self.text
        tokens = []

        # URL pattern (handles www, http, https, and common domains)
        url_pattern = r'(?:https?:\/\/)?(?:www\.)?[\w\-\.]+\.[a-zA-Z]{2,}(?:\/\S*)?'

        # Split text into segments of URLs and non-URLs
        segments = re.split(f'({url_pattern})', text)

        for segment in segments:
            if re.match(url_pattern, segment):
                # If segment is a URL, add it as a single token
                tokens.append(segment)
            else:
                segment = re.sub(r"([^\w\s'-])", r" \1 ", segment)  # space around punctuation
                if method == "standard":
                    # Split into words and punctuation while keeping words like wood-cut 
                    words = re.findall(r"\b[a-zA-Z0-9]+(?:[-'%][a-zA-Z0-9]+)?\b|\b[!#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]\b", segment)
                    tokens.extend(words)
                    
                elif method == "words_only":
                    segment = re.sub(r'[!"#$&()*+,./:;<=>?@[\\]^_`{|}~]', ' ', segment)
                    segment = segment.replace('_', ' ')
                    # Extract words only
                    words = re.findall(r'\b\w+[\'-]?\w*', segment)
                    tokens.extend(words)

        header = f"Tokenization Method: {method}\nLowercase: {self.lower_pre_processed_text}\n\n"
        content = header + "\n".join(tokens)
        output_file = f'Result/TextProcessing/tokens_{method}.txt'
        self.write_to_file(output_file,content)
        print(f"Tokenization complete. Found {len(tokens)} tokens. Results saved to {output_file}.")
        return tokens , method 

    def to_lowercase(self):
        lowercase_text = self.text.lower()
        output_file = 'Result/TextProcessing/lowercase_text.txt'
        self.write_to_file(output_file, lowercase_text)
        print("Text converted to lowercase successfully.")
        return lowercase_text
    

    def count_tokens(self):
        tokens = self.tokenize(method=self.tokenize_method)[0]
        token_counts = {}
        for t in tokens:
            if t in token_counts:
                token_counts[t] += 1
            else:
                token_counts[t] = 1

        header = f"Last Tokenization Method: {self.tokenize_method}\nLowercase: {self.lower_pre_processed_text}\n\n"
        output_lines = [f'{token}: {count}' for token, count in token_counts.items()]
        content = header + "\n".join(output_lines)

        output_file = 'Result/TextProcessing/token_counts.txt'
        self.write_to_file(output_file, content)
        print(f"Token counting complete. Found {len(token_counts)} unique tokens.")
        return token_counts

        
    
    def stemming(self):
        porter_stemmer = PorterStemmer()
        tokens = self.tokenize(method=self.tokenize_method)

        stemmed_tokens = []

        for t in tokens:
            stemmed_token = porter_stemmer.stem(t)
            stemmed_tokens.append(stemmed_token)


        header = f"Tokenization Method: {self.tokenize_method}\nLowercase: {self.lower_pre_processed_text}\n\n"
        content = header + "\n".join(stemmed_tokens)

        output_file = 'Result/TextProcessing/stemmed_tokens.txt'
        self.write_to_file(output_file, content)
        print("Stemming complete.")
        return stemmed_tokens




    def menu(self):
        while True:
            print("\n=== Text Processing Menu ===")
            print("1. Load Text")
            print("2. Tokenize Text")
            print("3. Convert to Lowercase")
            print("4. Count Tokens")
            print("5. Apply Stemming")
            print("0. Exit")
            print("========================")

            try:
                choice = input("Enter your choice (0-5): ")
                
                if choice == '0':
                    for i in range(3, 0, -1):
                        print(f"Exiting in {i}...", end="\r")
                        time.sleep(1)
                    break
                
                if choice == '1':
                    file_path = input("Enter file path (or press Enter for default 'Dataset/TextProcessing/61085-0.txt'): ")
                    if not file_path:
                        file_path = self.DEFAULT_FILE_PATH_IN
                    self.load_text(file_path)
                    print("\nLowercase Conversion:[Enter]. No [Else]. Yes")
                    lowercase_choice = input("Choose option: ")
                    lowercase = lowercase_choice != ''
                    if lowercase:
                        self.text = self.text.lower()
                    self.lower_pre_processed_text = lowercase
                
                elif choice == '2':
                    print("*** Tokenization Menu ***")
                    print("\nTokenization Methods:")
                    print("[Enter]. Standard (words and punctuation)")
                    print("[Else]. Words Only")
                    method_choice = input("Choose method: ")
                    method = 'standard' if method_choice == '' else 'words_only'
                    self.tokenize_method = method
                    self.tokenize(method=method)
                
                elif choice == '3':
                    self.to_lowercase()
                
                elif choice == '4':
                    self.count_tokens()
                
                elif choice == '5':
                    self.stemming()
                
                else:
                    print("Invalid choice. Please try again.")
                
            except Exception as e:
                print(f"An error occurred: {str(e)}")


