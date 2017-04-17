import toga
from colosseum import CSS


class Example(toga.App):

    ### TUTORIAL 2 - F2C

    def calculate(self, widget):
        try:
            self.c_input.value = (float(self.f_input.value) - 32.0) * 5.0 / 9.0
        except ValueError:
            self.c_input.value = '???'

    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        c_box = toga.Box()
        f_box = toga.Box()
        box = toga.Box()

        self.c_input = toga.TextInput(readonly=True)
        self.f_input = toga.TextInput()

        c_label = toga.Label('Celcius', alignment=toga.LEFT_ALIGNED)
        f_label = toga.Label('Fahrenheit', alignment=toga.LEFT_ALIGNED)
        join_label = toga.Label('is equivalent to', alignment=toga.RIGHT_ALIGNED)

        button = toga.Button('Calculate', on_press=self.calculate)

        f_box.add(self.f_input)
        f_box.add(f_label)

        c_box.add(join_label)
        c_box.add(self.c_input)
        c_box.add(c_label)

        box.add(f_box)
        box.add(c_box)
        box.add(button)

        box.style.set(flex_direction='column', padding_top=10)
        f_box.style.set(flex_direction='row', margin=5)
        c_box.style.set(flex_direction='row', margin=5)

        self.c_input.style.set(flex=1)
        self.f_input.style.set(flex=1, margin_left=160)
        c_label.style.set(width=100, margin_left=10)
        f_label.style.set(width=100, margin_left=10)
        join_label.style.set(width=150, margin_right=10)
        button.style.set(margin_top=15)

        self.main_window.content = box

        # Show the main window
        self.main_window.show()

    ### TUTORIAL 3 - Web browser

    # def load_page(self, widget):
    #     print("Load URL", self.url_input.value)
    #     self.webview.url = self.url_input.value

    # def startup(self):
    #     self.main_window = toga.MainWindow(self.name)
    #     self.main_window.app = self

    #     self.url_input = toga.TextInput(initial='http://pybee.org', placeholder='url...')
    #     self.webview = toga.WebView(style=CSS(flex=1))

    #     box = toga.Box(
    #         children=[
    #             toga.Box(
    #                 children=[
    #                     self.url_input,
    #                     toga.Button('Go', on_press=self.load_page, style=CSS(width=50))
    #                 ],
    #                 style=CSS(flex_direction='row', padding=5)
    #             ),
    #             self.webview,
    #         ],
    #         style=CSS(flex_direction='column')
    #     )

    #     self.main_window.title = self.name

    #     self.main_window.content = box

    #     # Show the main window
    #     self.main_window.show()
