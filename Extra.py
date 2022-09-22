from tkinter import font as tkfont
from dataclasses import dataclass

My_Font_Size = 8

@dataclass
class one_question():

    subject: str
    difficulty: int
    order: int
    audio: str
    question: str


def font_return(this_size):

    fonts = list(tkfont.families())
    return tkfont.Font(family=fonts[198], size=this_size)
