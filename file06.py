def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, mode="r")
    x=f.read()
    
    l=''
    for i in x:
        l+=i
    a=l.split("\n")
    k=[]
    for u in a:
        k.append(len(u))
    return k
print(main('data06.txt'))
    
# Read data from file