# This version was submitted as final one.

def main():
    list_of_months = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"
                      ]
    date = input_date()
    try:
        if date[-5] == "/":
            m, d, y = date.strip().split("/")
            if not m.isdigit():
                input_date()

            else:
                m = int(m)
            d = int(d)
            if 0 < d < 32 and 0 < m < 13:
                print(f"{y}-{m:02}-{d:02}")
                exit()
            else:
                input_date()

        else:
            try:
                date = date.strip()
                m, d, y = date.split(" ")
                m = m.strip()
                d = d.strip()
                y = y.strip()
                if date[-6] != ",":
                    input_date()
                else:
                    d = d.replace(",", "")
                    if not d.isdigit():
                        input_date()
                    else:
                        d = int(d)
                if not 0 < d < 32:
                    input_date()

                if m.find(","):
                    m = m.replace(",", "")
                if m in list_of_months:
                    m = (list_of_months.index(m)) + 1
                    print(f"{y}-{m:02}-{d:02}")
            finally:
                exit()
    except ValueError:
        input_date()


def input_date():
    date = input("Date: ")
    date = date.strip()
    return date


main()
