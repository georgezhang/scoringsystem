from Screen import Screen
from Game import Game
from Judge import Judge
from Team import Team

def load_game():
    game = Game()
    judge_george = Judge('ge', 'George Zhang')
    game.add_judge(judge_george)
    judge_vivian = Judge('vi', 'Vivan Jo')
    game.add_judge(judge_vivian)

    team_a1 = Team('a1', 'Raptor', 'Michael No, Lilian Fer')
    game.add_team(team_a1)
    team_a2 = Team('a2', 'Panda', 'Greg Wu, Grace Hi')
    game.add_team(team_a2)

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