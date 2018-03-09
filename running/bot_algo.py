

#Om Sri

# ------------------- extract relationship -------------------------
#
# -------------------  *****************  ---------------------------
def extract_relationship(inp, outp):

    zp = zip(inp, outp)
    zlist = sorted(zp, key=lambda p: p[0])  # sorting  based on the values of x in each (x,y) pair

    two_or_more = [x for x in outp if outp.count(x) > 1]
    uniq = set(two_or_more) # removes duplicates

    # https: // stackoverflow.com / questions / 473099 / check - if -a - given - key - already - exists - in -a - dictionary - and -increment - it
    occr = { }
    #for p in zlist:



# ------------------- find relationship between input and out ------
#
# -------------------  *****************  ---------------------------
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

    #value = eval(out1)/ eval(in1)
    code = "{} = [ ]\n".format(OUTPUT_SYMBOL) + \
    "{} = {} \n".format(var1, 2) + \
    "for x in {}:\n\t".format(INPUT_SYMBOL)  + \
    "{}.append({} {} x)\n\n\t".format(OUTPUT_SYMBOL, var1, op2)
    
    #print(code)
    return code


# ****** ------- 
# pass parms as argv * * so you can have any number with out naming.
def main_entry_point(in1, out1):
    global INPUT_SYMBOL    # need to state we are accessing Globally declared ones in this local method in order to modify them
    global OUTPUT_SYMBOL
    INPUT_SYMBOL = in1  # now access these in code_gen() methods
    OUTPUT_SYMBOL = out1

    in1_val = eval(in1)
    out1_val = eval(out1)
    rel = find_relationship(in1_val, out1_val)   # pass values of variable
    #print("\nrelatinship code is: ",rel)
    
    if rel < 3:
        params = call_order[rel]
        var1, op1, op2 = params  # unpack 
        code = get_fn_code(in1, out1, var1, op1, op2)  # pass string name of the input/output variables not names
        
        
    else:
         code = "Error: There is NO clear RELATIONSHIP between INPUT and PUT, please check input/out. Error code:".format(rel)
       
    print(code)
  

# ****** ------- MAIN program

# Global vars, these vars will be Set in main_entry_point() , they will be accessed in generate_code() place
INPUT_SYMBOL = ''
OUTPUT_SYMBOL = ''


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
'''
# un comment this for local testing
in1 = [1, 2, 4, 8]
out1 = [2, 4, 8, 16]

inp2 = [1, 2, 6, 7]
outp2 = [3, 4, 8, 9]

#main_entry_point(in1, out1)
'''

#main_entry_point(inp, outp)



