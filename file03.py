def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    x=f.readline()
    
    l=[]
    for i in x:
        if i.isdigit():
          l.append(int(i))
    return l
print(main("data03.txt"))

# Read data from file
