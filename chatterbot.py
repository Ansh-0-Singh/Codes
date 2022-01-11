from chatterbot import chatbot
from chatterbot.trainers import ListTrainer

#a new chatbot
chatbot = Chatbot('Jarvis')
trainer = ListTrainer(chatbot)
trainer.train([ 'hi, can i help you find a course'])

#response
response = chatbot.get_response("I want a course")
print(response)