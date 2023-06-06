def is_time_invalid(time):
    if time is None or not isinstance(time, int):
        return True
    return False


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for time in permanence_period:
        if is_time_invalid(time[0]) or is_time_invalid(time[1]):
            return None

        if time[0] <= target_time <= time[1]:
            count += 1

    return count