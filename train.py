from tkinter import*
from tkinter import ttk

from PIL import Image, ImageTk
from tkinter import messagebox

import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x790+0+0")
        self.root.title("face recognition System")


        title_lbl=Label(self.root, text="Train datset", font = ("times new roman", 35, "bold"), bg="white", fg = "darkgreen")
        title_lbl.place(x = 0, y=0, width=1500, height=45)

        
        img_top = Image.open(r"images\olaf.jpg")
        img_top = img_top.resize((1500, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1500, height=325)

        # Button
        b1_1 = Button(self.root, text = 'Train Data', command = self.train_classifier, cursor="hand2", font=("times new roman", 13, "bold"), bg = "darkblue", fg = "white")
        b1_1.place(x=0, y=325, width=1220, height=60)


        img_bottom = Image.open(r"images\minion.jpg")
        img_bottom = img_bottom.resize((150, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=425, width=1500, height=325)
    
    def train_classifier(self):
        data_dir = ("data") #give folder name
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        messagebox.showinfo("Result", "training datasets....")
        # self.display_message()
        for image in path:
            img = Image.open(image).convert('L') #Grey scale image
            imageNp=np.array(img, 'uint8')  #unit8 -- data type
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            
            cv2.waitKey(1)==1
        # training_msg.destroy()
        ids = np.array(ids)
        # self.destroy()
        # ============== Train the classifier ANd Save ===============
       
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "training datasets completed!")

    def display_message(self):
        global training_msg
        training_msg = Toplevel(self.root)
        training_msg.title("Training Image")
        training_msg.geometry("250x150")
        training_msg.config(bg = "white")
        training_msg = Label(training_msg, text = "Training Images")
        training_msg.pack(pady=10)
    def destroy(self):
        training_msg.destroy()










if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

