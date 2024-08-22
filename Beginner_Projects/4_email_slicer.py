"""
Collect email from user
split the email using @
Save the first part as username 
Save the second part as domain

hello@learnpython.com
1st part(username) - hello
2nd part(domain) - learnpython
"""


def slice_email(email):
    (username,domain) = email.split('@')
    (domain,extension) = domain.split(".")

    return username, domain, extension

print('\nWelcome to the Email Slicer!\n')
email = input("Enter Your Email Address: ")
slice = slice_email(email)

print(f'\nUsername: {slice[0]} \nDomain: {slice[1]} \nExtension: {slice[2]}\n')