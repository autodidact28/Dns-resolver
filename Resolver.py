import dns.resolver

# Get the domain from the user
domain = input("Enter a domain: ")

try:
    # Resolve the domain using A record to get IP addresses
    answers = dns.resolver.resolve(domain, 'A')

    # Iterate through the answers and print the IP address and IP version
    for answer in answers:
        ip_version = 'IPv4'
        print(f"{ip_version} address: {answer.to_text()}")

except dns.resolver.NoAnswer:
    print(f"No A records found for {domain}")

except dns.resolver.NXDOMAIN:
    print(f"Domain {domain} does not exist")

except dns.resolver.Timeout:
    print("DNS query timed out")

# Add exception handling for other possible exceptions
except dns.resolver.NoNameservers:
    print("No DNS servers available")

except dns.resolver.YXDOMAIN:
    print("Domain name does not exist or is not configured")

except dns.resolver.YXRRSET:
    print("RRSet with such owner name already exists")

except dns.resolver.Refused:
    print("DNS server refused the query")

except dns.resolver.NotImplemented:
    print("Feature not implemented")
