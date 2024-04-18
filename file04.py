def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, mode='r')
    x=f.readline()

    l=[]
    for i in x:
        l.append((i))
    return l
print(main("data04.txt"))
    
# Read data from file