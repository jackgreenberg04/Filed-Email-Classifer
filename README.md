# Filed Email Classifier

This project provides a simple email classification system built with Python. It demonstrates text preprocessing, machine learning, and batch processing of emails.

## Features
- Parse `.eml` or `.txt` email files
- Clean and tokenize email text with NLTK
- Train Naive Bayes and SVM models using TF-IDF features
- Predict categories for new emails
- Batch sort emails into folders

## Quickstart
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train a model with a CSV dataset containing `text` and `label` columns:
   ```bash
   python -m email_classifier.cli --train data/sample/train.csv
   ```
3. Predict a single email:
   ```bash
   python -m email_classifier.cli --predict path/to/email.eml --model models/email_model.joblib
   ```
4. Batch sort a directory of emails:
   ```bash
   python -m email_classifier.cli --batch incoming_emails --out sorted
   ```
