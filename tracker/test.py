import urllib.parse

# Extract the info_hash parameter from the query
info_hash_encoded = "%234%e7%ad%97%e1%83%7br%dd%5e%1a%0a%f2%03%d0%d9l%dbj"

# Decode the URL encoding
info_hash_bytes = urllib.parse.unquote_to_bytes(info_hash_encoded)

# Print the result
print(f"{repr(info_hash_bytes)}")
