$ printf 'blob 5\0Hello' | sha1sum | cut -f1 -d' '
5ab2f8a4323abafb10abb68657d9d39f1a775057
$ printf 'Hello' | git hash-object -t blob --stdin
5ab2f8a4323abafb10abb68657d9d39f1a775057
