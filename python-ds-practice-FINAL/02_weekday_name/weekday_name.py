def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    Weekday = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat",]

    if day_of_week > 7 or day_of_week < 1:
        return f"That's not a day of the week!"

    return Weekday[day_of_week - 1]
