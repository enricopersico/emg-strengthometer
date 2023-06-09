"""
DESCRIPTION: 
This is a python script for a small application to read the highest voltage 
generated by my EMG circuit and display it to the user as a "strength score".
AUTHOR: Enrico Persico
"""
import customtkinter as ctk
import time, serial, os, sys

port = "/dev/cu.usbmodem2101" # port that Arduino is using
baud = 50000 # baud rate set on Arduino script
ser = serial.Serial(port, baud)

root = ctk.CTk()
#ctk.set_appearance_mode("dark")
#ctk.set_default_color_theme("dark-blue")
root.geometry("800x500")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def countdown(old, new):
    new.pack(pady=12, padx=10)
    old.pack_forget()

# puts up "FLEX!!!" frame and gets rid of it after 3 seconds
def flex_frame():
    flex_label = ctk.CTkLabel(master=frame, text="FLEX!!!", font=("Roboto", 96), text_color="green")
    flex_label.pack(pady=42, padx=10)
    root.after(3000, flex_label.pack_forget)

# gets rid of two labels
def destroy_labels(one, two):
    one.pack_forget()
    two.pack_forget()

# records max voltage during flex and displays it
def record():
    high_score = 0
    start = time.time()
    end = time.time()
    while end - start < 3:
        getData=ser.readline()
        dataString = getData.decode('utf-8')
        data=dataString[0:][:-2]
        if float(data) > high_score:
            high_score = float(data)
        end = time.time()

    final_label = ctk.CTkLabel(master=frame, text="Strength Score:", font=("Roboto", 56), text_color="white")
    final_label.pack(pady=12, padx=10)
    high_score = high_score*3 + 100
    hs_label = ctk.CTkLabel(master=frame, text=int(high_score), font=("Roboto", 96), text_color="green")
    hs_label.pack(pady=12, padx=10)

    restart_button = ctk.CTkButton(master=frame, text="TEST ME AGAIN", command=restart, font=("Roboto", 33), width=360, height=80)
    restart_button.pack(pady=40, padx=10)

    
# handles start button press
def start():
    button.pack_forget()
    label.pack_forget()
    s_label.pack_forget()
    relax_label = ctk.CTkLabel(master=frame, text="Relax your arm.", font=("Roboto", 66), text_color="white")
    relax_label.pack(pady=12, padx=10)
    three_label = ctk.CTkLabel(master=frame, text="3", font=("Roboto", 116), text_color="red")
    three_label.pack(pady=12, padx=10)
    two_label = ctk.CTkLabel(master=frame, text="2", font=("Roboto", 116), text_color="yellow")
    one_label = ctk.CTkLabel(master=frame, text="1", font=("Roboto", 116), text_color="blue")
    root.after(1000, countdown, three_label, two_label)
    root.after(2000, countdown, two_label, one_label)
    root.after(3000, destroy_labels, one_label, relax_label)
    root.after(3000, flex_frame)
    root.after(3200, record)


s_label = ctk.CTkLabel(master=frame, text="The Strengthometer", font=("Roboto", 55), text_color="white")
s_label.pack(pady=12, padx=10)
label = ctk.CTkLabel(master=frame, text="Test Your Strength!", font=("Roboto", 32), text_color="green")
label.pack(pady=6, padx=10)

button = ctk.CTkButton(master=frame, text="TEST ME", command=start, font=("Roboto", 33), width=240, height=80)
button.pack(pady=40, padx=10)

root.mainloop()
