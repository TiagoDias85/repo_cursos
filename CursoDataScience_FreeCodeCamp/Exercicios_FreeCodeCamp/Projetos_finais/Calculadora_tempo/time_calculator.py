def add_time(start, duration, day=None):
    def parse_time(time):
        time_parts = time.split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1][:2])
        period = time_parts[1][2:].strip() if len(time_parts) > 1 else None

        return hour, minute, period

    def format_time(hour, minute, period):
        hour = hour % 12
        hour = hour if hour != 0 else 12
        minute_str = str(minute).zfill(2)
        period_str = period.upper() if period else ""
        return f"{hour}:{minute_str} {period_str}"

    start_hour, start_minute, start_period = parse_time(start)
    duration_hour, duration_minute, _ = parse_time(duration)

    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    if end_minute >= 60:
        end_hour += 1
        end_minute -= 60

    days_passed = end_hour // 24
    end_hour = end_hour % 24

    periods_passed = end_hour // 12
    end_hour = end_hour % 12

    if end_hour == 0:
        end_hour = 12

    if periods_passed % 2 == 1:
        if start_period == "AM":
            start_period = "PM"
        else:
            start_period = "AM"
            days_passed += 1

    for _ in range(days_passed):
        day = get_next_day(day)

    new_time = format_time(end_hour, end_minute, start_period)

    if day:
        new_time += f", {day.capitalize()}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time


def get_next_day(day):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if day:
        index = days.index(day.lower())
        next_index = (index + 1) % 7
        return days[next_index]
    else:
        return None
