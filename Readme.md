## Redis container

- Run: `docker run -p 6379:6379 --name redis-container -d redis`
- Test : `docker exec -it redis-container redis-cli ping`
