import UpdateProcedure as UpdateProcedure
import math

def Encode(m , k) :
    '''
    @param m: the size of input symbol sources {a1, a2, ..., ak,..., am}
    @param k: the numerical order of ak in input symbol sources
    @return: the binary string encoded of ak
    '''
    e = math.floor(math.log2(m))
    r = m-(2**e)
    if(1 <= k <= 2*r) :
        # ak = k-1 using e+1 bit
        return '{0:b}'.format(k-1).zfill(e+1)
    else:
        # ak = k-r-1 using e bit
        return '{0:b}'.format(k - r - 1).zfill(e)

def EncodeProcedure(inputSourceSize, symbols) :
    '''
    @param: inputSourceSize : # the total leafs ~ total size of source
    @param: symbols : the symbol string that need to encode
    @return: encodedString : the binary string encoded from the input
    '''
    # the total nodes
    totalNodes = 2*inputSourceSize - 1 
    # create a tree with only one node (NYT)
    AHM_Tree = UpdateProcedure.AdaptiveHuffmanTree(totalNodes) 
    # the binary string encoded from the input
    encodedString = ""
    for s in symbols :
        # if s have not been transmited yet
        if(AHM_Tree.SymbolsTransmited.get(s) == None):
           encodedString = encodedString + AHM_Tree.UpdateProcedure(s) + Encode(inputSourceSize, s)
        else: # if s have been transmited yet
            encodedString += AHM_Tree.UpdateProcedure(s)
    return encodedString





