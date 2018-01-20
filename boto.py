"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request, response
import json
import random
import datetime
import names
Game_start = ["play","game"]
Game_play = ["rock","paper","scissors"]
Welcoming_keywords = ("hi","hello","bonjour","shalom",)
Welcoming_answers = ["how are you bro?","sup?","manish?","ca va?"]
Bad_word = ["shit","bitch","fuck","asshole","cunt"]

Jokes_bot=["What's the difference between snowmen and snowladies? Snowballs",
           "How do you make holy water? You boil the hell out of it.",
           "I once farted in an elevator, it was wrong on so many levels.",
           "I used to like my neighbors, until they put a password on their WiFi",]

names_generator=["what is your favorite name?","how should i call my child","with who are you in love",]

def get_time():
    now = datetime.datetime.now()
    return str(now.hour) + ":" + str(now.minute).zfill(2)


def Answer(user_message):
    user_message = user_message.lower()
    word_message = user_message.split(" ")

    if set(names_generator).intersection([user_message]):
        return "waiting", names.get_first_name()

    if set(Game_start).intersection(word_message):
        return "excited", Game_play[random.randint(0, len(Game_play) - 1)]

    if "paper" in word_message:
        return "laughing", "i won i sayed scissors"

    if "rock" in word_message:
        return "waiting", "i won i sayed paper"

    if "scissors" in word_message:
        return "crying", "i let you win"


    if "time" in word_message:
        return"bored", "it is: " + get_time()
    if "date" in word_message:
        now = datetime.datetime.now()
        return"confused", "it is: " + str(now.day) +"/" + str(now.month)
    if "weather" in word_message:
        return "inlove","ask my girlfriend siri"
    if set(Welcoming_keywords).intersection(word_message):
        return"money",Welcoming_answers[random.randint(0, len(Welcoming_answers)-1)]
    if set(Bad_word).intersection(word_message):
        return "takeoff","this word doesnt represent you"
    if set (["joke","jokes"]).intersection(word_message):
        return "giggling","i have a good one, "+ Jokes_bot[random.randint(0, len(Jokes_bot)-1)]
    if "name" in word_message and "?" in word_message:
        return "laughing","call me how you wish pretty"
    if "how are you" in user_message and user_message.endswith("?"):
        return "afraid","i am good, you are good bro?"
    if "who" in user_message and user_message.endswith("?"):
        return "excited","thats a bad ass"

    return "no", "I cannot understand what you said"

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    animation, boto_response = Answer(user_message)

    return json.dumps({"animation": animation, "msg":boto_response })




@route("/test", method='POST')
def test():
    user_message = request.POST.get('msg')
    """hello_function=check_for_Welcoming()"""
    return json.dumps({"animation": "excited", "msg": "dog"})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')



def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
