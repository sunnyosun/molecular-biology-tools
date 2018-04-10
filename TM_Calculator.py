"""
Mutagenic Primer Design Calculator
by Sunny

This script can be executed by command line.
Running guide:
command: python TM_Calculator.py 'sequence' mismatch_count
The input sequence is neither case sensitive nor whitespace sensitive.
"""

###############################################################################
# Modules

import sys

###############################################################################
# Functions

# Calculates the Tm for input sequences.
def tm_calculator(sequence, mismatch_count):
    sequence = sequence.strip().replace(' ','')
    sequence = sequence.upper()
    G_count = sequence.count('G')
    C_count = sequence.count('C')
    GC_content = (float(G_count + C_count)/len(sequence)) * 100
    mismatch = (float(mismatch_count)/len(sequence)) * 100
    tm = 81.5 + 0.41*GC_content - (675/len(sequence)) - mismatch
    return tm


def pmole_calculator(sequence):
    sequence = sequence.strip().replace(' ','')
    sequence = sequence.upper()
    pmole = (125/float(330*len(sequence))) * 1000
    return pmole


###############################################################################
# Main

# sets to be executed by command line.
if __name__ == '__main__':
    sequence = sys.argv[1]
    mismatch_count = sys.argv[2]
    print 'Tm of ' + sequence + ' is:'
    print tm_calculator(sequence, mismatch_count)
    print 'pmole = %s' % pmole_calculator(sequence)
