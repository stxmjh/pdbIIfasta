# pdbIIfasta

***************
*pdbIIfasta.py*
***************

Introduction
=============
pdbIIfasta.py is a simple, easy to use conversion tool for extracting the EXACT
sequence of PDB (.pdb) file as a FASTA (.fasta) file for general bioinformatics use.

Why pdbIIfasta?
===============
Often the sequence information attached to structures deposited to the RCSB PDB is inaccurate and inconsistent with the the PDB file. The strucutre may be missing residues which have not been well resolved in the structure. Using the .fasta given can lead to fatal inconsistencies and can serious impeded the speed and accuarcy of bioinformatics studies. 

You need to know the EXACT sequence you are working with and this can be hard to determine sometime from multiple sources of information. The pdbIIfasta programme was written to overcome that problem. It tells you precisely what the sequence is for the model you're working with. 

Useage
=======
pdbIIfasta is easy to use! It is a simple programme written in python that works with version 3.x of the language.
It takes a .pdb as the input and puts out another file with the sequence in FASTA format
See in the example below

Example
=======
# python3 4k3b.pfb fasta

Explanation
- The first # indicates the start of the command prompt. You don't need to input this. Just everything that comes after;)
-  


Requirements
=============
python3(!)

Disclaimer
===========
Please note pdbIIfasta has currently only been tested on Linux operating systems (Ubuntu/OpenSUSE) so there's no guarantee it will work for you if you're using a Mac or Window OS. 
But fingers crossed, we hope it does. Give it a test and if doesn't work then just drop us an email and let us know why. You're free to use the code however you wish. 
We appreciate nice people who recognise others for their work but if you dont then that's fine too! There are other pdb to fasta conversion tools out there too.

WARNING!!!
==========
!!!Currently pdbIIfasta doesn't work with structures 'fetched' and saved through pymol!!! Give us time...we're working on it.
 






