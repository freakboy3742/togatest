import toga
from colosseum import CSS


class Example(toga.App):
    def load_page(self, widget):
        print("Load URL", self.url_input.value)
        self.webview.url = self.url_input.value

    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        self.url_input = toga.TextInput(initial='http://pybee.org', placeholder='url...')
        self.webview = toga.WebView(style=CSS(flex=1))

        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        toga.Button('Go', on_press=self.load_page, style=CSS(width=50))
                    ],
                    style=CSS(flex_direction='row', padding=5)
                ),
                self.webview,
            ],
            style=CSS(flex_direction='column')
        )

        self.main_window.title = self.name
        self.main_window.content = box

        # Show the main window
        self.main_window.show()
