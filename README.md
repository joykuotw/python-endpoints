# python-endpoints

An experiment to run python endpoints with simple frontend.

First run the following command to install the endpoint package:
```
pip install endpoints
```

Run the `DB.py` to create the SQLite database and read the data from CSV file:
```
python DB.py
```

And use this command to run the server:
```
endpoints --prefix=productController --host=localhost:8000
```

Then you can open the `Products.html` to interact with endpoints.