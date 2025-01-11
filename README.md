### University NLP Project

# TextProcessor Class - Text Processing Utility

This is a Python class that provides multiple utilities for processing textual data. The main features include loading text from a file, tokenizing the text, converting text to lowercase, counting tokens, and applying stemming using the Porter Stemmer algorithm. It also provides an interactive menu for users to easily choose and execute these operations.

## Features

- **Load Text**: Load a text file into the program.
- **Tokenization**: Tokenize text into words, URLs, or punctuation marks. Two tokenization methods are supported:
  - **Standard Tokenization**: Splits text into words and punctuation.
  - **Words Only**: Extracts only words by removing punctuation.
- **Lowercase Conversion**: Convert all text to lowercase.
- **Token Count**: Count the frequency of each token (word or punctuation) in the text.
- **Stemming**: Apply Porter Stemming to the tokens.

## Methods

### 1. `load_text(file_path)`

Loads the text from a file into the `TextProcessor` instance.

- `file_path`: The path to the text file to be loaded. If no path is specified, a default file is loaded.

### 2. `tokenize(method="standard")`

Tokenizes the loaded text into words and punctuation. Supports two methods:

- **standard**: Tokenizes words and punctuation marks.
- **words_only**: Only tokenizes words, ignoring punctuation.

### 3. `to_lowercase()`

Converts the loaded text to lowercase and saves it to a file.

### 4. `count_tokens()`

Counts the frequency of each token in the text and saves the result to a file.

### 5. `stemming()`

Applies Porter Stemming to the tokens and saves the result to a file.

### 6. `menu()`

Launches an interactive menu for the user to choose actions.

## Sample Usage

```python
text_processor = TextProcessor()
text_processor.menu()
```

### Output Files

The following files are generated after processing the text:

- **tokens_standard.txt**: Tokenized text using the standard method.
- **tokens_words_only.txt**: Tokenized text using the words-only method.
- **lowercase_text.txt**: Text converted to lowercase.
- **token_counts.txt**: Count of each token in the text.
- **stemmed_tokens.txt**: Stemming applied to the tokens.

## Installation

Before using this utility, ensure you have the required dependencies installed.

### Requirements

You can install the dependencies using the following steps:

1. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On MacOS/Linux:

      ```bash
      source venv/bin/activate
      ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Program



