import threading
import requests
import queue
import sys
import readline


def check_subdomain(domain):
    while not q.empty():
        sub = q.get()
        url = f"https://{sub}.{domain}"




        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                done = (f"discovered subdomain: {url}")
                print(done)
                with open(output_file, "a") as f:
                    f.write(done +"\n")

        except reuests.exceptions.RequestException:
            pass


        q.task_done()



try:
    def main():
        domain = input("Enter the domain to check for subdomains: ").strip()
        wordlist_file = input("Enter the path to the wordlist file: ").strip()
        output_file = input("Enter the path to the output file: ").strip()


        try:
            with open(wordlist_file, 'r') as f:
                subdomains = [line.strip() for line in f.readlines()]

        except Exception as e:
            print(f"error is{e}")
            print(f"please check the wordlist file and try again.")
            return


        q = queue.Queue()
        for sub in subdomains:
            q.put(sub)

        threads = []
        num_threads = int(input("enter speed:"))

        for s in range(num_threads):
            s = threading.Thread(target=check_subdomain, args=(domain,))
            threads.append(s)
            s.start()


        for s in threads:
            s.join()


        print("scan completed. check the output file for results.")


    

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("\n[] scan interrupted  Exiting...")
    print("happy hacking")
    sys.exit(0)


            