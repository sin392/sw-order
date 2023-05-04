# ディレクトリ名抽象化したい
app_dir = /app_dir
db_dir = /root/db
docs_dir = /root/docs
revision = ""

generate-revision:
	cd ${db_dir} && alembic revision --autogenerate -m ${revision}

generate-schema:
	openalchemy generate ${docs_dir}/openapi.yml schema.py

generate-main-models:
	fastapi-codegen --input ${docs_dir}/openapi.yaml --output ${app_dir}
