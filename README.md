# fastapi-whiteapp

A basic whiteapp for fastapi to be able to get started with a CRUD, file logging, connection to a db and testing
  
## Tech Stack

**Server:** Python, FastApi, SQLAlchemy, uvicorn, pytest


## Run Locally

Clone the project

```bash
  git clone https://github.com/mmick78/fastapi-whiteapp.git
```

Go to the project directory:

```bash
  cd fastapi-whiteapp
```

Install dependencies and start the server:

```bash
  dev_run.bat
```

You can also create a virtual environment via Pycharm and install the requirements.txt file then start the app via `main.py`


## Related

* [FastApi Documentation](https://fastapi.tiangolo.com/)
* [SQL Alchemy Documentation](https://www.sqlalchemy.org/library.html#tutorials)

  
## Roadmap

- Add user authentication
- Add AWS/Azure deployment via Kubernetes

  
## API Reference

[Local Swagger](http://localhost:4200/docs)

#### Get all beer items

```http
  GET /api/v1/beer_parameters/
```

#### Get only one beer item

```http
  GET api/v1/beer_parameters/${beer_name}
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `beer_name` | `string` | **Required**. Id of item to fetch |


## Running Tests

To run tests, run the following command

```bash
  python -m pytest
```


## Logs

- All log files are stored here: `app\core\Logs`

- Configuration can be modified in : `app\core\config`