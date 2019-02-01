def display(textToBeDisplayed):
	print(textToBeDisplayed)

def ask(textToBeAsked):
	input(textToBeAsked)



def reverse(string):
	print(string[::-1])


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    print(resultOfWordToBeRepeated)




def askWithAnswer(question, questionAnswer):
        babfdas = input(question)
        if babfdas == questionAnswer:
                print ("Thats the correct answer")
        else:
                print ("Wrong answer")

def calculateLengthOfWord(word):
        print (len(word))

def changeSizeOfWord(word, upperOrLower):
	if upperOrLower == "upper":
		print (word.upper())
	else if upperOrLower == "lower":
		print(word.lower())

		
def credits():
        print ("Made by Jeff Lim in 2019 as a Github project.")


def documentation():
	print("Download the free documentation at jefflim076@wixsite.com/rewind ")
