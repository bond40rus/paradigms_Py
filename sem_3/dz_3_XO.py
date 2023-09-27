from tkinter import *


class XO:
    def __init__(self, size):
        self._size = size
        self._matrix = []
        self._active_player = "Player # Х"
        self._markX = "X"
        self._markO = "O"
        self._enum_mark = "X"
        self.end_game = False

        for i in range(self._size):
            ls = ["-"] * self._size
            self._matrix.append(ls)

    def getMark(self):
        return self._enum_mark

    def setMark(self):
        if self._active_player == "Player # O":
            self._enum_mark = "X"
        elif self._active_player == "Player # Х":
            self._enum_mark = "O"

    def get_size(self):
        return self._size

    def getActivePl(self):
        return self._active_player

    def getX(self):
        return self._markX

    def getO(self):
        return self._markO

    def show_xo(self):
        for n, i in enumerate(self._matrix):
            for k in self._matrix[n]:
                print(k, end=" ")
            print()
        print()

    def step(self, x, y):
        """для игры через интефейс"""
        if self.check_end_game() or self.check_winner():
            print("End Game")
            self.end_game = True

        else:
            if (x <= self._size and y <= self._size) and self._matrix[x - 1][y - 1] == "-":
                print(f'Ходит {self._active_player}')
                if self._active_player == "Player # Х":
                    self._matrix[x - 1][y - 1] = self._markX
                    self._active_player = "Player # O"
                    self._enum_mark = "O"
                else:
                    self._matrix[x - 1][y - 1] = self._markO
                    self._active_player = "Player # Х"
                    self._enum_mark = "X"
                return self.show_xo()
            else:
                self.setMark()
                print(f'Не верно. {self._active_player} выберите другую ячейку ')



    def check_end_game(self):
        count = 0
        for n, i in enumerate(self._matrix):
            for k in self._matrix[n]:
                if k != "-":
                    count += 1
        return False if count < self._size ** 2 else True

    def start_game(self):
        """для  игры в терминале"""

        while not self.check_end_game():
            print(f'{self._active_player} выбирает...')
            x = int(input("Строка = "))
            y = int(input("Столбик = "))
            self.step(x, y)

    def check_winner(self) -> bool:
        for i in range(3):
            if self._matrix[i][0] == self._matrix[i][1] == self._matrix[i][2] == self._markX or \
                    self._matrix[i][0] == self._matrix[i][1] == self._matrix[i][2] == self._markO:

                return True
        if self._matrix[0][0] == self._matrix[1][1] == self._matrix[2][2] == self._markX or \
           self._matrix[0][2] == self._matrix[1][1] == self._matrix[2][0] == self._markO:

            return True
        else:
            return False


###########

class Window(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.ng = XO(3)

    def initUI(self):
        self.master.title("XO game")
        self.pack(fill=BOTH, expand=True)

        fr1 = Frame(self)
        fr1.pack(fill=X)
        self.lb = Label(fr1, text="Ходит Player # X")
        self.lb.pack(fill=X, padx=10, expand=True)

        fr2 = Frame(self)
        fr2.pack(fill=X)
        for i in range(3):
            for j in range(3):
                self.butt1 = Button(fr2, text="-", width=10)
                self.butt1.configure(command=lambda button=self.butt1: self.pr(button)) # узнаем по какой нопке щелкнул пользователь
                self.butt1.grid(row=i, column=j)

        fr3 = Frame(self)
        fr3.pack(fill=X)
        self.butt2 = Button(fr3, text="Exit", command=self.onExit)
        self.butt2.pack(fill=X, padx=0, expand=True, pady=5)

    def onExit(self):
        self.quit()

    def pr(self, butt):
        """Щелкаем по кнопке"""
        if self.ng.end_game:
            self.lb.configure(text="End Game")

        else:
            gi = butt.grid_info()
            x = gi['row']
            y = gi['column']
            self.ng.step(x + 1, y + 1)
            self.lb.configure(text=f"Ходит {self.ng.getActivePl()}")
            if self.ng.getActivePl() == "Player # O":
                butt.configure(text="X")
            else:
                butt.configure(text="O")


def main():
    window = Tk()
    # window.geometry("360x360")
    window.resizable(width=False, height=False)
    app = Window()
    window.mainloop()


if __name__ == '__main__':
    main()

# new_game = XO(3)
# new_game.show_xo()
# new_game.start_game()
