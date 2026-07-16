import requests

print("=" * 50)
print("        SECURITY HEADERS CHECKER")
print("=" * 50)

url = input("Enter Website URL (e.g., https://example.com): ").strip()

# Add https:// if the user forgets it
if not url.startswith(("http://", "https://")):
    url = "https://" + url

print(f"\nChecking security headers for: {url}\n")

security_headers = {
    "Content-Security-Policy": "Prevents XSS attacks",
    "Strict-Transport-Security": "Forces HTTPS connections",
    "X-Frame-Options": "Protects against Clickjacking",
    "X-Content-Type-Options": "Prevents MIME type sniffing",
    "Referrer-Policy": "Controls referrer information",
    "Permissions-Policy": "Restricts browser features"
}

try:
    response = requests.get(url, timeout=10)

    print("=" * 50)

    for header, description in security_headers.items():
        if header in response.headers:
            print(f"✅ {header:<30} Present")
        else:
            print(f"❌ {header:<30} Missing")

    print("=" * 50)
    print("Scan Completed Successfully.")

except requests.exceptions.RequestException as e:
    print("\nError:", e)
