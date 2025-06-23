words={
    "madad":"Help",
    "kursi":"Chair",
    "billi":"Cat"
}

word= input("Enter the word to be Translated: ").lower()

print(words.get(word, "Word not available in Dictionary"))