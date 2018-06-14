PROJECT_NAME := "pandas"

.PHONY: setup build_pandas

setup:
	@mkdir -p ~/.mysql_data_dir
	@ls ~/.mysql_data_dir

open_mysql:
	@docker exec -it pandas_data_1 bash

open_pandas:
	@docker run -it -v `pwd`:/app  --link pandas_db_1:db --net pandas_default pandas_pandas bash

build_p:
	@docker build -t pandas_app .

run_d:
	@docker run -v "/Users/sumitasok/arena/src/github.com/sumitasok/references/pandas:/app" -it pandas_app  /bin/sh
