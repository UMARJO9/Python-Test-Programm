import tkinter as tk
from tkinter import messagebox, ttk
import random
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle


class CSSTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест по CSS")
        self.root.geometry("620x550")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("plastik")

        self.background_image = Image.open("BackgroundTestCSS.jpg")
        self.background_image = self.background_image.resize((620, 550))
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.questions = [
            {
                "question": "Как изменить цвет текста в CSS?",
                "options": ["color: #FF0000;", "text-color: red;", "style-color: #00FF00;", "rgb(255, 0, 0);"],
                "correct_answer": "color: #FF0000;"
            },
            {
                "question": "Как создать внешнюю таблицу стилей в HTML?",
                "options": ["<style>...</style>", "<css>...</css>", "<link rel=\"stylesheet\" href=\"styles.css\">",
                            "<script src=\"styles.js\"></script>"],
                "correct_answer": "<link rel=\"stylesheet\" href=\"styles.css\">"
            },
            {
                "question": "Как установить полужирное начертание текста в CSS?",
                "options": ["font-weight: normal;", "text-decoration: bold;", "font-weight: bold;", "style: bold;"],
                "correct_answer": "font-weight: bold;"
            },
            {
                "question": "Как изменить размер шрифта в CSS?",
                "options": ["font-size: 12px;", "text-size: medium;", "size: 14px;", "font-height: 1.2;"],
                "correct_answer": "font-size: 12px;"
            },
            {
                "question": "Как установить фоновый цвет элемента в CSS?",
                "options": ["background-color: #FFFF00;", "color: background #FFFFFF;", "bg-color: #FF0000;",
                            "background: red;"],
                "correct_answer": "background-color: #FFFF00;"
            },
            {
                "question": "Как управлять отступами в CSS?",
                "options": ["padding: 10px;", "margin: 5px;", "spacing: 8px;", "indent: 15px;"],
                "correct_answer": "margin: 5px;"
            },
            {
                "question": "Как изменить форму краев блока в CSS?",
                "options": ["border-shape: round;", "edge-style: curved;", "border-radius: 8px;", "outline: circle;"],
                "correct_answer": "border-radius: 8px;"
            },
            {
                "question": "Как скрыть элемент с использованием CSS?",
                "options": ["display: none;", "visibility: hidden;", "opacity: 0;", "hidden: true;"],
                "correct_answer": "display: none;"
            },
            {
                "question": "Как изменить выравнивание текста в CSS?",
                "options": ["text-align: center;", "align: middle;", "text-position: center;", "alignment: middle;"],
                "correct_answer": "text-align: center;"
            },
            {
                "question": "Как добавить тень к блоку в CSS?",
                "options": ["shadow: 2px 2px 2px #888888;", "box-shadow: 4px 4px 4px #000000;",
                            "text-shadow: 1px 1px 1px #333333;", "darkness: 3px 3px 3px #555555;"],
                "correct_answer": "box-shadow: 4px 4px 4px #000000;"
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
    quiz = CSSTest(root)
    root.mainloop()
