import re

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
        self.write_tokens_to_file(tokens1, 'Result/tokens_method1.txt')
        # self.write_tokens_to_file(tokens2, 'Result/tokens_method2.txt')
        return tokens1


    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Load Text")
            print("2. Tokenize")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                # file_path = input("Enter the file path: ")
                file_path = "Dataset/TextProcessing/61085-0.txt"
                if self.load_text(file_path):
                    print("Text loaded successfully.")
                else:
                    print("Failed to load text.")
            elif choice == '2':
                if self.text:
                    self.tokenize()
                    print("Tokens generated and saved.")
                else:
                    print("No text loaded. Please load text first.")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


p = TextProcessor()
p.menu()