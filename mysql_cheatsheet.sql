-- https://stackoverflow.com/questions/16834880/mysql-export-resultset-as-csv-from-remote-server

mysql -umysqlusername -pmysqlpass databasename -B -e "select * from \`tablename\`;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > mysql_exported_table.csv

-- https://stackoverflow.com/questions/4743419/mysql-dump-to-localhost-outfile-from-a-remote-database

mysql -u test -pfoo --database test -h testdb201.name.host.com --port 3306 -ss -e "SELECT 'a','b','c' UNION SELECT col1, col2, col3 " | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > myDump.csv

# https://stackoverflow.com/questions/356578/how-to-output-mysql-query-results-in-csv-format

mysql db_name —user=username —password=password < my_request.sql | sed 's/\t/,/g' > out.csv
