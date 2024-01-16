def main():
    print(convert_dates())

def convert_dates():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    ans =""
    while True:
        date = input("Date: ")
        date = "".join(char for char in date if char.isalnum() or char == " " or char == "/")

        month = "".join(char for char in date if char.isalpha())
        if month  == "":
            m,d,y = date.split("/")
            if int(d)<10:
                d = "0"+d
            if int(m)<10:
                m = "0"+m
            if 1 <= int(m) <=12:
                ans = y+"-"+m+"-"+d
                return ans
        else:
            if month.lower().capitalize() in months and date.find(month) == 0:
                m =  str(months.index(month.lower().capitalize()) +1)
                date = date.removeprefix(month)
                d,y = date.strip().split(" ")
                d  = "".join(char for char in d if char.isdigit())
                y = "".join(char for char in y if char.isdigit())
                if int(d)<10:
                    d = "0"+d
                if int(m)<10:
                    m = "0"+m
                ans = y+"-"+m+"-"+d
                return ans
                    
        
            
main()