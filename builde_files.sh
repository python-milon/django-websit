
echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear You, now. Uncommitted changes
echo "BUILD END"
