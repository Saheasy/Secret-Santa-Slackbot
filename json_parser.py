import json

class JsonParser:
    def __init__(self, filename):
        self.filename = filename
        file = open(filename)
        self.data = json.load(file)
        if 'users' not in self.data:
            self.data['users'] = {}
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

    

if __name__ == "__main__":
    parser = JsonParser("test.json")
    parser.set_begin("2022-12-2", "2022-12-5", "dsadaiofja", "dmadadaj")
    parser.print_contents()
    
    
    