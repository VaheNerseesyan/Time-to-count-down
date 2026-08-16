import time

def hours_minutes_seconds_counter():
    """
        hms is Hours-Minutes-Seconds
    """
    hms = input("Input time with hours:minutes:seconds format to count down ! ")
    while True:
        hours_minutes_seconds = hms.split(":")

        if len(hours_minutes_seconds[1]) != 2 or len(hours_minutes_seconds[2]) != 2 or not len(hours_minutes_seconds[0]) >= 2:
            
            print("Invalid time format, please try again :( ")
            return hours_minutes_seconds_counter()
        else:
            loop_count = int(hours_minutes_seconds[0])*3600 + int(hours_minutes_seconds[1])*60 + int(hours_minutes_seconds[2])

            for i in range(loop_count, 0, -1):
                hours = i // 3600
                minutes = (i % 3600) // 60
                seconds = i % 60
                time.sleep(1)

                print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

hours_minutes_seconds_counter()