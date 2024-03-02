import tkinter as tk
from tkinter import messagebox, ttk
import random
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle


class JavaScriptTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест по JavaScript")
        self.root.geometry("620x550")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("plastik")

        self.background_image = Image.open("BackgroundTestJavaScript.jpg")
        self.background_image = self.background_image.resize((620, 550))
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.questions = [
            {
                "question": "Как объявить переменную в JavaScript?",
                "options": ["var x;", "variable x;", "x = 5;", "int x;"],
                "correct_answer": "var x;"
            },
            {
                "question": "Что такое RESTful API?",
                "options": [
                    "Тип API для взаимодействия с базой данных.",
                    "Архитектурный стиль для построения веб-сервисов.",
                    "Библиотека для обработки изображений в программировании.",
                    "Методология тестирования программного обеспечения."
                ],
                "correct_answer": "Архитектурный стиль для построения веб-сервисов."
            },
            {
                "question": "Как создать функцию в JavaScript?",
                "options": ["function myFunction() {}", "create function myFunction() {}",
                            "new function myFunction() {}", "function: myFunction() {}"],
                "correct_answer": "function myFunction() {}"
            },
            {
                "question": "Как добавить элемент в конец массива в JavaScript?",
                "options": ["arr.add(element);", "arr.insertLast(element);", "arr.push(element);",
                            "arr.append(element);"],
                "correct_answer": "arr.push(element);"
            },
            {
                "question": "Как получить случайное число от 1 до 10 в JavaScript?",
                "options": ["Math.random(1, 10);", "random(1, 10);", "Math.floor(Math.random() * 10) + 1;",
                            "randomNumber(1, 10);"],
                "correct_answer": "Math.floor(Math.random() * 10) + 1;"
            },
            {
                "question": "Как обратиться к элементу с id 'myElement' в JavaScript?",
                "options": ["getElement('myElement');", "document.getElementByName('myElement');",
                            "document.getElementById('myElement');", "$('#myElement');"],
                "correct_answer": "document.getElementById('myElement');"
            },
            {
                "question": "Что такое IIFE в JavaScript?",
                "options": [
                    "Это сокращенное название функции If-Else.",
                    "Это аббревиатура от Immediately Invoked Function Expression.",
                    "Это специальный оператор для создания объектов.",
                    "Это новый стандарт синтаксиса для объявления функций."
                ],
                "correct_answer": "Это аббревиатура от Immediately Invoked Function Expression."
            },
            {
                "question": "Как обработать клик на кнопке с id 'myButton' в JavaScript?",
                "options": ["$('#myButton').onClick();", "document.getElementByName('myButton').clickHandler();",
                            "document.getElementById('myButton').addEventListener('click', clickHandler);",
                            "button('myButton').click();"],
                "correct_answer": "document.getElementById('myButton').addEventListener('click', clickHandler);"
            },
            {
                "question": "Как создать объект в JavaScript?",
                "options": ["new Object();", "{};", "create.object();", "Object.create();"],
                "correct_answer": "{};"
            },
            {
                "question": "Как прервать выполнение цикла в JavaScript?",
                "options": ["break;", "continue;", "exit;", "stop;"],
                "correct_answer": "break;"
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
    quiz = JavaScriptTest(root)
    root.mainloop()
