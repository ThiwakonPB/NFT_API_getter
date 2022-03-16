from datetime import datetime

def roundDate(_listedTime):
    # Time from listed time in rankting API
    listed_time = _listedTime

    # convert time from milliseconds to seconds 
    time = listed_time // 1000

    # Convert to date format
    dt = datetime.utcfromtimestamp(time)

    # Round date to the beginning of the day 00:00
    dt = datetime(*dt.timetuple()[:3])

    dt = dt.timestamp()

    dt = dt - (dt % 86400)

    dt = dt * 1000

    return int(dt)
    # print("Next time: ", (int(dt) + 7776000000))
