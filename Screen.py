from utils import show_heart
from Mark import Mark

class Screen:
    def __init__(self, header_space, body_space, game):
        self.header_space = header_space
        self.body_space = body_space
        self.game = game
        self.first_command = ''
        self.second_command = ''
        self.current_team = None
        self.mark_id = 0

    def print_mult(self, count, msg):
        c = 0
        while c < count:
            print(msg)
            c = c + 1

    def exit(self):
        print('See you next time!')


    def show_scoreboad(self):
        print('-------- SCOREBOARD -----------')
        line_num = 1
        for m in self.game.get_marks():
            print('%d %s %d' % (line_num, m.team.name, m.points))
            line_num = line_num + 1
        return line_num

    def show_help(self):
        print('-------- HELP MENU -----------')
        print(' exit - Stop this program')
        print(' help - show all commands')
        return 3

    def clear_command(self):
        self.first_command = ''
        self.second_command = ''
        self.current_team = None

    def render(self, command):
        info = ''
        self.print_mult(self.header_space, '')
        if command == 'score':
            self.first_command = command

            body_line = self.show_scoreboad()
        elif command == 'help':
            self.first_command = command

            body_line = self.show_help()
        elif command == 'add':
            self.first_command = command
            info = 'Please type a team id.'

            body_line = self.show_scoreboad()
        elif command == 'cancel':
            self.clear_command()
            info = ''

            body_line = self.show_scoreboad()
        elif self.first_command == 'add':
            if self.second_command == '':
                self.current_team = self.game.get_team(command)
                if self.current_team:
                    self.second_command = command
                    info = 'Please type points.'
                else:
                    info = 'Please type a valid team id.'
            else:
                # TODO: validate command to be valid points
                points = int(command)
                self.mark_id = self.mark_id + 1
                mark = Mark(self.mark_id, self.current_team, None, 1, points)
                self.game.add_mark(mark)
                info = 'Added mark successfully!'
                self.clear_command()

            body_line = self.show_scoreboad()
        else:
            body_line = show_heart()

        # padding the bottom if necessary
        self.print_mult(self.body_space - body_line, '')
        print('-------------------------------')
        print('Info: %s' % info)

