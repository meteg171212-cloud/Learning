meme_dictionary = {
    "LOL": "Laugh out loud",
    "AFK": "Away from keyboard",
    "IDk": "I don't know",
    "IDC": "I don't care",
}

while True:
    
    ask = input("what meme would you like to learn about")
    
    if ask in meme_dictionary.keys():
        print(meme_dictionary[ask])
    elif ask not in meme_dictionary.keys():
        print("that word is not in dictionary list")
        ask2 = input("would you like to add to the dictionary?")
        if ask2 == "Yes" or "yes":
            new_word = input("Enter new word")
            meaning = input("meaning of the new word")
            meme_dictionary.update({new_word: meaning})

    
