#!/bin/bash
set -euo pipefail

HOSTNAME="https://testscoring.fly.dev"
USER_ENDPOINT="${HOSTNAME}/api/users/v1/"

echo "Creating new user"
echo "Please enter username (typically first name):"
read username
echo "Enter password:"
read -s password

curl -X POST -H "Content-Type: application/json" -d '{"username": "'${username}'", "password": "'${password}'"}' ${USER_ENDPOINT}
echo
