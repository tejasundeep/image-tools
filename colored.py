import cv2
import numpy as np

# Load the pre-trained model and weights
net = cv2.dnn.readNetFromCaffe("weights/colorization_deploy_v2.prototxt", "weights/colorization_release_v2.caffemodel")
pts = np.load("weights/pts_in_hull.npy")
layer1, layer2 = net.getLayerId("class8_ab"), net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(layer1).blobs = [pts.astype("float32")]
net.getLayer(layer2).blobs = [np.full([1, 313], 2.606, dtype="float32")]

# Load the black and white image, convert to LAB color space, and resize
test_image = cv2.cvtColor(cv2.imread('black_and_white.png'), cv2.COLOR_BGR2RGB)
lab_image = cv2.cvtColor(test_image.astype("float32") / 255.0, cv2.COLOR_RGB2LAB)
resized = cv2.resize(lab_image, (224, 224))
L = cv2.split(resized)[0] - 50

# Use the model to predict the 'a' and 'b' channels of the image
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
ab = cv2.resize(ab, (test_image.shape[1], test_image.shape[0]))

# Combine the 'L', 'a', and 'b' channels and convert the image back to RGB
L = cv2.split(lab_image)[0]
LAB_colored = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
RGB_colored = cv2.cvtColor(LAB_colored, cv2.COLOR_LAB2RGB)
RGB_colored = np.clip(RGB_colored, 0, 1)
RGB_colored = (255 * RGB_colored).astype("uint8")
BGR_colored = cv2.cvtColor(RGB_colored, cv2.COLOR_RGB2BGR)

# Output the colored image
cv2.imwrite("colored.png", BGR_colored)