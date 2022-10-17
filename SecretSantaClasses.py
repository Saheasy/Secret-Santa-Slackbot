import random
from json_parser import JsonParser

class SecretSanta(JsonParser):
    
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