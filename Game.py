def get_points(mark):
    return mark.points

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
        dict = {}
        for mark in self.marks:
            if mark.team.id in dict:
                if mark.points > dict[mark.team.id].points:
                    dict[mark.team.id] = mark
            else:
                dict[mark.team.id] = mark
        # unique mark for each team
        teams = []
        # turn dict into a list order by points descending
        for i in dict.items():
            teams.append(i[1])

        # use sort to sort the teams by points. get_points is a function at the top
        teams.sort(key=get_points, reverse=True)
        return teams

