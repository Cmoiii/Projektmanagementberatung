class MethodAttribute:
    def __init__(self, name, set, min, imin, imax, max):
        if set == 0:
            self.name = name
            self.min = min
            self.ideal_min = imin
            self.ideal_max = imax 
            self.max = max
        else:
            if min in set and imin in set and imax in set and max in set:
                self.name = name
                self.set = set
                self.min = min
                self.ideal_min = imin
                self.ideal_max = imax 
                self.max = max    

class ProjectMethod:
    def __init__(self, name: str, germanName:str, teams: MethodAttribute, teamsize: MethodAttribute, client: MethodAttribute, dependency: MethodAttribute, deadline: MethodAttribute, anforderung: MethodAttribute): 
            self.name = name
            self.germanName = germanName
            self.teams = teams
            self.teamsize = teamsize
            self.client = client
            self.dependency = dependency
            self.deadline = deadline
            self.anforderung = anforderung
            self.notIdeal = []

class Answer:
    def __init__(self, attribute, value, ideal: bool):
        self.attribute = attribute
        self.value = value
        self.ideal = ideal
