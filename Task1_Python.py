import re,csv
csvfile = "Number_of_mentions.csv"  # Creates Excel File for representation
header_count = 0
f = open('abs1.txt','r')   #opens the file
line = f.read()
j = 0
sub = re.findall('.*\n',line)   #uses Regular Expression
while 1:
        try:
            line = sub[j]
        except:
            break
        #print (j)
        if line:
            open("abs1_subdocs/file " + str(j + 1) + ".txt", 'w').write(line)
            j = j + 1
f.close()      #closes the file

def wordcount(filename, listofwords): #creates function that takes filename and the word to be find as arguments
	try:
		file = open(filename, 'r')
		read = file.readlines()
		file.close()
		for word in listofwords:
			lower = word.lower()  #lowers everything to make sure both capital and small characters are taken into consideration
			count = 0
			for sentence in read:
				line = sentence.split(" ")
				for each in line:
					line2 = each.lower()
					if lower == line2:
						count = count + 1
			print(lower, ':', count)
		return count

	except FileExistsError:
		print('File not existing')   #If the file doesnt exist it will print this

d = 1
while d < 866:
		print ('file ' + str(d))
		a = wordcount('abs1_subdocs/file ' + str(d) + '.txt', ['customers'])
		b = wordcount('abs1_subdocs/file ' + str(d) + '.txt', ['stakeholders'])
		c = wordcount('abs1_subdocs/file ' + str(d) + '.txt', ['investors'])
		print(a,b,c)
		mylist = [d,a,b,c]
		header = ['File Index', 'Customer', 'Stakeholder', 'Investor']
		with open(csvfile, 'a+') as mycsv:   #appends the values
			wr = csv.writer(mycsv)
			if d == 1:
				header_count = 1
			if header_count == 1:
				wr.writerow(header)
				header_count = 0
			wr.writerow(mylist)
		d += 1
        
        #OUTPUT: The abs1.txt file is created into sub docs, and the number of mentions of all 3 words are printed in the 
                 #output and excel file is created for a tabular form view