#! /usr/bin/python

import argparse
import re

residues    = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E',
               'GLN':'Q','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K',
               'MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
               'TYR':'Y','VAL':'V','---':'-'}

def pdbToSequence(_file,_format='fasta'):
    fasta = [[],[],[]]
    _output = [[],[]]
    _chains = []
    _header = []
    with open(_file, 'r') as inFile:
        for _line in inFile:
            if _line.startswith('HEADER'):
                _header.append(_line.rsplit()[-1])
            if _line.startswith('EXPDTA'):
                _header.append(_line.rsplit()[1:])
            if re.search('^ATOM.*CA',_line):
                _entry = _line.split()
                # Correct for lack of whitespace between chain and residue
                if len(_entry[4]) > 1:
                    _entry.insert(5,_entry[4][1:])
                    _entry[4] = _entry[4][:1]
                _entry[5] = int(_entry[5])
                # Avoid repetition of residues in crystal
                if len(fasta[0]) is 0:
                    fasta[0].append(residues[_entry[3][-3:]])
                    fasta[1].append(_entry[4])
                    fasta[2].append(_entry[5])
                else:
                    if fasta[2][-1] != _entry[5]:
                        # Corrects for gaps in sequence
                        while (fasta[1][-1] is _entry[4] and fasta[2][-1] != _entry[5]-1):
                            gap = 1
                            fasta[0].append('-')
                            fasta[1].append(_entry[4])
                            fasta[2].append(fasta[2][-1]+gap)
                            gap += 1
                        fasta[0].append(residues[_entry[3][-3:]])
                        fasta[1].append(_entry[4])
                        fasta[2].append(_entry[5])
    # Identify Chain positions for .ali output
    for i in range(1,len(fasta[1])):
        if i == 1:
            _chains.append(fasta[1][i])
            _chains.append(0)
        if fasta[1][i] != fasta[1][i-1]:
            _chains.append(i-1)
            _chains.append(fasta[1][i])
            _chains.append(i)
        if i == len(fasta[1])-1:
            _chains.append(i)
    # Create writable objects in FASTA format
    for i in range(len(_chains)/3):
        j = i*3
        _output[0].append(_chains[j])
        _output[1].append('')
        # Add \n every 60 characters to fit standard format
        for k in range(_chains[j+1],_chains[j+2]+1):
            _position = k - _chains[j+1]
            if (_position % 60) == 0:
                _output[1][i] += '\n'
            _output[1][i] += fasta[0][k]
    
    if _format == 'fasta':
        with open(_header[0]+'.fasta','w') as _outFile:
            for i in range(len(_output[0])):
                _outFile.write('>'+_header[0]+';'+_output[0][i])
                _outFile.write(_output[1][i]+'\n')
        print _header[0]+'.fasta has been created.'
    elif _format == 'ali':
        with open(_header[0]+'.ali','w') as _outFile:
            for i in range(len(_output[0])):
                j = i*3
                _outFile.write('>P1;'+_header[0]+'\n')
                _outFile.write('structure:%s:%d:%s:%d:%s:::0.00:0.00' % (_header[0],fasta[2][_chains[j+1]],_chains[j],fasta[2][_chains[j+2]],_chains[j]))
                #_outFile.write('structure:',_header[0],':',_chains[j+1],':',_chains[j],':',_chains[j+2],':',_chains[j],':::0.00:0.00')
                _outFile.write(_output[1][i]+'*\n')
        print _header[0]+'.ali has been created.'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a FASTA or .ali file from PDB. Splits output by chain.')
    parser.add_argument('input', help='Input PDB file')
    parser.add_argument('format', help='fasta or ali')
    args = parser.parse_args()
    
    pdbToSequence(args.input,args.format)