import threading


import os

#mKing a function for pinging and judging if host is up 
def ping(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"{ip} is up")

    else:
        print(f"{ip} is down")



# target ips obs we can take input   
ip_list = ["8.8.8.8","1.1.1.1"]


#imp topic threads for parralel reqs
threads = []
for ip in ip_list:
    t = threading.Thread(target=ping, args=(ip,))
    t.start()
    threads.append(t)


#for t in threads:
   # t.join()

print("ping scan complete")
