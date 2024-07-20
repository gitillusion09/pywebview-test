from threading import Thread
import datetime
import time

class Renderer():
	def __init__(self):
		self.py_window = None

		self.repaint_thread_active = False
		self.repaint_thread = Thread(target = self.render, args=())
		
	def set_window(self, window):
		self.py_window = window

	def release_renderer(self):
		self.disable_rendering()

	def enable_rendering(self):
		self.repaint_thread_active = True
		self.repaint_thread.start()  # Start the repaint method in another thread

	def disable_rendering(self):
		if (self.repaint_thread_active):
			self.repaint_thread_active = False  # Stop repaint thread
			self.repaint_thread.join()

	def render(self):
		while self.repaint_thread_active:
			self.update_ui(datetime.datetime.now())
			time.sleep(0.005)	# Pause the execution to avoid cpu overloading

	def update_ui(self, message):
		self.py_window.evaluate_js(("""DisplayInfo("{message}");""").format(message=message))  