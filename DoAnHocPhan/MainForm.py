import tkinter as tk

# Tạo form với kích thước 1000x600
form = tk.Tk()
form.geometry("1000x600")

# Lấy kích thước màn hình hiện tại
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()

# Tính toán để form xuất hiện ở giữa màn hình
x = (screen_width // 2) - (1000 // 2)
y = (screen_height // 2) - (600 // 2)

# Thiết lập vị trí của form
form.geometry("+{}+{}".format(x, y))

# Hiển thị form
form.mainloop()
