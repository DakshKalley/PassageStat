## given a passage, find the number of sentences, words, and characters.

passage = open("expassage.txt")
text = passage.read()

s = str((text.count(".")))
w = [item.lower() for item in (text.split())]
c = str(len(text))

print ("Full Passage: " + str(text))
print ("# of Sentences: " + s)
print ("# of Words: " + str(len(w)))
print ("# of Characters: " + c)


def wordcount():
    lwords = []
    for i in (w):
        if (lwords.count(i) > 0):
            continue
        else:
            lwords.append(i)
            print ("Word count of " + i + ": " + str(w.count(i)))

if input("Do you want to the # of times a word is repeated? (Y/N) ") == ("Y"):
    print (" ")
    wordcount()
