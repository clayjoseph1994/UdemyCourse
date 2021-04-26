# Given the donations dictionary, use a loop to add together all the donations and store the resulting number in a variable called total_donations

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
#way 1 (requires setting declaring variable and setting to 0)
total_donations = 0

for donation in donations.values():
    total_donations += donation
print(total_donations)

#way 2
total_donations1 = sum(donations.values())
print(total_donations1)