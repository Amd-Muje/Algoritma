import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    # Mengatur seed untuk random
    random.seed(40)
    
    # Menghasilkan bilangan acak
    data = [random.randint(0, 100) for _ in range(50)]
    print("Data sebelum diurutkan:")
    print(data)
    
    # Mengurutkan data menggunakan QuickSort
    sorted_data = quicksort(data)
    print("Data setelah diurutkan:")
    print(sorted_data)