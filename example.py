
import toga


def button_handler(widget):
    print("Hello")


class Example(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        box = toga.Box()

        button = toga.Button('Hello world', on_press=button_handler)

        button.style.set(margin=50)

        box.add(button)

        self.main_window.title = self.name
        self.main_window.content = box

        # Show the main window
        self.main_window.show()
