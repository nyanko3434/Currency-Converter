# Currency-Converter
Project to get exchange rate in realtime with the help of fastapi and API KEY from exchangerate.host

<h3>Features:</h3>
- Convert currency values (/convert)

- Fetch list of supported currencies (/currencies)

- Configurable via environment variables (.env)

- RESTful, versioned API (/api/v1)

<h2>Getting Started</h2>

<h3>Project Structure</h3>

currency-converter/
├── app/
│   ├── __init__.py
│   ├── main.py                 
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── routes.py       
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           
│   │   └── currency.py         
│   └── models/
│       ├── __init__.py
│       └── schemas.py              
│
├── tests/
│   ├── test_convert.py         
│   └── test_list.py
├── .env               
├── .gitignore
├── Dockerfile
├── docker-compose.yml       
├── requirements.txt
└── README.md

