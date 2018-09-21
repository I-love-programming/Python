file_name = input('Enter a file name:')
file_handle = open(file_name)
emails = list()
emails_count = dict()
maxnumber = None
for line in file_handle:
    line = line.strip()
    if line.startswith('From:'):
        words = line.split()
        emails.append(words[1])
for email in emails:
    emails_count[email] = emails_count.get(email, 0) + 1
for email in emails_count:
    if maxnumber is None or maxnumber < emails_count[email]:
        maxnumber = emails_count[email]
        maxemail = email
print(maxemail, maxnumber)
