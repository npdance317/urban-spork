import tkinter as tk
import sys

wgt = 1
hgt = 1
bmi = 1

def finish():
    print("Finished")
    sys.exit()

def bmicalc():
    global wgt
    global hgt
    global bmi
    
    wgt = int(wgt_ent.get())
    hgt = int(hgt_ent.get())

    bmi = (wgt/(hgt**2))*703
    bmi_lbl.config(text=f"BMI: {bmi:.2f}")

    data = [wgt, hgt, bmi]
    print(data)

def savefile():
    global wgt
    global hgt
    global bmi
    
    #ques = input("Save to file: ")
    #if(ques == "y"):
    file1 = open('bmi_file.txt', mode='a', newline='')

    #file1.write(str(wgt) + ',' + str(hgt) + ',' + str(bmi) +'\n')
    file1.write(f"{wgt}, {hgt}, {bmi:.2f} \n")
    print("Data saved.")
    
#Create a window
wnd = tk.Tk()
wnd.title("BMI Calculator")
wnd.configure(bg = "gray")
wnd.geometry("400x200")

# Create a frame for the form
form_frm = tk.Frame(wnd, bg = "gray")
form_frm.pack(padx=10, pady=10)

# Create a label for weight
wgt_lbl = tk.Label(form_frm, text="Weight (lbs)", bg="gray")
wgt_lbl.grid(row=0, column=0, padx = 10, pady = 10)
# Create the input entry for weight
wgt_ent = tk.Entry(form_frm)
wgt_ent.grid(row=0, column=1, padx = 10, pady = 10)

# Create a label for height
hgt_lbl = tk.Label(form_frm, text="Height (in.)", bg="gray")
hgt_lbl.grid(row=1, column=0,padx = 10, pady = 10)
# Create the input entry for height
hgt_ent = tk.Entry(form_frm)
hgt_ent.grid(row=1, column=1,padx = 10, pady = 10)

# Create a button to trigger the BMI calc function
bmi_btn = tk.Button(form_frm, text="Calc BMI", command=bmicalc)
bmi_lbl = tk.Label(form_frm, text = "")

# Save data to file
save_btn = tk.Button(form_frm, text = "Save", command=savefile)
# exit button to finish program
exit_btn = tk.Button(form_frm, text = "Exit", command=finish)

bmi_btn.grid(row=3, column=0, padx = 10, pady = 10)
bmi_lbl.grid(row=3, column=1, padx = 10, pady = 10)
save_btn.grid(row=4, column=0, padx = 10, pady = 10)
exit_btn.grid(row=4, column=1, padx = 10, pady = 10)

# Start the tkinter event loop
wnd.mainloop()