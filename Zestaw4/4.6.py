
def sum_seq(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item,(list,tuple)):
            suma += sum_seq(item)
        else:
            suma += item
    return suma

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print sum_seq(seq)
