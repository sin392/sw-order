# ディレクトリ名抽象化したい
root_dir = /home
app_dir = ${root_dir}/app
db_dir = ${root_dir}/db
openapi_dir = ${root_dir}/docs/openapi
templates_dir = ${root_dir}/templates

revision = ""

generate-revision:
	cd ${db_dir} && alembic revision --autogenerate -m ${revision}

generate-schema:
	openalchemy generate ${openapi_dir}/openapi.yml ${app_dir}/infra/schema.py

generate-code:
	# NOTE: routersを有効化するとtemplateが機能しなくなる（デフォルトが強制される）
	# NOTE: fastapi-codegenはoasの相対importをカレントディレクトリ基準で解決するのでcd
	cd ${openapi_dir} && \
	fastapi-codegen \
		--template-dir ${templates_dir} \
		--input ${openapi_dir}/openapi.yml \
		--model-file ${app_dir}/interface/handler/dto.py \
		--output ${app_dir}
		# --generate-routers
	sed -i -e 's/from \./from interface.handler./' ${app_dir}/main.py

migrate-up:
	cd ${db_dir} && alembic upgrade head

migrate-down:
	cd ${db_dir} && alembic downgrade base
