# port scanner using threading

import threading
import socket

# functions for port scanning

def port_scan(ip,port,filename):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            output = f"port {port} is open\n"
            with open(filename, "a") as f:
                f.write(output)
            print(output)

    except Exception as e:
        print(f" error scanning port : {port}")
        # print(e) for debuging error i got in socket.connect_ex well it fix now


target = input("enter ip addr or domain name :").strip()
port_choice = input("enter ports seprated by comma otherwise ports are default 1-1024 :").strip()
filename = input("enter file name to save results :").strip()



try:
    target_ip = socket.gethostbyname(target)
    print(f"target is {target_ip} ({target})")

except Exception as e:
    print(f"unable to resolve target: {target}")
    exit()


if port_choice:
    try:
        port_list = [ int(p) for p in port_choice.split(",") if p.isdigit()]
    except Exception as e:
        print(f"invalid port input. using default (1-1024)")
        port_list = range(1,1024)


else:
    port_list = range(1,1024)



with open(filename, "w") as f:
    f.write(f"scan results for  {target} ({target_ip})\n")
    f.write("=" * 50 +"\n")



def threaded_scan():
    threads =[]
    for port in port_list:
        t = threading.Thread(target=port_scan, args =(target_ip, port, filename))
        t.daemon = True
        t.start()
        threads.append(t)


    for t in threads:
        t.join()


    print(f"port scan complete results save to {filename}")



threaded_scan()

