import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(^\d{1,2})(:\d{2})? ([A,P]M) to (\d{1,2})(:\d{2})? ([A,P]M)$"
    match = re.search(pattern, s)

    if match:
        hour_start = match.group(1)
        min_start = match.group(2)
        start_letters = match.group(3)
        hour_end = match.group(4)
        min_end = match.group(5)
        end_letters = match.group(6)
        if "AM" in start_letters:
            hour_start = int(match.group(1))
            if hour_start > 12:
                raise ValueError
            elif hour_start == 12:
                hour_start = "00"
            if min_start is None:
                min_start = ":00"
            elif int(min_start[1:]) > 59:
                raise ValueError

        else:
            hour_start = int(match.group(1))
            if hour_start > 12:
                raise ValueError
            elif hour_start != 12:
                hour_start = hour_start + 12

            if min_start is None:
                min_start = ":00"
            elif int(min_start[1:]) > 59:
                raise ValueError

        if "AM" in end_letters:
            hour_end = int(match.group(4))
            if hour_end > 12:
                raise ValueError
            elif hour_end == 12:
                hour_end = "00"
            if min_end is None:
                min_end = ":00"
            elif int(min_end[1:]) > 59:
                raise ValueError
        else:
            hour_end = int(match.group(4))
            if hour_end > 12:
                raise ValueError
            elif hour_end != 12:
                hour_end = hour_end + 12

            if min_end is None:
                min_end = ":00"
            elif int(min_end[1:]) > 59:
                raise ValueError
        return f"{hour_start:02}{min_start} to {hour_end:02}{min_end}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
