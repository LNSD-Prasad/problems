print("hi im  hot kitchen chatbot")
while True:
    user_input=input("you: ")
    if user_input=="menue":
        print("Chatbot:1.idly / 2.dosa / 3.vada")
    elif user_input=="special offer":
        print("Chatbot:today we have 20 percent off on all items")
    elif user_input=="pre booking":
        print("Chatbot:you can pre book your table by calling us at 6281311524")
    elif user_input=="bye":
        print("Chatbot:thank you for choosing hot kitchen, have a nice day")
        break
    else:
        print("Chatbot:sorry i didnt understand that. please try again") 

