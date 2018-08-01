def loopOver_Converter(c, key, rang, _raise=True):
    intc = ord(c)               # Convert var to ASCII equivelent
    d = rang[1] - rang[0]       # Range of arg 'rang'
    if _raise:                  # Check if raise or lower num value
        intc += key             # Add key to value to encode/decode
        while intc >= rang[1]:  # While value is greater than printable ASCII range:
            intc -= d           # Subtract range of 'rang' to get a "loop-around" effect
    else:                       # Lower value instead of raise
        intc -= key             # Subtract key to value to encode/decode
        while intc < rang[0]:   # While value is less than printable ASCII range:
            intc += d           # Add range of 'rang' to get a "loop-around" effect
    return chr(intc)            # Return encoded/decoded value
def vigi_raise(data, key): # Raise
    rlist = [c for c in data] # Get every char in 'data'
    keylist = [int(c) for c in str(key)] #Get indivisual digits
    for idx, val in enumerate(rlist):   # For every character:
        rlist[idx] = loopOver_Converter(val, keylist[idx%len(keylist)], [32, 128]) # Perform loopOver_Converter with
    return ''.join(rlist)  #Return list                                            every key in order
def vigi_lower(data, key): #     Copy of vigi_raise, except loopOver_Converter's
    rlist = [c for c in data] #  _raise variable is False
    keylist = [int(c) for c in str(key)]
    for idx, val in enumerate(rlist):
        rlist[idx] = loopOver_Converter(val, keylist[idx%len(keylist)], [32, 128], _raise=False)
    return ''.join(rlist)
