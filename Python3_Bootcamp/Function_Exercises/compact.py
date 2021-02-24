#Write a function called compact that accepts a list and returns a list of values that
#are truthy values, excluding any falsey values from said list

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(ls):
    return [val for val in ls if val]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))