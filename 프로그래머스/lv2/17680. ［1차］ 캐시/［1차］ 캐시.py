from collections import deque

def solution(cacheSize, cities):
    answer = 0
    caches = deque(["0"]*cacheSize)
    
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        if city.lower() in caches:
            caches.remove(city.lower())
            caches.append(city.lower())
            answer += 1
        else:
            caches.popleft()
            caches.append(city.lower())
            answer += 5   
        
    return answer