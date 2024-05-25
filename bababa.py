import cv2
import os
from PIL import Image

os.chdir('D:/Open CV/Lesson 6/photos')
path = 'D:/Open CV/Lesson 6/photos'

mean_width = 0
mean_height = 0

num_img = len(os.listdir('.'))
print('image:', num_img)

for file in os.listdir('.'):
    img = Image.open(os.path.join(path,file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height
mean_width = mean_width//num_img
mean_height = mean_height//num_img

print('wid',mean_width)
print('hei',mean_height)
for file in os.listdir('.'):
    img = Image.open(os.path.join(path,file))
    img2 = img.resize((mean_width,mean_height))
    img2.save(file, 'JPEG', quality = 100)
    print('resized image')
def woah():
    name = 'woah.avi'
    os.chdir('D:/Open CV/Lesson 6/photos')
    images = []
    for img in os.listdir('.'):
        images.append(img)
    print(images)
    frame = cv2.imread(os.path.join('.', images[0]))
    height, width, layer = frame.shape
    print('lay', frame.shape)
    video = cv2.VideoWriter(name, 0, 1, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join('.', image)))

    cv2.destroyAllWindows()
    video.release()

woah()