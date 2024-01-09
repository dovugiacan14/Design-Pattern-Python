class French: 
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
    
    def translate(self, word):
        return self.translations.get(word, word)


class Spanish: 
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
    
    def translate(self, word):
        return self.translations.get(word, word)


class English: 
    def __init__(self):
        self.translations = {"car": "car", "bike": "bike",
                             "cycle":"cycle"}
    
    def translate(self, word):
        return self.translations.get(word, word)


def TranslatorFactory(language):
    localizers = {
        "French": French,
        "Spanish": Spanish,
        "English": English
    }
    return localizers[language]()

if __name__ == "__main__":
    f = TranslatorFactory("French")
    s = TranslatorFactory("Spanish")
    e = TranslatorFactory("English")
    words = ["car", "bike", "cycle"]
    for word in words:
        print(f"{word} -> {f.translate(word)}")
        print(f"{word} -> {s.translate(word)}")
        print(f"{word} -> {e.translate(word)}")
        print("\n")
