import random

class SecretSanta:
    pathfinders = {
        "michelle" : {
            "interests":"Penguins, crafts and pool", 
            "recommendation":"Get her a Piplup plush from pokemon",
            "groups":"Pathfinders Leadership",
            "location": "Iowa City"},
        "jill" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Leadership",
            "location": "Iowa City"}, 
        "gina" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Leadership",
            "location": "Iowa City"}, 
        "astrid" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Protozoic",
            "location": "San Antonio"}, 
        "david" : "Godzilla. Recomendation: Maybe something with Godzilla or dinosaurs.",
        "edwin" : "Incense, music and movies. Recomendation: Incense or movie tickets.",  
        "hallee" : "Harry Poter, Ice Cream, Tea Bombs. Recomendation: ", 
        "kaiser" : "3 Musketeers, Hippos, and color green. Recomendation: Maybe a plant they're green!",
        "kaleb" : {
            "interests": "", 
            "recommendation":"",
            "groups":"Pathfinders Protozoic",
            "location": "Iowa City"}, 
        "katie" : "Food, puzzles, art stuff and sleep. Recomendation: Restaurant gift cards or Liberty puzzels", 
        "lance" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City"}, 
        "lily" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City"}, 
        "matt" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Protozoic",
            "location": "Iowa City"}, 
        "miguel" : "Unicorns, Fairies, paintis, and dice. Recomendation: ", 
        "naoki" : "Food. Recommendation: Get him some restaurant gift cards.",
        "sadie" : " ", 
        "samantha" : "Chips, board games, movies, and travel. Recomendation: care package.", 
        "sara" : "Books, board games, and blankets. Recomendation: A pretty personal throw blanket.", 
        "spencer" : {
            "interests": "", 
            "recommendation":"",
            "groups":"Pathfinders Protozoic",
            "location": "Iowa City"}, 
        "shantel" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Protozoic",
            "location": "San Antonio"}, 
        "tammy" : {
            "interests": "", 
            "recommendation": "",
            "location": "San Antonio"}, 
        "trey" : {
            "interests": "", 
            "recommendation": "",
            "groups":"Pathfinders Archean",
            "location": "Iowa City"},  
        "viviana" : "The Nightmare before Christmas, Pokemons (Snorlax), Anime. Recomendation: Action figurines or plushies.", 
        "will" : "Star Wars. Recomendation: Starbucks gift card."
        } #end of dictionary 
    
    def __init__(self):
        pass

    def randomize(self):
        for name in self.pathfinders.keys():
            print(f'{name}')
            print(list(self.pathfinders.keys()))
    
if __name__ == "__main__":
    thisYear = SecretSanta()
    thisYear.randomize()