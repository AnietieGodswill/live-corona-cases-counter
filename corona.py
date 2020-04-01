#live corona case counter
import tkinter as tk
from tkinter import *
import time
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
class Corona(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(coronaPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
    
    
class coronaPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        label_1 = tk.Label(self, text="Live Corona Cases Counter", bg="orange", fg="black", font="none 28 bold")
        label_1.pack()
        space_1 = tk.Label(self, text="\n")
        space_1.pack()
        r = requests.get("https://virusncov.com/")
        data = r.content
        soup = BeautifulSoup(data,'html.parser')
        tot_cases = soup.h2.text
        totcase_split = tot_cases.split(" ")[-1]
        totcase_join = "".join(totcase_split)
        tot_death = soup.find("span",{"class":"red-text"}).text
        tot_recover = soup.find("span",{"class":"green-text"}).text
        last_update = soup.small.text
        label_2 = tk.Label(self,text=f"--------------", fg="black", font="none 15 bold")
        label_2.pack()        
        label_3 = tk.Label(self,text=f"Total Cases: {totcase_join}", fg="black", font="none 15 bold")
        label_3.pack()
        label_4 = tk.Label(self,text=f"Total Deaths: {tot_death}", fg="red", font="none 15 bold")
        label_4.pack()
        label_5 = tk.Label(self,text=f"Total Recovered: {tot_recover}", fg="green", font="none 15 bold")
        label_5.pack()
        label_6 = tk.Label(self,text=f"--------------\n", fg="black", font="none 15 bold")
        label_6.pack()
        button1 = tk.Button(self, text="Search By Country",command=lambda: master.switch_frame(coronaPage1),width=15,bg='orange',fg='white',font="none 15 bold")
        button1.pack()
        label_7 = tk.Label(self,text=f"{last_update}", fg="blue", font="none 15 bold")
        label_7.pack()
        label_8 = tk.Label(self,text=f"Developed By: Nishant Tiwari (dx4iot)", fg="black", font="none 15 bold")
        label_8.pack()
       
        
       
        
class coronaPage1(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        #drop down boxes
        def show():
        
            copy = clicked.get()
            copy_lower = copy.lower()
            copya = "https://virusncov.com/covid-statistics/"+copy_lower
            
            r1 = requests.get(copya)        
            dataa = r1.content
            soupa = BeautifulSoup(dataa,'html.parser')
            tot_deatha = soupa.findAll("strong",{"class":"red-text"}) 
            tot_deatha1 = tot_deatha[1].text
            tot_reca = soupa.find("strong",{"class":"green-text"}).text
            label_2 = tk.Label(self,text=f"Deaths: {tot_deatha1}",fg="red", font="none 15 bold")
            label_2.pack()
            label_3 = tk.Label(self,text=f"Recovered: {tot_reca}",fg="green", font="none 15 bold")
            label_3.pack()
            

        label_1 = tk.Label(self, text="SEARCH BY COUNTRY", bg="orange", fg="black", font="none 20 bold")
        label_1.pack()
        
        max_len = 40
        clicked = StringVar()

        
        choices = ['USA','Italy','Spain','China','Germany','France','Iran','UK','Switzerland','India'] 
        padded_choices = [x+' '*(max_len-len(x)) for x in choices]              
        clicked.set (choices[0])
        drop = tk.OptionMenu(self, clicked,*padded_choices)
        drop.configure(width=20,height=1)
        drop.pack()

        button = tk.Button(self, text="Show",command=show,width=10,bg='green',fg='white',font="none 15 bold") 
        button.pack( pady = 5)
       

        
        
if __name__ == "__main__":
    app = Corona()
    app.title("Corona Virus Update")
    app.mainloop()
    
    
