from parser.staff import StaffParser

import httpx

res = httpx.get("https://myanimelist.net/people/26543")

x = StaffParser(res.text)
