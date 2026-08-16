import time

def hours_minutes_seconds_counter():
    """
        hms is Hours-Minutes-Seconds
    """
    print("--- COUNTDOWN TIMER ---")
    hms = input("Input time in HH:MM:SS format (for example -> 08:05:23): ")
    print_method = input("Do you want to print the countdown with new lines? (y/n): ").strip().lower()
    
    try:
        parts = hms.split(":")
        if len(parts) != 3:
            raise ValueError
            
        hours, minutes, seconds = map(int, parts)
        
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        if total_seconds <= 0:
            print("Please enter a time greater than zero.")
            return hours_minutes_seconds_counter()

        for i in range(total_seconds, 0, -1):
            # I used integer division (//) to get the number of hours, minutes, and seconds from the total seconds.
            h = i // 3600
            m = (i % 3600) // 60
            s = i % 60
            
            # I used f-string formatting to ensure that hours, minutes, and seconds are always displayed with two digits.
            if print_method == "y":
                print(f"{h:02d}:{m:02d}:{s:02d}")
            else:
            # I used end="\r" to overwrite the same line in the console, not to create new line
                print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")
            time.sleep(1)
            
        print("00:00:00\nTime is up!!!")

    except ValueError:
        print("Invalid format! Please use HH:MM:SS (for example -> 08:05:23).")
        hours_minutes_seconds_counter()

hours_minutes_seconds_counter()