



 



def web_block(websites):
    host_path = 'C:/Windows/System32/drivers/etc/hosts'
    redirect = "127.0.0.1" 
    fileptr =  open(host_path,"r+")
    content = fileptr.read()  
    for website in websites:  
        if website in content:  
            pass  
        else:  
            fileptr.write(redirect+"    "+website+"\n")  
            fileptr.write(redirect+"    "+'www.'+website+"\n") 
web_block(L)