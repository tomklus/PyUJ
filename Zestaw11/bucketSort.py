
import listGenerator
from listGenerator import swap
import time
import timeit
from datetime import datetime
from timeit import default_timer as timer
import math

def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)

# Wersja z wartownikiem wg Sedgewicka.
# Ta wersja jest adaptacyjna.

def insertsort(L, left, right):
    for i in range(right, left, -1):   # ustawiam wartownika
        if L[i-1] > L[i]:
            swap(L, i-1, i)
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:   # robimy miejsce na item
            L[j] = L[j-1]
            j = j-1
        L[j] = item

# Wersja ulepszona wg Susly.
def bubblesort(L, left, right):
    limit = right
    while True:
        k = left-1   # wskaznik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
                k = i
        if k > left:
            limit = k
        else:
            break

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


def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) / 2
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie

def merge(L, left, middle, right):

    n1 = middle - left + 1
    n2 = right - middle
    A = [None] * (n1 + 1)
    B = [None] * (n2 + 1)
    for i in range(n1):
        A[i] = L[left + i]
    for i in range(n2):
        B[i] = L[middle + 1 + i]
    A[n1] = float("inf")   # wartownik
    B[n2] = float("inf")   # wartownik
    i, j = 0, 0
    for k in range(left, right+1):
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1

