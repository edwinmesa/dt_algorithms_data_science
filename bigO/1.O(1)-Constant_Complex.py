# Cuando su algoritmo no depende del tamaño de entrada n, se dice 
# que tiene una complejidad de tiempo constante con orden O(1). 
# Esto significa que el tiempo de ejecución siempre será el mismo, independientemente del tamaño de entrada.

# 1 Example
def firstElement(arr):
    return arr[0] # 1 step
score = [12, 55, 67, 94, 22]
print(firstElement(score))
print('#' * 60)

# 2 Example

def constant_something(arr):
    result = arr[0] * arr[0] # 1 step
    print(result)            # 2 step
constant_something(score)
print('#' * 60)

