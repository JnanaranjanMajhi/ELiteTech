import string

def create_acronym(phrase, separator=""):
    # Remove punctuation from the phrase
    phrase = phrase.translate(str.maketrans("", "", string.punctuation))
    # Split the phrase into words (handling multiple spaces)
    words = phrase.split()
    # Ensure there are words to create an acronym
    if not words:
        return "Error: No valid words provided to create an acronym."
    # Get the first letter of each word and capitalize it
    acronym = ''.join([word[0].upper() for word in words])
    # Return the acronym with the custom separator (if provided)
    if separator:
        return separator.join(acronym)
    return acronym

def get_user_input():
    while True:
        # Get the phrase from the user
        phrase = input("\nEnter a phrase to create an acronym (or 'quit' to exit): ").strip()
        # Exit condition
        if phrase.lower() == 'quit':
            print("Exiting Acronym Creator.")
            break
        # Get the separator (optional)
        separator = input("Enter a separator (or press Enter to skip): ").strip()
        # Validate and generate acronym
        acronym = create_acronym(phrase, separator)
        # Display the acronym
        print(f"The acronym is: {acronym}")

# Start the program
if __name__ == "__main__":
    get_user_input()
