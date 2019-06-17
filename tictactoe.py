import colorama


class Game:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def game_display(self):
        """Displays the game board"""
        print("   0  1  2")
        for index, row in enumerate(self.board):
            print(index, row)

    def get_rows(self):
        """Returns a combination of all possible winning rows."""
        board_rows = {
            'r1': self.board[0],
            'r2': self.board[1],
            'r3': self.board[2],
            'r4': [self.board[0][0], self.board[1][0], self.board[2][0]],
            'r5': [self.board[0][1], self.board[1][1], self.board[2][1]],
            'r6': [self.board[0][2], self.board[1][2], self.board[2][2]],
            'r7': [self.board[0][0], self.board[1][1], self.board[2][2]],
            'r8': [self.board[0][2], self.board[1][1], self.board[2][0]]}
        return board_rows

    def check_full(self):
        """Checks if tie / board is full"""
        full = True
        for i in self.board:
            if i.count(0) > 0:
                full = False
                break
        return full


class Player:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def get_move(move):
        """Helper function for self.player_move.
        Gets the move from user input."""
        result = []
        for l in move:
            if l.isdigit():
                result.append(int(l))
        return tuple(result)

    def player_move(self, board):
        """Prompts player to make a move, changes board"""
        move = input(colorama.Fore.CYAN + '\nplayer {}: '.format(self.num) + colorama.Fore.RESET)
        move = self.get_move(move)
        coord = board[move[0]][move[1]]
        if coord == 0:
            board[move[0]][move[1]] = self.num
        else:
            print(colorama.Fore.RED + '\nInvalid move. Try Again.' + colorama.Fore.RESET)
            self.player_move(board)

    def win_check(self, board_rows):
        """Checks if player won"""
        win = False
        for key, row in board_rows.items():
            if row.count(self.num) == 3:
                win = True
                break
        return win


def start(game_obj, player1_obj, player2_obj):
    """The main UI"""
    i = 0

    while i < 2:
        game_obj.game_display()
        if i == 0:
            player1_obj.player_move(game_obj.board)
            i += 1
            if player1_obj.win_check(game_obj.get_rows()):
                i = 2
            elif game_obj.check_full():
                i = 4
        else:
            player2_obj.player_move(game_obj.board)
            i -= 1
            if player2_obj.win_check(game_obj.get_rows()):
                i = 3
            elif game_obj.check_full():
                i = 4

    game_obj.game_display()
    if i == 2:
        print('Congratulations, player1!')
    elif i == 3:
        print('Congratulations, player2!')
    else:
        print('Tie!')


tictactoe = Game()
player1 = Player(1)
player2 = Player(2)

print(colorama.Fore.BLUE + '\nWelcome to tic-tac-toe!\n' + colorama.Fore.RESET)
start(tictactoe, player1, player2)
