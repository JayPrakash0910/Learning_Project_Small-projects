# collect email from user
# split the email using the @,the first part as the username, the second part is gone be saved as domain
# split domain using.
# jay414181@gmail.com
def main():
    print("welcome to the email address : ")
    print(" ")
    email_input = input("Enter your EmailAddress : ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("UserName :", username)
    print("Domain :", domain)
    print("extension :", extension)
while True:
    main()
