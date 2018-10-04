# testscoring

### Local Development
To bring up the backend: `docker-compose up`. Then run `scripts/first_run.sh` to apply initial migrations and create a test user.

To bring up UI: `cd ui; yarn start`

### Adding new assessments
To add new assessments, create an assessment class and add it to the "assessments" list in `backend/apps/testing/v1_views.py`. See another assessment for an example and the comments in `backend/apps/testing/utils.py`

Once the assessment class has been created, a slug and readable name need to be added to the `TEST_TYPE_CHOICES` field in the Test model in `backend/apps/testing/models.py`. Again, just follow the patterns that are there.

Because this changes the database model, a migration needs to be created. Exec into the docker container (`docker-compose exec api sh`) and run `python manage.py makemigrations`. This will find the changes and write them to a file. To test the changes, apply the migrations (run `python manage.py migrate`) and then use the UI to use the new assessment. 

### Contributing
Fork the repo, make your changes, then submit a pull request. Be sure your pull request includes any migrations that were created.

Please install and use the flake8 pre-commit hook, this will help PRs stay focused on the important things:

```
pre-commit install --install-hooks
```

