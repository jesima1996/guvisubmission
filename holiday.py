def main():
    string = str(input("Enter a day of week : "))
    count = 0
    check = string.lower()
    for i in range(0,len(week)):
        if(check == week[i]):
            if(i == 6):
                print(False)
            else:
                print(True)
        else:
            count += 1
            if(count == 7):
                print("Enter a valid day !!!")
                main()

if __name__ == '__main__':
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    main()

    Status API Training Shop Blog About 

    © 2016 GitHub, Inc. Terms Privacy Security
