#Declare a variable called full_name that is equal to artist's first and last names with a space in between
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
#or
full_name2 = f"{artist['first']} {artist['last']}"

print(full_name)
print()
print(full_name2)