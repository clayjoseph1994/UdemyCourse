#Write a function called last_element. This function takes on parameter (a list) and returns the value in the list.
#It should return None if the list is empty.

def last_element(list):
    if list:
        return list[-1]
    else:
        return None

print(last_element([3, 4, 6, 42, 16, 9]))