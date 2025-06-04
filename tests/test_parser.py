from pathlib import Path

from email_classifier.parser import parse_email


def test_parse_email_txt(tmp_path: Path):
    file = tmp_path / "test.txt"
    file.write_text("Subject line\nBody text")
    data = parse_email(file)
    assert 'body' in data
    assert 'subject' in data
