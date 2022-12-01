import pandas as pd
from openpyxl.styles.borders import Border, Side
from io import BytesIO
import shutil
import pathlib
import streamlit as st
import os.path

def oct_find(p,q,r):                                      
	if(p>0 and q>0 and r>0):    
		return 1
	elif(p>0 and q>0 and r<0):
		return -1
	elif(p<0 and q>0 and r>0):
		return 2
	elif(p<0 and q>0 and r<0):
		return -2
	elif(p<0 and q<0 and r>0):
		return 3
	elif(p<0 and q<0 and r<0):
		return -3
	elif(p>0 and q<0 and r>0):
		return 4
	elif(p>0 and q<0 and r<0):
		return -4


bor = Border(left=Side(style='thin'), right=Side(style='thin'),top=Side(style='thin'), bottom=Side(style='thin'))
h_c=['T','U','V','W','U Avg','V Avg','W Avg',r"U'=U-U avg",r"V'=V-V avg",r"W'=W-W avg",'Octant']

def single_file_octant(mod,file):
	import openpyxl
	from pandas import read_excel
	from openpyxl import Workbook
	from openpyxl import workbook,load_workbook
	from itertools import repeat
	from openpyxl.styles import PatternFill
	

	def wf(s,mod):							
		inputFilePath=s									
		df=read_excel(inputFilePath)									
		wb=Workbook()											
		sheet=wb.active													
		
		for i in range(11):										
			sheet.cell(row=2,column=i+1).value=h_c[i]	
		octant=[]

		u_mean=df['U'].mean()                                                 
		v_mean=df['V'].mean()
		w_mean=df['W'].mean()
		sheet.cell(row=1,column=14).value='Overall Octant Count'
		sheet.cell(row=1,column=45).value='Longest Subsequence Length'
		sheet.cell(row=1,column=49).value='Longest Subsquence Length with Range'
		sheet['E3'] = u_mean
		sheet['F3'] = v_mean
		sheet['G3'] = w_mean


		for i in df.index:
			sheet.cell(row=i+3,column=1).value=df['T'][i]
			sheet.cell(row=i+3,column=2).value=df['U'][i]
			sheet.cell(row=i+3,column=3).value=df['V'][i]
			sheet.cell(row=i+3,column=4).value=df['W'][i]
			sheet.cell(row=i+3,column=8).value=round(df['U'][i]-u_mean,3)
			sheet.cell(row=i+3,column=9).value=round(df['V'][i]-v_mean,3)
			sheet.cell(row=i+3,column=10).value=round(df['W'][i]-w_mean,3)
			sheet.cell(row=i+3,column=11).value=oct_find(df['U'][i]-u_mean,df['V'][i]-v_mean,df['W'][i]-w_mean)
			octant.append(oct_find(df['U'][i]-u_mean,df['V'][i]-v_mean,df['W'][i]-w_mean))
		
		def range_name_oct(mod=5000):
			octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}

			# dictionary creation in order to  mapping 
			dict_mapping={}                            
			# Creating opposite of dict_mapping dictionary                              
			opp_dict_mapping={}                                                      
			
			for i in range(4):                                            
				dict_mapping[i+1]=2*i+1-1                                           
				dict_mapping[-(i+1)]=2*(i+1)-1
				opp_dict_mapping[2*i+1-1]=i+1
				opp_dict_mapping[2*(i+1)-1]=-(i+1)

			# this function is used to find rank of each octant 
			def rankListFind(h_c):                                     
				temp_head_comp=h_c.copy()
				temp_head_comp.sort(reverse=True)
				res=[]

				for i in h_c:
					for j in range(8):
						if(i==temp_head_comp[j]):
							res.append(j+1)
							break
				# Return the list of ranks		
				return res                                                  
			
			