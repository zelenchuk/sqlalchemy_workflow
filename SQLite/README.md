# Work with SQLite DB

Documentation - https://www.sqlite.org/datatype3.html

Tutorials - https://www.sqlitetutorial.net/


## Links

1. DB Browser for SQLite - https://sqlitebrowser.org/dl/

2. Example - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/database.py



## QUERIES


- SELECT * FROM cost WHERE type=1

- INSERT INTO cost (title, value, type, date) VALUES ('Аренда жилья', 7800, 1, datetime('now'))

- 



## Notes

- Datetime like SQLite default

```
from datetime import datetime

datetime.now().strftime("%Y-%m-%d %H:%M:%S")
``` 
 