import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests

kivy.require('2.0.0')


class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Label to display fetched data
        self.label = Label(text="Press a button to fetch data", size_hint=(1, 0.4))
        self.layout.add_widget(self.label)

        # Button 1 - Fetch Data from Endpoint 1
        self.button1 = Button(text="Fetch Data 1", size_hint=(1, 0.2))
        self.button1.bind(on_press=self.fetch_data1)
        self.layout.add_widget(self.button1)

        # Button 2 - Fetch Data from Endpoint 2
        self.button2 = Button(text="Fetch Data 2", size_hint=(1, 0.2))
        self.button2.bind(on_press=self.fetch_data2)
        self.layout.add_widget(self.button2)

        return self.layout

    def fetch_data1(self, instance):
        """Fetch data from the first endpoint."""
        try:
            response = requests.get("http://127.0.0.1:8000/api/data1/")  # Replace with the actual API URL
            if response.status_code == 200:
                data = response.json()
                self.label.text = f"Data 1:\nMessage: {data['message']}\nStatus: {data['status']}"
            else:
                self.label.text = "Failed to fetch Data 1."
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def fetch_data2(self, instance):
        """Fetch data from the second endpoint."""
        try:
            response = requests.get("http://127.0.0.1:8000/api/data2/")  # Replace with the actual API URL
            if response.status_code == 200:
                data = response.json()
                self.label.text = f"Data 2:\nName: {data['name']}\nValue: {data['value']}"
            else:
                self.label.text = "Failed to fetch Data 2."
        except Exception as e:
            self.label.text = f"Error: {str(e)}"


if __name__ == '__main__':
    MyApp().run()

