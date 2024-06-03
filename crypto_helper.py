# Crypto Helper - Calculate when to sell your crypto to break
# even based on when you bought it and for how much you bought it for.

print("Welcome to crypto helper. A program to help you know when to sell your crypto to break even.")
print("\n")
name = input("What is the name of the Crypto? >> ")
quantity = float(input("How much of the crypto (quantity not $) do you have? >> "))
cost = float(input(f"What is the total value in USD of the {name} at the time you bought it? >> "))
answer = cost / quantity
print("\n")
print(f"To break even, sell your {name} when the USD cost per unit is: {answer}.")
