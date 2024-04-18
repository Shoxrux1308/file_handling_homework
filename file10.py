def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
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
    return max(k)
print(main('data10.txt'))

# Read data from file