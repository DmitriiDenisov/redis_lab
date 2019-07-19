import redis

r = redis.Redis(port=6380)
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

a = r.get("Bahamas").decode("utf-8")
print(a)
