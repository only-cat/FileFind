#!/usr/bin/python3.5
# FileName : ff.py

import os
import sys
class FileFind:
	
	FilePath=""
	FileName=""
	FindStr=""
	Recursion=0;
	FileCount=0;	
	def ReadFind(self,fpath):
		cout=0;
		try:
			
			with open(fpath ,'rt') as handle:
				for ln in handle:
					if self.FindStr in  ln:
						cout+=1
					#print self.FindStr in ln , ln
		except IOError:
			print('ERROR:[' + fpath + ']Not Read File')	  
		except UnicodeDecodeError:
			#print("Error:["+fpath+"]未识别的文件编码")
			print 
		if(cout>0):
			print(self.FilePath+self.FileName)
			self.FileCount+=1
#				print self.FindStr in ln , ln				
		


	def CheckPath(self,path):
		os.chdir(path)
		for obj in os.listdir(os.curdir):
			fpath=os.getcwd()+os.sep+obj
			self.FileName=os.sep+obj
			self.FilePath=os.getcwd()
			if(os.path.isfile(fpath)):
				self.ReadFind(fpath) 
			
			if (self.Recursion==1):
				if os.path.isdir(obj):
					self.CheckPath(obj)
					os.chdir(os.pardir)
	
	def CheckFile(self,path):
		os.chdir(path)
		for obj in os.listdir(os.curdir):
			fpath=os.getcwd()+os.sep+self.FileName;
			self.FilePath=os.getcwd()
		
			if(os.path.isfile(fpath) and obj == self.FileName):
				self.ReadFind(fpath) 
			
			if (self.Recursion==1):
				if os.path.isdir(obj):
					self.CheckFile(obj)
					os.chdir(os.pardir)
				

	def __init__(self ,Path='', File='',Str=''):
		self.FilePath=Path
		self.FileName=File
		self.FindSte=Str
	
	def main(self):
		Path=""
		File=""
		Str=""
		flag=''
		for i in sys.argv:
			if i == 'p' or  i== '-p':
				flag='p'
				continue
			elif i== 'f' or  i == '-f':
				flag='f'	
				continue
			elif i=='s' or  i=='-s':
				flag='s'
				continue
			elif i=='r'  or  i == '-r':
				flag='r'
	
			if flag== 'p':
				Path=i.strip()
			elif flag=='f':
				File=i.strip()
			elif flag=='s':
				Str=i.strip()
			elif flag=='r':
				self.Recursion=1
			flag=''
			
		self.FileName=File
		self.FindStr=Str.strip()

		if(Path == ''):
			self.FilePath=os.getcwd()
		else:
			self.FilePath=Path
		

		
t=FileFind()
t.main()

print ("FindPath:"+t.FilePath+"\tFindName:" +t.FileName +"\tFindStr:"+t.FindStr )
print ('------------------------------------------------------------------------------')
if t.FileName =="":
	t.CheckPath(t.FilePath)
else:
	t.CheckFile(t.FilePath)	
		
print ('------------------------------------------------------------------------------')
print ('Found File Count Num:' , t.FileCount)



