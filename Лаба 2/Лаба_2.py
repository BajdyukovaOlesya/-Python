import json
class Animal:
     def __init__(self,n):
         self.name=n
    

class Bird(Animal):
    def __init__(self,n,s):
        Animal.__init__(self,n)
        self.sound=s
    def what(self):
        return f'{self.name} says {self.sound}'
       
bird=Bird('titmouse','tweet-tweet')
print(bird.what())

json_string = json.dumps(bird, default=lambda obj: obj.__dict__,sort_keys=True,indent=4)
print(json_string)

def ld(d):
    return Bird(d['name'],d['sound'])

bird=json.loads(json_string, object_hook=ld)
print(bird.what())
