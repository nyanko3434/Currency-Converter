# Currency-Converter
Project to get exchange rate in realtime with the help of fastapi and API KEY from exchangerate.host

<h3>Features:</h3>
- Convert currency values (/convert)

- Fetch list of supported currencies (/currencies)

- Configurable via environment variables (.env)

- RESTful, versioned API (/api/v1)

<h2>Getting Started</h2>

<h3>Project Structure</h3>

currency-converter/<br>
├── app/<br>
│   ├── __init__.py<br>
│   ├── main.py          
│   ├── api/<br>
│   │   ├── __init__.py<br>
│   │   └── v1/<br>
│   │       ├── __init__.py<br>
│   │       └── routes.py      <br>
│   ├── core/<br>
│   │   ├── __init__.py<br>
│   │   ├── config.py       
│   │   └── currency.py        <br>
│   └── models/<br>
│       ├── __init__.py<br>
│       └── schemas.py             
│<br>
├── tests/<br>
│   ├── test_convert.py       
│   └── test_list.py<br>
├── .env               <br>
├── .gitignore<br>
├── Dockerfile<br>
├── docker-compose.yml
├── requirements.txt<br>
└── README.md<br>

