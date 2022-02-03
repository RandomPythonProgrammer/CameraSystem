import cv2
import os
import time


def captureImage(name, captureFolder):
	camera = cv2.VideoCapture(0)

	ret, frame = camera.read()

	if ret:
		path = captureFolder + f"/{name}.png"
		cv2.imwrite(path, frame)
		camera.release()
		cv2.destroyAllWindows()


def main():
	rootFolderPath = f"C:/Users/{os.getlogin()}/Documents/LoginImages"
	folderPath = rootFolderPath + f"/{time.strftime('%T(%D)', time.localtime(time.time())).replace(':', '-').replace('/', '-')}"
	if not os.path.exists(rootFolderPath):
		os.mkdir(rootFolderPath)
	os.mkdir(folderPath)
	for i in range(3):
		captureImage("Capture"+str(i+1), folderPath)


if __name__ == '__main__':
	main()
