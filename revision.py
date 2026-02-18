def slab_bill(unit:(int|float)) -> (int|float):
    if unit<=0:
        return 0
    slabs = [(10,2),(15,3),(20,5),(50,9),(100,14),(float('inf'),25)]
    bill = 0
    for slab in slabs:
        u,price = slab
        used = min(u,unit)
        bill += used * price
        unit-=used
    return bill
print(slab_bill(300.45))
def recr_slab_bill(unit,slabs=None):
    if slabs is None:
        slabs = [(10,2),(15,3),(20,5),(50,9),(100,14),(float('inf'),25)]

    if unit<=0 or not slabs:
        return 0
    
    used = min(unit,slabs[0][0])
    unit-=used
    return used*slabs[0][1]+recr_slab_bill(unit, slabs[1:])
print(recr_slab_bill(300.45))