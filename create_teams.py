import tkinter as tk
from Extra import *
from Game_Board import Game_Board_dlg_class, Check_Answers_dlg

class Get_Number_Of_Teams(tk.Frame):

    def __init__(self, The_Game, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def Next():
            nonlocal The_Game

            The_Game.set_number_of_teams(int(self.nametowidget('number_teams').get()))
            self.winfo_toplevel().nametowidget('create_teams_frame').tkraise()


        this_row = 0
        tk.Label(self, text='Number of Teams', font=font_return(
            My_Font_Size*5)).grid(pady=75, row=this_row, column=0)
        tk.Entry(self, width=15, name='number_teams', font=font_return(
            My_Font_Size*5)).grid(
            row=this_row, column=1)

        this_row += 1
        tk.Button(self, text='Choose Team Names', command=Next, font=font_return(
            My_Font_Size*5)).grid(
            row=this_row, column=1)

class Create_Teams_Dlg(tk.Frame):

    def __init__(self, The_Game, the_questions, * args, **kwargs):
        super().__init__(*args, **kwargs)


        def done():
            self.winfo_toplevel().nametowidget('home_frame').tkraise()

        def set_team_name():
            nonlocal Which_Team

            The_Game.set_team_name(
                Which_Team, self.nametowidget('team_name').get())
            Which_Team += 1

            if Which_Team == The_Game.number_teams:
                Check_Answers_dlg(The_Game,  self.winfo_toplevel(), name='check_answer').grid(
                    row=1, column=1, sticky='news')
                Game_Board_dlg_class(the_questions, The_Game,  self.winfo_toplevel(), name='game_board_frame').grid(
                    row=1, column=1, sticky='news')
                self.winfo_toplevel().nametowidget('home_frame').tkraise()
            else:
                self.nametowidget('team_name').delete(0,tk.END)
                self.nametowidget('team_name').insert(
                    0, 'Team ' + str(Which_Team + 1),)
                self.nametowidget('team_label')[
                    'text']='Team Number ' + str(Which_Team+1)

        Which_Team=0
        this_row = 0
        tk.Label(self, text='Create Teams', font=font_return(
            My_Font_Size*5)).grid(pady=75, row=this_row, column=2, columnspan=3)

        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        this_row+=1

        tk.Label(self, name='team_label', text='Team Number ' + str(Which_Team+1), font=font_return(
            int(My_Font_Size*2.5))).grid(pady=75, row=this_row, column=2)
        tk.Entry(self, width=15, name='team_name', font=font_return(
            My_Font_Size*2)).grid(
            pady=20, row=this_row, column=4)
        self.nametowidget('team_name').insert(
            0, 'Team ' + str(Which_Team + 1),)

        this_row += 1
        tk.Button(self, font=font_return(
            30), text='Set Team Name', command=set_team_name).grid(pady=20, row=this_row, column=2)

        # tk.Button(self, font=font_return(
        #     My_Font_Size*3), text='Done', command=done).grid(
        #     pady=20, row=this_row, column=4)
