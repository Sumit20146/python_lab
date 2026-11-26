import re

passwords = ["Python@123", "python123"]

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$!]).+$'

for p in passwords:
    if re.match(pattern, p):
        print(p, "- Valid password")
    else:
        print(p, "- Invalid password")
