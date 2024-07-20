import cv2

def detect_faces_haar(image_path):
    # Load the pre-trained Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_faces_haar('path_to_image.jpg')


import dlib
from skimage import io

def detect_faces_dlib(image_path):
    detector = dlib.get_frontal_face_detector()

    # Load the image
    image = io.imread(image_path)

    # Detect faces
    detected_faces = detector(image, 1)

    # Draw rectangles around faces
    for i, face_rect in enumerate(detected_faces):
        left, top, right, bottom = face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the output
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_faces_dlib('path_to_image.jpg')


import face_recognition

def recognize_faces(image_path, known_faces_dir):
    # Load the image to be recognized
    unknown_image = face_recognition.load_image_file(image_path)

    # Detect faces and get encodings
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)

    # Load known faces
    known_face_encodings = []
    known_face_names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
            encodings = face_recognition.face_encodings(img)
            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])

    # Compare faces
    for unknown_face_encoding in unknown_face_encodings:
        results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
        name = "Unknown"
        if True in results:
            first_match_index = results.index(True)
            name = known_face_names[first_match_index]
        print(f"Found {name} in the image!")

recognize_faces('path_to_image.jpg', 'path_to_known_faces_directory')


import torch
import torchvision.transforms as transforms
from PIL import Image
from insightface import iresnet100, ArcFace

def arcface_recognition(image_path, known_faces_dir):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = iresnet100(pretrained=True).to(device)
    model.eval()

    arcface = ArcFace().to(device)

    transform = transforms.Compose([
        transforms.Resize((112, 112)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    # Load and preprocess the image to be recognized
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)

    # Get the face embedding
    with torch.no_grad():
        embedding = model(image)

    # Load and preprocess known faces
    known_face_embeddings = []
    known_face_names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(os.path.join(known_faces_dir, filename)).convert('RGB')
            img = transform(img).unsqueeze(0).to(device)
            with torch.no_grad():
                known_face_embeddings.append(model(img))
            known_face_names.append(os.path.splitext(filename)[0])

    # Compare faces
    distances = [(name, torch.dist(embedding, known_embedding)) for name, known_embedding in zip(known_face_names, known_face_embeddings)]
    distances.sort(key=lambda x: x[1])
    print(f"Found {distances[0][0]} in the image with distance {distances[0][1]}!")

arcface_recognition('path_to_image.jpg', 'path_to_known_faces_directory')
