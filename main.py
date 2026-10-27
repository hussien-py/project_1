from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
    

class BMICalculatorApp(App):
    def build(self):
        # Set the app window's background color (red, green, blue, opacity)
        Window.clearcolor = (0.06, 0.08, 0.12, 1)

        # Create a vertical layout to arrange widgets from top to bottom
        root = BoxLayout(
            orientation="vertical",
            padding=24,  # Space between the layout's edges and its contents
            spacing=14   # Space between widgets
        )

        # Add the app title
        root.add_widget(Label(
            text="BMI Calculator",
            font_size=28,
            bold=True,
            color=(0.92, 0.95, 1, 1),
            size_hint_y=None,  # Use a fixed height instead of automatic sizing
            height=60
        ))

        # Create a text field for the user's weight in kilograms
        self.weight_input = TextInput(
            hint_text="Weight in kg",
            input_filter="float",  # Allow numeric input, including decimals
            multiline=False,       
            size_hint_y=None,
            height=50,
            padding=12,
            background_color=(0.12, 0.15, 0.21, 1),
            foreground_color=(0.94, 0.96, 1, 1),  # Typed text color
            hint_text_color=(0.55, 0.60, 0.70, 1),
            cursor_color=(0.25, 0.85, 0.72, 1)
        )
        root.add_widget(self.weight_input)

        # Create a text field for the user's height in centimeters
        self.height_input = TextInput(
            hint_text="Height in cm",
            input_filter="float",
            multiline=False,
            size_hint_y=None,
            height=50,
            padding=12,
            background_normal="",
            background_active="",
            background_color=(0.12, 0.15, 0.21, 1),
            foreground_color=(0.94, 0.96, 1, 1),
            hint_text_color=(0.55, 0.60, 0.70, 1),
            cursor_color=(0.25, 0.85, 0.72, 1)
        )
        root.add_widget(self.height_input)

        # Display instructions or the calculated BMI result
        self.result = Label(
            text="Enter your weight and height",
            font_size=18,
            color=(0.72, 0.78, 0.88, 1)
        )
        root.add_widget(self.result)

        # Create the button the user presses to calculate BMI
        button = Button(
            text="Calculate BMI",
            size_hint_y=None,
            height=52,
            background_normal="",
            background_down="",
            background_color=(0.10, 0.72, 0.60, 1),
            color=(0.03, 0.10, 0.10, 1),
            font_size=16,
            bold=True
        )

        # Call calculate_bmi when the button is pressed
        button.bind(on_press=self.calculate_bmi)
        root.add_widget(button)

        # Return the root layout so Kivy can display it
        return root

    def calculate_bmi(self, *_):
        # Try to read the text fields and calculate BMI
        try:
            weight = float(self.weight_input.text)
            height_cm = float(self.height_input.text)

            # Reject zero or negative measurements
            if weight <= 0 or height_cm <= 0:
                raise ValueError

            # Convert height from centimeters to meters, then calculate BMI
            bmi = weight / ((height_cm / 100) ** 2)

            # Choose a category based on the BMI value
            if bmi < 18.5:
                category = "Below normal range"
            elif bmi < 25:
                category = "Normal range"
            elif bmi < 30:
                category = "Above normal range"
            else:
                category = "High BMI"

            # Show the BMI rounded to one decimal place and its category
            self.result.text = f"BMI: {bmi:.1f} — {category}"

        # Show an error message if the input is missing or invalid
        except ValueError:
            self.result.text = "Please enter valid weight and height."


# Run the app when this file is executed directly
if __name__ == "__main__":
    BMICalculatorApp().run()