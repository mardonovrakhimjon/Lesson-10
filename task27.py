email = str(input("email: "))

a = email.endswith(".pdf") or email.endswith(".docx") or email.endswith(".txt")
print(a)