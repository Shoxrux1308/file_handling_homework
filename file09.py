def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, mode="r")
    x=f.read()
    
    l=[]
    for i in x:
        if i.isdigit():
            l.append(int(i))
    return min(l)
print(main('data09.txt'))

# Read data from file