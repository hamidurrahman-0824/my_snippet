def validate_email(email):
    if '@' not in email:
        return False
    local, domain = email.split('@')
    if '.' not in domain:
        return False
    return True
#print(validate_email('majed@gmail.com'))
import re
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))
print(validate_email('hamidurmajed@gmail.com'))
pattern = r'^[A-Za-z0-9.%+-_]+@[A-Za-z0-9]+\.[A-Za-z]{2,}$'