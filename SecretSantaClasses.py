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
    
    def write_user(self, username, user_data):
        print(self.data)
        self.data['users'][username] = {
            "name":user_data["name"],
            "interests": user_data["interests"],
            "groups": user_data["groups"],
            "location": user_data["location"],
            "secret_santa_recipient": "",
            "roles": user_data["roles"]
            }
        self.dump(self.data)

    def make_user_data(self, name, interests, groups, location, roles):
        return {"name":name,
            "interests": interests,
            "groups": groups,
            "location": location,
            "secret_santa_recipient": "",
            "roles": roles 
            }

    def set_begin(self, begin_date, start_date, manager, channel_id):
        self.data['begin_date'],self.data['start_date'],self.data['manager'], self.data['channel_id'] =  begin_date, start_date, manager, channel_id
        self.dump(self.data)

if __name__ == "__main__":
    thisYear = SecretSanta('test.json')
    thisYear.randomize()

