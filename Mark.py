class Mark:
    def __init__(self, id, team, judge, task_type, points):
        self.id = id
        self.team = team
        self.judge = judge
        self.task_type = task_type #1 - performance, 2 - presentation
        self.points = points