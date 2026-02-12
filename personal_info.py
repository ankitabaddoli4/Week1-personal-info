# ============================================
# Personal Information Manager
# Author: Riya
# Description: Week 1 Python project using
# variables, input/output, validation,
# calculations, and string formatting
# ============================================

# Welcome message
print("=" * 50)
print("        PERSONAL INFORMATION MANAGER")
print("=" * 50)
print()

# --------------------------------------------
# Static information (pre-defined)
# --------------------------------------------
name = "Riya"                # Name of the person
age = 21                     # Age in years
city = "Pune"                # City name
hobby = "reading books"      # Hobby or interest

# --------------------------------------------
# Get user input with validation
# --------------------------------------------
print("Please tell me about yourself:")
print("-" * 40)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("❌ Input cannot be empty.")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("❌ Input cannot be empty.")
    favorite_color = input("What's your favorite color? ").strip()

email = input("What's your email address? ").strip()
while email == "":
    print("❌ Email cannot be empty.")
    email = input("What's your email address? ").strip()

country = input("Which country are you from? ").strip()
while country == "":
    print("❌ Country cannot be empty.")
    country = input("Which country are you from? ").strip()

# --------------------------------------------
# Calculations
# --------------------------------------------
age_in_months = age * 12

# --------------------------------------------
# Display formatted output
# --------------------------------------------
print()
print("=" * 50)
print("              YOUR INFORMATION")
print("=" * 50)
print()

print(f"Name           : {name}")
print(f"Age            : {age} years ({age_in_months} months old)")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.capitalize()}")
print()
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")
print(f"Email          : {email.lower()}")
print(f"Country        : {country.title()}")
print()

# --------------------------------------------
# Goodbye message
# --------------------------------------------
print("=" * 50)
print("Thank you for using the program!")
print("=" * 50)

