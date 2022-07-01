import tkinter as tk
from Extra import *
import time, copy
import os

class Game_Board_dlg_class(tk.Frame):
    def __init__(self, the_questions, The_Game, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.game_scores=None
        

        def button_pressed(this_subject):
            these_questions = []

            for one_question in the_questions:
                if one_question.subject == this_subject:
                    these_questions.append(one_question)

            these_questions.sort(key=lambda x: x.order, reverse=False)

            
            display_question_dlg = self.winfo_toplevel().nametowidget('display_question')
            display_question_dlg.set_questions(these_questions)
            display_question_dlg.start_these_questions()

        self.the_subjects = []
        self.get_the_subject_names(the_questions)

        this_row=0
        this_column=0

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)

        for column_index, one_team in enumerate(The_Game.teams):
            tk.Label(self, text=one_team.name, font=font_return(
                int(My_Font_Size*3))).grid(row=this_row, column=column_index)
            tk.Label(self, name=one_team.name.lower() + '-score', text=0, font=font_return(
                int(My_Font_Size*3))).grid(row=this_row+1, column=column_index)

        this_row = this_row + 2
        for one_subject in self.the_subjects:
            font_multiplier=3
            the_text = one_subject
            if the_text.find(' ')>0:
                the_text = the_text.replace(' ','\n')
            elif len(the_text)>14:
                font_multiplier=2.5

            tk.Button(self, font=font_return(
                int(My_Font_Size*font_multiplier)), width=12, height=3, name=one_subject.lower(), text=the_text,
                    command=lambda subject=one_subject: button_pressed(subject))\
                        .grid(row=this_row, column=this_column, padx=20, pady=20)

            this_column+=1
            if this_column==5:
                this_row+=1
                this_column=0

    def set_scores(self, scores):
        self.game_scores = scores

    def get_the_subject_names(self, the_questions):

        for one_question in the_questions:
            if not(one_question.subject in self.the_subjects):
                self.the_subjects.append(one_question.subject)

class Check_Answers_dlg(tk.Frame):
    def __init__(self, The_Game, *args, **kwargs):

        def done():
            nonlocal winvar
            nonlocal losevar

            for index in range(The_Game.number_teams):
                self.nametowidget('no_play_'+str(index)
                                ).config(state='normal')
                self.nametowidget('play_'+str(index)
                                ).config(state='normal')


            self.winfo_toplevel().nametowidget('display_question').next_question()

        def go():
            nonlocal winvar
            nonlocal losevar
            
            no_one_right = True
            done = [] 
            for index in range(The_Game.number_teams):
                done.append(False)

                if winvar[index].get() == 1:
                    done[index]=True
                    no_one_right = False
                    self.The_Game.won(index)
                    self.nametowidget('no_play_'+str(index)
                                      ).config(state='disabled')
                    self.nametowidget('play_'+str(index)
                                      ).config(state='disabled')
                    winvar[index].set(0)
                elif losevar[index].get() == 1:
                    done[index] = True
                    self.nametowidget('no_play_'+str(index)
                                      ).config(state='disabled')
                    self.nametowidget('play_'+str(index)
                                      ).config(state='disabled')
                    self.The_Game.lost(index)
                    losevar[index].set(0)

                self.nametowidget('score'+str(index))['text']=str(self.The_Game.teams[index].score)

            if no_one_right:
                self.The_Game.answered_wrong()
            else:
                self.The_Game.answered_right()

            for index in range(The_Game.number_teams):
                if not(done[index]):
                    self.nametowidget(
                        'win_score_'+str(index))['text'] = str(self.The_Game.teams[index].win_score)
                    self.nametowidget('lose_score_'+str(index)
                                    )['text'] = str(self.The_Game.teams[index].lose_score)


        super().__init__(*args, **kwargs)

        self.game_scores=None
        this_row=1
        tk.Label(self, text='Check Answers',  font=font_return(
            My_Font_Size*5)).grid(row=this_row, column=1, columnspan=5)


        tk.Label(self, width=15, text='Team', padx=15, font=font_return(
            My_Font_Size*3)).grid(row=this_row, column=1)
        tk.Label(self, width=15, text='Score', padx=15, font=font_return(
            My_Font_Size*3)).grid(row=this_row, column=2)
        tk.Label(self, width= 9, padx=15, text='Right', font=font_return(
            My_Font_Size*3)).grid(row=this_row, column=3)
        tk.Label(self, width=9, padx=15, text='Wrong', font=font_return(
            My_Font_Size*3)).grid(row=this_row, column=4)
        tk.Label(self, width=5, padx=15, text='Win', font=font_return(
            My_Font_Size*3)).grid(row=this_row, column=5)
        tk.Label(self, width=5, padx=15, text='Lose', font=font_return(
            My_Font_Size*3)).grid(row=this_row, column=6)

        self.The_Game=The_Game

        winvar = []
        losevar = []

        for index in range(The_Game.number_teams):
            winvar.append(tk.IntVar())
            losevar.append(tk.IntVar())

        self.number_teams = The_Game.number_teams
        for this_team in range(The_Game.number_teams):

            this_row += 1

            
            tk.Label(self, text=The_Game.teams[this_team].name, pady=25, name='team'+str(this_team), font=font_return(
                My_Font_Size*3)).grid(row=this_row, column=1)
            tk.Label(self, text='0', pady=25, name='score'+str(this_team), font=font_return(
                My_Font_Size*3)).grid(row=this_row, column=2)
            tk.Checkbutton(self,  name='play_'+str(this_team), variable=winvar[this_team]).grid(
                row=this_row, column=3)
            tk.Checkbutton(self, name='no_play_'+str(this_team), variable=losevar[this_team]).grid(
                row=this_row, column=4)
            tk.Label(self, text='', width=5,  pady=15, name='win_score_'+str(this_team), font=font_return(
                My_Font_Size*3)).grid(row=this_row, column=5)
            tk.Label(self, text='', width=5, pady=15, name='lose_score_'+str(this_team), font=font_return(
                My_Font_Size*3)).grid(row=this_row, column=6)

        this_row += 1
        tk.Button(self, text='Go',  font=font_return(
            My_Font_Size*5), command=go).grid(row=this_row, column=1, columnspan=2)
        tk.Button(self, text='Done',  font=font_return(
            My_Font_Size*5), command=done).grid(row=this_row, column=4, columnspan=2)
    
    def set_scores(self, difficulty):

        self.The_Game.calculate_scores(difficulty)


        for index in range(self.number_teams):
            self.nametowidget('win_score_'+str(index))['text']=str(self.The_Game.teams[index].win_score)
            self.nametowidget('lose_score_'+str(index)
                              )['text'] = str(self.The_Game.teams[index].lose_score)

class Display_Question_dlg(tk.Frame):
    def __init__(self, *args, **kwargs):

        def play_audio():
            file = self.these_questions[self.which_question].audio
            os.startfile(file)

        super().__init__(*args, **kwargs)
        self.question_label_width = 35

        this_row = 1

        tk.Label(self, font=font_return(
            int(My_Font_Size*7.5)), width=3, name='clock', text=' ').grid(row=this_row, column=1)
        tk.Label(self, font=font_return(
            int(My_Font_Size*7.5)), width=20, name='title', text=' ').grid(row=this_row, column=2)

        this_row += 1
        self.grid_rowconfigure(this_row,weight=1) 
        tk.Label(self, text='', justify='left', anchor=tk.W, borderwidth=1, relief="solid", height=6, width=self.question_label_width, \
            name='the_question', font=font_return(My_Font_Size*5)).grid(sticky='news', row=this_row, column=2, columnspan=2)

        this_row += 1
        tk.Button(self, text='', name='the_button', font=font_return(
            My_Font_Size*3), width=10, command=self.button_pressed).grid(sticky='news', row=this_row, column=2)
        tk.Button(self, text='Play', name='play', font=font_return(
            My_Font_Size*3), width=4, command=play_audio).grid(sticky='news', row=this_row, column=3)

        self.nametowidget('play')['state']='disabled'
        self.these_questions=[]
        self.which_question=0

    def button_pressed(self):
        
        if self.nametowidget('the_button')['text'] in ['Check Answers','Stop']:
            self.winfo_toplevel().nametowidget('check_answer').set_scores(
                self.these_questions[0].difficulty)
            self.winfo_toplevel().nametowidget('check_answer').tkraise()
        else:
            self.nametowidget('the_button')['text'] = 'Stop'
            start_time = time.time()
            total_time = 5
            time_used = 0

            self.display_next_question()
            self.nametowidget('clock')[
                'text'] = str(total_time)

            self.update()


        
            while True:
                if time.time()-start_time > total_time:
                    self.nametowidget('the_button')[
                        'text'] = 'Done'
                    break
                elif time.time()-start_time > (time_used+1):
                    time_used += 1
                    self.nametowidget('clock')[
                        'text'] = str(total_time-time_used)
                    self.update()

            self.nametowidget('the_question')[
                        'text'] = 'Time is up'
            self.nametowidget('clock')[
                'text'] = ''
            self.nametowidget('the_button')['text']='Check Answers'

    def set_questions(self, these_questions):
        self.these_questions = these_questions

    def start_these_questions(self):

        self.nametowidget('title')[
            'text'] = self.these_questions[self.which_question].subject
        self.prepare_for_next_question()

        self.tkraise()

    def prepare_for_next_question(self):
        self.nametowidget('the_button')[
            'text'] = 'Question ' + str(self.which_question + 1)
        self.nametowidget('the_question')[
            'text'] = ''

    def display_next_question(self):

        too_many_lines=True
        characters_per_line = self.question_label_width
        while too_many_lines:
            
            question_to_display = copy.deepcopy(
                self.these_questions[self.which_question].question)

            final_text = ''

            while len(question_to_display)>0:

                if len(question_to_display)<characters_per_line:
                    final_text = final_text + \
                        question_to_display
                    question_to_display = ''
                else:
                    length_this_row = min(characters_per_line,question_to_display.find('\n'))
                    if length_this_row == -1:
                        length_this_row = characters_per_line
                    length_this_row = min(length_this_row, len(question_to_display))

                    while not(question_to_display[length_this_row-1] in ['\n', ' ']):
                        length_this_row -= 1

                    final_text = final_text + question_to_display[:length_this_row-1] + '\n'
                    question_to_display=question_to_display[length_this_row:]
                
            if final_text.count('\n') < 7:
                too_many_lines=False
            else:
                characters_per_line += 8
                self.nametowidget('the_question')[
                    'width'] = characters_per_line
                font_size = int(My_Font_Size*5*(40/characters_per_line))
                self.nametowidget('the_question')[
                    'font'] = font_return(font_size)

        if not self.these_questions[self.which_question].audio == '':
            self.nametowidget('play')['state'] = 'normal'
        self.nametowidget('the_question')[
            'text'] = final_text


    def next_question(self):
        self.which_question += 1
        if self.which_question==len(self.these_questions):
            self.winfo_toplevel().nametowidget('game_board_frame').nametowidget(self.these_questions[0].subject.lower())['state']='disabled'
            self.winfo_toplevel().nametowidget('game_board_frame').tkraise()


        self.prepare_for_next_question()
        self.tkraise()




        

