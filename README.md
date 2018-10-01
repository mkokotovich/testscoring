# testscoring

###Local Development
To bring up the backend: `docker-compose up`

To bring up UI: `yarn start`
###Adding new assessments

To add new assessments, create an assessment class and add it to the "assessments" list in `backend/apps/testing/v1_views.py`. See another assessment for an example and the comments in `backend/apps/testing/utils.py`

### Contributing
Fork the repo, make your changes, then submit a PR.

Please install and use the flake8 pre-commit hook, this will help PRs stay focused on the important things:

```
pre-commit install --install-hooks
```

