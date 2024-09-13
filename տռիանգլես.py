WHITE = 1
BLACK = 0
def correct_coords(row, col):
    """Ֆունկցիան ստուգում է, որ (row, col) կոորդինատները
    գտնվում են խաղատախտակի ներսում"""
    return 0 <= row < 8 and 0 <= col < 8

def opponent(col):
    if col == WHITE:
        return  BLACK
    return WHITE
class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        # Սպիտակ զինվորը E2 դաշտում։
        self.field[1][4] = Pawn(1, 4, WHITE)
        self.field[0][0] = Rook(7, 0, BLACK)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Տեղափոխել խաղաքարը (row, col) կետից (row1, col1) կետ:
        Եթե տեղափոխումը հնարավոր է, ապա մեթոդը կկատարի այն և կվերադարձնի True արժեքը:
        Հակառակ դեպքում այն կվերադարձնի False արժեքը"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # չի կարելի խաղաքարը միևնույն դաշտ տեղափոխել
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Վերցնել խաղաքարը:
        self.field[row1][col1] = piece  # Դնել նոր տեղում:
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Զինվորը կարող է քայլել միայն ուղղահայաց ուղղությամբ
        # "անցման ժամանակ զինվորը վերցնելու" կանոնը իրականացված չէ
        if self.col != col:
            return False

        # Սկզբնական դիրքից զինվորը կարող է 2 դաշտ առաջ տեղափոխվել,
        # ուստի սկզբնական շարքի ցուցիչը տեղադրենք start_row փոփոխականում:
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # քայլ 1 դաշտ առաջ
        if self.row + direction == row:
            return True

        # քայլ սկզբնական դիրքից 2 դաշտ առաջ
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        #  Հնարավոր չէ խաղաքարը տեղափոխել դաշտ, որը միևնույն շարքում
        # կամ սյունակում չի գտնվում:
        if self.row != row and self.col != col:
            return False

        return True
def print_board(board):  # Տպել խաղատախտակը տեքստային տեսքով (տե՛ս էկրանի պատկերը)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Ստեղծում ենք շախմատի խաղատախտակ
    board = Board()
    # Խաղացողների հրամանների ներածման ցիկլ
    while True:
        # Արտածում ենք խաղատախտակի վրա խաղաքարերի դասավորությունը
        print_board(board)
        # Հուշում հրամանների վերաբերյալ
        print('Հրամաններ՝')
        print('    exit                               -- ելք')
        print('    move <row> <col> <row1> <col1>     -- хքայլ (row, col) դաշտից')
        print('                                          դաշտ (row1, col1)')
        if board.current_player_color() == WHITE:
            print('Սպիտակների քայլը՝')
        else:
            print('Սևերի քայլը՝')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Հաջող քայլ')
        else:
            print('Կոորդինատները սխալ են: Փորձեք ուրիշ քայլ կատարել:')
main()