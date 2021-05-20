import re
from unicodedata import normalize as unicode_normalize


def normalize_text(text: str) -> str:
    """Performs text normalization using regex patterns
    """
    text = unicode_normalize("NFC", text)
    text = text.lower()
    text = re.sub("```(.|\n|\r)*?```", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub("[-_:/]", " ", text)

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\.+", ".", text)
    text = re.sub("[?!;…]", ".", text)
    text = text.replace("\n", ".")
    return text