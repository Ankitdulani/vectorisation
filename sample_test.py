import vectorizer
if __name__ == "__main__":

	import sys
	import cv2
	
	img = cv2.imread(sys.argv[1])

	algo = vectorizer.vectorizer()
	vectorised_img = algo.execute(img)

	print(vectorised_img.shape)
	cv2.imwrite("vectorization_result.svg",vectorised_img)