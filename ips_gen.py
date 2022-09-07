import random
import concurrent.futures

print ("""
░██████╗░██╗░░░██╗███╗░░██╗███╗░░██╗██╗░░░██╗
██╔════╝░██║░░░██║████╗░██║████╗░██║██║░░░██║
██║░░██╗░██║░░░██║██╔██╗██║██╔██╗██║██║░░░██║
██║░░╚██╗██║░░░██║██║╚████║██║╚████║██║░░░██║
╚██████╔╝╚██████╔╝██║░╚███║██║░╚███║╚██████╔╝
░╚═════╝░░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝░╚═════╝░

""")

length = int(input("Enter The Amount: "))
thread = int(input("\nThread: "))


IPS = ""

def gen():
    global IPS
    make = f"{random.randint(000,255)}.{random.randint(000,255)}.{random.randint(000,255)}.{random.randint(000,255)}"
    IPS += make + "\n"
    

with concurrent.futures.ThreadPoolExecutor(max_workers=(thread)) as executor:
        worker_to_queue = {
            executor.submit(gen): x for x in range(length)
        }
        for worker in concurrent.futures.as_completed(worker_to_queue):
            worker_to_queue[worker]

with open('ips.txt', 'w') as f:
    f.write(IPS)
print("Generated Successfully\nSaved In ips.txt\nMade By @Gunnu_xD")