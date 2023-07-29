import whois

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return str(e)

# Test için örnek bir alan adı
domain_name = "example.com"
whois_data = get_whois_info(domain_name)

if isinstance(whois_data, dict):
    for key, value in whois_data.items():
        print(f"{key}: {value}")
else:
    print(f"WHOIS query failed: {whois_data}")
