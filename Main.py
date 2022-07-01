import tkinter as tk
from Home_Screen import Home_dlg_class
from Add_Questions import Add_Questions_dlg_class
from create_teams import Create_Teams_Dlg, Get_Number_Of_Teams
from Game_Board import Game_Board_dlg_class, Display_Question_dlg, Check_Answers_dlg
from Extra import *
from the_game import The_Game_Class


def load_questions(the_questions):

    try:
        this_file = open('the_questions.txt', 'r')

        for one_line in this_file.readlines():
            subject = one_line.partition(',')[0]
            one_line = one_line.partition(',')[2]
            difficulty = int(one_line.partition(',')[0])
            one_line = one_line.partition(',')[2]
            order = int(one_line.partition(',')[0])
            one_line = one_line.partition(',')[2]
            the_question = one_line.partition(',')[0].replace('~n', '\n')
            audio_file = one_line.partition(',')[2].replace('\n','')
            
            while(the_question[len(the_question)-1] == '\n'):
                the_question = the_question[0:len(the_question)-1]


            the_questions.append(one_question(
                subject, difficulty, order, audio_file, the_question))
    except IOError:
        pass

the_questions = []
load_questions(the_questions)

The_Game = The_Game_Class()
the_teams = ['Team 1', 'Team 2', 'Team 3', 'Team 4']
game_scores = [0,0,0,0]

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)

#root.attributes('-fullscreen', True)


Add_Questions_dlg_class(the_questions, root, name='add_questions_frame').grid(
    row=1, column=1, sticky='news')
Create_Teams_Dlg(The_Game, the_questions, root, name='create_teams_frame').grid(
    row=1, column=1, sticky='news')
Get_Number_Of_Teams(The_Game, root, name='get_number_of_teams').grid(
    row=1, column=1, sticky='news')

Display_Question_dlg(root, name='display_question').grid(
    row=1, column=1, sticky='news')

Home_dlg_class(root, name='home_frame').grid(row=1, column=1, sticky='news')

root.nametowidget('home_frame').tkraise()

root.mainloop()
