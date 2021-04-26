def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(Joseph="purple", Justyce="pink", Nancy="teal")

print("=================================================")

def special_greeting(**kwargs):
    if "Joseph" in kwargs and kwargs["Joseph"] == "special":
        return "You get a special greeting, Joseph!"
    elif "Joseph" in kwargs:
        return f'{kwargs["Joseph"]} Joseph!'

    return "Not sure who this is..."

print(special_greeting(Joseph="Hello", Justyce="special"))
print(special_greeting(Bob="Hello"))
print(special_greeting(Joseph="special", Justyce="Hello"))
