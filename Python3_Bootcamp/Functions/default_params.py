#default parameters have to be assignd at the end of a fucntion. In this case, there is no other parameter, but if there
#was it would need to be assigned as the last parameter of the function

def speak(animal = "dog"):
    if animal =="pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

#default is dog, so this is executed when no argument is specified when calling function
print(speak())
print(speak("pig"))
print(speak("duck"))
print(speak("cat"))
print(speak("dog"))
#animal as anything besides pig, duck, cat, dog, or blank arg, this should return "?"
print(speak("banana"))
