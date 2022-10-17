import random
from json_parser import JsonParser

class SecretSanta(JsonParser):

    pathfinders = {
        "michelle" : {
            "interests":"Penguins, crafts and pool", 
            "recommendation":"Get her a Piplup plush from pokemon",
            "groups":"Pathfinders Leadership",
            "location": "Iowa City",
            "secret_santa_recipient":"",
            "roles":[]},
        "jill" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Leadership",
            "location": "Iowa City",
            "secret_santa_recipient":"",
            "roles":[]}, 
        "gina" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Leadership",
            "location": "Iowa City",
            "secret_santa_recipient":"",
            "roles":[]}, 
        "astrid" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Protozoic",
            "location": "San Antonio",
            "secret_santa_recipient":"",
            "roles":[]}, 
        "david" : {
            "interests": "Godzilla. Recomendation: Maybe something with Godzilla or dinosaurs.", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City",
            "roles":[]}, 
        "edwin" : "Incense, music and movies. Recomendation: Incense or movie tickets.",  
        "hallee" : "Harry Poter, Ice Cream, Tea Bombs. Recomendation: ", 
        "kaiser" : "3 Musketeers, Hippos, and color green. Recomendation: Maybe a plant they're green!",
        "kaleb" : {
            "interests": "", 
            "recommendation":"",
            "groups":"Pathfinders Protozoic",
            "location": "Iowa City",
            "roles":[]}, 
        "katie" : "Food, puzzles, art stuff and sleep. Recomendation: Restaurant gift cards or Liberty puzzels", 
        "lance" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City",
            "roles":[]}, 
        "lily" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City",
            "roles":[]}, 
        "matt" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Protozoic",
            "location": "Iowa City",
            "roles":[]}, 
        "miguel" : "Unicorns, Fairies, paintis, and dice. Recomendation: ", 
        "naoki" : "Food. Recommendation: Get him some restaurant gift cards.",
        "sadie" : " ", 
        "samantha" : "Chips, board games, movies, and travel. Recomendation: care package.", 
        "sara" : "Books, board games, and blankets. Recomendation: A pretty personal throw blanket.", 
        "spencer" : {
            "interests": "", 
            "recommendation":"",
            "groups":"Pathfinders Protozoic",
            "location": "Iowa City",
            "roles":[]}, 
        "shantel" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Protozoic",
            "location": "San Antonio",
            "roles":[]}, 
        "tammy" : {
            "interests": "", 
            "recommendation": "",
            "location": "San Antonio",
            "roles":[]}, 
        "trey" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City",
            "roles":[]},  
        "viviana" : "The Nightmare before Christmas, Pokemons (Snorlax), Anime. Recomendation: Action figurines or plushies.", 
        "will" : "Star Wars. Recomendation: Starbucks gift card."
        } #end of dictionary 
    
    def __init__(self, filename):
        JsonParser.__init__(self,filename)

    def randomize(self):
        
        my_list = list(self.data['users'].keys())
        random.shuffle(my_list)
        pairs = zip(my_list[::2], my_list[1::2] )
        print(dict(pairs))

if __name__ == "__main__":
    thisYear = SecretSanta('test.json')
    thisYear.randomize()