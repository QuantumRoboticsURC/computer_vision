
import numpy as np
import time
import cv2
import math
from ultralytics import YOLO



class Aruco():
	def __init__(self):
		self.ARUCO_DICT = {
					"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
					"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
					"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
					"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
					"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
					"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
					"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
					"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
					"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
					"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
					"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
					"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
					"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
					"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
					"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
					"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
					"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
					"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
					"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
					"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
					"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
				}
		self.aruco_type = "DICT_4X4_50"

		self.arucoDict = cv2.aruco.getPredefinedDictionary(self.ARUCO_DICT[self.aruco_type])


		self.arucoParams = cv2.aruco.DetectorParameters()
	
	def aruco_display(self,corners, ids, rejected, image):
		cX, cY = None, None
		if len(corners) > 0:
			ids = ids.flatten()
			for (markerCorner, markerID) in zip(corners, ids):
				
				corners = markerCorner.reshape((4, 2))
				(topLeft, topRight, bottomRight, bottomLeft) = corners

				topRight = (int(topRight[0]), int(topRight[1]))
				bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
				bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
				topLeft = (int(topLeft[0]), int(topLeft[1]))
				cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
				cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
				cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
				cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
				cX = int((topLeft[0] + bottomRight[0]) / 2.0)
				cY = int((topLeft[1] + bottomRight[1]) / 2.0)
				cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
				cv2.putText(image, str(markerID),(topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
					0.5, (0, 255, 0), 2)
		 
		return image,cX,cY

	def aruco_detect(self,frame):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		corners, ids, rejected = cv2.aruco.detectMarkers(image=gray,dictionary=self.arucoDict,parameters=self.arucoParams)
		frame,x,y = self.aruco_display(corners, ids, rejected, frame)
		return frame,x,y

class Orange():
	def __init__(self):
		self.saturation_threshold = 50


	def contornos(self,frame):

		# Convertir el fotograma al espacio de color HSV
		frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		saturation = frame_hsv[:,:,1]
		saturation_normalized = cv2.normalize(saturation,None,0,100,cv2.NORM_MINMAX)

		# Definir los umbrales de color naranja en el espacio de color HSV
		lower_orange = np.array([5, 130, 160])
		upper_orange = np.array([22, 255, 255])

		# Crear una máscara para detectar objetos de color naranja
		mask1 = cv2.inRange(frame_hsv, lower_orange, upper_orange)
		mask2 = cv2.inRange(saturation_normalized,self.saturation_threshold,100)
		combined_mask = cv2.bitwise_and(mask1,mask2)

		# Aplicar Adaptive Thresholding
		thresh = cv2.adaptiveThreshold(combined_mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

		# Aplicar operaciones morfológicas para eliminar el ruido
		thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

		# Encontrar contornos en la máscara
		contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
				
		return contours

	def orange_display(self, contours, image):
		cx, cy = None, None
		if contours:
			
			for (idx, contour) in enumerate(contours):
				x, y, w, h = cv2.boundingRect(contour)

				corners = np.array([[x, y], [x + w, y], [x + w, y + h], [x, y + h]], dtype = np.int32)
				corners = corners.reshape((-1, 1, 2))

				cv2.polylines(image, [corners], isClosed=True, color=(0, 255, 0), thickness=2)

				cx = int(x + w / 2.0)
				cy = int(y + h / 2.0)

				self.x = cx
				self.y = cy

		return image,cx,cy

	def orange_detect(self,frame):
		contours = self.contornos(frame)
		frame,x,y = self.orange_display(contours, frame)
		return frame,x,y

class Bottle():
	def __init__(self):
		self.saturation_threshold = 50
		self.model = YOLO("yolov8n.pt")

	def bottle_display(self, frame, bboxes, classes):
		cx, cy = None, None
		if bboxes.any():

			for bbox, cls in zip(bboxes, classes):
				if cls == 39:
					(x, y, x2, y2) = bbox

					# Dibujar un rectángulo alrededor de la botella
					cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)

					cv2.putText(frame, 'Botella', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

					cx = int(x + (x2 - x) / 2.0)
					cy = int(y + (y2 - y) / 2.0)
		return frame,cx,cy

	def bottle_detect(self,image):
		results = self.model(image)

		result = results[0]
		bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
		classes = np.array(result.boxes.cls.cpu(), dtype="int")

		detected_bottle,x,y = self.bottle_display(image, bboxes, classes)
		return detected_bottle,x,y