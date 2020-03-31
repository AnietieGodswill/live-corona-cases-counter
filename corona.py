#live corona case counter
import tkinter as tk
from tkinter import *
import time
import requests
from bs4 import BeautifulSoup 
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
        label_7 = tk.Label(self,text=f"{last_update}", fg="blue", font="none 15 bold")
        label_7.pack()
        label_8 = tk.Label(self,text=f"Developed By: Nishant Tiwari (dx4iot)", fg="black", font="none 15 bold")
        label_8.pack()
 
if __name__ == "__main__":
    app = Corona()
    app.title("Corona Virus Update")
    app.mainloop()
    
    
