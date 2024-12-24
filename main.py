import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

class DjangoHomePage(BoxLayout):
    SERVER_URL = "http://100.84.160.153:8000"  # Replace with your Django server URL

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        # Button to Fetch Home Page
        fetch_button = Button(text="Fetch Home Page", size_hint=(1, 0.2))
        fetch_button.bind(on_press=self.fetch_home_page)
        self.add_widget(fetch_button)

        # Scrollable Area for Content Display
        self.content_scroll = ScrollView(size_hint=(1, 0.8))
        self.content_label = Label(text="Home Page Content will appear here.", size_hint_y=None, valign="top", halign="left")
        self.content_label.bind(texture_size=self.content_label.setter('size'))
        self.content_scroll.add_widget(self.content_label)
        self.add_widget(self.content_scroll)

    def fetch_home_page(self, instance):
        try:
            # Sending request to Django server
            response = requests.get(self.SERVER_URL)
            if response.status_code == 200:
                self.content_label.text = response.text  # Display raw HTML content
            else:
                self.show_popup("Error", f"Failed to fetch data. Status code: {response.status_code}")
        except Exception as e:
            self.show_popup("Error", f"Unable to connect to server: {e}")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

class MyApp(App):
    def build(self):
        return DjangoHomePage()

if __name__ == "__main__":
    MyApp().run()

