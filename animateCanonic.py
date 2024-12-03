"""
aut.
"""

from common.pauli import *
#from common.generator import *
from classifier.transform import *
from stuff.drawing import *
from stuff.recording import *



def buildAndAnimate(nodes):
    record = RecordGraph()
    canonics = transformToCanonics(nodes, record = record, debug=False)
    animationGraph(record)

if __name__ == '__main__':
    generators = getAllCommutators(8, getAlgebra("a6"))
    buildAndAnimate(generators)






