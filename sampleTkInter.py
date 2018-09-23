#!/usr/bin/env python
# -*- coding: utf8 -*-
# 標準GUI
# 参考　https://qiita.com/canard0328/items/5ea096352e160b8ececa

import os,sys,time
import tkinter as Tk
import tkinter.filedialog as tkFD
import tkinter.messagebox as tkMsg

class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.pack(expand=1, fill=Tk.BOTH, anchor=Tk.NW)
        self.create_widgets()
    
    def create_widgets(self):
        self.label = Tk.Label(self, text=u'入力ファイル')

        self.var_entry = Tk.StringVar()
        self.var_entry.trace('w', self.entry_changed)
        self.entry = Tk.Entry(self, textvariable=self.var_entry)

        self.button = Tk.Button(self, text=u'開く', command=self.button_pushed)
        self.button2 = Tk.Button(self, text=u'Msagebox', command=self.button_pushed2)
        self.var_check = Tk.BooleanVar()
        self.check = Tk.Checkbutton(self, text=u'拡張子をtxtに限定', variable=self.var_check)
        self.text = Tk.Text(self, wrap=Tk.NONE)
        
        self.yscroll = Tk.Scrollbar(self, command=self.text.yview)
        self.xscroll = Tk.Scrollbar(self, command=self.text.xview,
                                    orient=Tk.HORIZONTAL)
        self.text['yscrollcommand'] = self.yscroll.set
        self.text['xscrollcommand'] = self.xscroll.set

        self.text.grid(column=0, columnspan=3, row=3, rowspan=2, sticky=Tk.NSEW)
        self.yscroll.grid(column=2, row=2, sticky=Tk.NS + Tk.E)
        self.xscroll.grid(column=0, columnspan=3, row=4, sticky=Tk.EW + Tk.S)        

        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.button.grid(column=2, row=0)
        self.button2.grid(column=0, row=2)
        self.check.grid(column=0, row=1)
        self.text.grid(column=0, columnspan=3, row=3)

    def entry_changed(self, *args):
        if os.path.exists(self.var_entry.get()):
            self.text.delete('1.0', Tk.END)
            self.text.insert('1.0', open(self.var_entry.get()).read())

    def button_pushed(self):
        self.var_entry.set(u'ボタンが押されました．')
        ft = [('text files', '.txt')] if self.var_check.get() else []

        print(ft)
        self.var_entry.set(tkFD.askopenfilename(filetypes=ft))

    def button_pushed2(self):
        tkMsg.askquestion(title="Question", message="message...")

root = Tk.Tk()
app = Application(master=root)
app.mainloop()
