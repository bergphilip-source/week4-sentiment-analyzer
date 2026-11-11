# week4-sentiment-analyzer
Week 4 Assignment
# Sentiment Analysis System
## Overview
This project implements sentiment analysis for product reviews using Natural Language Processing (NLP) techniques from Chapter 23.

## Features
- **Two Analysis Methods:**
  - Simple: Word counting based on positive/negative word lists
  - Advanced: Machine learning using TextBlob
- **REST API** for easy integration
- **Visualization** of sentiment distributions
- **Text preprocessing** including tokenization and stop word removal

## How to Run
### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Test the Analyzer
```bash
python test_sentiment.py
```

### 3. Start the API Server
```bash
python api_server.py
```
Then visit http://localhost:5000

### Train with Labeled Reviews
```python
from sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()
review_count = analyzer.train_from_file("test_reviews.txt")
print(f"Trained on {review_count} reviews")
print(analyzer.analyze_sentiment_advanced("The product is excellent!"))
```
The training file uses `Good:` and `Bad:` sections, with each review beginning
with a star rating. This file contains only a few examples, so predictions may
not generalize well.

## API Usage Example
```python
import requests
response = requests.post('http://localhost:5000/analyze',
                        json={'text': 'This product is amazing!'})
print(response.json())
```

## Understanding NLP Concepts
### Tokenization
Breaking text into words: "I love this" → ["I", "love", "this"]

### Stop Words
Common words we filter out: "the", "is", "at", "which"

### Sentiment Analysis
Determining if text is positive, negative, or neutral

## Challenges Encountered
I fought with debugging the code becuase I had to install the packages seperately.
## Real-World Applications
The 3 ways that this could be used in the real world is helping analytics by getting a quick number of good/bad complaints. Another, is the purchasing team seeing if their products are getting good feedback. The last is product development teams getting a better understanding on if they need to improve the product.
## What I Learned
I learned that NPL's can understand and deduce whether or not a review has good or bad intentions, this helps multiple teams in a company and it gives good feedback! I understand that it could also possibly be used in a call or email enviroment to give that feedback as well.