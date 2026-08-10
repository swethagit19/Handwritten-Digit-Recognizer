# Handwritten Digit Recognizer

A handwritten digit recognition system built using a Convolutional Neural Network (CNN) and the MNIST dataset.

The project can recognize handwritten digits from 0 to 9. It also includes an interactive interface where users can draw a digit using the mouse and receive the model's prediction and confidence score.

## Features

- Trained using the MNIST handwritten digit dataset
- CNN-based image classification
- Image preprocessing and normalization
- Achieves high accuracy on the MNIST test dataset
- Interactive drawing interface
- Predicts digits from 0 to 9
- Displays prediction confidence
- Clear button to draw another digit

## Technologies Used

- Python 3.11
- TensorFlow / Keras
- NumPy
- Matplotlib
- Pillow
- Tkinter
- CNN (Convolutional Neural Network)

## Dataset

The project uses the **MNIST dataset**, which contains 70,000 grayscale images of handwritten digits.

- 60,000 training images
- 10,000 testing images
- Image size: 28 × 28 pixels
- Classes: 0–9

The dataset is automatically downloaded through TensorFlow/Keras.

## Model Architecture

The CNN consists of:

1. Convolutional Layer
2. Max Pooling Layer
3. Flatten Layer
4. Dense Layer with 128 neurons
5. Output Layer with 10 neurons

The output layer uses the Softmax activation function to calculate the probability of each digit.

## How It Works

### 1. Load Dataset

The MNIST dataset is loaded using TensorFlow/Keras.

### 2. Preprocess Images

Pixel values are normalized from:

`0–255`

to:

`0–1`

The images are then reshaped for CNN processing.

### 3. Train CNN

The CNN is trained for 5 epochs using the Adam optimizer.

### 4. Evaluate Model

The trained model is evaluated using the MNIST test dataset.

### 5. Draw Your Own Digit

The interactive application provides a drawing canvas.

The user can:

- Draw a digit using the mouse
- Click **Predict**
- View the predicted digit
- View the model's confidence
- Click **Clear** to try another digit

## Project Structure

```text
Handwritten-Digit-Recognizer/
│
├── digit_recognizer.py
├── requirements.txt
├── README.md
└── .gitignore