import json

class JsonParser:
    def __init__(self, filename):
        self.filename = filename
        file = open(filename)
        self.data = json.load(file)
        file.close()
    
    def update_from_file(self):
        file = open(self.filename)
        self.data = json.load(file)
        file.close()

    def print_contents(self):
        print(self.data)

    def dump(self, dictionary):
        with open(self.filename, "w") as file:
            json.dump(dictionary, file)
            file.close()

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
    parser = JsonParser("test.json")
    parser.set_begin("2022-12-2", "2022-12-5", "dsadaiofja", "dmadadaj")
    parser.print_contents()
    
    
    