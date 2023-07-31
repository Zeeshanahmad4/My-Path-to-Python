
scp -i /path/to/your/key.pem username@remote:/path/to/remote/file /local/directory

chmod 400 /path/to/your/key.pem


createdb -U postgres financebro_local
pg_restore -d financebro_local -F c -C < /path/to/db_dump.sql
