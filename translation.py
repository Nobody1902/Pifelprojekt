import json, dotenv, os
import codecs

translations = {}


def load():
    global translations
    dotenv.load_dotenv()
    with codecs.open(
        os.environ.get("TRANSLATION_FILE", "translation.json"), encoding="utf-8"
    ) as f:
        translations = json.loads(f.read())


def get(key: str, lang: str) -> str:
    load()
    if lang not in translations:
        return translations["sl"][key]
    return translations[lang][key]
