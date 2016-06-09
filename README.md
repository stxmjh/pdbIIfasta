# pdbIIfasta

***************
*pdbIIfasta.py*
***************

![alt tag](https://github.com/stxmjh/pdbIIfasta/blob/master/pdbIIfastasnake.png)
Introduction
=============
pdbIIfasta.py is a simple, easy to use conversion tool for extracting the EXACT
sequence of a Protein Data Bank or PDB (.pdb) file as a FASTA (.fasta) file for general bioinformatics use.

Why pdbIIfasta?
===============
Often the sequence information attached to structures deposited to the RCSB PDB is inaccurate and inconsistent with the the PDB file. 
The strucutre may be missing residues which have not been well resolved in the structure. Using the .fasta given can lead to fatal inconsistencies 
and can seriously impede the speed and accuarcy of bioinformatics studies. 

You need to know the EXACT sequence you are working with and this can be hard to determine sometimes from multiple sources of information. 

Usage
=======
pdbIIfasta is easy to use! It is a simple programme written in python that works with version 2.x of the language.
It takes a .pdb as the input and puts out another file with the sequence in FASTA format...
See below for an example of how to use.

Example
===========

$ python test_pdbIIfasta.py 4k3b.pdb fasta

Explanation
===========
- The $ sign indicates the start of the command prompt. You don't need to write this. Just what comes after;)
- The first bit calls the python3 interpreter. You will need python3 installed on your computer (see below). 
- The second bit calls the programme to run, with the .py extension.
- The third piece of the line, called an arguemnt in proper terminology, calls the file you want to convert. 
- The second argument states the file type for output. The default is FASTA. (other .ali for use with A. Salis awesome MODELLER [1] software are also available)
- Try running the script from the same folder where the .pdb is stored or direct to where the input file is with some forward slashes (ie /home/wherever/here/MyPDBS/4k3b.pdb)  
- Try '# python3 test_pdbIIfasta.py -f' for some pointers if you forget.
- HANDY TIP: for can use the tab key (the two backwards arrows) for autocomplete so you don't have to write the whole thing out.
- ADVANCED USE: try calling the programme in a 'loop' from BASH or python for batch conversion jobs. More on this later.

Requirements
=============
You will need python2(!) and a terminal window to run pdbIIfasta eg Command Prompt (Windows), BASH (Linux), Terminal (Mac) etc
A version for use with python3 language is on its way!
https://www.python.org/downloads/

Disclaimer
===========
Please note pdbIIfasta has currently only been tested on some Linux operating systems (Ubuntu/OpenSUSE) so there's no guarantee it will work for you if you're using a Mac or Window OS. 
But fingers crossed, we hope it does. Give it a test and if doesn't work then just drop us an email and let us know why. You're free to use the code however you wish. 
We appreciate nice people who recognise others for their work but if you dont then that's fine too! There are other pdb to fasta conversion tools out there too.
pdbIIfasta was written by Jedd-Bellamy Carter and Matt Hardcastle (University of Nottingham, 2016)
WARNING!!!
==========
!!!Currently pdbIIfasta doesn't work with structures 'fetched' and saved through pymol!!! Give us time...we're working on it.


[1] B. Webb, A. Sali. Comparative Protein Structure Modeling Using Modeller. Current Protocols in Bioinformatics, John Wiley & Sons, Inc., 5.6.1-5.6.32, 2014. 






