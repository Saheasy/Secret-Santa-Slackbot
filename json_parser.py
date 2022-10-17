import json

class JsonParser:
    def __init__(self, filename):
        self.filename = filename
        file = open(filename)
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

if __name__ == "__main__":
    parser = JsonParser("test.json")
    parser.print_contents()
    
    