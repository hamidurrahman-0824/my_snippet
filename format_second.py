def format_second(sec):
    if sec<0:
        return sec
    hour, reminder = divmod(sec,3600)
    minute,second = divmod(reminder,60)
    return f"{hour:02d}:{minute:02d}:{second:02d}"
print(format_second(3670))