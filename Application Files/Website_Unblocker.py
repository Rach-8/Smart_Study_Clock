
def web_unblock():
    host_path = 'C:/Windows/System32/drivers/etc/hosts'
    with open(host_path,'r+') as file:  
        file.truncate()  

web_unblock()