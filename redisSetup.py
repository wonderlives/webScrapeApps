import redis

# Redis Set-up
redisHost = "test-001.6lkeyx.0001.usw2.cache.amazonaws.com"
redisPort = 6379
redisDb = 0

# Create Redis
redis = redis.StrictRedis(host=redisHost, port=redisPort, db=redisDb)

# Test Redis Working
# for i in range(10000):
#     redis.sadd("testItem", i)
#     k = redis.spop("testItem")
#     print(k.decode('utf-8'))

# Add url to Redis queue
def addToRedis(url):
    item = url
    return redis.sadd("Col", item)

# Pop url from Redis queue
def removeFromRedis():
    return redis.spop()


