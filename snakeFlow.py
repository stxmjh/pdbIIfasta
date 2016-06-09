#)SNAAAAAAAKE!!!! TEST LINUX
#Rewritten for python3. #Futureproof

#"Lets play a game of snakes and ladders..."
#Useage
#1)Start the programme. $ python3 snakeFlow.py
#2)Follow the onscreen instructions
#
#!/usr/bin/env python
#Author: Matt Hardcastle and Jedd Bellamy-Carter
# -*- coding: utf-8 -*-
'''Snake

    1.  -------------------------DEPRECATED-MJH Uniprot search terms/bigFasta files pre-downloaded
1.  Download FASTAs from Uniprot server to file 'query.fasta' (CHECK)    
2.  Get sequence lengths from the FASTA stack
3.  
4.  

Use Rpy2 to interface Python with R and make good graphs + stats.
'''

import re
import glob
import time


from rpy2.robjects import r
import rpy2.robjects.lib.ggplot2 as ggplot2
from rpy2.robjects.lib.dplyr import DataFrame
import rpy2.robjects as robjects 


#from rpy2.robject.packages import importr
from urllib.request import urlopen



##Do that cool logo thing.
#Cant use function yet cus im too stoopid def termHeader():
print ("\nThis program is free software: you can redistribute it and/or modify\n\
it under the terms of the GNU General Public License as published by\n\
the Free Software Foundation, either version 3 of the License, or\n\
(at your option) any later version.\n\n\
This program is distributed in the hope that it will be useful,\n\
but WITHOUT ANY WARRANTY; without even the implied warranty of\n\
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\
GNU General Public License for more details.\n\n\
You should have received a copy of the GNU General Public License\n\
along with this program.  If not, see <http://www.gnu.org/licenses/>.\n")

print('\033[96m     /\  \         /\__\         /\  \         /\__\         /\  \   ') 
print('    /::\  \       /::|  |       /::\  \       /:/  /        /::\  \   	')
print('   /:/\ \  \     /:|:|  |      /:/\:\  \     /:/__/        /:/\:\  \  	')
print('  _\:\~\ \  \   /:/|:|  |__   /::\~\:\  \   /::\__\____   /::\~\:\  \ 	')
print(' /\ \:\ \ \__\ /:/ |:| /\__\ /:/\:\ \:\__\ /:/\:::::\__\ /:/\:\ \:\__\	')
print(' \:\ \:\ \/__/ \/__|:|/:/  / \/__\:\/:/  / \/_|:|~~|~    \:\~\:\ \/__/	')
print('  \:\ \:\__\       |:/:/  /       \::/  /     |:|  |      \:\ \:\__\  	')
print('   \:\/:/  /       |::/  /        /:/  /      |:|  |       \:\ \/__/  	')
print('    \::/  /        /:/  /        /:/  /       |:|  |        \:\__\    	')
print('     \/__/         \/__/         \/__/         \|__|         \/__/	')             
print('      Copyright (C) 2016 JBC and MJH, University of Nottingham\n')







#Get FASTA stack from the Uniprot server.
query = input("Please enter your search term: ").replace(" ","+")
print ("Data retrieval in progress.....")
print ("...please hold on a sec.")

seqdata = urlopen("http://www.uniprot.org/uniprot/?query=" + query + "&format=fasta").read()
print (seqdata)

print ("Your sequences have been successfully retreived.")
print ("Saving data to file " + query + ".fasta")
print ("...")

stack_file = open(query + ".fasta", 'wb')
stack_file.write(seqdata)

print ("Done.")

#Sleep for a sec. Do some jazzy stuff
print ("Preparing for seqeunce length distribution analysis.")
time.sleep(0.4)
print(".")
time.sleep(0.4)
print("..")
time.sleep(0.4)
print("...")
time.sleep(1)
print("Modules ready for analysis.")
time.sleep(2)

#File should now have been saved. Do the length calculation routine.
#Credit: JBC
list = glob.glob("*.fasta")
print (list)

inFastaFile = 'kapa.fasta'

for i in list:
	lens = []
	
	with open(i, 'r') as inFile:
		lines 			= inFile.readlines()
		allFasta 		= ''.join(lines)
		allFastaSplit		= re.split('>', allFasta)
		allFastaSplit.pop(0)    #Remove null first entry
		for each in allFastaSplit:	
			seq = ''.join(each.split('\n')[1:])
			lens.append(str(len(seq.strip())))

	with open(i + '_lengths.txt', 'w') as outFile:
		outFile.write('\n'.join(lens))	
nhits = len(lens)
print ("Your sequences have been measured..." )
#To do: If nhits > 0 cool! if ==o print uncool!
print (str(nhits) + " hits found! Cool!")
print ("Saving to file.")
time.sleep(5)

#R plotting function. This is not going to be fun.
r('lengths <- read.table("kapa.fasta_lengths.txt", quote="\", comment.char="")')
r('attach(lengths)')
#r('print(lengths)')
r('V1 <- sort(V1)')
#r('print(V1)')
#Generate frequency tables from lengths
r('freq_lengths <- count(lengths,V1)')
#r('print(freq_lengths)')
r('stats <- boxplot.stats(V1)$stats')
r('mean <- mean(V1)')
r('max  <- max(V1)')
r('min  <- min(V1)')
r('sd   <- sd(V1)')
print("The maximum sequence length is:")
r('print(max)')
print("The minimum sequence length is:")
r('print(min)')
print("Mean average sequence length is:")
r('print(mean)')
print("Standard deviation of the data is:")
r('print(sd)')

print("Plotting data...")
print("..please hold on.")
#Get a RawInput for the plot file name e.g 'something.png', turn it into something R can see.
getName = input("Please enter file name from plot:")
r.assign('getName', getName)
plotFunc = r("""
vlines <- c(mean-sd,mean+sd,mean-2*sd,mean+2*sd)
library(ggplot2)
gg =    ggplot(data = freq_lengths, aes(V1,n))
pp =	gg + 
	geom_point(alpha=0.5, size=2) + 
	theme_light() + 
	labs(title='Frequency of sequence lengths', x='Sequence Length', y='Frequency') + 
	geom_vline(xintercept=vlines[c(1,2)], colour=4, linetype=3) + 
	geom_vline(xintercept=vlines[c(3,4)], colour=2, linetype=3) + 
	geom_vline(xintercept=mean, colour=1, linetype=3) + 
	geom_text(aes(label='')) 

 
print(pp)
ggsave(getName)
""")





































	







