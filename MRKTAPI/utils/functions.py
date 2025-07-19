from urllib.parse import quote_plus
import re

def nanoToNormal(num) -> str:
    value = float(num) / 1_000_000_000
    return format(value, '.15f').rstrip('0').rstrip('.') or '0'
    
def toShortName(gift_name: str) -> str:
    return gift_name.replace(" ", "").replace("'", "").replace("’", "").replace("-", "").lower()

def rarityPerMilleToPercent(per_mille) -> str:
    percent = float(per_mille) / 10
    return f"{percent:.1f}"

def cap(text) -> str:
    words = re.findall(r"\w+(?:'\w+)?", text)
    for word in words:
        if len(word) > 0:
            cap = word[0].upper() + word[1:]
            text = text.replace(word, cap, 1)
    return text

def listToURL(gifts: list) -> str:
    return '%2C'.join(quote_plus(cap(gift)) for gift in gifts)

def convertToNano(num) -> int:
    return int(float(num) * 1_000_000_000)