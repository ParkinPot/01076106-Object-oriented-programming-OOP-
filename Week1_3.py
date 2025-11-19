def check_time(Inmin, Outmin, Inhr, Outhr):

    Inhr = int(Inhr)
    Inmin = int(Inmin)
    Outhr = int(Outhr)
    Outmin = int(Outmin)

    if Outhr == 24:
        Outhr = 0

    a = Inhr * 60 + Inmin
    b = Outhr * 60 + Outmin

    time_diff = b - a

    if 0 < time_diff <= 15:
        return("0")
    elif a < 0:
        return("Invalid")
    elif Outmin < 0:
        return("Invalid")
    elif 15 <= time_diff <= 180:
        if 0 < Outmin - Inmin <= 60:
            Hr = (Outhr - Inhr) + 1
            return(Hr * 10)
        else:
            Hr = Outhr - Inhr
            return(Hr * 10)
    elif 180 <= time_diff < 360:
        Hr = (Outhr - Inhr - 3)
        if 0 < Outmin - Inmin <= 60:
            Hr = Hr + 1
            return((Hr * 20) + 30)
        else:
            return((Hr * 20) + 30)
    elif time_diff > 360:
        return("200")
    else:
        return("Invalid")

Inhr, Inmin, Outhr, Outmin = input("").split()
output = check_time(Inmin, Outmin, Inhr, Outhr)
print(output)
