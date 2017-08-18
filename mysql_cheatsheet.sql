# https://stackoverflow.com/questions/356578/how-to-output-mysql-query-results-in-csv-format

mysql db_name —user=username —password=password < my_request.sql | sed 's/\t/,/g' > out.csv
