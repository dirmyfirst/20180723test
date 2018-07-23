#-*- coding:utf-8 -*-
from __future__ import print_function
from pandas import read_csv
from pandas import ExcelWriter
from tkinter import Tk
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import filedialog
from tkinter import messagebox
import os


class Tkview(object):

	def __init__(self, master):
		self.root = master
		
		self.createPage() 

	def createPage(self):
		Label(self.root, text="打开文件目录：").grid(row=0,  column=0)
		self.pathdb = StringVar()
		Entry(self.root, textvariable = self.pathdb, width=50).grid(row=0, column=1)
		Button(self.root, text='打开目录', command=self.Path).grid(row=0, column=2)
		Button(self.root, text='运行', width=15, command=self.run).grid(row=1, column=1, columnspan=2)

	def Path(self):
		path = filedialog.askdirectory()
		print(path)
		self.pathdb.set(path)
		self.temp = path

	def fileLs(self):
		curdir = os.path.abspath(self.temp)
		files = os.listdir(self.temp)
		L = []
		for fil in files:
			if os.path.splitext(fil)[1] == '.csv':
				L.append(os.path.join(curdir, fil))
		print(L)
		self.L = L

	def read(self, file_address, sep=','):
		directory_name, file_name = os.path.split(file_address)
		fileName, suffix = os.path.splitext(file_name)
		df = read_csv(file_address,
			sep = sep,
			header = 0,
			encoding = 'gbk',
			engine = 'python',
			)
		xlsxName = fileName + '.xlsx'
		write = ExcelWriter(xlsxName)
		df.to_excel(write, index=None, header=1)
		write.save()

	def run(self):
		self.fileLs()
		for f in self.L:
			self.read(f, sep=',')

		messagebox.showinfo('提示', '处理完成')


def main():
	root = Tk()
	root.title("批量文件转换工具")
	root.geometry('580x200')
	Tkview(root)
	root.mainloop()

if __name__ == '__main__':
	main()

