#Super simple program to ask how many miles a user cycled and then take the input they enter
#The program then performs a conversion and rounds the result to output how many miles that number of Kilometers is equivalent to
print("How many Kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was equal to {miles}mi")