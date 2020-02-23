# Help Module for Custom Ping
# Version 1.0p1
# Written in Python 3.7.4
# Progress : 90% Finishing
import os
import tkinter
import sys
import pkgutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os import system

def gui_ping20():
    process.process20.init(self)

def gui_ping70():
    process.process70.init(self)

def gui_ping200():
    process.process200.init(self)

def gui_ping500():
    process.process500.init(self)

def gui_ping3000():
    process.process3000.init(self)

def gui_pingto():
    process.processto.init(self)

def gui_pingdnu():
    process.processdnu.init(self)

def gui_pinggf():
    process.processgf.init(self)

def gui_restore_backup():
    process.create_backup(self)

def gui_ask_single_multi():
    global ask_init
    ask_init = Toplevel()
    ask_init.configure(background='white')
    ask_init.geometry('300x200')
    ask_init.title('Choose one')
    ask = Frame(ask_init)
    ask.configure(background='white')
    ask.pack()
    Label(ask, text=' ', background='white').pack()
    Label(ask, text='Choose one', background='white').pack()
    Label(ask, text=' ', background='white').pack()
    Label(ask, text=' ', background='white').pack()
    Button(ask, text='Multi-Line', background='white', command=gui_multi).pack(side=LEFT)
    Button(ask, text='Single-Line', background='white').pack(side=LEFT)

def gui_multi():
    ask_init.quit()
    gui.ask_single_multi(self)

def gui_about_customping():
    parent_main = Toplevel()
    parent_main.geometry('800x500')
    parent_main.configure(background='#D3D3D3')
    parent_main.title('About Custom Ping')
    Label(parent_main, text='Custom Ping                                                        ', font='Vendeta 18 bold', background='#D3D3D3').grid(row=1, column=1)
    Label(parent_main, text="A Customized 'ping.exe' for windows in batch, where you can modify output ping and make your own!", background='#D3D3D3').grid(row=2, column=1)
    Label(parent_main, text='', background='#D3D3D3').grid(row=3, column=1)
    Label(parent_main, text='', background='#D3D3D3').grid(row=4, column=1)
    parent_main.mainloop()

def gui_start_customping():
    if os.path.exists('Custom_Ping.bat'):
        system('start \"\" \"Custom_Ping.bat\"')
    elif os.path.exists('FIXED_Custom_Ping.bat'):
        system('start \"\" \"FIXED_Custom_Ping.bat\"')
    else:
        messagebox.askyesno('Error', 'Custom Ping not found, Do you want to create one ?')

class init():
    def prepare_variable(self):
        hide = tkinter.Tk()
        hide.withdraw()

class gui():
    def main_menu(self):
        global main
        main = tk.Tk()
        main.eval('tk::PlaceWindow . center')
        main.geometry("400x225")
        main.title("Help Module for Custom Ping")
        main.configure(background='white')
        Label(main, text='Welcome!', background='white').pack()
        Label(main, text='See what you need', background='white').pack()
        Label(main, text='', background='white').pack()
        Button(main, text='Start Custom Ping', width=30, background='white', command=gui_start_customping).pack()
        Button(main, text='Change Custom Ping Messages', width=30, background='white', command=gui_ask_single_multi).pack()
        Button(main, text='Fix Missing or Corrupt Script', width=30, command=gui_restore_backup, background='white').pack()
        Button(main, text='About Custom Ping', width=30, background='white', command=gui_about_customping).pack()
        Label(main, text=' ', background='white').pack()
        Label(main, text='Version 1.0', background='white').pack()
        Label(main, text='', background='white').pack()
        main.mainloop()

    def ask_single_multi(self):    
        global ask_main
        ask_main = Toplevel()          
        ask_main.geometry("300x300")
        ask_main.title("Custom Multi Messages")
        Label(ask_main, text='Choose one of these').pack()
        Button(ask_main, text='ping less than 20', width=25, command=gui_ping20).pack()
        Button(ask_main, text='ping less than 70', width=25, command=gui_ping70).pack()
        Button(ask_main, text='ping less than 200', width=25, command=gui_ping200).pack()
        Button(ask_main, text='ping less than 500', width=25, command=gui_ping500).pack()
        Button(ask_main, text='ping less than 3000', width=25, command=gui_ping3000).pack()
        Button(ask_main, text='ping Timed Out', width=25, command=gui_pingto).pack()
        Button(ask_main, text='ping Destination net unreachable', width=25, command=gui_pingdnu).pack()
        Button(ask_main, text='ping General Failure', width=25, command=gui_pinggf).pack()
        ask_main.mainloop()


class cmdline():
    def check_cmdline_beta(self):
        global cmdline
        cmdline = len(sys.argv)
        if cmdline == 1:
            gui.main_menu(self)
        if cmdline == 2:
            init.prepare_variable(self)
            if sys.argv[1] == "-restore-backup":
                process.create_backup(self)
            elif sys.argv[1] == "-gui-open-files":
                messagebox.showerror("Error", "Invalid Command Line")
            elif sys.argv[1] == "-help":
                pass
            else:
                messagebox.showerror("Error", "Invalid Command Line")
        if cmdline == 3:
            init.prepare_variable(self)
            if sys.argv[1] == "-gui-open-files":
                if sys.argv[2] == "-ping20":
                    process.process20.init(self)
                elif sys.argv[2] == "-ping70":
                    process.process70.init(self)
                elif sys.argv[2] == "-ping200":
                    process.process200(self)
                elif sys.argv[2] == "-ping500":
                    process.process500(self)
                elif sys.argv[2] == "-ping3000":
                    process.process3000(self)
                elif sys.argv[2] == "-pingto":
                    process.processto(self)
                elif sys.argv[2] == "-pingdnu":
                    process.processdnu(self)
                elif sys.argv[2] == "-pinggf":
                    process.processgf(self)
                else:
                    messagebox.showerror("Error", "Invalid Command Line")
            else:
                messagebox.showerror("Error", "Invalid Command Line")
        if cmdline > 3:
            messagebox.showerror("Error", "Invalid Command Line")


    def check_cmdline(self):
        global cmdline
        cmdline = len(sys.argv)
        if cmdline == 1:
            gui.main_menu(self)
        if cmdline == 2:
            init.prepare_variable(self)
            if sys.argv[1] == "-restore-backup":
                process.create_backup(self)
            elif sys.argv[1] == "-gui-open-files":
                messagebox.showerror("Error", "Invalid Command Line")
            elif sys.argv[1] == "-help":
                pass
            else:
                messagebox.showerror("Error", "Invalid Command Line")
        if cmdline == 3:
            init.prepare_variable(self)
            value_var_messagebox = messagebox.askyesno("Do you want to change multi or single custom messages ?", "Click yes for changing multi custom messages\nClick no for changing single custom messages")
            print(value_var_messagebox)
            if value_var_messagebox == True:
                process.process20.init(self)
                process.process70.init(self)
                process.process200.init(self)
                process.process500.init(self)
                process.process3000.init(self)
                process.processto.init(self)
                process.processdnu.init(self)
                process.processgf.init(self)
            else:
                pass
        if cmdline == 4:
            init.prepare_variable(self)
            if sys.argv[1] == "-gui-open-files":
                if sys.argv[2] == "-multi":
                    if sys.argv[3] == "-ping20":
                        process.process20.init(self)
                    elif sys.argv[3] == "-ping70":
                        process.process70.init(self)
                    elif sys.argv[3] == "-ping200":
                        process.process200(self)
                    elif sys.argv[3] == "-ping500":
                        process.process500(self)
                    elif sys.argv[3] == "-ping3000":
                        process.process3000(self)
                    elif sys.argv[3] == "-pingto":
                        process.processto(self)
                    elif sys.argv[3] == "-pingdnu":
                        process.processdnu(self)
                    elif sys.argv[3] == "-pinggf":
                        process.processgf(self)
                    else:
                        messagebox.showerror("Error", "Invalid Command Line")
                elif sys.argv[2] == "-single":
                    pass
                else:
                    messagebox.showerror("Error", "Invalid Command Line")
        if cmdline > 4:
            init.prepare_variable(self)
            messagebox.showerror("Error", "Invalid Command Line")

# Process Multi-Line Custom Output ping Messages
class process():
    # Fixed a bug after opening a file that can't be decoded through tkinter module, Help Module won't return to askopenfiles function
    # FINALLY WORKED !!
    # Grabbing directory files with GUI open files Using filedialog(tkinter)
    class process20():
        def init(self):
            global rollback_process_process20
            global rollback_process_process70
            global dir_embed_multi_files_20
            global embed_file
            global y
            x = True
            y = True
            rollback_process_process70 = ''
            rollback_process_process20 = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping less than 20", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        dir_embed_multi_files_20 = ''
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.process20.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            global dir_embed_multi_files_20
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_20 = str_dir_files[files_find_start:files_find_end].replace("/", "\\")
            read = open(dir_embed_multi_files_20, "r")
            try:
                read_result = read.read()
                process.process20.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.process20.init(self)

        def process2(self):
            global rollback_process_process20
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/ping20.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/ping20.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_process20 = 0

    class process70():
        def init(self):
            global rollback_process_process20
            global rollback_process_process70
            global dir_embed_multi_files_70
            global embed_file
            global y
            x = True
            y = True
            rollback_process_process20 = ''
            rollback_process_process70 = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping less than 70", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.process70.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_70 = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_70, "r")
            try:
                read_result = read.read()
                process.process70.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.process70.init(self)

        def process2(self):
            global rollback_process_process70
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/ping70.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/ping70.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_process70 = 0

    class process200():
        def init(self):
            global rollback_process_process200
            global dir_embed_multi_files_200
            global embed_file
            global y
            x = True
            y = True
            rollback_process_process200 = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping less than 200", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.process200.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_200 = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_200, "r")
            try:
                read_result = read.read()
                process.process200.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.process200.init(self)

        def process2(self):
            global rollback_process_process200
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/ping200.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/ping200.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_process200 = 0



    class process500():
        def init(self):
            global rollback_process_process500
            global dir_embed_multi_files_500
            global embed_file
            global y
            x = True
            y = True
            rollback_process_process500 = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping less than 500", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.process500.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_500 = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_500, "r")
            try:
                read_result = read.read()
                process.process500.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.process500.init(self)

        def process2(self):
            global rollback_process_process500
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/ping500.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/ping500.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_process500 = 0


    class process3000():
        def init(self):
            global rollback_process_process3000
            global dir_embed_multi_files_3000
            global embed_file
            global y
            x = True
            y = True
            rollback_process_process3000 = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping less than 3000", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.process3000.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_3000 = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_3000, "r")
            try:
                read_result = read.read()
                process.process3000.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.process3000.init(self)

        def process2(self):
            global rollback_process_process3000
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/ping3000.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/ping3000.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_process3000 = 0


    class processdnu():
        def init(self):
            global rollback_process_processdnu
            global dir_embed_multi_files_dnu
            global embed_file
            global y
            x = True
            y = True
            rollback_process_processdnu = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping Destination net unreachable", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.processdnu.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_dnu = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_dnu, "r")
            try:
                read_result = read.read()
                process.processdnu.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.processdnu.init(self)

        def process2(self):
            global rollback_process_processdnu
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/pingdnu.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/pingdnu.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_processdnu = 0

    class processto():
        def init(self):
            global rollback_process_processto
            global dir_embed_multi_files_to
            global embed_file
            global y
            x = True
            y = True
            rollback_process_processto = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping Timed Out", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.processto.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_to = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_to, "r")
            try:
                read_result = read.read()
                process.processto.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.processto.init(self)

        def process2(self):
            global rollback_process_processto
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/pingto.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/pingto.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_processto = 0

    class processgf():
        def init(self):
            global rollback_process_processgf
            global dir_embed_multi_files_gf
            global embed_file
            global y
            x = True
            y = True
            rollback_process_processgf = 1
            while x == True:
                embed_file = filedialog.askopenfiles(initialdir =  "/", title = "Select A File to be messages for ping Destination net unreachable", filetype =(("TXT FILE","*.txt"),("all files","*.*")))
                if embed_file == '':
                    value_var_messagebox = messagebox.askyesno("Error", "You dont choose any file, Do You want to skip ?")
                    if value_var_messagebox == True:
                        x = False
                    elif value_var_messagebox == False:
                        x = True
                    else:
                        pass
                else:
                    process.processgf.process(self)
                    x = False

        def process(self):
            global read
            global read_result
            files_find_start = str(embed_file).find("'")
            files_find_end = str(embed_file).find("mode=")
            files_find_start+=1
            files_find_end-=2
            str_dir_files = str(embed_file)
            dir_embed_multi_files_gf = str_dir_files[files_find_start:files_find_end].replace("/", "\\")

            read = open(dir_embed_multi_files_gf, "r")
            try:
                read_result = read.read()
                process.processgf.process2(self)
            except:
                messagebox.showerror("ERROR", "File Cannot be Opened (Unreadable)")
                process.processgf.init(self)

        def process2(self):
            global rollback_process_processgf
            read.close()
            if os.path.exists("custom_ping_messages/multi_messages"):
                write = open("custom_ping_messages/multi_messages/pinggf.txt", "w")
            else:
                os.mkdir("custom_ping_messages")
                os.mkdir("custom_ping_messages/multi_messages")
                write = open("custom_ping_messages/multi_messages/pinggf.txt", "w")
            write.write(read_result)
            write.close()
            messagebox.showinfo("Success", "The operation was successful")
            rollback_process_processgf = 0


    # Creating Backup if Custom_Ping.bat is missing or corrupted
    # (For Development Only) Type "Help.py -restore-backup" if you want to see it
    def create_backup(self):
        try:
            write_backup = open("FIXED_Custom_Ping.bat", "w")
            write_backup.write("""::Custom Ping (CP) v1.1
::Customed Version for 'ping.exe'
::Written in Batch Language

::Bug 
::when Deleting 'enable_count' and 'server_address' var, Custom Ping doesn't recreating 'config.txt' file (FIXED and TESTED)

::Checking for Debug Mode (You can do it too, type "Custom_Ping.bat" -debug)
::or You want to check your custom messages ?, type "Custom_Ping.bat" -debug-ping
title LOADING...
set init_count=0
set loop_azure=1
set debug_azure=0
set debug_ping=0
if "%1"=="" (
    @echo off
    cls
) else (
    if "%1"=="-debug" echo on
    if "%1"=="-debug-ping" @echo off && set debug_ping=1 && goto debug_ping
    if "%1"=="-run-azure-pipelines" @echo off && set debug_azure=1 && goto debug_azure_pipelines
)

::Preparation from 'config.txt' file and 'custom_ping_messages' folder for Custom Ping
:init_preparation
set searched=0
set message_showed=0
:init
set missing_messages=0
if %debug_ping%==1 (
    set debug_ping=1
) else (
    timeout 1 /nobreak>NUL
)
if exist "config.txt" (
    goto preparation
) else (
    set ADDRESS_SERVER=8.8.8.8
    echo 'config.txt' file not found, recreating one.... (All config will return to Default)
    if not exist "custom_ping_messages" set missing_messages=1 && echo 'custom_ping_messages' folder not found, recreating one.... (All Output Ping Messages will return to Default)
    goto create_config
)
goto preparation

:debug_ping
set VAR_MODIFED_VERIFY_2=1
goto init_preparation
:loop
set /a VAR_MODIFED_VERIFY_2=VAR_MODIFED_VERIFY_2+1
if %VAR_MODIFED_VERIFY_2% LEQ 20 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_20%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 70 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_70%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 200 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_200%
    goto init
) 
if %VAR_MODIFED_VERIFY_2% LEQ 500 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_500%
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 3000 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_3000%
    goto init
)
goto init_preparation

:preparation
set COM=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr change_output_message') do set COM=%%b
if "%COM%"=="1" goto open_editor
if "%COM%"=="0" set unknown=1
if "%COM%"=="NOT_FOUND" (
    echo ERROR : 'change_output_message' var not found in 'config.txt' file, recreating file....
    goto create_config
)
set ETTL=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr enable_ttl') do set ETTL=%%b
if "%ETTL%"=="1" set ETTL_VAR=1
if "%ETTL%"=="0" set ETTL=0 && set VAR_TTL_MODIFIED=
if "%ETTL%"=="NOT_FOUND" (
    echo ERROR : 'enable_ttl' var not found in 'config.txt' file, recreating file....
    goto create_config
)
set EC=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr enable_count') do set EC=%%b
if "%EC%"=="1" set EC_VAR=1 && set count_messages=count=
if "%EC%"=="0" set count= && set count_messages=
if "%EC%"=="NOT_FOUND" (
    echo ERROR : 'enable_count' var not found in 'config.txt' file, recreating file....
    goto create_config
)
set ADDRESS_SERVER_CHECK=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER_CHECK=%%b
if "%ADDRESS_SERVER_CHECK%"=="NOT_FOUND" (
    echo ERROR : 'server_address' var not found in 'config.txt' file, recreating file....
    goto create_config
)
if %message_showed%==1 goto preparation2
:find_address_server
set ADDRESS_SERVER=NOT_FOUND
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER=%%b
if "%ADDRESS_SERVER%"=="NOT_FOUND" (
    echo ERROR : 'server_address' var not found in 'config.txt' file, recreating file....
    goto create_config
)
goto preparation2

:preparation2
goto preparation3

:preparation3
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER2=%%b
if not exist "custom_ping_messages" set missing_messages=1 && echo 'custom_ping_messages' folder not found, recreating one.... (All Output Ping Messages will return to Default) && goto write_custom_messages
if "%ADDRESS_SERVER%"=="%ADDRESS_SERVER2%" (
    goto 1time_message
) else (
    echo Host Address Changed!, from %ADDRESS_SERVER% to %ADDRESS_SERVER2%
    echo.
    echo Pinging %ADDRESS_SERVER2% with 32 bytes of data:
    set ADDRESS_SERVER=%ADDRESS_SERVER2%
    goto 1time_message
)

::An editor for Custom Ping Messages (ECM = Editor Custom Messages)
:open_editor
set message_showed=0
cls
title Editor for Custom Ping
echo type Anything for ping less than 20
echo press enter if you want to leave it Default
set PING_20=Your internet IS UNBELIEVEABLE!!!
set /p "PING_20=>"
if "%PING_20%"=="" set PING_20=Your internet IS UNBELIEVEABLE!!!
cls
echo type Anything for ping less than 70
echo press enter if you want to leave it Default
set PING_70=Your internet is EXCELLENT
set /p "PING_70=>"
if "%PING_70%"=="" set PING_70=Your internet is EXCELLENT
cls
echo type Anything for ping less than 200
echo press enter if you want to leave it Default
set PING_200=Your internet is GOOD
set /p "PING_200=>"
if "%PING_200%"=="" set PING_200=Your internet is GOOD
cls
echo type Anything for ping less than 500
echo press enter if you want to leave it Default
set PING_500=Your internet is BAD
set /p "PING_500=>"
if "%PING_500%"=="" set PING_500=Your internet is BAD
cls
echo type Anything for ping less than 3000
echo press enter if you want to leave it Default
set PING_3000=Your internet is VERY BAD
set /p "PING_3000=>"
if "%PING_3000%"=="" set PING_3000=Your internet is VERY BAD
cls
echo type Anything if ping 'timed out'
echo press enter if you want to leave it Default
set PING_TIMED_OUT=Your internet is NOT RESPONDING!!!
set /p "PING_TIMED_OUT=>"
if "%PING_TIMED_OUT%"=="" set PING_TIMED_OUT=Your internet is NOT RESPONDING!!!
cls
echo type Anything if ping 'Destination net unreachable'
echo press enter if you want to leave it Default
set PING_DNU=Connected but no internet.
set /p "PING_DNU=>"
if "%PING_DNU%"=="" set PING_DNU=Connected but no internet.
cls
echo type Anything if ping 'General Failure'
echo press enter if you want to leave it Default
set PING_GENERAL_FAILURE=Something not right...
set /p "PING_GENERAL_FAILURE=>"
if "%PING_GENERAL_FAILURE%"=="" set PING_GENERAL_FAILURE=Something not right...
cls
goto write_custom_messages
::if 'custom_ping_messages' is missing, recreating a new one with Default value (Example : 'Ping less than 20' printing 'Your internet IS UNBELIEVEABLE!!!')
:write_custom_messages
if %missing_messages%==1 (
    set PING_20=Your internet IS UNBELIEVEABLE!!!
    set PING_70=Your internet is EXCELLENT
    set PING_200=Your internet is GOOD
    set PING_500=Your internet is BAD
    set PING_3000=Your internet is VERY BAD
    set PING_TIMED_OUT=Your internet is NOT RESPONDING!!!
    set PING_DNU=Connected but no internet.
    set PING_GENERAL_FAILURE=Something not right...
)
if not exist "custom_ping_messages" (
    md custom_ping_messages>NUL
)
echo %PING_20% > custom_ping_messages\messages20.txt
echo %PING_70% > custom_ping_messages\messages70.txt
echo %PING_200% > custom_ping_messages\messages200.txt
echo %PING_500% > custom_ping_messages\messages500.txt
echo %PING_3000% > custom_ping_messages\messages3000.txt
echo %PING_TIMED_OUT% > custom_ping_messages\messagesTO.txt
echo %PING_DNU% > custom_ping_messages\messagesDNU.txt
echo %PING_GENERAL_FAILURE% > custom_ping_messages\messagesGF.txt
goto search_custom_messages


::Search Custom Messages from 'custom_ping_messages' folder (SCM)
:search_custom_messages
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages20.txt"') do set PING_20=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages70.txt"') do set PING_70=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages200.txt"') do set PING_200=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages500.txt"') do set PING_500=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messages3000.txt"') do set PING_3000=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messagesTO.txt"') do set PING_TIMED_OUT=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messagesDNU.txt"') do set PING_DNU=%%b
for /f "tokens=*" %%b in ('type "custom_ping_messages\messagesGF.txt"') do set PING_GENERAL_FAILURE=%%b

set searched=1
if %debug_azure%==1 goto loop_azure
if %missing_messages%==1 goto 1time_message
if "%ADDRESS_SERVER%"=="" call :scm_find_server_address
echo # Host / Server Address > config.txt
echo server_address = %ADDRESS_SERVER% >> config.txt
echo. >> config.txt
echo # Change the output Messages ping (1 = yes , 0 = no) >> config.txt
echo change_output_message = 0 >> config.txt
if "%ETTL%"=="1" goto scm_server_write1
:scm_server2
if "%EC%"=="1" goto scm_server_write2
echo. >> config.txt
echo # Enable TTL (Time To Live) (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_ttl = 0 >> config.txt
echo. >> config.txt
echo # Enable Count Ping (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_count = 0 >> config.txt
:scm_server3
if %message_showed%==1 goto 1time_message
echo.
echo Pinging %ADDRESS_SERVER2% with 32 bytes of data:
set message_showed=1
goto 1time_message

::Recreating Config if 'config.txt' not found
:create_config
echo # Host / Server Address > config.txt
echo server_address = 8.8.8.8 >> config.txt
echo. >> config.txt
echo # Change the output Messages ping (1 = yes , 0 = no) >> config.txt
echo change_output_message = 0 >> config.txt
echo. >> config.txt
echo # Enable TTL (Time To Live) (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_ttl = 0 >> config.txt
echo. >> config.txt
echo # Enable Count Ping (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_count = 0 >> config.txt
echo Using Default Host (8.8.8.8) / Google DNS 
if %missing_messages%==1 goto write_custom_messages
echo.
echo Pinging %ADDRESS_SERVER2% with 32 bytes of data:
goto 1time_message

::Example Ping Result
::Reply from 8.8.8.8: bytes=32 time=217ms TTL=54
::Pinging 8.8.8.8 with 32 bytes of data

:1time_message
title Custom Ping by trollfist20 , Server: %ADDRESS_SERVER% %VAR_TTL_MODIFIED% %count_messages%%count%
if %debug_azure%==1 goto search_custom_messages
if %debug_ping%==1 goto loop
if %message_showed%==1 goto Module_Ping
echo Ping Customed Version v1.0 
echo Server Address : %ADDRESS_SERVER%
echo.
echo Pinging %ADDRESS_SERVER% with 32 bytes of data:
set message_showed=1
goto Module_Ping


::Unique Module Custom Ping (UMCP)
:Module_Ping
set VAR=NOT_FOUND
set VAR_MODIFIED=NOT_FOUND
set VAR_MODIFED_VERIFY=NOT_FOUND
set VAR_MODIFED_VERIFY_2=NOT_FOUND
for /f "tokens=*" %%b in ('ping %ADDRESS_SERVER% -n 1 ^| findstr /C:Reply /C:General /C:Destination /C:Request') do set VAR=%%b
for /f "tokens=5" %%b in ("%VAR%") do set VAR_MODIFIED=%%b
for /f "delims=time tokens=1" %%b in ('echo %VAR_MODIFIED% ^| findstr [0-9]') do set VAR_MODIFED_VERIFY=%%b
for /f "delims=time tokens=1" %%b in ('echo %VAR_MODIFED_VERIFY%') do set VAR_MODIFED_VERIFY_2=%%b
if "%ETTL%"=="1" for /f "tokens=6" %%b in ("%VAR%") do set VAR_TTL_MODIFIED=%%b
set /a init_count=init_count+1
if "%EC%"=="1" set count=%init_count%
if %VAR_MODIFED_VERIFY_2%==NOT_FOUND (
    goto Module_Ping_Error
) else (
    goto Module_Ping_Success
)
goto Module_Ping


:Module_Ping_Success
::if SCM (Search Custom Messages) has finished search, return variable 'searched' to 1 (Finished Searching)
::And Redirecting to Module_Ping_Success2 Label/Function
if %searched%==1 goto Module_Ping_Success2
goto search_custom_messages


:Module_Ping_Success2
if %VAR_MODIFED_VERIFY_2% LEQ 20 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_20% 
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 70 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_70% 
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 200 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_200% 
    goto init
) 
if %VAR_MODIFED_VERIFY_2% LEQ 500 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_500% 
    goto init
)
if %VAR_MODIFED_VERIFY_2% LEQ 3000 (
    echo [%VAR_MODIFED_VERIFY_2%] %PING_3000% 
    goto init
)
echo Return ERROR : Result not Found, Make sure you type correctly host or server address
goto init

:Module_Ping_Error
set VAR_ERROR=NOT_FOUND
for /f "tokens=1" %%b in ("%VAR%") do set VAR_ERROR=%%b
if %VAR_ERROR%==General (
    echo [General Failure] %PING_GENERAL_FAILURE%
    goto init
)
if %VAR_ERROR%==Reply (
    echo [Destination net unreachable] %PING_DNU%
    goto init
)
if %VAR_ERROR%==Request (
    echo [Timed Out] %PING_TIMED_OUT% 
    goto init
)
echo Return ERROR : Result not Found, Make sure you type correctly host or server address
goto init


::Debugging in Azure Pipelines
:debug_azure_pipelines
goto init_preparation
:loop_azure
if 20 LEQ 20 echo [20] %PING_20%
if 70 LEQ 70 echo [70] %PING_70%
if 200 LEQ 200 echo [200] %PING_200%
if 500 LEQ 500 echo [500] %PING_500%
if 3000 LEQ 3000 echo [3000] %PING_3000%
echo [Timed Out] %PING_TIMED_OUT%
echo [Destination net unreachable] %PING_DNU%
echo [General Failure] %PING_GENERAL_FAILURE%
exit

:scm_server_write1
echo. >> config.txt
echo # Enable TTL (Time To Live) (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_ttl = 1 >> config.txt
goto scm_server2

:scm_server_write2
echo. >> config.txt
echo # Enable Count Ping (1 = yes, 0 = no) (Default Value is 0) >> config.txt
echo enable_count = 1 >> config.txt
goto scm_server3

:scm_find_server_address
for /f "tokens=3" %%b in ('type config.txt ^| findstr server_address') do set ADDRESS_SERVER=%%b
set ADDRESS_SERVER2=%ADDRESS_SERVER%
            """)
            write_backup.close()
            messagebox.showinfo('Success', "The Operation was Successful")
        except:
            messagebox.showerror('Error', "Something Happened, Please try again")
class main():
    def main(self):
        self = ''
        try:
            cmdline.check_cmdline(self)
        except KeyboardInterrupt:
            value_var_messagebox = messagebox.askyesno("Goodbye", "Are You Sure want to exit ?")
            if value_var_messagebox == True:
                sys.exit(0)
            elif value_var_messagebox == False:
                main.rollback(self)
            else:
                pass

    def rollback(self):
        x = 1
        while x < 2:
            if rollback_process_process20 == 1:
                try:
                    process.process20.init(self)
                    x = 2
                except KeyboardInterrupt:
                    value_var_messagebox = messagebox.askyesno("Goodbye", "Are You Sure want to exit ?")
                    if value_var_messagebox == True:
                        sys.exit(0)
                    elif value_var_messagebox == False:
                        process.process20.init(self)
                    else:
                        pass
            if rollback_process_process70 == 1:
                try:
                    process.process70.init(self)
                    x = 2
                except KeyboardInterrupt:
                    value_var_messagebox = messagebox.askyesno("Goodbye", "Are You Sure want to exit ?")
                    if value_var_messagebox == True:
                        sys.exit(0)
                    elif value_var_messagebox == False:
                        process.process70.init(self)
                    else:
                        pass


if __name__ == "__main__":
    self = ''
    main.main(self)
