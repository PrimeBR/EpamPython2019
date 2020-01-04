import redis
import json
import pickle
import pymongo


def redis_handler(data, status):
    r = redis.Redis()
    if status == 1:
        r.set(hash(data), data)
        hashes.append(hash(data))
    else:
        return r.get(data)


def mongo_handler(data, status):
    client = pymongo.MongoClient(host='localhost', port=27017)
    if status == 1:
        db = client['test_db']
        coll = db['test_coll']
        hash_ = coll.insert({'data': data})
        hashes.append(hash_)
    else:
        db = client['test_db']
        coll = db['test_coll']
        res = coll.find_one(data)
        return coll.find_one(res)['data']


def deserialize_json(data):
    return json.loads(data)


def deserialize_pickle(data):
    return pickle.loads(data)


def serialize_json(data):
    return json.dumps(data)


def serialize_pickle(data):
    return pickle.dumps(data)


def set(data, protocol, storage):
    if protocol == 'json':
        data = serialize_json(data)
    elif protocol == 'pickle':
        data = serialize_pickle(data)
    storage_links[storage](data, 1)


def get(data, protocol, storage):
    result = storage_links[storage](data, 2)
    if protocol == 'json':
        return deserialize_json(result)
    elif protocol == 'pickle':
        return deserialize_pickle(result)


storage_links = {'redis': redis_handler, 'mongo': mongo_handler}
hashes = []

if __name__ == '__main__':
    data_ = {"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}
    set(data_, 'pickle', 'redis')
    result = get(hashes[0], 'pickle', 'redis')
    print(result)
    set(data_, 'json', 'mongo')
    result = get(hashes[1], 'json', 'mongo')
    print(result)