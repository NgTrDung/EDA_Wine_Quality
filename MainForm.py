import tkinter as tk
import FormVoiceAssistant as FVA

# Tạo một instance của Tkinter
root = tk.Tk()

# Lấy thông tin kích thước màn hình
screen_width = root.winfo_screenwidth()

# Tính toán vị trí hiển thị form
x = (screen_width/2) - (1000/2)
y = (screen_height/2) - (600/2)

# Thiết lập kích thước và vị trí của form
root.geometry('%dx%d+%d+%d' % (1000, 600, x, y))

#Đặt title cho Form
root.title('14 Nguyễn Trọng Dũng, 21133_HCMUTE, Đồ Án Học Phần: Lập Trình Python, T5.2023')

# Tạo panel
panel = tk.Label(root, text="14 Nguyễn Trọng Dũng, 21133_HCMUTE, Đồ Án Học Phần: Lập Trình Python: EDA Wine Quality", font=("Times New Roman", 20))
panel.pack()

def move_text():
        x, y = panel.winfo_x(), panel.winfo_y()
        panel.place(x=x-10, y=y)
        if x <= -panel.winfo_width():
            panel.place(x=root.winfo_width(), y=y)
        root.after(50, move_text)

# Gọi hàm di chuyển chữ bên trong panel
move_text()

# Tạo button "Voice_Assistant" và đặt vị trí
voice_button = tk.Button(root, text="Voice_Assistant", font=("Times New Roman", 16),command=FVA.run_form_NTDung_14)
voice_button.place(x=250, y=250)

# Tạo button "EDA" và đặt vị trí
eda_button = tk.Button(root, text="EDA", font=("Times New Roman", 16))
eda_button.place(x=450, y=250)

# Tạo button "Thoát" và đặt vị trí
exit_button = tk.Button(root, text="Thoát", font=("Times New Roman", 16), command=root.destroy)
exit_button.place(x=550, y=250)

# Hiển thị form
root.mainloop()
