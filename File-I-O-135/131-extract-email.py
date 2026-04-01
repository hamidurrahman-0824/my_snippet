import re
email_pattern = r'^[A-Za-z0-9\.+-_%]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'#'^$' strictly follows from start to end
pat = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
#[before@portion,can contain included special char]+more than1@onlyone@[subdomain can like edu.org.ca]
match = re.match(pat,"linebyline")
findall = re.findall(pat,"at a time whole file->list of found pat")
def is_email(e):
    pat = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})$"
    return bool(re.match(pat,e))
    