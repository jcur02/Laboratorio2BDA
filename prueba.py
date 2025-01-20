from pymongo import MongoClient
import redis
import time

# Create
def test_mongo_create(collection, data):
    start_time = time.time()
    collection.insert_many(data)
    elapsed_time = time.time() - start_time
    return elapsed_time

# Read
def test_mongo_read(collection):
    start_time = time.time()
    _ = collection.find_one({"id": 5000})  
    _ = list(collection.find({"value": {"$gte": 50000}}))  
    _ = collection.aggregate([{"$group": {"_id": None, "total": {"$sum": "$value"}}}])  
    elapsed_time = time.time() - start_time
    return elapsed_time

# Update
def test_mongo_update(collection):
    start_time = time.time()
    collection.update_many({}, {"$set": {"updated": True}})
    elapsed_time = time.time() - start_time
    return elapsed_time

# Delete
def test_mongo_delete(collection):
    start_time = time.time()
    collection.delete_many({})
    elapsed_time = time.time() - start_time
    return elapsed_time

# Create
def test_redis_create(client, data):
    start_time = time.time()
    for item in data:
        hash_key = f"item:{item['name']}" 
        for field, value in item.items():
            client.hset(hash_key, field, value)
    elapsed_time = time.time() - start_time
    return elapsed_time


# Read
def test_redis_read(client):
    start_time = time.time()
    _ = client.hgetall("item:5000") 
    keys = client.keys("item:*")
    _ = [client.hgetall(key) for key in keys if int(client.hget(key, "value")) >= 50000]  
    elapsed_time = time.time() - start_time
    return elapsed_time

# Update
def test_redis_update(client):
    start_time = time.time()
    keys = client.keys("item:*")
    for key in keys:
        if client.hexists(key, "value"):
            client.hset(key, "value", 0)
    elapsed_time = time.time() - start_time
    return elapsed_time

# Delete
def test_redis_delete(client):
    start_time = time.time()
    keys = client.keys("item:*")
    for key in keys:
        client.delete(key)
    elapsed_time = time.time() - start_time
    return elapsed_time

def run_tests():
    # MongoDB setup
    mongo_client = MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["test_db"]
    mongo_collection = mongo_db["test_collection"]

    # Redis setup
    redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Crear datos
    data_for_mongo = [{"id": i, "name": f"Item {i}", "value": i*10} for i in range(1, 10001)]

    data_for_redis = []
    for item in data_for_mongo:
        redis_item = {**item}  
        del redis_item['id']  
        data_for_redis.append(redis_item)

    # MongoDB tests
    print("MongoDB Tests:")
    print(f"Create: {test_mongo_create(mongo_collection, data_for_mongo):.2f} seconds")
    print(f"Read: {test_mongo_read(mongo_collection):.2f} seconds")
    print(f"Update: {test_mongo_update(mongo_collection):.2f} seconds")
    print(f"Delete: {test_mongo_delete(mongo_collection):.2f} seconds")

    # Redis tests
    print("\nRedis Tests:")
    print(f"Create: {test_redis_create(redis_client, data_for_redis):.2f} seconds")
    print(f"Read: {test_redis_read(redis_client):.2f} seconds")
    print(f"Update: {test_redis_update(redis_client):.2f} seconds")
    print(f"Delete: {test_redis_delete(redis_client):.2f} seconds")

run_tests()
