import winsound
def newForm():
    response = input("\nWould you like to submit a new form? \n").lower().strip()

    if response == "yes":
        start()
    elif response == "no":
        print("\nOk thank you, bye! Remember: we're only sometimes here to help. Hope we never see you again \n")
    else:
        print("\nCould not recognize response, please try again")
        newForm()

def start():

    blooben = input("\nDoes your question pass the base blooben test? \n").lower().strip()

    if blooben == "yes":
        print("\nGood Job")
        newForm()
    elif blooben == "no":
        print("\nBad Job")
        newForm()
    elif "what" in blooben or "idk" in blooben or "i don't know" in blooben or "i dont know" in blooben:
        winsound.PlaySound("Grain_Says_Please_Hold.wav", 0)
        winsound.PlaySound("Please_Hold.wav", 0)
        newForm()
    else:
        print("\nPlease try again.")
        start()

start()
