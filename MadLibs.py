#Paige E. Hungate
#E754Q367
#CS410: Programming Paradigms, MW 7:05p-8:20p
#Final Project
#These "Mad Libs" were found in a google images search. I did not create the stories.

#FIX ALL THE FORMATTING OF THE INPUT

def mad_lib():
	print("\nThis is the edit for the Software Engineering assignment!\n")
	print("\nThis is the SECOND edit for the Software Engineering assignment!\n")
	print("\nHello! This program functions as a Mad Lib generator.\n")
	name = input("What is your name? ")
	print("\nOkay {0}. Here are the 5 stories to choose from:".format(name))
	print("\t1. How to Date the Coolest Guy/Girl in School")
	print("\t2. How to Study")
	print("\t3. Newspaper Article")
	print("\t4. Political Speech")
	print("\t5. The Art of Espionage")
	selection = eval(input("\nWhich story would you like to choose? Enter 1 - 5 to make your selection: "))
	
	if (selection == 1):
		print("\nAll right, {0}. Here we go with 'How to Date the Coolest Guy/Girl in School'.".format(name))
		print("You are going to be prompted to enter in 17 different words. Okay...go!")
		first = input("\nEnter a plural noun: ")
		second = input("Enter an adverb: ")
		third = input("Enter a verb: ")
		fourth = input("Enter an article of clothing: ")
		fifth = input("Enter a body part: ")
		sixth = input("Enter an adjective: ")
		seventh = input("Enter a noun: ")
		eighth = input("Enter another plural noun: ")
		ninth = input("Enter another body part: ")
		tenth = input("Enter another plural noun: ")
		eleventh = input("Enter another body part: ")
		twelfth = input("Enter another noun: ")
		thirteenth = input("Enter another noun: ")
		fourteenth = input("Enter a verb ending in 'ing': ")
		fifteenth = input("Enter another adjective: ")
		sixteenth = input("Enter another adjective: ")
		seventeenth = input("Okay. Last one. Enter another verb: ")
		
		print("\nGet excited, {0}, because here comes your Mad Lib:\n".format(name))		
	
		print("It's simple. Turn the {0}. Make him/her want {1} to date you. Make".format(first, second))
		print("sure you're always dressed to {0}. Each and everyday, wear a/an {1)".format(third, fourth))
		print("that you know shows off your {0} to {1} advantage and make your {2}".format(fifth, sixth, seventh))
		print("look like a million {0}. Even if the two of you make meaningful".format(eighth))
		print("{0} contact, don't admit it. No hugs or {1}. Just shake his/her".format(ninth, tenth))
		print("{0} firmly. And remember, when he/she asks you out, even though".format(eleventh))
		print("a chill may run down your {0} and you can't stop your {1}".format(twelfth, thirteenth))
		print("from {0}, just play it {1}. Take a long pause before answering".format(fourteenth, fifteenth))
		print("in a very {0} voice, 'I'll have to {1} it over.'".format(sixteenth, seventeenth))
	
	elif (selection == 2):
		print("\nAll right, {0}. Here we go with 'How to Study'.".format(name))
		print("You are going to be prompted to enter in 13 different words. Okay...go!")
		first = input("Enter an adjective: ")
		second = input("Enter another adjective: ")
		third = input("Enter a noun: ")
		fourth = input("Enter another noun: ")
		fifth = input("Enter a plural noun: ")
		sixth = input("Enter an adverb: ")
		seventh = input("Enter a verb: ")
		eighth = input("Enter another adjective: ")
		ninth = input("Enter another plural noun: ")
		tenth = input("Enter another adjective: ")
		eleventh = input("Enter another ajective: ")
		twelfth = input("Enter another adjective: ")
		thirteenth = input("Okay. Last one. Enter another plural noun: ")

		print("Get excited, {0}, because here comes your Mad Lib:\n".format(name))

		print("{0} teachers always give out {1} assignments. But as everyone".format(first, second))
		print("everyone knows, if you want to pass all your classes so you can")
		print("go to a/an {0} and become president of a big international {1}".format(third, fourth))
		print("and have millions of {0} in the bank, you must do your homework".format(fifth))
		print("and study {0}. If you just sit around and {1}, you won't get".format(sixth, seventh))
		print("ahead in life. You must learn to pay attention every {0} thing".format(eighth))
		print("your teacher says. Do not interrupt or whisper to other {0}".format(ninth))
		print("during class. Be sure to have a nice, {0} notebook in which".format(tenth))
		print("you can write down anything the teacher says that seems {0}.".format(eleventh))
		print("Then go home and memorize all of those {0} notes. When your".format(twelfth))
		print("teacher gives a suprise quiz, you will know all of the {0}.".format(thirteenth))
		
	elif (selection == 3):
		print("\nAll right, {0}. Here we go with 'Newspaper Article'.".format(name))
		print("You are going to be prompted to enter in 10 different words. Okay...go!")
		first = input("Enter an adjective: ")
		second = input("Enter another adjective: ")
		third = input("Enter another adjective: ")
		fourth = input("Enter a noun: ")
		fifth = input("Enter another noun: ")
		sixth = input("Enter a past tense verb: ")
		seventh = input("Enter a color: ")
		eighth = input("Enter another adjective: ")
		ninth = input("Enter an exclamation: ")
		tenth = input("Okay. Last one. Enter an animal: ")

		print("Get excited, {0}, because here comes your Mad Lib:\n".format(name))
		
		print("Mrs. Fifi Vanderbold, the {0} and {1} heiress, has filed for".format(first, second))
		print("divorce from her husband, Percy Vanderbold, the former {0} {1}".format(third, fourth))
		print("of Harvard, class of '38, now in the {0} business. Mrs. Vanderbold".format(fifth))
		print("claimed that her husband had {0} her bed of {1} flowers and".format(sixth, seventh))
		print("tracked {0} mud into the house. He also criticized her cooking.".format(eighth))
		print("Mr. Vanderbold, when asked to commend, said '{0}! I didn't do".format(ninth))
		print("it. The pet {0} ruined the flowers. And I offered to take her".format(tenth))
		print("out to restaurants more often!")
	
	elif (selection == 4):
		print("\nAll right, {0}. Here we go with 'Political Speech'.".format(name))
		print("You are going to be prompted to enter in 19 different words. Okay...go!")
		first = input("Enter an adjective: ")
		second = input("Enter another adjective: ")
		third = input("Enter a plural noun: ")
		fourth = input("Enter another plural noun: ")
		fifth = input("Enter another adjective: ")
		sixth = input("Enter a noun: ")
		seventh = input("Enter another noun: ")
		eighth = input("Enter another plural noun: ")
		ninth = input("Enter another adjective: ")
		tenth = input("Enter a male in the room: ")
		eleventh = input("Enter another adjective: ")
		twelfth = input("Enter another noun: ")
		thirteenth = input("Enter another adjective: ")
		fourteenth = input("Enter another noun: ")
		fifteenth = input("Enter another plural noun: ")
		sixteenth = input("Enter another plural noun: ")
		seventeenth = input("Enter another adjective: ")
		eighteenth = input("Enter another adjective: ")
		nineteenth = input("Okay. Last one. Enter another adjective: ")

		print("Get excited, {0}, because here comes your Mad Lib:\n".format(name))
	
		print("Ladies and gentlemen, on this {0} occasion it is a privilege".format(first))
		print("to address such a/an {0}-looking group of {1}. I can tell from".format(second, third))
		print("your smiling {0} that you will support my {1} program in coming".format(fourth, fifth))
		print("election. I promise that, if elected, there will be a/an {0} in".format(sixth))
		print("every {0} and two {1} in every garage. I want to warn you against".format(seventh, eighth))
		print("my {0} opponent, Mr. {1}. The man is nothing but a/an {2} {3}.".format(ninth, tenth, eleventh, twelfth))
		print("He has a/an {0} character and is working {1} in glove with".format(thirteenth, fourteenth))
		print("the criminal element. If elected, I promise to eliminate vice. I")
		print("will keep the {0} off the city's streets. I will keep crooks from".format(fifteenth))
		print("dipping their {0} in the public till. I promise you {1} government,".format(sixteenth, seventeenth))
		print("{0} taxes, and {1} schools.".format(eighteenth, nineteenth))
		
	elif (selection == 5):
		print("\nAll right, {0}. Here we go with 'The Art of Espionage'.".format(name))
		print("You are going to be prompted to enter in 17 different words. Okay...go!")
		first = input("Enter a verb ending in 'ing': ")
		second = input("Enter an adjective: ")
		third = input("Enter another adjective: ")
		fourth = input("Enter a plural noun: ")
		fifth = input("Enter another adjective: ")
		sixth = input("Enter a person in the room: ")
		seventh = input("Enter another plural noun: ")
		eighth = input("Enter a place: ")
		ninth = input("Enter another adjective: ")
		tenth = input("Enter a celebrity: ")
		eleventh = input("Enter a noun: ")
		twelfth = input("Enter another plural noun: ")
		thirteenth = input("Enter another adjective: ")
		fourteenth = input("Enter another plural noun: ")
		fifteenth = input("Enter another plural noun: ")
		sixteenth = input("Enter another noun: ")
		seventeenth = input("Okay. Last one. Enter another plural noun: ")

		print("Get excited, {0}, because here comes your Mad Lib:\n".format(name))
		
		print("Espionage is the formal word for {0}. In the shadowy world of".format(first))
		print("spies, a/an {0} organization like the US government uses spies".format(second))
		print("to infiltrate {0} groups for the purpose of obtaining top secret".format(third))
		print("{0}. For example, spies might have to crack the code for accessing".format(fourth))
		print("confidential, {0} files, or their mission could be far more".format(fifth))
		print("dangerous - like stealing the key ingredient for making {0}'s".format(sixth))
		print("award-winning Explosive Fudgy {0}. Spies are found all over (the)".format(seventh))
		print("{0} - but they are not allowed to reveal their {1} identities. A".format(eighth, ninth))
		print("teacher, {0}, or even the little old {1} with the cane and fifteen".format(tenth, eleventh))
		print("pet {0} who lives next door to you could be a spy. The world of".format(twelfth))
		print("spying might seem glamorous and {0} - but it's filled with risks".format(thirteenth))
		print("and {0}! Sure, spies have a never-ending supply of supercool".format(fourteenth))
		print("electronic {0}, but they can't trust any {1} - which is why the".format(fifteenth, sixteenth))
		print("number one rule of spies is to keep friends close - and {0} closer!".format(seventeenth))
		
	else:
		print("You didn't input a correct value for one of the stories. Program ending :(")


mad_lib()
