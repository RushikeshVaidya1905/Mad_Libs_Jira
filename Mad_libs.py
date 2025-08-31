# Mad Libs Program

def mad_libs():
    print("Welcome to Mad Libs! Let's create a fun story.\n")

    # Asking user for inputs
    college_class = input("Enter a college class: ")
    adjective = input("Enter an adjective: ")
    activity = input("Enter an activity: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    friend = input("Enter a friend's name: ")

    # Creating the story with placeholders
    story = f"""
    Today in {college_class} class, things were really {adjective}.
    Our teacher told us to {activity}, which was unexpected!
    Later, we went to {place}, and surprisingly saw a {animal}.
    My friend {friend} couldn’t stop laughing.
    It was one of the most {adjective} days ever!
    """

    # Printing final story
    print("\nHere’s your Mad Libs story:")
    print(story)


# Run the program
if __name__ == "__main__":
    mad_libs()
