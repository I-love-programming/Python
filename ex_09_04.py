file_name = input('Enter a file name:')
file_handle = open(file_name)
emails = list()
emails_count = dict()
for line in file_handle:
    line = line.strip()
    if line.startswith('From:'):
        words = line.split()
        domain_name = words[1].split('@')
        emails.append(domain_name[1])
for email in emails:
    emails_count[email] = emails_count.get(email, 0) + 1
print(emails_count)
