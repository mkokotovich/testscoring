release: backend/one_time_user_upgrade.sh && python backend/manage.py migrate --no-input
web: bin/start-nginx sh -c 'cd backend && exec python server.py'
