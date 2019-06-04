# questions for easy madlib
easy_madlib = """A __1__ is a decentralized community's complete and __2__ transaction history that everyone who is part of the community agrees on. This __3__ automatically gets updated in regular time frames, is accepted by the community as a fact, and gets __4__ on every participant's computer. This way, no central party has to govern the community, since no one can double-spend."""

# answers for easy madlib
easy_madlib_answers = ["blockchain", "unchangeable", "ledger", "stored"]

# questions for medium madlib
medium_madlib = """In cryptocurrencies, you cannot store __1__, because they are always recorded on the blockchain and this information never changes. You use so-called __2__ to store the private __3__ that lets you send the coins to another __4__ by signing a cryptographic function on the blockchain."""

# answers for medium madlib
medium_madlib_answers = ["coins", "wallets", "key", "address"]

# questions for hard madlib
hard_madlib = """In a __1__, any rule or regulation is programmed into the cryptographic __2__ that governs the __3__ community using the currency. The combination of cryptography and currencies gives __1__ its name. This basically mean a currency that is backed by and made __4__ through cryptography."""

# answers for hard madlib
hard_madlib_answers = ["cryptocurrency", "algorithm", "decentralized", "rare"]

# list of question numbers for player to add answer
questions = ["__1__", "__2__","__3__","__4__"]

# ask player to select a level to play game
def play_game():
    print "Welcome to the blockchain quiz based on Julian Hosp's book Cryptocurrencies Simply Explained. Choose the word that best fits the blank. You have 4 tries per question."
    level_selection = raw_input("Please select a level by typing the word easy, medium or hard. ").lower()
    if level_selection=="easy":
        process_madlib(easy_madlib, questions, easy_madlib_answers)
    elif level_selection=="medium":
        process_madlib(medium_madlib, questions, medium_madlib_answers)
    elif level_selection=="hard":
        process_madlib(hard_madlib, questions, hard_madlib_answers)
    else:
        print "Please choose only easy, medium or hard."
    print play_game

# start quiz, check answers, limits player's number of tries
def process_madlib(quiz, blanks, answers):
	print quiz
	for count_blanks in range(0, len(blanks)):
		answer_input = raw_input("What is " + blanks[count_blanks] +"? ")
		tries = 1
		max_tries = 4
		while answer_input.lower()!= answers[count_blanks]:
			tries += 1
			answer_input = raw_input("Try again! What is " + blanks[count_blanks] + "? ")
			if tries == max_tries:
				print ("Don't worry! Let's restart the game and try again!")
				play_game()
		else:
			quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
			print("That is correct! Let's continue filling in the blanks! " + quiz)
	if len(blanks) == len(answers):
		print ("You're on the path to becoming #cryptofit! Let's try another level?")
		play_game()

play_game()
