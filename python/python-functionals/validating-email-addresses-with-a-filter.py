import re


email_regex = re.compile(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$')
emails = [raw_input() for email in range(int(raw_input()))]
print sorted(filter(lambda email: re.match(email_regex, email), emails))
