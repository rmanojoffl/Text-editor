"""
using TKinter to develop the graphical user interface
To create the program to 
    1.creating a new file
     - creating new window 
     - hiding the main window
     - creating the required labels,buttons,contents
     - creating the file using the contents obtained from the above widgets 
    2.opening the existing file
"""
from tkinter import *
from pathlib import Path



# Function to creating the file
def new_file():
    #creating the new file
    def create_file():
        try:
            with open(file_name_entry.get(),"x") as file:
                file.write(text_box.get("1.0",END))
            create_button.config(text="Created")
        except FileExistsError:
            print("The file name already exit")
    
    def show_main_window():
        window.deiconify()
        new_file_window.withdraw()


    #Creating a new window for creating a new file
    new_file_window=Toplevel()
    new_file_window.title("Creating New File")
    new_file_window.minsize(width=500,height=500)
    new_file_window.config(padx=20,pady=20)
    window.withdraw()

    file_name_label=Label(new_file_window,text="Enter the file name : ")
    file_name_label.grid(column=0,row=0)

    file_name_entry=Entry(new_file_window,width=25)#TO get the name of the new file
    file_name_entry.grid(column=1,row=0)

    text_label=Label(new_file_window,text="Enter the content of the file below :")
    text_label.grid(column=0,row=1)
    text_label.config(pady=20)

    text_box=Text(new_file_window,height=20,width=50)#text box to get the content of the file
    text_box.grid(column=0,row=3,columnspan=2)

    create_button=Button(new_file_window,text="Create file",command=create_file)#Button to create the file
    create_button.grid(column=0,row=4,columnspan=2,pady=20)

    go_back_button=Button(new_file_window,text="Go back",command=show_main_window)
    go_back_button.grid(column=3,row=4,columnspan=2)




#For the editing or checking the existing file
def existing_file():
    #To check the file is present or not
    def check_file_present():
        save_button.config(text="save")
        filename=Path(file_name_entry.get())
        print(file_name_entry.get())

        if filename.exists(): #checks does file exists or not and return boolean value
            with open(file_name_entry.get(),"r") as file:
                content=file.read()
                print(content)
            
            text_box.focus#Focus the cursor in the text box
            text_box.insert(END,content)#inset the content of the file in the text box
        else:
            print("file does not exists")
        
    def save():
         with open(file_name_entry.get(),"w") as file:
            file.write(text_box.get("1.0",END))
            save_button.config(text="Saved")
    
    
    def show_main_window():
        window.deiconify()
        existing_file_window.withdraw()

    #Creating a new window for checking the existing file
    existing_file_window=Toplevel()
    existing_file_window.title("open an exisiting file")
    existing_file_window.minsize(width=500,height=500)
    existing_file_window.config(padx=20,pady=20)
    window.withdraw()
    
    file_name_label=Label(existing_file_window,text="File Name  :  ")
    file_name_label.grid(column=0,row=0)

    file_name_entry=Entry(existing_file_window,width=20)
    file_name_entry.grid(column=1,row=0,padx=20)

    search_button=Button(existing_file_window,text="search",width=10,command=check_file_present)
    search_button.grid(column=2,row=0,padx=20)

    text_box=Text(existing_file_window,height=20,width=50)#Creates the text box
    text_box.grid(column=0,row=1,pady=20,columnspan=3,padx=20)

    save_button=Button(existing_file_window,text="Save",width=10,command=save)
    save_button.grid(column=1,row=3,pady=20)

    go_back_button=Button(existing_file_window,text="Go back",command=show_main_window)
    go_back_button.grid(column=3,row=3,columnspan=2)


#main window
window=Tk() #using tk class from tkinter module to setup the main screen
window.title("Text editor") # Title of the graphical user interface 
window.minsize(width=300,height=200)# To set the height of the screen
window.config(pady=20,padx=80)

new_file_button=Button(text="Create a new file",command=new_file)#To create the new file once the button is clicked
new_file_button.grid(column=0,row=0)

or_label=Label(text="or")
or_label.grid(column=0,row=1)
or_label.config(pady=20)

open_existing_file=Button(text="Open existing file",command=existing_file)#To open the existing file once the button is clicked
open_existing_file.grid(column=0,row=2)

window.mainloop()#To keep the screen listening for any activities

