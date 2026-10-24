"""
=============================================================================
Project Name   : Personal Introduction Program
Week           : Week 1 - Python Basics
Internship     : Developers Arena Python Internship
Description    : An interactive beginner-friendly Python program that collects
                 user details, processes basic math and list data, and displays
                 a warm, personalized welcome summary.
=============================================================================
"""

from datetime import datetime


def display_welcome_banner():
    """Prints a friendly welcome header."""
    print("=" * 60)
    print("      🌟 WELCOME TO THE PERSONAL INTRODUCTION PROGRAM 🌟      ")
    print("=" * 60)
    print("Let's get to know you! Please answer a few quick questions.\n")


def get_user_profile():
    """
    Collects personal information from the user using input()
    and validates critical inputs.
    """
    # 1. Ask for user's name (String variable)
    while True:
        name = input("👉 What is your name? ").strip()
        if name:
            break
        print("   ⚠️  Name cannot be empty. Please enter your name.")

    # 2. Ask for user's age (Integer / Math operations)
    while True:
        age_input = input("👉 How old are you? ").strip()
        if age_input.isdigit() and int(age_input) > 0:
            age = int(age_input)
            break
        print("   ⚠️  Please enter a valid positive number for your age.")

    # 3. Ask for favorite hobby (String variable)
    while True:
        hobby = input("👉 What is your favorite hobby? ").strip()
        if hobby:
            break
        print("   ⚠️  Hobby cannot be empty. What do you love doing?")

    # 4. Ask for current city / location (String variable)
    city = input("👉 What is your dream destination?").strip()
    if not city:
        city = "Earth"

    # 5. Ask for favorite foods or interests (Demonstrating Lists)
    foods_input = input("👉 What are your top 2 favorite foods (separated by comma)? ").strip()
    if foods_input:
        # Splitting input into a list and stripping whitespace
        favorite_foods = [food.strip().title() for food in foods_input.split(",") if food.strip()]
    else:
        favorite_foods = ["Pizza", "Pasta"]

    return {
        "name": name,
        "age": age,
        "hobby": hobby,
        "city": city,
        "favorite_foods": favorite_foods,
    }


def generate_introduction(profile):
    """
    Processes the collected data and prints a formatted,
    friendly welcome card with calculations.
    """
    name = profile["name"].title()
    age = profile["age"]
    hobby = profile["hobby"].title()
    city = profile["city"].title()
    foods = profile["favorite_foods"]

    # Basic Math Operations (Week 1 Concept)
    current_year = datetime.now().year
    approx_birth_year = current_year - age
    years_to_hundred = 100 - age

    print("\n" + "=" * 60)
    print(f"🎉 Welcome, {name}! 🎉")
    print("=" * 60)
    print(f"📍 Location      : {city}")
    print(f"🎂 Age           : {age} years old (Estimated birth year: ~{approx_birth_year})")
    if years_to_hundred > 0:
        print(f"⏳ Milestone     : You will hit 100 in {years_to_hundred} years!")
    print(f"🎨 Favorite Hobby: {hobby}")

    # List Concept (Week 1 Concept)
    print("\n🍽️  Favorite Foods:")
    for idx, food in enumerate(foods, start=1):
        print(f"   {idx}. {food}")

    print("\n" + "-" * 60)
    print(f"💬 \"It's fantastic to have you here, {name}!")
    print(f"    Keep practicing Python and enjoying {hobby} in {city}!\"")
    print("=" * 60 + "\n")


def main():
    """Main execution function."""
    display_welcome_banner()
    profile = get_user_profile()
    generate_introduction(profile)
    print("✨ Thank you for using the Personal Introduction Program! Have a great day! ✨\n")


if __name__ == "__main__":
    main()
