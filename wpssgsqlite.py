import sys
import re
import collections
import sqlite3
assert len(sys.argv) >= 4
conn = sqlite3.connect(sys.argv[1])
sqlddl = open(sys.argv[2]).read()
sqldata = open(sys.argv[3]).read()
cur = conn.cursor()
cur.executescript(sqlddl)
conn.commit()
data = collections.defaultdict(list)
pythoncode = re.sub(r'^INSERT INTO `(.+?)` VALUES (.+);$', r'data["\1"].append(\2)', sqldata, flags = re.MULTILINE)
exec(pythoncode, dict(data = data))
for tbl, tuples in data.items():
    cur.executemany(f' INSERT INTO `{tbl}` VALUES (' + ('?,' * len(tuples[0])).rstrip(',') + ');', tuples)
conn.commit()
# cannot just pipe the sqldata to sqlite3 because of this mysqldump bug: https://bugs.mysql.com/bug.php?id=65941 which escapes single quotes with backslashes which breaks sqlite3 binary
