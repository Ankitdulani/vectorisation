class vectorizer:

	def __inti__():
		self.image

	def execute(self,image):
		# step for vectorisation
		self.get_marked_image()
		self.draw_boundaries()
		self.extract_boundaries()
		self.spline_fit_boundaries()
		self.write_svg_image()


	def get_marked_image(self):
		print("marking region")

	def draw_boundaries(self):
		print("drawing boundaries")

	def extract_boundaries(self):
		print("extracting boundaries")

	def spline_fit_boundaries(self):
		print("spline fittingh the curve")

	def write_svg_image(self):
		print("writing svg image")