from Screen import Screen
from Game import Game
from Judge import Judge
from Team import Team

def load_game():
    game = Game()
    # add judges to the game
    f1 = open("./data/judges.txt", "r")
    while True:
        line = f1.readline()
        # check if end of file
        if len(line) == 0:
            break
        x1 = line.split('|')
        judge = Judge(x1[0], x1[1])
        game.add_judge(judge)
    f1.close()

    # add teams to the game
    f2 = open("./data/teams.txt", "r")
    while True:
        line = f2.readline()
        # check if end of file
        if len(line) == 0:
            break
        x2 = line.split('|')
        team = Team(x2[0], x2[1], x2[2])
        game.add_team(team)
    f2.close()

    '''
    judge_vivian = Judge('vi', 'Vivan Jo')
    game.add_judge(judge_vivian)

    team_a1 = Team('a1', 'Raptor', 'Michael No, Lilian Fer')
    game.add_team(team_a1)
    team_a2 = Team('a2', 'Panda', 'Greg Wu, Grace Hi')
    game.add_team(team_a2)
    '''

    return game

if __name__ == "__main__":
    game = load_game()
    screen = Screen(6, 10, game) # define screen size (header, body)

    # start command console
    command = 'score'
    while command != 'exit':
        screen.render(command)
        command = input('>')

    screen.exit()