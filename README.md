# sam

## Developpment

- Create venv, postfixed with "-env", activate it and install dependancies.

```python
python3 -m venv dev-env
source dev-env/bin/activate
pip install -r requirements.txt
```

- apply migration
  `python manage.py migrate`
- run projet
  `python manage.py runserver`
