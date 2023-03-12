def fun(string):
    lower=0
    upper=0
    for char in string:  
        if (char.islower()):
            lower=lower+1
        
        elif (char.isupper()):
            upper=upper+1
        
    print('the no of lower case:',lower)
    print('the no of upper case',upper)
string='The quick Brow Fox'      
fun(string)