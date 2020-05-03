import  random
import string

def generatePassword(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Random String password is generating...\n", generatePassword())
print ("\nPassword generated successfully!")