import tkinter as tk
from Extra import *
import sys

class Home_dlg_class(tk.Frame):

    def __init__(self, *args, **kwargs):


        super().__init__(*args, **kwargs)

        def add_questions():
            self.winfo_toplevel().nametowidget('add_questions_frame').tkraise()
        
        def add_teams():
            self.winfo_toplevel().nametowidget('get_number_of_teams').tkraise()

        def play_game():
            #self.winfo_toplevel().nametowidget('check_answer').Set_Team_Names(self.teams)
            self.winfo_toplevel().nametowidget('game_board_frame').tkraise()

        def admin():
            pass
            
        def exit():
            sys.exit()

        this_row = 0
        
        tk.Label(self, borderwidth=1, relief="solid", text='Stacey''s Fun Time\nTrivia Game', font=font_return(
            My_Font_Size*8)).grid(row=this_row, column=1, columnspan=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        this_row += 1

        tk.Button(self,  width=13,text='Add Questions', command=add_questions, font = font_return(
            My_Font_Size*3), name='add_questions').grid(row=this_row, column=1, pady=50)
        
        tk.Button(self,  width=13,text='Set Up', command=add_teams, font=font_return(
            My_Font_Size*3), name='add_teams').grid(row=this_row, column=2, pady=50)
     
        tk.Button(self,  width=13,text='Play Game', command=play_game, font=font_return(
            My_Font_Size*3), name='play_game').grid(row=this_row, column=3, pady=50)
 
        this_row += 1
        tk.Button(self,  width=13,text='Admin', command=admin, font=font_return(
            My_Font_Size*3), name='admin').grid(row=this_row, column=1, pady=50)

        tk.Button(self,  width=13, text='Exit', command=exit, font=font_return(
            My_Font_Size*3), name='exit').grid(row=this_row, column=3, pady=50)

    def set_teams(self, teams):
        self.teams = teams
