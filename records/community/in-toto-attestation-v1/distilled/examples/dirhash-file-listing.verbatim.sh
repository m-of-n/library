$ find . -type f | cut -c3- | LC_ALL=C sort | xargs -r sha256sum
3a137eef6458bfb76bb2c63fc29ffc7166604d2d2e09ed9d8250a534122a8364  github.com/marklodato/go-hello-world@v0.0.1/README.md
28e7c942a036902d981759d0bf5704d2bfc7cb500caf68b84711b234af01c6a5  github.com/marklodato/go-hello-world@v0.0.1/go.mod
ddc4da627d9a9f45fb29641a1b185d6f53287ecfd921aacbf4fe54b7a86fe8d1  github.com/marklodato/go-hello-world@v0.0.1/main.go
