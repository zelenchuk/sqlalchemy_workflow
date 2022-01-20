# sqlalchemy_workflow
Create project for my work



## Open DB to connection

1. `cd /etc/postgresql/12/main/`

2. `sudo mcedit postgresql.conf`

3. `listen_addresses = '*'`

Edit and save file

4. `sudo mcedit pg_hba.conf`

5. `host  all  all 0.0.0.0/0 md5`

Edit and save file

6. `sudo systemctl restart postgresql`

7. Enjoy 