'''
Implement a small in-memory cache class, TTLCache.

Requirements:

TTLCache(capacity: int, ttl_seconds: float)
put(key, value) stores a value. If the cache is already at capacity, evict the least recently used entry to make room.
get(key) returns the value, or None if the key is missing or expired. A successful get counts as a "use" for the LRU ordering.
An entry expires ttl_seconds after it was last put. Expired entries must never be returned.
__len__ returns the number of live (non-expired) entries.
'''
