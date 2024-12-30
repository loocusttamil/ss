import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import requests
import os

kivy.require('2.0.0')


class MyApp(App):
    def build(self):
        # Path to the background image in the assets folder
        image_path = os.path.join("assets", "background.jpg")

        # Main layout with background
        root = FloatLayout()

        # Add HD background image
        background = Image(source=image_path, allow_stretch=True, keep_ratio=False)
        root.add_widget(background)

        # Foreground layout for label and buttons
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Label to display fetched data
        self.label = Label(text="Press a button to fetch data", size_hint=(1, 0.6), color=(1, 1, 1, 1))  # White text
        layout.add_widget(self.label)

        # Horizontal layout for buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint=(1, 0.1))

        # Button 1 - Fetch Data from Endpoint 1
        self.button1 = Button(text="Data 1", size_hint=(0.3, 1), background_color=(0, 0, 0, 0.5))  # Transparent background
        self.button1.bind(on_press=self.fetch_data1)
        button_layout.add_widget(self.button1)

        # Button 2 - Fetch Data from Endpoint 2
        self.button2 = Button(text="Data 2", size_hint=(0.3, 1), background_color=(0, 0, 0, 0.5))  # Transparent background
        self.button2.bind(on_press=self.fetch_data2)
        button_layout.add_widget(self.button2)

        # Add button layout to the main layout
        layout.add_widget(button_layout)

        # Add the foreground layout to the root layout
        root.add_widget(layout)

        return root

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

