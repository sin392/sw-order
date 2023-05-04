# ディレクトリ名抽象化したい
app_dir = /home/app_dir
db_dir = /home/db
docs_dir = /home/docs
revision = ""

generate-revision:
	cd ${db_dir} && alembic revision --autogenerate -m ${revision}

generate-schema:
	openalchemy generate ${docs_dir}/openapi.yml schema.py

generate-main-models:
	fastapi-codegen --input ${docs_dir}/openapi.yml --output ${app_dir}
