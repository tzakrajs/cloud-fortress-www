import json
import tornado.web

from core import route


users = {10010: {"name": "Sundar McBrowser-Barr",
                 "title": "Chief Electrity Officer",
                 "manager": [10000,],
                 "employees": [10020, 10021, 10022]},
         10000: {"name": "Larry Pagerton",
                 "title": "Master of Everything",
                 "manager": [],
                 "employees": [10010, 11000]}, 
         10020: {"name": "Kenneth Ham",
                 "title": "SVP of Theology Engineering",
                 "manager": [10010],
                 "employees": []}, 
         10021: {"name": "Jesse Jackson",
                 "title": "SVP of Faith Marketing",
                 "manager": [10010],
                 "employees": []}, 
         10022: {"name": "Pat Robertson",
                 "title": "SVP of Religious Recruiting",
                 "manager": [10010],
                 "employees": [10030, 10031, 10032]}, 
         10030: {"name": "Billy Gates",
                 "title": "Director of Recruitment Strategy",
                 "manager": [10022],
                 "employees": []}, 
         10031: {"name": "Mark Zarkerderg",
                 "title": "Director of Recruitment Apps",
                 "manager": [10022],
                 "employees": []}, 
         10032: {"name": "Jerry Yin-Yang",
                 "title": "Director of Recruitment Marketing",
                 "manager": [10022],
                 "employees": []}, 
         11000: {"name": "Sergio Brine",
                 "title": "Chief Secrets Officer",
                 "manager": [10000],
                 "employees": [11001, 11002]},
         11001: {"name": "Lawrence Kriss-Kross",
                 "title": "SVP of Moonshot Theoretics",
                 "manager": [11000],
                 "employees": [11020, 11021, 11022]}, 
         11020: {"name": "Fox Mulder",
                 "title": "Director of Belief",
                 "manager": [11001],
                 "employees": []}, 
         11021: {"name": "Alex Jonestown",
                 "title": "Director of Fear",
                 "manager": [11001],
                 "employees": []}, 
         11022: {"name": "Tronald Dump",
                 "title": "Director of Attrition",
                 "manager": [11001],
                 "employees": []}, 
         11002: {"name": "Tyson Degrasse O'neil",
                 "title": "SVP of Moonshot Physics",
                 "manager": [11000],
                 "employees": [11030, 11031]},
         11030: {"name": "Steven Hawkiverse",
                 "title": "Director of [REDACTED]",
                 "manager": [11002],
                 "employees": []}, 
         11031: {"name": "Alan Toorang",
                 "title": "Director of Enigmatics",
                 "manager": [11002],
                 "employees": []}, 
}

# Test ListUsers
@route('/api/users')
class ListUsers (tornado.web.RequestHandler):
    def get(self):
        user_list = list(users.keys())
        self.write(json.dumps(user_list))

# Test GetUser
@route('/api/user')
class GetUser (tornado.web.RequestHandler):
    def get(self):
        user_id = self.get_argument('id', None)
        user_info = users.get(int(user_id))
        self.write(json.dumps(user_info))
