import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import re

def lockinfo():
    tx_bmi.config(state=DISABLED)
    tx_glu.config(state=DISABLED)
    tx_hoten.config(state=DISABLED)
    tx_tuoi.config(state=DISABLED)
    cb_gioitinh.config(state="disabled")
    cb_heartdis.config(state="disabled")
    cb_hypertention.config(state="disabled")
    cb_married.config(state="disabled")
    cb_residence.config(state="disabled")
    cb_smoked.config(state="disabled")
    cb_worktype.config(state="disabled")


def confirm():   
    #gán thông tin
    name = tx_hoten.get()
    gender = cb_gioitinh.get()
    age=tx_tuoi.get()
    hypertention=cb_hypertention.get()
    heartdisease=cb_heartdis.get()
    married=cb_married.get()
    worktype=cb_worktype.get()
    residence=cb_residence.get()
    glucoseindex=tx_glu.get()
    bmiindex=tx_bmi.get()
    smoked=cb_smoked.get()
    if(checkage(age)==1 and checkglucose(glucoseindex)==1 and checkbmi(bmiindex)==1 and checkcombobox(gender, hypertention, heartdisease, married, worktype, residence, smoked)==1):
        lockinfo()
        messagebox.showinfo(title="Thông tin", message=name+"\n"+gender+"\n"+age+"\n"+hypertention+"\n"+heartdisease+"\n"+married+"\n"+worktype+"\n"+residence+"\n"+glucoseindex+"\n"+bmiindex+"\n"+smoked)
    else: 
        messagebox.showerror(title="Lỗi", message="Nhập sai dữ liệu. Xin vui lòng nhập lại.")
        # lb_result.config(text = 'die')
        # lb_result.config(text = 45)
#check age
def checkage(age):
    if(re.search('[a-zA-Z]', age)==None and (' ' in age) == False and age!=''):
        if(int(age) in range(1,100)):
            return 1
        else:
            return 0
    else:
        return 0

#check glucose index
def checkglucose(glucoseindex):
    if(re.search('[a-zA-Z]', glucoseindex)==None and (' ' in glucoseindex) == False and glucoseindex!=''):
        if(float(glucoseindex)>0):
            return 1
        else:
            return 0
    else:
        return 0

#check bmi index
def checkbmi(bmiindex):
    if(re.search('[a-zA-Z]', bmiindex)==None and (' ' in bmiindex) == False and bmiindex!=''):
        if(float(bmiindex)>0):
            return 1
        else:
            return 0
    else:
        return 0

#check combo box
def checkcombobox(gender, hypertention, heartdisease, married, worktype, residence, smoked):
    if(gender!='' and hypertention!='' and heartdisease!='' and married!='' and worktype!='' and residence!='' and smoked!=''):
        return 1
    else:
        return 0


    
def reset():
    tx_hoten.config(state=NORMAL); tx_hoten.delete("0","end")
    tx_bmi.config(state=NORMAL); tx_bmi.delete("0","end")
    tx_glu.config(state=NORMAL); tx_glu.delete("0","end")
    tx_tuoi.config(state=NORMAL); tx_tuoi.delete("0","end")
    cb_gioitinh.config(state="readonly"); cb_gioitinh.set('')
    cb_heartdis.config(state="readonly"); cb_heartdis.set('')
    cb_hypertention.config(state="readonly"); cb_hypertention.set('')
    cb_married.config(state="readonly"); cb_married.set('')
    cb_residence.config(state="readonly"); cb_residence.set('')
    cb_smoked.config(state="readonly"); cb_smoked.set('')
    cb_worktype.config(state="readonly");  cb_worktype.set('')

#window
window = tk.Tk()
ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
window.title("Chẩn đoán đột quỵ")
window.geometry("500x700")
window.minsize(500,700)
window.maxsize(500,700)
window.wm_iconphoto(False, photo)

#tiêu đề
title= Label(window, text = "CHƯƠNG TRÌNH CHẨN ĐOÁN ĐỘT QUỴ", fg = "red", font = ("Helvetica", 16, "bold"))
title.place(x=50, y=20)
#chỉ dẫn
lb_chidan=Label(window, text = "Hãy nhập các thông tin dưới đây", fg="blue", font=("Arial", 14, "italic"))
lb_chidan.place(x=110, y=50)
#họ tên
lb_hoten=Label(window, text = "Họ và tên", fg="black", font=("Arial", 10))
lb_hoten.place(x=100, y=100)
tx_hoten = Entry(window, width = 20)
tx_hoten.place(x=220, y=100)


#giới tính
lb_gioitinh=Label(window, text = "Giới tính", fg="black", font=("Arial", 10))
lb_gioitinh.place(x=100, y=140)
gioitinh = ['Nam', 'Nữ']
cb_gioitinh = ttk.Combobox(window, values = gioitinh, state="readonly", width=10)
cb_gioitinh.place(x=220, y=140)

#tuổi
lb_tuoi=Label(window, text = "Tuổi", fg="black", font=("Arial", 10))
lb_tuoi.place(x=100, y=180)
tx_tuoi = Entry(window, width = 10)
tx_tuoi.place(x=220, y=180)
#tăng huyết áp
lb_hypertention=Label(window, text = "Bị tăng huyết áp", fg="black", font=("Arial", 10))
lb_hypertention.place(x=100, y=220)
hypertentionstatus = ['Có', 'Không']
cb_hypertention = ttk.Combobox(window, values = hypertentionstatus, state="readonly", width=10)
cb_hypertention.place(x=220, y=220)
#bệnh tim
lb_heartdis=Label(window, text = "Bị bệnh tim", fg="black", font=("Arial", 10))
lb_heartdis.place(x=100, y=260)
heartdisstatus = ['Có', 'Không']
cb_heartdis = ttk.Combobox(window, values = heartdisstatus, state="readonly", width=10)
cb_heartdis.place(x=220, y=260)
#đã từng kết hôn
lb_married=Label(window, text = "Đã từng kết hôn", fg="black", font=("Arial", 10))
lb_married.place(x=100, y=300)
marriedstatus = ['Có', 'Không']
cb_married = ttk.Combobox(window, values = marriedstatus, state="readonly", width=10)
cb_married.place(x=220, y=300)
#loại nghề nghiệp
lb_worktype=Label(window, text = "Loại nghề nghiệp", fg="black", font=("Arial", 10))
lb_worktype.place(x=100, y=340)
worktypes = ['Trẻ con', 'Tự do', 'Nhà nước', 'Tư nhân']
cb_worktype = ttk.Combobox(window, values = worktypes, state="readonly", width=10)
cb_worktype.place(x=220, y=340)
#Nơi sinh sống
lb_residence=Label(window, text = "Nơi sinh sống", fg="black", font=("Arial", 10))
lb_residence.place(x=100, y=380)
residencestatus = ['Nông thôn', 'Đô thị']
cb_residence = ttk.Combobox(window, values = residencestatus, state="readonly", width=10)
cb_residence.place(x=220, y=380)
#Chỉ số Glucose trung bình trong máu
lb_glu=Label(window, text = "Chỉ số Glucose tb", fg="black", font=("Arial", 10))
lb_glu.place(x=100, y=420)
tx_glu = Entry(window, width = 10)
tx_glu.place(x=220, y=420)
lb_glu_unit=Label(window, text = "mg/dL", fg="black", font=("Arial", 10))
lb_glu_unit.place(x=290, y=420)
#bmi
lb_bmi=Label(window, text = "Chỉ số BMI", fg="black", font=("Arial", 10))
lb_bmi.place(x=100, y=460)
tx_bmi = Entry(window, width = 10)
tx_bmi.place(x=220, y=460)
#hút thuốc
lb_smoked=Label(window, text = "Tình trạng hút thuốc", fg="black", font=("Arial", 10))
lb_smoked.place(x=100, y=500)
smokedstatus = ['Từng hút', 'Chưa từng hút', 'Đang hút', 'Không rõ']
cb_smoked = ttk.Combobox(window, values = smokedstatus, state="readonly", width=10)
cb_smoked.place(x=220, y=500)

#Nút chẩn đoán
btn_chandoan = Button(window, text="Chẩn đoán", command=confirm, width=15)
btn_chandoan.place(x=300, y=550)

#Nút reset
btn_reset = Button(window, text="Nhập lại", command=reset, width=15)
btn_reset.place(x=100, y=550)

#result
lb_result=Label(window, text = '', fg="black", font=("Arial", 10))
lb_result.place(x=200, y=600)



window.mainloop()
