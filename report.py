import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


class Report:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2030x990+0+0")
        self.root.title("Face recognition System")


        df = pd.read_csv("attendance.csv")
        self.students = df['Names'].tolist()
        self.students = ["Select Student"] + self.students
    


        days_df = df.columns
        self.days = list(days_df)[2:]
        self.days = ["Select Date"] + self.days

        title_label_report = tk.Label(
            self.root,
            text="Report",
            font= ("Arial Narrow", 35, "italic"),
            bg="dark blue",
            fg="white",
        )
        title_label_report.place(x=0, y=0, width=1500, height=100)

        img3 = Image.open(r"images\white.jpg")
        img3 = img3.resize((1500, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1500, height=710)

        left_frame = Frame(bg_img, bd = 2, bg = "pink")
        left_frame.place(x = 300, y = 300, width = 400, height = 100)

        right_frame = Frame(bg_img, bd = 2, bg = "yellow")
        right_frame.place(x = 700, y = 300, width = 400, height = 100)

 
        
        #Selecting student 
        select_names = Label(left_frame, text='Select a Student', font = ("times new roman", 18), bg="white")
        select_names.grid(row = 1, column=0, padx=10)
        self.std_name = Combobox(left_frame, values=self.students)
        self.std_name.grid(row = 1, column=1)
   
        self.std_name.current(0)
        self.b1 = Button(left_frame, text="Check", command=self.plot_graph_name).grid(row = 2, column= 3)
        

        #selecting Date
        select_date = Label(right_frame, text='Select date', font = ("times new roman", 12), bg="white")
        select_date.grid(row = 1, column=15, padx=10)
        self.std_date = Combobox(right_frame, values=self.days)
        self.std_date.current(0)
        self.std_date.grid(row = 1, column=20)
        self.b11 = Button(right_frame, text="Report", command=self.plot_graph_date).grid(row = 2, column= 3)
        


    def plot_graph_date(self):
        global df
        df = pd.read_csv("attendance.csv")
        date = self.std_date.get()
        day_details = df[date].tolist()

        no_present = day_details.count('Present')
        no_absent = day_details.count('Absent')

        plt.pie([no_present, no_absent], labels=["Students present", "Students absent"], autopct='%1.1f%%', shadow=True)
        plt.title("Report on " +  date )
        plt.show()
        

    def plot_graph_name(self):
            global df
            df = pd.read_csv("attendance.csv")
            
            students = df['Names'].tolist()
            days_df = df.columns
            days = list(days_df)[2:]
        
            name = self.std_name.get()
            
            student_df = df.loc[df["Names"] == name]
            student = student_df.values[0].tolist()
        
            present_days = student.count("Present")
            data = [present_days, len(days)]
            
            plt.pie(data, labels=["present", "absent"], autopct='%1.1f%%', shadow=True)
            plt.title(name + "  Report")
            plt.show()


    
    




if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()