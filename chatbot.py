import random
import nltk
import spacy
from nltk.stem import WordNetLemmatizer

# Download required data for NLTK
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great!", "I'm fine, thanks for asking!", "I'm just a bot, but I'm good!"],
    "your name": ["I'm a simple chatbot.", "Call me ChatBot!", "I'm your virtual assistant!"],
    "bye": ["Goodbye!", "See you soon!", "Bye! Have a nice day!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase that?", "I don't understand."]
}

# Function to preprocess and lemmatize input
def preprocess_input(user_input):
    # Tokenize and lemmatize the input
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return tokens

# Function to get chatbot response
def get_response(user_input):
    tokens = preprocess_input(user_input)
    
    for key in responses:
        # Check if any token matches a keyword in predefined responses
        if key in tokens:
            return random.choice(responses[key])
    
    # If no match, return default response
    return random.choice(responses["default"])

# Chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break
        
        # Get and display the response
        response = get_response(user_input)
        print("Chatbot:", response)

# Run chatbot
if __name__ == "__main__":
    chatbot()