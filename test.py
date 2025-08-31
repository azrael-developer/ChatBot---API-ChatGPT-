import certifi, ssl, socket

hostname = "api.openai.com"
context = ssl.create_default_context(cafile=certifi.where())

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print("✅ SSL funcionando com:", ssock.version())
