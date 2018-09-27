import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
if len(sys.argv) >= 3:
    cascPath = sys.argv[2]
else:
    cascPath = "haarcascade_frontalface_default.xml"

print(cascPath)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

my_list = [33, 34, 35]

i = 1.01
while i <= 1.05:
    n = 1
    while n <= 6:
        f = 10
        while f <= 15:
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=i,
                minNeighbors=n,
                minSize=(f, f),
            )

            print("Found {0} faces! scaleFactor {1} minNeighbors {2} minSize ({3},{3})".format(len(faces), i, n, f))
            imagea = cv2.imread(imagePath)
            # if len(faces) in my_list:
            for (x, y, w, h) in faces:
                cv2.rectangle(imagea, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.imshow("Faces found", imagea)
            cv2.waitKey(0)
            f = f + 1
        n = n + 1
    i = i + 0.01
