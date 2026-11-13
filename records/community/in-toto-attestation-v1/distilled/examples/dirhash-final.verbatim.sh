$ find . -type f | cut -c3- | LC_ALL=C sort | xargs -r sha256sum | sha256sum | cut -f1 -d' '
2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8f
