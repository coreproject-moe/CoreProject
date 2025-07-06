async def decode_dictionary(data):
    if isinstance(data, dict):
        return {k.decode(): await decode_dictionary(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [await decode_dictionary(i) for i in data]
    elif isinstance(data, bytes):
        return data.decode()
    else:
        return data
