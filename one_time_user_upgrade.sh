#!/bin/sh
set -xe

echo "INSERT INTO django_migrations (app, name, applied) VALUES ('evaluators', '0001_initial', CURRENT_TIMESTAMP);" | python backend/manage.py dbshell
echo "UPDATE django_content_type SET app_label = 'evaluators' WHERE app_label = 'auth' and model = 'user';" | python backend/manage.py dbshell
