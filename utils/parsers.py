import re


def parse_price(text):

    if not text:
        return None

    cleaned = re.sub(r"[^\d]", "", text)

    if cleaned == "":
        return None

    return int(cleaned)


def parse_area(text):

    if not text:
        return None

    text = text.replace(",", ".")
    numbers = re.findall(r"\d+\.?\d*", text)

    if not numbers:
        return None

    return float(numbers[0])