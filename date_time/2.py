# Today Is "2025, 1, 1"

"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"

import datetime 
now= datetime.datetime(2025,1,1)
print(f"{now.year}-{now.month}-{now.day}")
print(now.strftime("%b")+f" {now.month},{now.year}")
print(f"{now.month}-{now.strftime("%b")}-{now.year}")
print(f"{now.month}/{now.strftime("%b")}/{now.strftime("%y")}")
print(f"{now.month}/{now.strftime("%B")}/{now.strftime("%Y")}")
print(f"{now.strftime("%a")}/{now.strftime("%B")}/{now.strftime("%Y")}")
