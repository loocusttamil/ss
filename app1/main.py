from kivy.app import App
from kivy.uix.button import Button
import os

class TermuxApp(App):
    def build(self):
        return Button(
            text="Run Termux Command",
            on_press=self.run_termux_command
        )

    def run_termux_command(self, instance):
        # Example: Running a Termux API command
        os.system("termux-toast 'Hello from Kivy!'")

if __name__ == "__main__":
    TermuxApp().run()