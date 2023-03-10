import pandas as pd
import os

pop_excel = pd.read_excel("Population_Data.xlsx", sheet_name="Hoja1")
cpath = os.path.dirname(os.path.abspath(__file__))
os.chdir(cpath + "\\history\\provinces")

#print(pop_excel)

for i in range(len(pop_excel)):
	current_id = str(pop_excel.loc[i,"Province ID"]) + " -"
	current_name = pop_excel.loc[i,"Province Name"]
	current_filename = current_id + " - " + current_name + ".txt"
	current_filename = [filename for filename in os.listdir(cpath + "\\history\\provinces") if os.path.isfile(os.path.join(cpath, 'history', 'provinces', filename)) and filename.startswith(current_id)][0]
	
	print("\n[" + str(i) + "/" + str(len(pop_excel)) + "] Current file: " + current_filename + "...")
	with open(current_filename, "r", encoding='iso-8859-1') as current_file:
		lines = current_file.readlines()
		lines.reverse()
		found = False
		pos = 0
		for index, line in enumerate(lines,start=0):
			if "100.1.1 = {" in line:
				found = True
				pos = index
				break

		if found == True:
			lines.reverse()
			fileLength = len(lines)
			linePos = (fileLength - 1) - pos
			#print(linePos)
			lines = lines[:linePos]
			
			while lines[-1] == '\n':  # while the last item in lst is blank
				lines.pop(-1)  # removes last element			
			
			with open(current_filename, "w", encoding='iso-8859-1', newline='') as current_file2:
				current_file2.writelines("%s" % line for line in lines)
				


	with open(current_filename, mode='a', encoding='iso-8859-1') as current_file:
		current_file.write("\n100.1.1 = {")
		current_file.write("\n\tset_variable = { which = starting_rural_pop_1350 value = %.3f }" % (pop_excel.loc[i,"RP 1350"]/1000))
		current_file.write("\n\tset_variable = { which = starting_urban_pop_1350 value = %.3f }" % (pop_excel.loc[i,"UP 1350"]/1000))
		current_file.write("\n\tset_variable = { which = starting_rural_pop_1400 value = %.3f }" % (pop_excel.loc[i,"RP 1400"]/1000))
		current_file.write("\n\tset_variable = { which = starting_rural_pop_1450 value = %.3f }" % (pop_excel.loc[i,"RP 1450"]/1000))
		current_file.write("\n\tset_variable = { which = starting_rural_pop_1850 value = %.3f }" % (pop_excel.loc[i,"RP 1850"]/1000))
		
		current_file.write("\n}")
		print("Done!")