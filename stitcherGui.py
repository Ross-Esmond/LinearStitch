import twodstitcher
import numpy as np
import os
import tkinter
from tkinter import filedialog
from stitcher import Stitcher
import _thread

class StitcherGUI:

	fileList = None;
	columnList = None;
	finishedFiles = None;
	readyToTerminate = False;
	progress = 0;

	def shorten_filename(self,filename):
		f = os.path.split(filename)[1]
		return "%s~%s" % (f[:3], f[-16:]) if len(f) > 19 else f

	def __init__(self, master):
		self.master = master
		master.title("Stitcher")
		self.outputFile = None
		self.browse_button = tkinter.Button(master, text="Select Files", command=self.browseFiles)
		self.browse_button.grid(row=0)

		self.save_file = tkinter.Button(master, text="Output File", command=self.saveFile)
		self.save_file.grid(row=1)

		self.maskImages = tkinter.BooleanVar()
		self.maskImages.set(0);
		self.mask_button = tkinter.Checkbutton(master, text="Mask Images", onvalue=1, offvalue=0,variable=self.maskImages)
		self.mask_button.grid(row=5)


		self.file_label_text = tkinter.StringVar()
		self.file_label_text.set(self.outputFile)
		self.file_label = tkinter.Label(master, textvariable=self.file_label_text)
		self.label = tkinter.Label(master, text="Output File:")
		self.label.grid(row=2, column=0)
		self.file_label.grid(row=2, column=1)


		self.stitch = tkinter.Button(master, text="Stitch", command=self.stitch)
		self.stitch.grid(row=3, column=1)

		self.progressText = tkinter.IntVar()
		self.progressText.set(self.progress)
		
		tkinter.Label(master, text="Progress :").grid(row=4,column=0)
		self.progress_label = tkinter.Label(master, textvariable=self.progressText)
		self.progress_label.grid(row=4, column=1)
		
	def browseFiles(self):
		# Tk().withdraw()
		files = filedialog.askopenfilenames(filetypes = (("JPEG", "*.jpeg"),("JPEG", "*.jpg")
														 ,("PNG", "*.png")
														 ,("All files", "*.*") ))
		parentName = os.path.split(os.path.dirname(files[0]))[1]
		self.outputFile = os.path.join(os.path.dirname(files[0]),parentName + ".tiff")
		self.file_label_text.set(parentName + ".tiff")
		self.fileList = root.tk.splitlist(files)


	def saveFile(self):
		# Tk().withdraw()
		self.outputFile = filedialog.asksaveasfilename(filetypes=[("TIFF", ".tiff")], title="Select Output File")
		self.file_label_text.set(self.shorten_filename(self.outputFile))

	def stitch(self):
		stitcherHandler = Stitcher()
		print(self.fileList)
		print(self.outputFile);
		if(self.outputFile is None):
			exit()

		parentName = os.path.split(os.path.dirname(self.fileList[0]))[1]
		outputFile = os.path.join(os.path.dirname(self.fileList[0]),parentName + str(len(self.fileList)) + ".tiff")
		self.finishedFiles = []
		self.finishedFiles.append(outputFile)

		_thread.start_new_thread(stitcherHandler.stitchFileList, (self.fileList, outputFile,self.progressCallback,self.maskImages.get()))

	def progressCallback(self, status, progress):
		self.progressText.set(progress);


root = tkinter.Tk()
root.geometry('{}x{}'.format(400, 200))
my_gui = StitcherGUI(root)
root.mainloop()