def seconds_to_hms(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    return f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}"

total_seconds = 1234567
formatted_time = seconds_to_hms(total_seconds)
print(formatted_time)