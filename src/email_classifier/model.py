from pathlib import Path
from typing import List, Tuple

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

from .preprocess import clean_text


class EmailModel:
    """Train and evaluate email classification models."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.models = {
            'nb': MultinomialNB(),
            'svm': LinearSVC(),
        }
        self.trained_models = {}

    def load_data(self, csv_path: Path) -> Tuple[List[str], List[str]]:
        df = pd.read_csv(csv_path)
        texts = [clean_text(t) for t in df['text']]
        return texts, df['label'].tolist()

    def train(self, texts: List[str], labels: List[str], k: int = 3) -> None:
        X = self.vectorizer.fit_transform(texts)
        kf = KFold(n_splits=k, shuffle=True, random_state=42)
        for name, model in self.models.items():
            scores = cross_val_score(model, X, labels, cv=kf, scoring='f1_weighted')
            model.fit(X, labels)
            self.trained_models[name] = (model, scores.mean())

    def evaluate(self, texts: List[str], labels: List[str]) -> str:
        X = self.vectorizer.transform(texts)
        results = []
        for name, (model, _) in self.trained_models.items():
            preds = model.predict(X)
            report = classification_report(labels, preds)
            results.append(f"Model: {name}\n{report}")
        return "\n".join(results)

    def save(self, path: Path) -> None:
        joblib.dump({'vectorizer': self.vectorizer, 'models': self.trained_models}, path)

    def load(self, path: Path) -> None:
        data = joblib.load(path)
        self.vectorizer = data['vectorizer']
        self.trained_models = data['models']
