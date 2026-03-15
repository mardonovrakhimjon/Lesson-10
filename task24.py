email = str(input("email: "))

a = email.count("@") == email.endswith(".com")
print(a)