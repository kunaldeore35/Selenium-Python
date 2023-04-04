from fbhw import Fbusr

user = Fbusr("https://www.facebook.com/")
user.eml("59846010033596")
user.pwd("lsspl#123")
user.login()
print(user.chkusr("Shinigami"))