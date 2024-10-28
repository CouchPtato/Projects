import requests
import pyttsx3

def get_word_info(word):
    
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        meanings = data.get("meanings", [])  

        print(f"\n\tDetails for '{word}'")

        top_meaning = meanings[0]["definitions"][0]["definition"]
        print(f"\nTop Meaning: {top_meaning}")
        pronounce_text(top_meaning)

    else:
        print(f"Word '{word}' not found.")


def pronounce_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def pronounce_word(word):
    pronounce_text(word)

def menu():
    while True:
        print("\n\tDictionary Menu")
        print("1. Search word meaning")
        print("2. Pronounce word")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            word = input("Enter the word: ").strip().lower()
            get_word_info(word)
        elif choice == '2':
            word = input("Enter the word to pronounce: ").strip().lower()
            pronounce_word(word)
        elif choice == '3':
            print("See ya soon. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
