import tkinter as tk # import thư viện tkinter để tạo giao diện
from tkinter import messagebox # import messagebox để hiển thị hộp thoại thông báo
import speech_recognition as sr # import thư viện speech_recognition để nhận dạng giọng nói
from gtts import gTTS # import thư viện gTTS để tạo file âm thanh
import playsound  # import thư viện playsound để phát file âm thanh
import os  # import thư viện os để tạo thư mục
from tkinter import scrolledtext

NguyenTrongDung_14_FILE = "14_NguyenTrongDung_Voice_Assistant.mp3" # tên file âm thanh sẽ được tạo ra
NguyenTrongDung_14_DIR = "F:/13_21133021_NguyenTrongDung_LuuTruMonHoc/Lap Trinh Python/DoAnHocPhan/14_NguyenTrongDung_Voice_Assistant" # tên thư mục sẽ được tạo ra
os.makedirs(NguyenTrongDung_14_DIR, exist_ok=True)

def Lenh_NTDung_14(language_choice, duration_choice): # Hàm ghi âm và nhận dạng giọng nói
    r = sr.Recognizer() # khởi tạo đối tượng Recognizer để nhận dạng giọng nói
    with sr.Microphone() as Source: # mở microphone để ghi âm
        messagebox.showinfo("Nhắc nhở", "Hiệu chỉnh nhiễu trước khi nói!") # hiển thị thông báo
        r.adjust_for_ambient_noise(Source, duration=1) # hiệu chỉnh để loại bỏ nhiễu
    
        language = language_choice.get() # lấy ngôn ngữ lựa chọn
        if language not in ['vi', 'en-US']: # kiểm tra xem ngôn ngữ lựa chọn có hỗ trợ hay không
            messagebox.showwarning("Cảnh báo", "Ngôn ngữ bạn chọn không được hỗ trợ, chương trình chỉ chạy 2 ngôn ngữ Tiếng Việt (vi)"+
                                   " và English (en_US)")
            return # thoát hàm
        else:
            messagebox.showinfo("Cảnh báo", "Bấm OK để bắt đầu ghi âm bằng ngôn ngữ đã chọn, trong thời gian bạn muốn")
        audio_data = r.record(Source, duration=duration_choice.get()) # ghi âm trong khoảng thời gian lựa chọn
        try:
            vlenh = r.recognize_google(audio_data, language=language) # nhận dạng giọng nói bằng Google
        except:
            vlenh = "Không nhận diện được âm thanh, hãy thử lại." # Thông báo không nhận diện được âm thanh
        #messagebox.showinfo("Quý vị đã nói là", vlenh) #hiển thị lời vừa nói
        vText = gTTS(text=vlenh, lang=language) #tạo file âm thanh
        vText.save(NguyenTrongDung_14_FILE) #lưu file
        vText.save(os.path.join(NguyenTrongDung_14_DIR, NguyenTrongDung_14_FILE)) #lưu vào thư mục
        playsound.playsound(NguyenTrongDung_14_FILE) #phát lại âm thanh
        return vlenh

def run_form_NTDung_14():
    wf = tk.Tk()
    wf.title("14_Nguyễn Trọng Dũng_VoiceAssistant")

    # Lấy thông tin kích thước màn hình
    screen_width = wf.winfo_screenwidth()
    screen_height = wf.winfo_screenheight()

    # Tính toán vị trí hiển thị form
    x = (screen_width/2) - (1000/2)
    y = (screen_height/2) - (600/2)

    # Thiết lập kích thước và vị trí của form
    wf.geometry('%dx%d+%d+%d' % (1000, 600, x, y))

    panel = tk.Label(wf, text="Hiện Tại Voice_Assistant chỉ cung cấp khả năng với 2 ngôn ngữ: vi (Tiếng Việt) và en-US (Tiếng Anh)",
                      font=("Times New Roman", 20))
    panel.pack()

    def move_text():
        x, y = panel.winfo_x(), panel.winfo_y()
        panel.place(x=x-10, y=y)
        if x <= -panel.winfo_width():
            panel.place(x=wf.winfo_width(), y=y)
        wf.after(50, move_text)

    # Gọi hàm di chuyển chữ bên trong panel
    move_text()

    language_choice = tk.StringVar(value='')
    duration_choice = tk.IntVar(value=0)

    language_label = tk.Label(wf, text="Ngôn ngữ:",font=("Times New Roman", 16))
    language_label.place(x=130, y=130)

    language_input = tk.Entry(wf, textvariable=language_choice) # Tạo ô nhập liệu cho người dùng chọn ngôn ngữ
    language_input.place(x=240, y=135)

    duration_label = tk.Label(wf, text="Thời gian ghi âm:",font=("Times New Roman", 16))
    duration_label.place(x=130, y=170)

    duration_input = tk.Entry(wf, textvariable=duration_choice) # Tạo ô nhập liệu cho người dùng nhập thời gian ghi âm
    duration_input.place(x=300, y=175)

    result_label1=tk.Label(wf,text="Bạn đã nói: ",font=("Times New Roman", 16))
    result_label1.place(x=130, y=260)

    def on_click(): # Hàm xử lý sự kiện khi người dùng nhấn nút Ghi âm
        kq_voice=Lenh_NTDung_14(language_choice, duration_choice)

        # Tạo Frame để chứa TextBox
        frame = tk.Frame(wf)
        frame.pack()
        frame.place(x=130,y=300)

        # Tạo TextBox
        textbox = scrolledtext.ScrolledText(frame, width=50, height=10)
        textbox.pack()

        # Xóa nội dung của TextBox
        textbox.delete(1.0, tk.END)

        # Thêm nội dung mới vào TextBox
        textbox.insert(tk.INSERT, kq_voice)
    

    button_GhiAm = tk.Button(wf, text="Ghi âm",font=("Times New Roman", 16), command=on_click) # Tạo nút Ghi âm
    button_GhiAm.place(x=420, y=210)

    def Thoat_Form():
        wf.destroy()

    button_Thoat = tk.Button(wf, text="Thoát",font=("Times New Roman", 16), command=Thoat_Form) # Tạo nút Thoát
    button_Thoat.place(x=750, y=210)

    wf.mainloop()

if __name__ == '__main__':
    run_form_NTDung_14()
