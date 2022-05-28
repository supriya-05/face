import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import numpy as np
import cv2
import csv
import numpy as np
from tkinter import filedialog
mydata = []
# yellow

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x790+0+0")
        self.root.title("face fffff recognition System")

        # ========variables==========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()









        olaf = Image.open(r"images\olaf.jpg")
        olaf = olaf.resize((800, 200), Image.ANTIALIAS)
        self.photoolaf = ImageTk.PhotoImage(olaf)

        f_lbl = Label(self.root, image=self.photoolaf)
        f_lbl.place(x=0, y=0, width=800, height=100)

        # 2
        olaf1 = Image.open(r"images\olaf.jpg")
        olaf1 = olaf.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(olaf)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=100)

        tile_label = Label(
            
            text="Attendance Management Details",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg= "black",
        )
        tile_label.place(x=0, y=200, width=1400, height=30)

        main_frame = Frame(bd = 2, bg = "White")
        main_frame.place(x = 20, y = 100, width = 1200, height = 600)

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student attendance Details", font = ("times new roman", 12, "bold"), )
        Left_frame.place(x=10, y=10, width=580, height=500)


        img_left = Image.open(r"images\olaf.jpg")
        img_left = img_left.resize((520, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=580, height=100)

        Left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg = "white")
        Left_inside_frame.place(x=0, y=135, width=550, height=500)
        
        # labels and entries
        # attendance id
        attendanceID_label = Label(Left_inside_frame, text='Attendance', font = ("times new roman", 12), bg="white")
        attendanceID_label.grid(row = 0, column=0, padx = 10, pady = 5, sticky=W)

        attendanceID_entry = ttk.Entry(Left_inside_frame, textvariable = self.var_atten_id, font = ("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10,pady = 5)

        #nameLabel
        nameLabel = Label(Left_inside_frame, text='Name:', font = ("times new roman", 12), bg="white")
        nameLabel.grid(row = 1, column=0, padx =4, pady=8)

        atten_name = ttk.Entry(Left_inside_frame,textvariable = self.var_atten_name, font = ("times new roman", 12, "bold"))
        atten_name.grid(row=1, column=1, padx=2)


        # Roll number
        rollLabel = Label(Left_inside_frame, text='Roll:', font = ("times new roman", 12), bg="white")
        rollLabel.grid(row = 0, column=2, padx =4, pady=8)

        atten_roll = ttk.Entry(Left_inside_frame, textvariable = self.var_atten_roll,font = ("times new roman", 12, "bold"))
        atten_roll.grid(row=0, column=3, pady = 8)

        # Department
        depLabel = Label(Left_inside_frame, text='Department', font = ("times new roman", 12), bg="white")
        depLabel.grid(row = 1, column=2, padx =4, pady=8)

        atten_dep= ttk.Entry(Left_inside_frame,textvariable = self.var_atten_dep, font = ("times new roman", 12, "bold"))
        atten_dep.grid(row=1, column=3, pady = 8)


       

        #Time

        timeLabel = Label(Left_inside_frame, text='Time', font = ("times new roman", 12), bg="white")
        timeLabel.grid(row = 2, column=0)

        atten_time = ttk.Entry(Left_inside_frame,textvariable = self.var_atten_time, font = ("times new roman", 12, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

         # Date
        dateLabel = Label(Left_inside_frame, text='date', font = ("times new roman", 12), bg="white")
        dateLabel.grid(row = 2, column=2)

        atten_date = ttk.Entry(Left_inside_frame, textvariable = self.var_atten_date,font = ("times new roman", 12, "bold"))
        atten_date.grid(row=2, column=3, pady = 8)
        #attendance label

        attendanceLabel = Label(Left_inside_frame, text='Attendance', font = ("times new roman", 12), bg="white")
        attendanceLabel.grid(rows=3, column = 0)

        self.atten_status = ttk.Combobox(Left_inside_frame, textvariable = self.var_atten_attendance,font = ("times new roman", 12, "bold"),  state="readonly")
        self.atten_status['values'] = ("Status", "Present", "Absent" )
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=8)


         
        # button frame
        btn_frame = Frame(Left_inside_frame, bd = 2, relief=RIDGE, bg = "yellow")
        btn_frame.place(x=0,y=200,width=600, height=100)
        
        save_btn = Button(btn_frame, text = 'import csv',command=self.importCsv,  font=("times new roman", 13, "bold"), width=12)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text = 'export csv', command=self.exportCsv, font=("times new roman", 13, "bold"), width=12)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text = 'update',  font=("times new roman", 13, "bold"), width=12)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text = 'reset',command=self.reset_data, font=("times new roman", 13, "bold"), width=12)
        reset_btn.grid(row=0, column=3)






        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,bg = "white",   text="Attendance Details", font = ("times new roman", 12, "bold"))
        Right_frame.place(x=610, y=10, width=580, height=490)


        table_frame = Frame(Right_frame, bd = 2, relief=RIDGE, bg = "white")
        table_frame.place(x=5,y=5,width=550, height=445)


        ## ===========scroll bar table ===================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview) 

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        #===========================  face data =============
    
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    # importCsv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title = "open CSV", filetypes=(("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myFile:
            csvread = csv.reader(myFile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    # export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title = "open CSV", filetypes=(("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data export", "your data is exported to "+os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("error", f"Due To : {str(es)}", parent = self.root)


    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_roll.set("")
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")

        self.var_atten_attendance.set("")
        













        




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()