import email
from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import Dict
from bs4 import BeautifulSoup


def parse_email(file_path: Path) -> Dict[str, str]:
    """Parse an email file (.eml or .txt) and return components."""
    if file_path.suffix == '.eml':
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        subject = msg['subject'] or ''
        sender = msg['from'] or ''
        body = msg.get_body(preferencelist=('plain', 'html'))
        content = body.get_content() if body else ''
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        subject = ''
        sender = ''
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text('\n')
    return {
        'subject': subject,
        'sender': sender,
        'body': text,
    }
