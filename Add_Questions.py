import tkinter as tk
from Extra import *


class Add_Questions_dlg_class(tk.Frame):

    def __init__(self, the_questions, *args, **kwargs):

        super().__init__(*args, **kwargs)

        def done():
            self.winfo_toplevel().nametowidget('home_frame').tkraise()
        
        def save():

            this_file = open('the_questions.txt','w')
            for one_question in the_questions:

                one_question.question = one_question.question.replace('\n', '~n')

                this_file.write(one_question.subject)
                this_file.write(',')
                this_file.write(str(one_question.difficulty))
                this_file.write(',')
                this_file.write(str(one_question.order))
                this_file.write(',')
                this_file.write(one_question.question)
                this_file.write(',')
                this_file.write(one_question.audio)
                this_file.write('\n')

                one_question.question = one_question.question.replace('~n','\n')
                
            this_file.close()

        def add_question():
            
            the_question = self.nametowidget('question_text').get(
                "1.0", tk.END)
            
            audio_file=''

            audio_file_start = the_question.find('*')
            if not audio_file_start == -1:
                
                audio_file = the_question.partition('*')[2].replace('\n','')
                the_question = the_question.partition(
                    '*')[0].replace('\n', '~n')
            else:
                the_question = the_question.replace('\n', '~n')
                
            the_questions.append(one_question(
                self.nametowidget('subject').get(),
                int(self.nametowidget('difficulty').get()),
                int(self.nametowidget('order').get()),
                audio_file,
                the_question)
            )

            self.nametowidget('subject').delete(0, tk.END)
            self.nametowidget('difficulty').delete(0, tk.END)
            self.nametowidget('order').delete(0, tk.END)
            self.nametowidget('question_text').delete('0.0', tk.END)

        this_row=0
        tk.Label(self, text='Add Questions', font=font_return(
            My_Font_Size*5)).grid(pady=75, row=this_row, column=2, columnspan=3)
        
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        this_row+=1
        tk.Label(self, text='Subject', font=font_return(
            My_Font_Size*2)).grid(pady=20, row=this_row, column=2)
        tk.Entry(self, width=10, name='subject', font=font_return(
            My_Font_Size*2)).grid(
            pady=20, row=this_row, column=4)

        this_row += 1
        tk.Label(self, text='Difficulty', font=font_return(
            My_Font_Size*2)).grid(pady=20, row=this_row, column=2)
        tk.Entry(self, width=5, name='difficulty', font=font_return(
            My_Font_Size*2)).grid(
            pady=20, row=this_row, column=4)

        this_row += 1
        tk.Label(self, text='Order', font=font_return(
            My_Font_Size*2)).grid(pady=20, row=this_row, column=2)
        tk.Entry(self, width=5, name='order', font=font_return(
            My_Font_Size*2)).grid(
            pady=20, row=this_row, column=4)

        this_row += 1
        tk.Text(self, width=50, height=10, name='question_text', font=font_return(
            int(My_Font_Size*1.6))).grid(pady=20,
            row=this_row, column=2, columnspan=3)


        this_row += 1
        tk.Button(self, font=font_return(
            My_Font_Size*3), text='Add Question', command=add_question).grid(pady=20, row=this_row, column=2)
        tk.Button(self, font=font_return(
            My_Font_Size*3), text='Save Question', command=save).grid(pady=20, row=this_row, column=3)            
        tk.Button(self, font=font_return(
            My_Font_Size*3), text='Done', command=done).grid(
            pady=20, row=this_row, column=4)
