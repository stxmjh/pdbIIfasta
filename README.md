# pdbIIfasta

![alt tag](https://github.com/stxmjh/pdbIIfasta/blob/master/pdbIIfastasnake.png)

## Introduction

pdbIIFasta.py is a simple conversion tool that generates sequence information from recorded PDB data (i.e. missing residues are treated as gaps (-)). The sequence information is then written to file in either .fasta or .ali [[1]](#1) format for general bioinformatics use.

## Why pdbIIfasta?

FASTA files downloaded from the RCSB database to accompany a PDB file represent the ideal sequence, however this may not correspond to the PDB file as some residues do not resolve well from X-Ray crystallography or NMR. 
In some cases a sequence that corresponding to the PDB resolved residues is desired such as when using MODELLER [[1]](#1), it is for those cases that this tool is designed.


## Usage

To use pdbIIfasta in the command line simply do `python pdbIIFasta.py <inputFile> <outputFormat>` and an output file will be created in the same directory as the inputFile.

For example:

```bash
python pdbIIFasta.py 4k3b.pdb ali
```

Will generate the file `4k3b.ali`. 

***Note***: The `fasta` format is default and may be omitted in command line.

## Requirements

pdbIIFasta is Python 2 and 3 compatible at time of writing.

## Disclaimer

We appreciate nice people who recognise others for their work but if you dont then that's fine too! There are other pdb to fasta conversion tools out there too.
pdbIIfasta was written by Jedd-Bellamy-Carter and Matt Hardcastle (University of Nottingham, 2016)

## References

<a name="1">1</a> : B. Webb, A. Sali. Comparative Protein Structure Modeling Using Modeller. Current Protocols in Bioinformatics, John Wiley & Sons, Inc., 5.6.1-5.6.32, 2014. 






