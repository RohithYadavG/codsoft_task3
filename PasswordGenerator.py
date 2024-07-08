import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True,
                     include_digits=True, include_punctuation=True):
  """
  Generates a strong random password based on user-specified criteria.
  """
  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_digits:
    characters += string.digits
  if include_punctuation:
    characters += string.punctuation

  # Ensure at least one character from each category if selected
  if not (include_uppercase and include_lowercase and include_digits and include_punctuation):
    min_one = random.sample(
        [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation],
        min(include_uppercase, include_lowercase, include_digits, include_punctuation))
    characters = ''.join(min_one) + characters

  password = ''.join(random.sample(characters, length))
  return password

def main():
  """
  Prompts the user for password length and complexity options initially.
  Then, it keeps regenerating passwords until user is satisfied and asks
  if they want to generate another set of passwords.
  """
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length must be at least 8 characters.")
        continue

      include_uppercase = input("Include uppercase letters (y/n)? ").lower() == "y"
      include_lowercase = input("Include lowercase letters (y/n)? ").lower() == "y"
      include_digits = input("Include digits (y/n)? ").lower() == "y"
      include_punctuation = input("Include punctuation characters (y/n)? ").lower() == "y"

      while True:
        password = generate_password(length, include_uppercase, include_lowercase,
                                     include_digits, include_punctuation)
        print(f"Your generated password is: {password}")

        satisfied = input("Are you satisfied with the password (y/n)? ").lower()
        if satisfied == "y":
          break
        else:
          print("Generating another password...")

      choice = input("Generate another set of passwords (y/n)? ").lower()
      if choice != "y":
        break
    except ValueError:
      print("Invalid input. Please enter a number for password length.")

if __name__ == "__main__":
  main()
