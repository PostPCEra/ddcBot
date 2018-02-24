import sys
import os


inp = [3, 5 ,4]
outp = [ 6, 10]


#Om Sri


# ****** ------- find replationship between input and out
def find_relationship( inp, outp):
    v1, v2 = (inp, outp)
    if ( inp [1] > outp[1]): #keep bigger values in v2
        v1, v2 = (outp, inp )
        
    found = True
    val = v2[0] / v1[0]  # check for Ratio
    i = 1
    while (i < len(v1)):
        if (val != v2[i] / v1[i]):
            found = False
            break
        i += 1
        
    if found:
        return relation['ratio1']
    
    found = True
    val = v2[0] - v1[0] # check for difference
    i = 1
    while (i < len(v1)):
        if (val != v2[i] - v1[i]):
            found = False
            break
        i += 1
        
    if found:
        return relation['difference']
    
    return relation['notfound']   # last default return


# ****** ------- construct & return function CODE
def get_fn_code(inp, outp, var1, op1, op2):
    
    str = "\ndef relation(lst, output):\n\t" \
    "out = [ ]\n\t" \
    "{} = int(output[0] {} lst[0])\n\t" \
    "for x in lst:\n\t\t" \
    "out.append({} {} x)\n\n\t" \
    "return out"
    code = str.format(var1, op1, var1, op2)
    
    str = "\n\n##******-- MAIN program:\n" \
    "inp = {}\n" \
    "outp = {}\n" \
    "print( relation(inp, outp) )\n"
    code = code + str.format(inp, outp)
    
    #print(code)
    return code


# ****** ------- 
# pass parms as argv * * so you can have any number with out naming.
def main_entry_point(in1, out1):
    rel = find_relationship(in1, out1)
    #print("\nrelatinship code is: ",rel)
    
    if rel < 3:
        params = call_order[rel]
        var1, op1, op2 = params  # unpack 
        code = get_fn_code(in1, out1, var1, op1, op2)
        
        
    else:
         code = "Error: There is NO clear RELATIONSHIP between INPUT and PUT, please check input/out. Error code:".format(rel)
       
    print(code)
  

# ****** ------- MAIN program

relation = {
  'ratio1' : 0,
  'ratio2' : 1,
  'difference' : 2,
  'notfound' : 3
}
#print(relation)

call_order = [
 ("ratio", " / ", "*") ,
 ("ratio", " / ", "*") ,
 ("difference", " - ", " + ") 
 ]

# ****** -------  calling Main()

in1 = [1, 2, 4, 8]
out1 = [2, 4, 8, 16]

inp2 = [1, 2, 6, 7]
outp2 = [3, 4, 8, 9]

#main_entry_point(in1, out1)
main_entry_point(inp, outp)

#st = open('pdb_next.py', 'r').read()
#print(st)
 

# ****** -------  
# TODO for Latter  **************************
# ****** ------- find data types
"""
var_types = []
#from types import *
def find_type(item):
  i = 0
  if type(item) is ListType:
      var_types[i] = ListType
  else :
      print("not list type")
"""
