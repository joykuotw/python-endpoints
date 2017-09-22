# python-endpoints

An experiment to build a lightweight REST API using python [endpoints](https://github.com/firstopinion/endpoints) with simple frontend.

# Setup

First run the following command to install the python endpoints:
```
pip install endpoints
```

Then install dependencies, e.g. express:
```
$ npm install
```

Run `DB.py` to create a SQLite database and read data from CSV file:
```
python DB.py
```

# Running

Start a server to run the index page:
```
npm start
```

Use this command to start the API server:
```
endpoints --prefix=productController --host=localhost:8000
```

Enter url `http://localhost:8080` into browser address and see if the `Products.html` is displayed. Now you can interact with endpoints.