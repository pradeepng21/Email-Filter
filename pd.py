#importing libraries
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import re
import csv
from tkinter import messagebox

class ng:
    def browseFiles(self):
        self.file = filedialog.askopenfile(mode='r' , filetypes=[('select a text file' , '*txt')])
        messagebox.showinfo("File", "Uploaded successfully!")
        # print(self.file.name) 
        
        
    def clicked(self):
        f = open(self.file.name)
        d = []
        mail = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        phone = "^[0-9]{1,10}$"
        for i in f:
            t = i.split(",")
            
            if re.match(mail,t[0]) and re.match(phone,t[1]):
                d.append(t) 
        file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV', '*.csv')])

        # write the data to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(d)  

        messagebox.showinfo("Success", "Your operation was successful!")  #success message after saving the file
                
    def main_ng(self):
        root = Tk()
        root.title("mail filter")
        root.geometry('500x500')
        label_file_explorer = Label(root, text = "Filter", width = 70, height = 4, fg = "black")    
        button_explore = Button(root, text = "Browse Files", command = ng.browseFiles)
        file = Label(root, text = " Select the txt file: ") 
        submit_button = Button(root, text = "click for output", command = self.clicked) 

        label_file_explorer.grid(column = 1, row = 1)
        button_explore.place(x=200, y=140)
        file.place(x=80 , y=140)
        submit_button.place(x = 150, y = 200)

        root.mainloop()
ng = ng()    
ng.main_ng()
