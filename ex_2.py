import datetime
import redis

r = redis.Redis(port=6380)

today = datetime.date.today()
visitors = {"dan", "jon", "alex"}
stoday = today.isoformat()

# r.sadd(today, *visitors) # error
r.sadd(stoday, *visitors)
get_members = r.smembers(stoday)
print(get_members)
a = r.scard(today.isoformat())  # get number of elements by key
print(a)
