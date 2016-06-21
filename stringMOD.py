#fastMOD.py
#Mapping and replacement function. Takes two lists 'searchList' and 'replaceList' and 
#replaces the string then writes out to the new file 
#Take 2 argument for input file name and output file names. Currently lists have to be adjusted manually. 

#Try this code in a BASH shell for making a list.

#sed -i 's/^/"/' replaceList.txt 
#sed -i 's/^/"/' searchList.txt 
#sed -i 's/$/"/' searchList.txt 
#sed -i 's/$/"/' replaceList.txt 
#sed -i 's/$/,/' replaceList.txt 
#sed -i 's/$/,/' searchList.txt
 

from sys import argv
import re

#Command line arguments 
script, infileName, outfileName = argv


#Open and read file
openFile = open(fileName, 'r')
readFile = openFile.read()

#Define search list
searchList = ["A7H1K8_CAMJD","A0A0W8KQJ0_CAMJU","A0A0M4UJN5_CAMJU","A0A0D6FB29_CAMJU","A0A0W8LD60_CAMJU","E6LB56_CAMUP","Q4HQ18_CAMUP","A6Q212_NITSB","B9L681_NAUPA",
"A6DDB3_9PROT","G2HWB0_9PROT","A0A0G9K570_9PROT","A8EU47_ARCB4","A0A0G9KHD1_9PROT","S5P594_9PROT","A0A0M1UMC2_9PROT","A0A0G9KW79_9PROT","E6L5T8_9PROT","J1FC60_9HELI",
"Q7MAB6_WOLSU","E6WZH2_NITSE","C6REK3_9PROT","M5IPJ2_9PROT","B9CYC1_CAMRE","M3J9M3_9PROT","A0A0A8H2T3_9PROT","B9KEU3_CAMLR","A0A0G3DG35_CAMLA",
"A0A0A8H6X6_CAMLA","A0A0A8GR24_9PROT","A0A0A8HB34_9PROT","A0A0A8HTP9_CAMLA","A0A0A8GYM0_9PROT","A0A0A8I5X5_CAMLA","A0A0A8HKV1_9PROT","A7I3V7_CAMHC","S3XHU6_9PROT",
"A0A0K1HED5_9PROT","C8PIG8_9PROT","U5Y2R3_CAMFE","A0A0E1GNA1_CAMFE","A0A076F967_9PROT","A0A0S4R6P5_CAMFE","A0A071L861_CAMHY","A0A0M3V226_9PROT",
"U2EZ76_9PROT","U2EYD7_9PROT","U2F1V0_9PROT","U2GQ94_9PROT","G9QT12_9PROT","I1DS87_9PROT","J7UKA2_9PROT","A7GZZ8_CAMC5","U2F8K5_9PROT",
"A0A0D8B729_CAMJU","H7X9G3_CAMJU","A0A0E1ER23_CAMJU","A0A0W8LKC6_CAMJU","A0A0W8KTV2_CAMJU","A5KGC2_CAMJU","A0A059I0K9_CAMJU",
"A0A0W8L176_CAMJU","D2N0E6_CAMJU","W8KL32_CAMCO","T2LH74_CAMCO","A0A0H3PJ47_CAMJJ"]

replaceList = ["Campylobacter jejuni subsp. doylei (strain ATCC BAA-1458 / RM4099 / 269.97)",
"Campylobacter jejuni HB-CJGB-LXC","Campylobacter jejuni subsp. jejuni","Campylobacter jejuni","Campylobacter jejuni BJ-CJGB96114",
"Campylobacter upsaliensis JV21","Campylobacter upsaliensis RM3195","Nitratiruptor sp. (strain SB155-2)","Nautilia profundicola (strain ATCC BAA-1463 / DSM 18972 / AmH)","Caminibacter mediatlanticus TB-2","Arcobacter sp. L","Arcobacter butzleri L348",
"Arcobacter butzleri (strain RM4018)","Arcobacter butzleri L353","Arcobacter butzleri 7h1h","Arcobacter butzleri ED-1",
"Arcobacter butzleri L355","Arcobacter butzleri JV22","Thiovulum sp. ES","Wolinella succinogenes (strain ATCC 29543 / DSM 1740 / LMG 7466 / NCTC 11488 / FDC 602W) (Vibrio succinogenes)",
"Nitratifractor salsuginis (strain DSM 16511 / JCM 12458 / E9I37-1)","Campylobacter showae RM3277","Campylobacter showae CSUNSWCD",
"Campylobacter rectus RM3267","Campylobacter showae CC57C","Campylobacter insulaenigrae NCTC 12927","Campylobacter lari (strain RM2100 / D67 / ATCC BAA-1060)","Campylobacter lari","Campylobacter lari subsp. concheus LMG 11760","Campylobacter peloridis LMG 23910",
"Campylobacter subantarcticus LMG 24374","Campylobacter lari NCTC 11845","Campylobacter sp. RM16704","Campylobacter lari RM16712",
"Campylobacter volucris LMG 24379","Campylobacter hominis (strain ATCC BAA-381 / LMG 19568 / NCTC 13146 / CH001A)",
"Campylobacter ureolyticus ACS-301-V-Sch3b","Campylobacter ureolyticus RIGS 9880","Campylobacter gracilis RM3268","Campylobacter fetus subsp. testudinum 03-427","Campylobacter fetus subsp. fetus 04/554","Campylobacter iguaniorum","Campylobacter fetus subsp. fetus","Campylobacter hyointestinalis subsp. hyointestinalis","Campylobacter concisus","Campylobacter concisus UNSW3","Campylobacter concisus UNSWCS","Campylobacter concisus UNSW1","Campylobacter concisus ATCC 51561","Campylobacter sp. 10_1_50","Campylobacter concisus UNSWCD","Campylobacter sp. FOBRC14","Campylobacter curvus (strain 525.92)","Campylobacter concisus ATCC 51562","Campylobacter jejuni subsp. jejuni","Campylobacter jejuni subsp. jejuni LMG 23216","Campylobacter jejuni subsp. jejuni","Campylobacter jejuni HB-CJGB-LC","Campylobacter jejuni HB-CJGB-QYT","Campylobacter jejuni subsp. jejuni CG8486","Campylobacter jejuni K5","Campylobacter jejuni HB-CJGB-LL",
"Campylobacter jejuni subsp. jejuni 414","Campylobacter coli RM4661","Campylobacter coli 76339","Campylobacter jejuni subsp. jejuni serotype O:23/36 (strain 81-176)"]

#Create the dictionary from the two lists.
entry_dict = dict(zip(searchList, replaceList))
 
#Match and swap terms in the input file (this is a much better solution that for loop as it doesnt matter what orders the items are in). 
pattern = re.compile(r'\b(' + '|'.join(entry_dict.keys()) + r')\b')
newFile = pattern.sub(lambda x: entry_dict[x.group()], readFile)

#Write out the new file. 
with open(outfileName, 'w') as file:
  file.write(newFile)

#END OF FILE





