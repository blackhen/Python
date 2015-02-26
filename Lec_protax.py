"""Lecture_ProgressiveTax"""
def pro_tax(num):
    """for calculate tax"""
    if num <= 150000:
        box = 0
    elif num > 150000 and num <= 300000:
        box = (num-150000)*0.05
    elif num > 300000 and num <= 500000:
        box = 7500+(num-300000)*0.10
    elif num > 500000 and num <= 750000:
        box = 7500+20000+(num-500000)*0.15
    elif num > 750000 and num <= 1000000:
        box = 7500+20000+37500+(num-750000)*0.20
    elif num > 1000000 and num <= 2000000:
        box = 7500+20000+37500+50000+(num-1000000)*0.25
    elif num > 2000000 and num <= 4000000:
        box = 7500+20000+37500+50000+250000+(num-2000000)*0.30
    elif num > 4000000:
        box = 7500+20000+37500+50000+250000+600000+(num-4000000)*0.35
    return int(box)
print pro_tax(input())
