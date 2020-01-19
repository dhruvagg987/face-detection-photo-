import cv2
print("hello")
# print(img)
# resized=cv2.resize(img,(200,200))
face_cascade=cv2.CascadeClassifier("D:/haarcascade_frontalface_default.xml")
img = cv2.imread("C:/Users/Dhruv Agarwal/Desktop/machine learning/pic.jpg",1)
#reading image as gray scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img , scaleFactor = 1.05 , minNeighbors = 5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("tony",img)
cv2.waitKey(0)
cv2.destroyAllWindows()