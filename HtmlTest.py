import tkinter as tk
from tkinter import messagebox, ttk
import random
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

class HTMLTEST:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест по HTML")
        self.root.geometry("620x550")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("plastik")

        self.background_image = Image.open("BackgroundTestHtml.jpg")
        self.background_image = self.background_image.resize((620, 550))
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.questions = [
            {
                "question": "Какое расширение у файлов, содержащих HTML-код?",
                "options": [".html", ".css", ".js", ".xml"],
                "correct_answer": ".html"
            },
            {
                "question": "Как создать заголовок первого уровня в HTML?",
                "options": ["<h1>Заголовок</h1>", "<head>Заголовок</head>", "<h>Заголовок</h>", "<header>Заголовок</header>"],
                "correct_answer": "<h1>Заголовок</h1>"
            },
            {
                "question": "Как вставить изображение на веб-страницу в HTML?",
                "options": ["<img src=\"image.jpg\" alt=\"Изображение\">", "<image src=\"image.jpg\" alt=\"Изображение\">",
                            "<img alt=\"Изображение\">image.jpg</img>", "<picture>image.jpg</picture>"],
                "correct_answer": "<img src=\"image.jpg\" alt=\"Изображение\">"
            },
            {
                "question": "Как создать ссылку в HTML?",
                "options": ["<link>http://example.com</link>", "<a href=\"http://example.com\">Ссылка</a>",
                            "<url>http://example.com</url>", "<a link=\"http://example.com\">Ссылка</a>"],
                "correct_answer": "<a href=\"http://example.com\">Ссылка</a>"
            },
            {
                "question": "Какой тег используется для создания списка в HTML?",
                "options": ["<list>", "<ol>", "<ul>", "<li>"],
                "correct_answer": "<ul>"
            },
            {
                "question": "Как вставить перенос строки в HTML?",
                "options": ["<br>", "<newline>", "<nl>", "<enter>"],
                "correct_answer": "<br>"
            },
            {
                "question": "Как изменить цвет текста в HTML?",
                "options": ["<color>#FF0000</color>", "<text color=\"#FF0000\">Текст</text>",
                            "<span style=\"color: #FF0000\">Текст</span>", "<style>color: #FF0000;</style>"],
                "correct_answer": "<span style=\"color: #FF0000\">Текст</span>"
            },
            {
                "question": "Как вставить комментарий в HTML?",
                "options": ["<!-- Комментарий -->", "<comment>Комментарий</comment>", "<# Комментарий #>", "<* Комментарий *>"],
                "correct_answer": "<!-- Комментарий -->"
            },
            {
                "question": "Как создать форму в HTML?",
                "options": ["<form>...</form>", "<input>...</input>", "<form>...<input>...</form>",
                            "<form action=\"/submit\" method=\"post\">...</form>"],
                "correct_answer": "<form>...</form>"
            },
            {
                "question": "Как добавить таблицу в HTML?",
                "options": ["<table>...</table>", "<grid>...</grid>", "<tab>...</tab>", "<data>...</data>"],
                "correct_answer": "<table>...</table>"
            },
        ]
        random.shuffle(self.questions)

        self.score = 0
        self.current_question_index = 0

        self.label_question = tk.Label(root, text="", anchor="w", padx=10, font=("Times New Roman", 16, "bold"))
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.check_answer,
                                          anchor="w", font=("Times New Roman", 14))
            radio_button.pack(fill="x")
            self.radio_buttons.append(radio_button)

        self.style.configure("TButton", padding=5, borderwidth=5, relief="flat", foreground="white",
                             background="#4CAF50", font=("Times New Roman", 14, "bold"))

        self.next_button = ttk.Button(root, text="Далее", command=self.next_question, style="TButton")
        self.next_button.pack(pady=20, side="top")

        self.style.map("TButton",
                       foreground=[('active', '!disabled', 'black')],
                       background=[('active', '#45a049'), ('disabled', '#d3d3d3')])

        self.root.bind_all("<ButtonRelease-1>",
                           self.button_release)

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            options = [opt for opt in question_data["options"] if opt not in self.used_options]
            random.shuffle(options)

            for i in range(4):
                self.radio_buttons[i].config(text=options[i], value=options[i])

            self.next_button.state(["disabled"])
        else:
            self.show_result()

    def update_question(self):
        for radio_button in self.radio_buttons:
            radio_button.config(fg="black", state=tk.NORMAL)

        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            options = question_data["options"].copy()
            random.shuffle(options)

            for i in range(4):
                self.radio_buttons[i].config(text=options[i], value=options[i])

            self.next_button.state(["disabled"])
        else:
            self.show_result()

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        for i in range(4):
            if self.radio_buttons[i].cget("value") == selected_answer:
                if selected_answer == correct_answer:
                    self.score += 1
                    self.radio_buttons[i].config(fg="green", bg="light green")
                else:
                    self.radio_buttons[i].config(fg="red", bg="misty rose")
                    self.radio_buttons[self.get_correct_button_index()].config(fg="green", bg="light green")

        for radio_button in self.radio_buttons:
            radio_button.config(state=tk.DISABLED)

        self.next_button.state(["!disabled"])

    def reset_colors_and_next_question(self):
        self.background_label.config(bg="white")
        for radio_button in self.radio_buttons:
            radio_button.config(fg="black", state=tk.NORMAL)

        self.current_question_index += 1
        self.radio_var.set(None)
        self.next_button.state(["disabled"])
        self.update_question()

    def get_correct_button_index(self):
        correct_answer = self.questions[self.current_question_index]["correct_answer"]
        for i in range(4):
            if self.radio_buttons[i].cget("value") == correct_answer:
                return i

    def next_question(self):
        for radio_button in self.radio_buttons:
            radio_button.config(fg="black", bg=self.background_label.cget("bg"))
        self.current_question_index += 1
        self.radio_var.set(None)
        self.next_button.state(["disabled"])
        self.root.after_idle(self.update_question)

    def button_release(self, event):
        if event.widget == self.next_button:
            self.next_button.state(["!disabled"])
            self.root.focus_set()

    def show_result(self):
        messagebox.showinfo("Результат", f"Ваш счет: {self.score} из {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = HTMLTEST(root)
    root.mainloop()