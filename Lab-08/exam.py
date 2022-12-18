def inputInteger():
    inpt = input("Enter a integer number: ")

    try:
        i = int(inpt)
    except (ValueError, TypeError):
        print("Error: Invalid value")

    