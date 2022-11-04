secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_name = int(input("Enter the number: "))

while user_name != secret_number:
    print("Ha ha!, your stuck in my loop!")
    user_name = int(input("Enter the number again"))
print("the secret_number is", secret_number)