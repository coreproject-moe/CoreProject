from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from webview import WebView


class BrowserApp(App):
    def build(self):
        self.browser = None
        b1 = Button(
            text="Tap for Figma (HomePage | Desktop)",
            on_press=self.view_homepage_desktop,
        )
        b2 = Button(
            text="Tap for Figma (HomePage | Laptop/Tablets)",
            on_press=self.view_homepage_laptop_or_tablets,
        )
        b3 = Button(
            text="Tap for Figma (HomePage | Mobile)",
            on_press=self.view_homepage_mobile,
        )

        self.label = Label(text="")
        box = BoxLayout(orientation="vertical")
        box.add_widget(b1)
        box.add_widget(b2)
        box.add_widget(b3)
        box.add_widget(self.label)
        return box

    def view_homepage_desktop(self, b):
        self.browser = WebView(
            "https://www.figma.com/proto/tNUUtsk20ltOrQICdEoggG/Core-Project?page-id=587%3A1423&node-id=690%3A686&viewport=552%2C423%2C0.21&scaling=contain&starting-point-node-id=690%3A686&show-proto-sidebar=1",
            enable_javascript=True,
            enable_zoom=False,
        )

    def view_homepage_laptop_or_tablets(self, b):
        self.browser = WebView(
            "https://www.figma.com/proto/tNUUtsk20ltOrQICdEoggG/Core-Project?page-id=587%3A1423&node-id=719%3A1262&viewport=552%2C423%2C0.21&scaling=contain&starting-point-node-id=719%3A1262&show-proto-sidebar=1",
            enable_javascript=True,
            enable_zoom=False,
        )

    def view_homepage_mobile(self, b):
        self.browser = WebView(
            "https://www.figma.com/proto/tNUUtsk20ltOrQICdEoggG/Core-Project?page-id=587%3A1423&node-id=719%3A2421&viewport=552%2C423%2C0.21&scaling=contain&starting-point-node-id=719%3A2421&show-proto-sidebar=1",
            enable_javascript=True,
            enable_zoom=False,
        )

    def on_pause(self):
        if self.browser:
            self.browser.pause()
        return True

    def on_resume(self):
        if self.browser:
            self.browser.resume()


BrowserApp().run()
