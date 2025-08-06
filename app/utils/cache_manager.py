"""Redis caching utilities."""
import redis
from config.settings import settings
import json

redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def cache_set(key: str, value: dict, ttl: int = 3600):
    redis_client.setex(key, ttl, json.dumps(value))

def cache_get(key: str):
    val = redis_client.get(key)
    return json.loads(val) if val else None