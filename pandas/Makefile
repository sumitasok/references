PROJECT_NAME := "pandas"

.PHONY: setup

setup:
	@mkdir -p ~/.mysql_data_dir
	@ls ~/.mysql_data_dir

open_mysql:
	@docker exec -it pandas_data_1 bash

open_pandas:
	@docker run -it -v `pwd`:/app  --link pandas_db_1:db --net pandas_default pandas_pandas bash
