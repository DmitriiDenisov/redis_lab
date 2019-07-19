import redis

r = redis.Redis(db=1, port=6380)

# Get info for a particular hat
print(r.hgetall("hat:56854717"))
# Print all hats
print(r.keys())

# Imitate that somebody buys a hat
# r.hincrby("hat:56854717", "quantity", -1)
print(r.hget("hat:56854717", "quantity"))
r.hincrby("hat:56854717", "npurchased", 1) # increase npurchased field
# print(r.hget("hat:56854717", "quantity"))