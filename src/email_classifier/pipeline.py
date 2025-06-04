from pathlib import Path
from typing import List

from .parser import parse_email
from .preprocess import clean_text
from .model import EmailModel


class EmailClassifier:
    """Pipeline to train and predict email categories."""

    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.model = EmailModel()
        if model_path.exists():
            self.model.load(model_path)

    def train_from_csv(self, csv_path: Path) -> None:
        texts, labels = self.model.load_data(csv_path)
        self.model.train(texts, labels)
        self.model.save(self.model_path)

    def predict_email(self, file_path: Path) -> str:
        data = parse_email(file_path)
        text = clean_text(data['subject'] + ' ' + data['body'])
        vec = self.model.vectorizer.transform([text])
        best_model = max(self.model.trained_models.items(), key=lambda x: x[1][1])[1][0]
        return best_model.predict(vec)[0]

    def batch_sort(self, input_dir: Path, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        for file in input_dir.iterdir():
            if file.is_file():
                label = self.predict_email(file)
                dest = output_dir / label
                dest.mkdir(exist_ok=True)
                dest.joinpath(file.name).write_text(file.read_text())
