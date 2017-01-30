import listGenerator
import bucketSort
import math

def swap(L, left, right):
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item



# Wersja wg Kernighana i Ritchiego.

def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) / 2)
    pivot = left
    for i in range(left + 1, right + 1):
        if L[i] < L[left]:
            pivot = pivot + 1
            swap(L, pivot, i)
    swap(L, left, pivot)
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)


def mediana_sort(L, left, right):
    bucketSort.quicksort(L, left, right)
    mediana = L[len(L)/2]
    print(mediana)

L = listGenerator.random_list(100, 100)
mediana_sort(L, 0, 99)

