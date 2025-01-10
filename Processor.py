import re
from nltk.stem import PorterStemmer

class TextProcessor:
    def __init__(self):
        self.text = ""

    def load_text(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
                return True
        except:
            print(f"File '{file_path}' not found.")
            return False
    
    
    def tokenize_method1(self, text):
        # words and punctuation
        pattern = r'\b\w+\b|[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]'
        tokens = re.findall(pattern, text)  
        return tokens

    # def tokenize_method2(self, text):
    #     # Replaces punctuation with spaces
    #     text = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]', ' ', text)
    #     # Replaces multiple spaces with a single space
    #     text = re.sub(r'\s+', ' ', text)
    #     # Splits the text into tokens by whitespace
    #     tokens = text.strip().split()
    #     return tokens
    
    
    def write_tokens_to_file(self, tokens, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write('\n'.join(tokens))

    
    def tokenize(self):
        tokens1 = self.tokenize_method1(self.text)
        # tokens2 = self.tokenize_method2(self.text)
        self.write_tokens_to_file(tokens1, 'Result/TextProcessing/tokens_method1.txt')
        # self.write_tokens_to_file(tokens2, 'Result/tokens_method2.txt')
        return tokens1

    def to_lowercase(self):
        lowercase_text = self.text.lower()
        with open('Result/TextProcessing/lowercase_text.txt', 'w', encoding='utf-8') as file:
            file.write(lowercase_text)
        return lowercase_text
    

    def count_tokens(self):
        with open('./Result/TextProcessing/tokens_method1.txt', 'r', encoding='utf-8') as file:
            tokens = file.read().splitlines()

        token_counts = {}
        for t in tokens:
            if t in token_counts:
                token_counts[t] += 1
            else:
                token_counts[t] = 1

    
        with open('./Result/TextProcessing/tokens-count.txt', 'w', encoding='utf-8') as output:
            for token, count in token_counts.items():
                output.write(f'{token}: {count}\n')

        return token_counts
    
    def stemming(self):
        porter_stemmer = PorterStemmer()
        with open('./Result/TextProcessing/tokens-count.txt', 'r', encoding='utf-8') as file:
            tokens = file.read().splitlines()

        stemmed_tokens = []
        for line in tokens:
            token = line.split(':')[0]
            stemmed_token = porter_stemmer.stem(token)
            stemmed_tokens.append(stemmed_token)

    
        with open('./Result/TextProcessing/stemming.txt', 'w', encoding='utf-8') as output_file:
            for token in stemmed_tokens:
                output_file.write(f"{token}\n")

        return stemmed_tokens




    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Load Text")
            print("2. Tokenize")
            print("3. Convert to Lowercase")
            print("4. Count Tokens")
            print("5. Stemming")
            print("[anythingElse]. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                # file_path = input("Enter the file path: ")
                file_path = "Dataset/TextProcessing/61085-0.txt"
                if self.load_text(file_path):
                    print("Text loaded successfully.")
                else:
                    print("Failed to load text.")
                    continue
            elif choice == '2':
                self.tokenize()
            elif choice == '3':
                self.to_lowercase()
                print("Text converted to lowercase and saved.")
            elif choice == '4':
                self.count_tokens()
            elif choice == '5':
                self.stemming() 
            else:
                print("Exiting...")
                break


p = TextProcessor()
p.menu()