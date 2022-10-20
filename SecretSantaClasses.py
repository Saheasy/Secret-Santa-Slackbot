import random
from json_parser import JsonParser
from apscheduler.schedulers.background import BackgroundScheduler

class SecretSanta(JsonParser):

    def __init__(self, filename):
        JsonParser.__init__(self,filename)
        self.scheduler = BackgroundScheduler()
        if "begin_date" in self.data and "start_date" in self.data:
            #self.begin_date = self.scheduler.add_job(self.begin, self.data['begin_date'])
            #self.start_date = self.scheduler.add_job(self.start, self.data['start_date'])
            #self.scheduler.start()
            print("start scheduler")

    def begin(self):
        pass

    def start(self):
        pass

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
    
    def set_user(self, id, name, username, interests, groups,groups_slack, location, location_slack):
        self.data['users'][id] = {
            'name':name,
            'username':username,
            'interests':interests,
            'groups':groups,
            'groups_slack':groups_slack,
            'location':location,
            'location_slack': location_slack
        }
        self.dump(self.data)
    
    def get_user(self, id):
        return {
            'interests':self.data['users']['id']['interests'],
            'groups':self.data['users']['id']['groups'],
            'location':self.data['users']['id']['location']
        }

    def isUserInDatabase(self, user_id):
        if user_id in self.data['users']:
            return True
        return False

    
if __name__ == "__main__":
    thisYear = SecretSanta('test.json')
    thisYear.randomize()

