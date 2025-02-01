
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    if len(lst) <= 1:
        return True
    increasing = True
    decreasing = True
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
            print('decrease')
        if lst[i] < lst[i - 1]:
            increasing = False
            print('increase')
    return (increasing or decreasing)

def main():
    lstA=[1,1,3,100]
    lstB=[11,1,-9,-10]
    lstC=[2,3,2,3]

    print(monotonic(lstA))
    print(monotonic(lstB))
    print(monotonic(lstC))
main()
