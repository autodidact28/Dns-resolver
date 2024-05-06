import dns.resolver

domain = 'google.com'
try:
    answers = dns.resolver.resolve(domain, 'A')
    for answer in answers:
        print(answer.to_text())
except dns.resolver.NoAnswer:
    print("No A records found for", domain)
except dns.resolver.NXDOMAIN:
    print("Domain", domain, "does not exist")
except dns.resolver.Timeout:
    print("DNS query timed out")
