import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("handwritten_digit_model.keras")


class DigitRecognizer:

    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognizer")

        # Drawing canvas
        self.canvas = tk.Canvas(
            root,
            width=280,
            height=280,
            bg="black"
        )
        self.canvas.pack(pady=10)

        # Image used by the model
        self.image = Image.new("L", (280, 280), "black")
        self.draw = ImageDraw.Draw(self.image)

        # Mouse drawing
        self.canvas.bind("<B1-Motion>", self.draw_digit)

        # Predict button
        tk.Button(
            root,
            text="Predict",
            command=self.predict
        ).pack(pady=5)

        # Clear button
        tk.Button(
            root,
            text="Clear",
            command=self.clear
        ).pack(pady=5)

        # Result
        self.result = tk.Label(
            root,
            text="Draw a digit (0-9)",
            font=("Arial", 18)
        )
        self.result.pack(pady=10)

    def draw_digit(self, event):
        x = event.x
        y = event.y

        # Draw on canvas
        self.canvas.create_oval(
            x - 10, y - 10,
            x + 10, y + 10,
            fill="white",
            outline="white"
        )

        # Draw on image
        self.draw.ellipse(
            (x - 10, y - 10,
             x + 10, y + 10),
            fill="white"
        )

    def predict(self):

        # Resize to MNIST format
        img = self.image.resize((28, 28))

        # Convert to NumPy
        img = np.array(img)

        # Normalize
        img = img / 255.0

        # CNN input shape
        img = img.reshape(1, 28, 28, 1)

        # Prediction
        prediction = model.predict(img, verbose=0)

        digit = np.argmax(prediction)
        confidence = prediction[0][digit] * 100

        self.result.config(
            text=f"Prediction: {digit}\n"
                 f"Confidence: {confidence:.2f}%"
        )

    def clear(self):

        self.canvas.delete("all")

        self.image = Image.new(
            "L",
            (280, 280),
            "black"
        )

        self.draw = ImageDraw.Draw(self.image)

        self.result.config(
            text="Draw a digit (0-9)"
        )


# Start application
root = tk.Tk()

app = DigitRecognizer(root)

root.mainloop()