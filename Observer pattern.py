class Subject:
    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self, message):
        pass

class Observer:
    def update(self, message):
        pass

class EnglishTextService(Subject):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def translate_to_english(self, text):
        translated_text = text 
        self.notify_observers(f"Text translated to English: {translated_text}")
        return translated_text

class FrenchTextService(Observer):
    def update(self, message):
        print(f"French Text Service received notification: {message}")

class EnglishToFrenchAdapter(FrenchTextService):
    def __init__(self, english_text_service):
        self.english_text_service = english_text_service
        self.english_text_service.add_observer(self)

    def translate_to_french(self, text):
        english_text = self.english_text_service.translate_to_english(text)
        french_text = self.perform_translation(english_text)
        return french_text

    def perform_translation(self, english_text):
        return "Translated to French: " + english_text

def main():
    english_text_service = EnglishTextService()
    french_text_service = FrenchTextService()
    english_to_french_adapter = EnglishToFrenchAdapter(english_text_service)

    user_input = input("Enter English text: ")
    french_text = english_to_french_adapter.translate_to_french(user_input)
    print(french_text)

if __name__ == "__main__":
    main()
