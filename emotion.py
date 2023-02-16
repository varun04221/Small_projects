import cv2
from deepface import DeepFace
from PIL import Image

def imotion(image):
    apple=cv2.imread(image)
    print("Processing...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    emo=DeepFace.analyze(apple)
    return (emo[0]["dominant_emotion"])

def image():
    print("Please be ready for your picture")
    choice = input("Press any key when you are ready:")
    if choice == "" or choice != "":
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('temp_Emotion.png', image)
        img_png = Image.open('temp_Emotion.png')
        img_png.save('Emotion.jpg')
        del(camera)
        return "Emotion.jpg"

