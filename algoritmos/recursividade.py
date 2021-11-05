def fatorial (n: int) -> int:
    #Caso base
    if n == 1:
        return 1
    #Caso recursivo
    return n * fatorial(n-1)

def finobaci(n:int)-> int:
    if n == 1: return 1
    if n == 0: return 0
    return finobaci(n-1) + finobaci(n-2)
        

if __name__ == "__main__":
    print(fatorial(5))
    print(finobaci(6))