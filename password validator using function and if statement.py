#!/usr/bin/env python
# coding: utf-8

# # password validator using function and if statement

# In[ ]:


pw = input("Enter your new password: ")
rp = input("Renter your password for confirmation: ")
def confam(pw,rp):
    if pw == rp:
        print("Password Confirmed")
    else:
        print("You will need to renter the password, Thanks")
confam(pw,rp)        
        

