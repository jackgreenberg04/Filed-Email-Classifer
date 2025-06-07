import argparse
from pathlib import Path

from .pipeline import EmailClassifier


def main() -> None:
    parser = argparse.ArgumentParser(description="Email classifier")
    parser.add_argument('--train', type=Path, help='Path to training csv')
    parser.add_argument('--predict', type=Path, help='Email file to predict')
    parser.add_argument('--batch', type=Path, help='Directory of emails to sort')
    parser.add_argument('--out', type=Path, default=Path('sorted'), help='Output directory for batch')
    parser.add_argument('--model', type=Path, default=Path('models/email_model.joblib'))
    args = parser.parse_args()

    clf = EmailClassifier(args.model)

    if args.train:
        clf.train_from_csv(args.train)
    if args.predict:
        label = clf.predict_email(args.predict)
        print(label)
    if args.batch:
        clf.batch_sort(args.batch, args.out)


if __name__ == '__main__':
    main()
