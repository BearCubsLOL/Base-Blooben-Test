import winsound
def newForm():
    response = input("\nWould you like to submit a new form? \n").lower().strip()

    if "yes" in response or response == "y":
        start()
    elif "no" in response or response == "n":
        print("\nOk thank you, bye! Remember: we're only sometimes here to help. Hope we never see you again \n")
    else:
        print("\nCould not recognize response, please try again")
        newForm()

def start():

    blooben = input("\nDoes your question pass the base blooben test? \n").lower().strip()

    if "yes" in blooben or "yeah" in blooben or blooben == "y":
        print("\nGood Job")
        newForm()
    elif "no" in blooben or "nah" in blooben or blooben == "n":
        print("\nBad Job")
        newForm()
    elif "what" in blooben or "idk" in blooben or "i don't know" in blooben or "i dont know" in blooben or "huh" in blooben or "?" in blooben:
        winsound.PlaySound("Grain_Says_Please_Hold.wav", 0)
        winsound.PlaySound("Please_Hold.wav", 0)
        newForm()
    else:
        print("\nPlease try again.")
        start()

start()