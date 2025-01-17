# Text Processing, Classification & Recommendation System

A comprehensive project implementing text processing, classification using Naive Bayes, and a collaborative filtering recommendation system.

## Project Structure
```
project/
│
├── Dataset/
│   ├── TextProcessing/
│   │   └── input_text.txt
│   ├── Classification-Train And Test/
|   |   |____class1
│   │   |   ├── train_files
│   │   |   └── test/
|   |   |____class2..   
│   └── Collaborative Filtering/
│       └── Songs Dataset Truncated.csv
|
├── Classification.py
├── CollaborativeFiltering.py
├── PreProcessor.py
├── main.py
|
├── Result
└── requirements.txt
```

## 1. Text Processing Module

### Features
- Text tokenization
- Lowercase conversion
- Token frequency counting
- Porter Stemming implementation


## 2. Text Classification Module (Naive Bayes)

### Implementation Steps
1. Dictionary Creation
2. Class Probability Calculation (P(C))
3. Conditional Probability Calculation (P(W|C))
4. Classification using Bayes' Rule

## 3. Recommendation System (User-User Collaborative Filtering)

### Features
- Utility Matrix Construction
- Mean-Centering
- User Similarity Calculation
- K-Nearest Neighbors Selection
- Rating Prediction


## Installation
```bash
pip install -r requirements.txt
```

## To run the project, simply execute the following command:
```bash
python main.py
```
