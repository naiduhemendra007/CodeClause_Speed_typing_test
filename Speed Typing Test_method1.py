### Program for making a Speed Typing Test in Python in python by using tkinter/ GUI (Method 1) ###
### PROGRAM MADE BY HEMENDRA NAIDU ###
from tkinter import * # importing all the functions from tkinter(GUI Library)
import time


class TypeTest:

    def __init__(self):
        self.start_time = time.time()
        self.timer = time.time() 
        #these are the words which you have to type as fast as you can
        self.words = ['apple', 'pear', 'cucumber', 'banana', 'pineapple', 'orange', 'melon', 'dragonfruit', 'watermelon',
                  'jackfruit', 'mango', 'tomato', 'avocado', 'duran'] 
        self.correct_words = 0

    # Start countdown timer and generate words
    def start(self):
        for i in range(3, 0, -1):
            timer_text.config(text=i)
            window.update()
            time.sleep(1)
        timer_text.config(text='Type!')
        text.config(text=self.words)
        self.start_time = time.time()

    # Compare user input with list of words and calculate words typed per minute
    def compare(self, event):
        text.config(text='')
        word_list = self.words
        user_words = user_text_entry.get()
        user_list = user_words.split()
        for word in word_list:
            for i in user_list:
                if i == word:
                    self.correct_words += 1
        user_text_entry.delete(0, END)

        end_time = time.time()
        total_time = round(end_time - self.start_time)
        words_per_minute = round((self.correct_words / total_time) * 100)
        timer_text.config(text=f'{words_per_minute}wpm!')
        self.correct_words = 0


session = TypeTest()

window = Tk()
window.title("TypingSpeedTest9000")
window.config(padx=50, pady=50)
window.geometry("900x600")

# Words and user text input
text = Label(window, height=4, width=100)
text.grid(row=2, column=1, pady=30)
user_entry_label = Label(window, text='Type here: ')
user_entry_label.grid(row=3, column=1)
user_text_entry = Entry(window, width=80)
user_text_entry.grid(row=4, column=1, columnspan=2)

# Countdown timer
timer_text = Label(window, width=7, font=('Courier', 44))
timer_text.grid(row=1, column=1)


# Keybindings and Buttons
window.bind('<Return>', session.compare)
button = Button(window, text="Submit", command=session.compare)
button.grid(row=5, column=1)
start_button = Button(window, pady=10, text="Click to Start", command=lambda: session.start())
start_button.grid(row=6, column=1)




window.mainloop()