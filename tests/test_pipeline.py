from pathlib import Path

from email_classifier.pipeline import EmailClassifier


def test_training(tmp_path: Path):
    csv = Path('data/sample/train.csv')
    model_path = tmp_path / 'model.joblib'
    clf = EmailClassifier(model_path)
    clf.train_from_csv(csv)
    assert model_path.exists()
