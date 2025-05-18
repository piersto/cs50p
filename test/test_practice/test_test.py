def test_test():

    time_start = 0
    inserted_time = "9:00 AM to 5:00 PM"
    if "AM" in inserted_time:
        time_start = int(inserted_time[0:1])

    print(f"{time_start:02}")
