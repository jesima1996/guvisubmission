def convert(check):
    a = (check.split(':'))
    minute = int(a[0],10)*60+int(a[1],10)
    return minute

def find(a,b):
    x = convert(a)
    y = convert(b)
    return y - x

def main():
    time1 = str(input("Enter the min time in 24 hr-format(HH:MM) : "))
    time2 = str(input("Enter the maxtime in 24 hr-format(HH:MM) : "))
    ans = find(time1,time2)
    print("The Minute difference is : %d"%ans)

if __name__ == '__main__':
    main()
