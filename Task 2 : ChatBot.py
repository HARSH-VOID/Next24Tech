''' Install Necessary Libraries
Install the required libraries using pip:

pip install chatterbot chatterbot_corpus spacy
python -m spacy download en_core_web_sm

'''

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import spacy


# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Create a new chatbot instance
chatbot = ChatBot(
    'AdvancedBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Train the chatbot with the English corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")

# Train the chatbot with custom data
custom_trainer = ListTrainer(chatbot)
custom_trainer.train([
    "Hi, how can I help you?",
    "I need assistance with my account.",
    "Sure, I can help you with that. What seems to be the problem?",
    "I forgot my password.",
    "You can reset your password by clicking on 'Forgot Password' at the login screen."
])

# Function to process user input and generate response
def get_response(user_input):
    doc = nlp(user_input)
    if any(ent.label_ == 'GPE' for ent in doc.ents):
        return "It seems you're asking about a location. How can I assist you with that?"
    response = chatbot.get_response(user_input)
    return response

# Running the chatbot
print("Chatbot is ready to talk! (type 'exit' to stop)")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        bot_response = get_response(user_input)
        print("Chatbot:", bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
