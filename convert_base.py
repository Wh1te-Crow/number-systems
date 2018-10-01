def convert_n_to_m(x, n, m):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if (isinstance(x,str)):
        x=x.upper()
    if not (isinstance(x,str) or isinstance(x,int)):
        return False
    if n == m:
        return x
    for i in str(x):
        if not (i in alphabet[0:n]) :
           return False
        if not(i in alphabet):
            return False
    def convert_base(num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        if n < to_base:
            return alphabet[n]
        else:
            return convert_base(n // to_base, to_base) + alphabet[n % to_base]
    return convert_base(x,m,n)  



