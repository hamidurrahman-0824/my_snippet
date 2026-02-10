def bills_with_4_slab(unit):
    price = [5,10,15,20,25]
    if unit<=50:
        bill = unit*price[0]
    elif unit<=75:
        bill = 50*5+(unit-50)*price[1]
    elif unit<=125:
        bill = 50*5+25*price[1]+(unit-75)*price[2]
    elif unit<=225:
        bill = 50*5+25*price[1]+50*price[2]+(unit-125)*price[3]
    else:
        bill = 50*5+25*price[1]+50*price[2]+125*price[3]+(unit-225)*price[4]
    return bill

def slab_billing(unit):
    slabs = [(10,2),(20,4),(30,6),(40,8),(50,10),(float('inf'),15)]
    bill = 0
    for limit,price in slabs:
        if unit<=0:
            break
        used = min(unit,limit)
        bill += used*price
        unit -= used
    return bill
i = 10
"""while i<50:
    print(slab_billing(i))
    i+=10"""


def recursive_slab_billing(unit,slabs=None):
    if slabs is None:
        slabs = [(10,2),(20,4),(30,6),(40,8),(50,10),(float('inf'),15)]
    if not slabs or unit<=0:
        return 0
    limit,price = slabs[0]
    used =min(limit,unit)
    return used*price + recursive_slab_billing(unit-used,slabs[1:])
print(recursive_slab_billing(22))
def recursive_bill(unit,slabs=None):
    if slabs is None:
        slabs=[(10,1),(20,2),(40,4),(100,8),(float('inf'),15)]
    if not slabs or unit<=0:
        return 0
    limit, price = slabs[0]
    used = min(limit,unit)
    return used*price+recursive_bill(unit-used,slabs[1:])