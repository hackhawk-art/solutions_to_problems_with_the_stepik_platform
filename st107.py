class TicTacToe:
    def __init__(self):
        # Инициализация пустого поля 3x3
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Первый ход делает игрок, ставящий крестики
        self.game_over = False

    def mark(self, row, col):
        # Проверка, завершена ли игра
        if self.game_over:
            print("Игра окончена")
            return

        # Проверка корректности координат (1-3)
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Недоступная клетка")
            return

        r, c = row - 1, col - 1

        # Проверка, свободна ли клетка
        if self.board[r][c] != ' ':
            print("Недоступная клетка")
            return

        # Помечаем клетку текущим игроком
        self.board[r][c] = self.current_player

        # Проверяем победителя после хода
        winner = self.winner()
        if winner or winner == "Ничья":
            self.game_over = True

        # Меняем игрока только если игра не завершена
        if not self.game_over:
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def winner(self):
        lines = []

        # строки и столбцы
        for i in range(3):
            lines.append(self.board[i])  # строки
            lines.append([self.board[0][i], self.board[1][i], self.board[2][i]])  # столбцы

        # диагонали
        lines.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        lines.append([self.board[0][2], self.board[1][1], self.board[2][0]])

        # Проверка на победителя
        for line in lines:
            if line[0] == line[1] == line[2] != ' ':
                return line[0]

        # Проверка на ничью (если все клетки заполнены и победителя нет)
        if all(cell != ' ' for row in self.board for cell in row):
            return "Ничья"

        # Игра еще не завершена
        return None

    def show(self):
        for i in range(3):
            print('|'.join(self.board[i]))
            if i < 2:
                print('-----')
    
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
        
