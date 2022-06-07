import re
from datetime import datetime

pattern = r'GET /images/stands/TH_photo_[0-9]+\.jpg HTTP/1\.1'

file_name = "access.txt"
date = '%d/%b/%Y:%H:%M:%S'
date_from = datetime.strptime('24/Mar/2009:14:39:35', date)
date_to = datetime.strptime('25/Mar/2009:11:43:29', date)
file = open(file_name, 'r')
lines = file.readlines()

count = 0
for line in lines:
    count += 1
    split_line = re.split(pattern, line)

print(count)
