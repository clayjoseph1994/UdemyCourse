print("How many Kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was equal to {miles}mi")