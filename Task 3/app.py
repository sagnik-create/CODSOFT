import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained VGG16 model + higher level layers
model = VGG16(weights='imagenet')

# Load the image file, resizing it to 224x224 pixels (required input size for VGG16)
img_path = '/blue-peafowl-tail-Indian-peacock-courtship-displays.webp'  # replace with your image path
img = image.load_img(img_path, target_size=(224, 224))

# Convert the image to a numpy array
img_array = image.img_to_array(img)

# Add an extra dimension for batch size (Keras models expect a batch dimension)
img_array = np.expand_dims(img_array, axis=0)

# Preprocess the image to match the input format the model expects
img_array = preprocess_input(img_array)

# Make predictions
predictions = model.predict(img_array)

# Decode the predictions into human-readable labels
decoded_predictions = decode_predictions(predictions, top=5)[0]

# Print the top 5 predictions
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")

# Plot the image
plt.imshow(img)
plt.axis('off')
plt.show()