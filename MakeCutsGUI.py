import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from MakeCuts import cut_video_by_timestamps
import os

class VideoCutterApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Cutter")
        master.geometry("500x300")
        
        # Стиль
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        
        # Виджеты
        self.create_widgets()
        
    def create_widgets(self):
        # Выбор файла
        self.file_frame = ttk.Frame(self.master)
        self.file_frame.pack(pady=10, fill='x', padx=10)
        
        self.file_label = ttk.Label(self.file_frame, text="Видеофайл:")
        self.file_label.pack(side='left')
        
        self.file_entry = ttk.Entry(self.file_frame, width=40)
        self.file_entry.pack(side='left', padx=5)
        
        self.browse_btn = ttk.Button(self.file_frame, text="Обзор...", command=self.browse_file)
        self.browse_btn.pack(side='left')
        
        # Поле для таймкодов
        self.time_frame = ttk.Frame(self.master)
        self.time_frame.pack(pady=10, fill='x', padx=10)
        
        self.time_label = ttk.Label(self.time_frame, text="Таймкоды (ЧЧ:ММ:СС через запятую):")
        self.time_label.pack(anchor='w')
        
        self.time_entry = tk.Text(self.time_frame, height=5, width=50)
        self.time_entry.pack()
        
        # Кнопка вставки из буфера
        self.paste_btn = ttk.Button(
            self.time_frame, 
            text="Вставить из буфера", 
            command=self.paste_from_clipboard
        )
        self.paste_btn.pack(pady=5)
        
        # Кнопка обработки
        self.process_btn = ttk.Button(self.master, text="Нарезать видео", command=self.process_video)
        self.process_btn.pack(pady=10)
        
        # Прогресс бар
        self.progress = ttk.Progressbar(self.master, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=10)
        
    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Выберите видеофайл",
            filetypes=[("Video files", "*.mp4 *.avi *.mov"), ("All files", "*.*")]
        )
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)
            
    def paste_from_clipboard(self):
        """Вставляет текст из буфера обмена в поле таймкодов"""
        try:
            clipboard_text = self.master.clipboard_get()
            if clipboard_text.strip():
                self.time_entry.delete("1.0", tk.END)
                self.time_entry.insert(tk.END, clipboard_text)
                messagebox.showinfo("Успех", "Текст из буфера успешно вставлен")
        except tk.TclError:
            messagebox.showerror("Ошибка", "Буфер обмена пуст или содержит не текстовые данные")

    def process_video(self):
        video_path = self.file_entry.get()
        timestamps = self.time_entry.get("1.0", tk.END).strip()
        
        if not video_path or not timestamps:
            messagebox.showerror("Ошибка", "Укажите видеофайл и таймкоды")
            return
            
        try:
            self.progress['value'] = 0
            self.master.update_idletasks()
            
            cut_video_by_timestamps(video_path, timestamps)
            
            self.progress['value'] = 100
            messagebox.showinfo("Готово", "Видео успешно нарезано!")
            
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            self.progress['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoCutterApp(root)
    root.mainloop()
