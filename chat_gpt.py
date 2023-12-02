import random2
from tkinter import Tk, Frame, Button, Label

class TicTacToe:
    def __init__(self):
        self.user_win_times = 0
        self.computer_win_times = 0
        self.players = ["X", "O"]
        self.player = random2.choice(self.players)

    def switch_player(self):
        self.player = self.players[1] if self.player == self.players[0] else self.players[0]

    def check_winner(self):
        # Check for a winner and update the UI accordingly
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.declare_winner(self.buttons[i][0]["text"])
                return True

            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.declare_winner(self.buttons[0][i]["text"])
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.declare_winner(self.buttons[0][0]["text"])
            return True
        elif self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.declare_winner(self.buttons[0][2]["text"])
            return True

        if all(self.buttons[x][y]["text"] != "" for x in range(3) for y in range(3)):
            self.declare_winner("Tie")
            return True

        return False

    def declare_winner(self, winner):
        if winner == "Tie":
            self.label2.config(text="Tie, No Winner!")
        else:
            self.label2.config(text=f"{winner} wins!")

        for x in range(3):
            for y in range(3):
                self.buttons[x][y].config(bg="cyan" if winner != "Tie" else "red")

        if winner == "X":
            self.user_win_times += 1
        elif winner == "O":
            self.computer_win_times += 1

        self.update_score()

    def computer_turn(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"] == ""]

        if empty_cells:
            i, j = random2.choice(empty_cells)
            self.buttons[i][j]["text"] = self.players[1]
            self.buttons[i][j]["state"] = "disabled"

            if not self.check_winner():
                self.switch_player()

    def restart_game(self):
        self.label2.config(text="")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j].config(bg="SystemButtonFace")
                self.buttons[i][j]["state"] = "active"

    def update_score(self):
        self.label.config(text=f"You: {self.user_win_times} Computer: {self.computer_win_times}")

    def turn(self, i, j):
        if self.buttons[i][j]["text"] == "" and not self.check_winner():
            self.buttons[i][j]["text"] = self.player
            self.buttons[i][j]["state"] = "disabled"

            if not self.check_winner():
                self.switch_player()
                self.computer_turn()

    def create_gui(self):
        self.window = Tk()
        self.new_frame = Frame(self.window)
        self.window.title("Tic-Tac-Toe game")

        self.buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.new_frame, text="", font=("sans", 40),
                                            width=10, height=3, command=lambda i=i, j=j: self.turn(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.label = Label(self.window, text=f"You: {self.user_win_times} Computer: {self.computer_win_times}",
                           font=("sans", 20))
        self.label2 = Label(self.window, text="", pady=15, font=("bold", 40))
        self.restart_button = Button(self.window, text="restart", width=10, height=1,
                                     font=("sans", 15), command=self.restart_game)

        self.label.pack()
        self.label2.pack()
        self.restart_button.pack()
        self.new_frame.pack()

        self.window.mainloop()

def main():
    game = TicTacToe()
    game.create_gui()

if __name__ == "__main__":
    main()
