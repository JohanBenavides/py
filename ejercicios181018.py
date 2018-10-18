"""
a = [12,32,65,75,1,5,7,33,4]
print(a)

a=[(i*2)for i in range(11)]
print(a)
"""
from random import randint

def bubble_sort(a):
    for i in range(len(a)-1):
        swapped = False
        for j in range(len(a)-1):
            if a[j]> a[j+1]:
                swap = a[j]
                a[j] = a[j+1]
                a[j+1]=swap
                swapped = True
                
        if not swapped:
            break

def insertion_sort(a):
    for i in range(1,len(a)):
        x=a[i]
        index_hole = i

        while index_hole> 0 and a[index_hole -1] >x:
            a[index_hole]= a[index_hole - 1]
            index_hole -= 1

        a[index_hole] = x

def quick_sort(a):
    if len(a)<= 1:
        return a
    else:
        pivot = a[0]
        less_subarray = []
        greater_subarray = []
        
        for i in range(1,len(a)):
            if a[i]<pivot:
                less_subarray.append(a[i])
            else:
                greater_subarray.append(a[i])

        quick_sort(less_subarray)
        quick_sort(greater_subarray)

        result =[]
        result.extend(quick_sort(less_subarray))
        result.append(pivot)
        result.extend(quick_sort(greater_subarray))

    return result



            
a = [randint(1,1000) for i in range(200)]
print("cadena desordenada: ",a,"\n")
"""insertion_sort(a)algoritmo de ordenamiento insertion"""
"""bubble_sort(a) algoritmo de ordenamiento burbuja"""
quick_sort(a)
"""definir a """
print("cadena ordenada: ",a,"\n")






        
    




