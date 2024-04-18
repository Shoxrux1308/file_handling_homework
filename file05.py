def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, mode="r")
    x=f.read()
    
    l=''
    k=0
    for i in x:
        if i.isdigit():
            k+=1
        if i.isalpha():
            l+=i
    return [len(l),k]
print(main("data05.txt"))
    
# Read data from file