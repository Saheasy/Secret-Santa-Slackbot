''' Create a program in Python that will assign secret Santa's for the apprenticeship group.
Adding ideas of gifting a presents per apprentice when they're been pair.

Need an input from user. 
Program will ask for the user's name and select a randon apprentice from the list to assigned
and displays the likes/gift ideas for that person (maybe)

- Need to create list(s) of apprentice 
- Randomization cannot assigened the appretice to themselves 
- cannot be assiged the same person more than once 
- once it assings will dispaly a list of likes to the secret santa (maybe) '''
#============================================================================================================
# Desired output from code: 
# Name --------- Secrete Santa
# Kaiser ------- Astrid 
# Lily --------- Trey 
# Hallee ------- Lance
#
# Enter your secrete Sata's name: Naoki  
# Naoki likes food. Recommendation: Get him some restaurant gift cards.
# Enter your secrete Sata's name: Michelle
# Michelle likes penguins, crafts and pool. Recomendation: Get her a Piplup plush from pekemon.
#=============================================================================================================

# importing the random object
import random


#list of apprentice
apprentices1 = ["Michelle", "Jill", "Gina", "David", "Hallee", "Kaiser", "Lance", "Lily", "Naoki", "Trey", "Matt",
"Kaleb", "Katie", "Sadie", "Samantha", "Sara", "Spencer", "Astrid", "Miguel", "Edwin", "Shantel", "Tammy", 
"Viviana", "Will"]

apprentices2 = ["Michelle", "Jill", "Gina", "David", "Hallee", "Kaiser", "Lance", "Lily", "Naoki", "Trey", "Matt",
"Kaleb", "Katie", "Sadie", "Samantha", "Sara", "Spencer", "Astrid", "Miguel", "Edwin", "Shantel", "Tammy", 
"Viviana", "Will"]

# Code is going thru both list to pair the apprentice for their secrete santa
all_pairings = []                       # new list that is saving the pairs of names after then been drown

while (bool(apprentices1)):              # loop is going thur the list until all names have a pair 
    bowl1 = random.choice(apprentices1)  # randomizer 

    bowl2 = random.choice(apprentices2)  # randomizer 
    if bowl1 != bowl2:                   # true false condition to make sure no name gets asing to itselt 
        apprentices1.remove(bowl1)       # name is drown and romeoved from bowl

        apprentices2.remove(bowl2)

        pairing = [bowl1, bowl2]        # pairing names from both bowls 

        all_pairings.append(pairing)    # adding pairs to list of all_pairings 

print("The secrete santa's List is: " "\n Participants \tSecrete Santa" ) #+ str(all_pairings))
for pairs in range(len(all_pairings)):
    print(all_pairings[pairs])

# Dictionary 
apprentice_info = {"michelle" : "Penguins, crafts and pool. Recomendation: Get her a Piplup plush from pekemon.",
 "jill" : " ", 
 "gina" : " ",
 "astrid" : " ", 
 "david" : "Godzilla. Recomendation: Maybe something with Godzilla or dinosaurs.",
 "edwin" : "Incense, music and movies. Recomendation: Incense or movie tickets.",  
 "hallee" : "Harry Poter, Ice Cream, Tea Bombs. Recomendation: ", 
 "kaiser" : "3 Musketeers, Hippos, and color green. Recomendation: Maybe a plant they're green!",
 "kaleb" : " ", 
 "katie" : "Food, puzzles, art stuff and sleep. Recomendation: Restaurant gift cards or Liberty puzzels", 
 "lance" : " ",
 "lily" : " ",
 "matt" : " ",
 "miguel" : "Unicorns, Fairies, paintis, and dice. Recomendation: ", 
 "naoki" : "Food. Recommendation: Get him some restaurant gift cards.",
 "sadie" : " ", 
 "samantha" : "Chips, board games, movies, and travel. Recomendation: care package.", 
 "sara" : "Books, board games, and blankets. Recomendation: A pretty personal throw blanket.", 
 "spencer" : " ",  
 "shantel" : " ",
 "tammy" : " ",
 "trey" : " ", 
 "viviana" : "The Nightmare before Christmas, Pokemons (Snorlax), Anime. Recomendation: Action figurines or plushies.", 
 "will" : "Star Wars. Recomendation: Starbucks gift card."} #end of dictionary 

#Code to print the suggestions on gifts 
#users_name == apprentice_info
while True:
    users_name = input("Enter your secret santa's name: ").lower() # saves the input into the variable
    if users_name == "exit":
        break
    print(users_name + " likes " + apprentice_info[users_name])