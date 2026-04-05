# Java

Solutions and notes for Java.

## Compile and run inside the container

From the project root:

```bash
docker compose exec dev bash -lc 'mkdir -p languages/java/bin && javac -d languages/java/bin languages/java/src/ContainsDuplicate.java && java -cp languages/java/bin ContainsDuplicate'
```
