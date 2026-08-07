from collections import Counter

with open("auth.log", "r") as file:
    logs = file.readlines()

failed = 0
ips = []

for line in logs:
    if "Failed login" in line:
        failed += 1
        ip = line.split()[-1]
        ips.append(ip)

print("Failed Logins:", failed)

count = Counter(ips)

print("\nSuspicious IPs:")
for ip, num in count.items():
    print(ip, "-", num)