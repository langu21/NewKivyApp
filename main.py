from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread

KV = """
ScreenManager:
    HomeScreen:
    ProductScreen:
    AboutScreen:
    ContactScreen:

<HomeScreen>:
    name: "home"
    BoxLayout:
        orientation: "vertical"
        padding: 12
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: "48dp"
            spacing: 8
            Button:
                text: "Home"
                on_release: root.manager.current = "home"
            Button:
                text: "Product"
                on_release: root.manager.current = "product"
            Button:
                text: "About"
                on_release: root.manager.current = "about"
            Button:
                text: "Contact"
                on_release: root.manager.current = "contact"

        Label:
            id: content
            text: root.display_text
            halign: "left"
            valign: "top"
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]

<ProductScreen>:
    name: "product"
    BoxLayout:
        orientation: "vertical"
        padding: 12
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: "48dp"
            spacing: 8
            Button:
                text: "Home"
                on_release: root.manager.current = "home"
            Button:
                text: "Product"
                on_release: root.manager.current = "product"
            Button:
                text: "About"
                on_release: root.manager.current = "about"
            Button:
                text: "Contact"
                on_release: root.manager.current = "contact"

        Label:
            id: product_content
            text: root.display_text
            halign: "left"
            valign: "top"
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]

<AboutScreen>:
    name: "about"
    BoxLayout:
        orientation: "vertical"
        padding: 12
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: "48dp"
            spacing: 8
            Button:
                text: "Home"
                on_release: root.manager.current = "home"
            Button:
                text: "Product"
                on_release: root.manager.current = "product"
            Button:
                text: "About"
                on_release: root.manager.current = "about"
            Button:
                text: "Contact"
                on_release: root.manager.current = "contact"

        Label:
            id: about_content
            text: root.display_text
            halign: "left"
            valign: "top"
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]

<ContactScreen>:
    name: "contact"
    BoxLayout:
        orientation: "vertical"
        padding: 12
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: "48dp"
            spacing: 8
            Button:
                text: "Home"
                on_release: root.manager.current = "home"
            Button:
                text: "Product"
                on_release: root.manager.current = "product"
            Button:
                text: "About"
                on_release: root.manager.current = "about"
            Button:
                text: "Contact"
                on_release: root.manager.current = "contact"

        Label:
            id: contact_content
            text: root.display_text
            halign: "left"
            valign: "top"
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]
"""

class HomeScreen(Screen):
    display_text = "Welcome to the Home Page!"

    @mainthread
    def _update_text(self, new_text):
        self.ids.content.text = new_text

class ProductScreen(Screen):
    display_text = "This is the Product Page. We sell amazing things!"

    @mainthread
    def _update_text(self, new_text):
        self.ids.product_content.text = new_text

class AboutScreen(Screen):
    display_text = "About Us: We are dedicated to making students' lives easier."

    @mainthread
    def _update_text(self, new_text):
        self.ids.about_content.text = new_text

class ContactScreen(Screen):
    display_text = "Contact Us: Email support@example.com"

    @mainthread
    def _update_text(self, new_text):
        self.ids.contact_content.text = new_text

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    MyApp().run()
