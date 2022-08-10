class Game:
    def __init__(self):
        self.judges = []
        self.teams = []
        self.marks = []

    def add_judge(self, judge):
        self.judges.append(judge)

    def add_team(self, team):
        self.teams.append(team)

    def get_team(self, id):
        for t in self.teams:
            if t.id == id:
                return t
        return None

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_marks(self):
        # TODO: group by team and sort by points descending
        return self.marks