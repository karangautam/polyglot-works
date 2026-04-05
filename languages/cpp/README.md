# C++

Solutions and notes for C++.

## Compile and run inside the container

From the project root:

```bash
docker compose exec dev bash -lc 'mkdir -p languages/cpp/bin && g++ -O2 -std=c++17 languages/cpp/src/contains_duplicate.cpp -o languages/cpp/bin/contains_duplicate && ./languages/cpp/bin/contains_duplicate'
```
