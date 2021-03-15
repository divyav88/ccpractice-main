
from json import JSONEncoder
class JsonClassEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__  