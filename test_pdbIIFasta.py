#! /usr/bin/python

import argparse
import re


# Dictionary containing reference for 3-letter code to 1-letter code
residues    = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E',
               'GLN':'Q','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K',
               'MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
               'TYR':'Y','VAL':'V','---':'-'}

def pdbToSequence(_file):
    _sequence = [[],[],[]]
    _header = _file[:-4]
    with open(_file, 'r') as inFile:
        for _line in inFile:
            if re.search('^ATOM.*CA',_line):
                _entry = _line.split()
                # Correct for lack of whitespace between chain and residue
                if len(_entry[4]) > 1:
                    _entry.insert(5,_entry[4][1:])
                    _entry[4] = _entry[4][:1]
                _entry[5] = int(_entry[5])
                # Avoid repetition of residues in crystal
                if len(_sequence[0]) is 0:
                    _sequence[0].append(residues[_entry[3][-3:]])
                    _sequence[1].append(_entry[4])
                    _sequence[2].append(_entry[5])
                else:
                    if _sequence[2][-1] != _entry[5]:
                        # Corrects for gaps in _sequence
                        while (_sequence[1][-1] is _entry[4] and _sequence[2][-1] != _entry[5]-1):
                            gap = 1
                            _sequence[0].append('-')
                            _sequence[1].append(_entry[4])
                            _sequence[2].append(_sequence[2][-1]+gap)
                            gap += 1
                        _sequence[0].append(residues[_entry[3][-3:]])
                        _sequence[1].append(_entry[4])
                        _sequence[2].append(_entry[5])
    return _sequence, _header

def sequenceToFile(_sequence,_header,_format='fasta'):
    _output = [[],[]]
    _chains = []
    # Identify Chain positions for .ali output
    for i in range(1,len(_sequence[1])):
        if i == 1:
            _chains.append(_sequence[1][i])
            _chains.append(0)
        if _sequence[1][i] != _sequence[1][i-1]:
            _chains.append(i-1)
            _chains.append(_sequence[1][i])
            _chains.append(i)
        if i == len(_sequence[1])-1:
            _chains.append(i)
            
    # Create writable objects in _sequence format
    for i in range(len(_chains)//3):
        j = i*3
        _output[0].append(_chains[j])
        _output[1].append('')
        # Add \n every 60 characters to fit standard format
        for k in range(_chains[j+1],_chains[j+2]+1):
            _position = k - _chains[j+1]
            if (_position % 60) == 0:
                _output[1][i] += '\n'
            _output[1][i] += _sequence[0][k]
    
    if _format == 'fasta':
        with open(_header+'.fasta','w') as _outFile:
            for i in range(len(_output[0])):
                _outFile.write('>'+_header+';'+_output[0][i])
                _outFile.write(_output[1][i]+'\n')
        print (_header+'.fasta has been created.')
    elif _format == 'ali':
        with open(_header+'.ali','w') as _outFile:
            for i in range(len(_output[0])):
                j = i*3
                _outFile.write('>P1;'+_header+'\n')
                _outFile.write('structure:%s:%d:%s:%d:%s:::0.00:0.00' % (_header,_sequence[2][_chains[j+1]],_chains[j],_sequence[2][_chains[j+2]],_chains[j]))
                _outFile.write(_output[1][i]+'*\n')
        print (_header+'.ali has been created.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a .fasta or .ali file from PDB. Splits output by chain.')
    parser.add_argument('input', help='Input PDB file')
    parser.add_argument('format', help='fasta or ali', default='fasta', nargs='?')
    args = parser.parse_args()

    sequence, header = pdbToSequence(args.input)
    sequenceToFile(sequence, header,args.format)
