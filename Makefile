# ディレクトリ名抽象化したい
app_dir = /home/app
db_dir = /home/db
docs_dir = /home/docs
revision = ""

generate-revision:
	cd ${db_dir} && alembic revision --autogenerate -m ${revision}

generate-schema:
	openalchemy generate ${docs_dir}/openapi.yml ${app_dir}/schema.py

generate-main-models:
	fastapi-codegen \
		--template-dir ${app_dir}/templates \
		--input ${docs_dir}/openapi.yml \
		--output ${app_dir} \
		--generate-routers
