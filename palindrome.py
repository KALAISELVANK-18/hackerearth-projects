
test = int(input())


def isdate(year, date, month):
    if year < 1 or year > 9999:
        return False
    else:
        if month > 12 or month < 1:
            return False
        elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if date <= 31 and date > 0:
                return True
            else:
                return False
        elif month == 4 or 6 or 9 or 11:
            if date <= 30 and date > 0:
                return True
            else:
                return False
        elif month == 2:
            if year % 4 == 0 and year % 100 == 0:
                if year % 400 == 0:
                    if date < 30:
                        return True
                    else:
                        return False
            if year % 4 == 0 and year % 100 != 0:

                if date < 29:
                    return True
                else:
                    return False


zoo = None
for i in range(test):
    date = input()
    case = []
    if date[4] == '0':
        if date[5] == '0':
            if date[6] == '0':
                year = int(date[-1])
    if date[4] == '0':
        if date[5] == '0':
            if date[6] != '0':
                year = int(date[6:8])

    if date[4] == '0':
        if date[5] != '0':
            if date[6] != '0':
                year = int(date[5:8])
    if date[4] != 0:
        year = int(date[4:8])

    for z in range(0, year + 1):

        yea = str(z)

        if len(yea) == 1:
            yea = '000' + yea

        elif len(yea) == 2:
            yea = '00' + yea
        elif len(yea) == 3:
            yea = '0' + yea
        else:
            pass
        rev = yea[::-1]

        if rev[0] == '0' and rev[1] != '0':
            dat = rev[1]

        elif rev[0] == '0' and rev[1] == '0':
            dat = 0
        else:
            dat = rev[0:2]

        if rev[2] == '0' and rev[3] != '0':
            month = rev[3]
        elif rev[2] == '0' and rev[3] == '0':
            month = 0
        else:

            month = rev[2:4]
        rev += yea

        if isdate(z, int(dat), int(month)) is True:
            zoo = rev
            case.append(zoo)

    if len(case) != 0:
        if case[-1] == date:
            if len(case) > 2:
                print(case[-2])
            elif len(case) == 1:
                print(-1)
        elif zoo[4:8] == date[4:8]:
            if zoo[2:4] < date[2:4]:
                print(zoo)
        elif zoo[4:8] == date[4:8]:
            if zoo[2:4] == date[2:4]:
                if zoo[0:2] < date[0:2]:
                    print(zoo)
                else:
                    if len(case) > 2:
                        print(case[-2])
                    elif len(case) == 1:
                        print(-1)
        else:
            print(case[-1])
    elif len(case) == 0:
        print(-1)
