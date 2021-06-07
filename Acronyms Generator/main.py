def get_acro(phrase):
    text = phrase.split()

    acro = ""

    for i in text:
        acro = acro + i[0].upper()
    return acro
    

user_input = input("Enter a Phrase: ")
# acro = get_acro(user_input)
print("Acronym of" , user_input , " is " , get_acro(user_input))