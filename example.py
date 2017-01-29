import toga


class Example(toga.App):
    def button_handler(self, widget):
        print("Hello,", self.text.value())

    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        box = toga.Box()

        self.text = toga.TextInput(placeholder='something...')
        box.add(self.text)

        button = toga.Button('Hello world', on_press=self.button_handler)

        button.style.set(margin=50)

        box.add(button)

        self.main_window.title = self.name
        self.main_window.content = box

        # Show the main window
        self.main_window.show()
