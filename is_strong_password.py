def is_strong_password(password):
    if len(password)<8:
        return False
def strong_password(p):
    if len(p) < 8:
        return False
    
    has_upper = any(c.isupper() for c in p)
    has_lower = any(c.islower() for c in p)
    has_digit = any(c.isdigit() for c in p)
    has_special = any(not c.isalnum() for c in p)

    return has_upper and has_lower and has_digit and has_special


print(strong_password("Abc@1234"))   # True
print(strong_password("abc123"))     # False
def strong_password(p):
    return (
        len(p) >= 8 and
        any(c.isupper() for c in p) and
        any(c.islower() for c in p) and
        any(c.isdigit() for c in p) and
        any(not c.isalnum() for c in p)
    )