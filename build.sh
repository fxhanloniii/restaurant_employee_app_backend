# #Install dependencies
# pip3 install -r deps.txt

# python manage.py collectstatic --no-input
# #Run migrations
# python3 manage.py migrate

# #!/usr/bin/env bash
# set -o errexit
# pip install -r requirements.txt
# python manage.py collectstatic --no-input
# python manage.py migrate

#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
gunicorn restaurant_employee_backend_project.wsgi:application --bind 0.0.0.0:$PORT --workers 4

