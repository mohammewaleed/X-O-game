import random2
from tkinter import *

user_win_times = 0
computer_win_times = 0
players = ["X", "O"]
player = random2.choice(players)

def turn(i, j):
  global player, user_win_times, computer_win_times
  if player == players[0] and not check_winner():
    buttons[i][j]["text"] = player
    buttons[i][j]["state"] = "disabled"

    if check_winner() is True and check_winner()!="tie":
      user_win_times+=1
      label.config(text=("You: " + str(user_win_times) + " ") + ("Computer: " + str(computer_win_times)))
    else:
      player = players[1]
      computer_turn()

  elif player == players[1] and not check_winner():
    computer_turn()

def computer_turn():
    global player,computer_win_times
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]
    
    if empty_cells:
      i, j = random2.choice(empty_cells)
      buttons[i][j]["text"] = players[1] 
      buttons[i][j]["state"] = "disabled"

      if check_winner() is True and check_winner() != "tie":
        computer_win_times += 1
        label.config(text=("You: " + str(user_win_times) + " ") + ("Computer: " + str(computer_win_times)))
      else:
        player = players[0]

def check_winner():
    # row check
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            label2.config(text=f"{buttons[i][0]['text']} wins!")
            buttons[i][0].config(bg="cyan")
            buttons[i][1].config(bg="cyan")
            buttons[i][2].config(bg="cyan")
            return True

    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            label2.config(text=f"{buttons[0][j]['text']} wins!")
            buttons[0][j].config(bg="cyan")
            buttons[1][j].config(bg="cyan")
            buttons[2][j].config(bg="cyan")
            return True

    # diagonal check
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        label2.config(text=f"{buttons[0][0]['text']} wins!")
        buttons[0][0].config(bg="cyan")
        buttons[1][1].config(bg="cyan")
        buttons[2][2].config(bg="cyan")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        label2.config(text=f"{buttons[0][2]['text']} wins!")
        buttons[0][2].config(bg="cyan")
        buttons[1][1].config(bg="cyan")
        buttons[2][0].config(bg="cyan")
        return True

    # tie check
    for x in range(3):
        for y in range(3):
            if buttons[x][y]["text"] == "":
                return False  # There are still empty spaces, the game is not a tie

    for x in range(3):
        for y in range(3):
            buttons[x][y].config(bg="red")
    label2.config(text="Tie, No Winner!")
    return "tie"

def restart_game():
    label2.config(text="")
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j].config(bg="SystemButtonFace")
            buttons[i][j]["state"] = "active"

window = Tk()
new_frame = Frame(window)
window.title("Tic-Tac-Toe game")

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(new_frame, text="", font=("sans", 40), width=10, height=3, command=lambda i=i, j=j: turn(i, j))
        buttons[i][j].grid(row=i, column=j)

label = Label(window, text=("You: " + str(user_win_times) + " ") + ("Computer: " + str(computer_win_times)),font=("sans", 20))
label2 = Label(window, text="", pady=15, font=("bold", 40))
restart_button = Button(window, text="restart", width=10, height=1, font=("sans", 15), command=restart_game)

label.pack()
label2.pack()
restart_button.pack()
new_frame.pack()
window.mainloop()