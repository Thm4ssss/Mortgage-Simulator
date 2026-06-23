def monthly_payment(p,r,n):
    return p*r*((1+r)**n)/((1+r)**n-1)

def deferred_monthly_payment(p,r,d):
    if d==0:
        return 0
    return p*r

def total_deferred_amount(d_m,d):
    return d_m*d
    
