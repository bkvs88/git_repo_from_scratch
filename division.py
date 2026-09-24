from readdata import a,b
def div(a,b):
    if b ==0 :
        print ("cannot division by zero hence change value of b to 1")
        a=0
        b=1
    c=a/b
    print(f"Division of {a} and {b} is : {c}")
    return c