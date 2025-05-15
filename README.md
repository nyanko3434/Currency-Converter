# Currency-Converter
Project to get exchange rate in realtime with the help of fastapi and API KEY from exchangerate.host

## Features:
- Convert currency values (/convert)

- Fetch list of supported currencies (/currencies)

- Configurable via environment variables (.env)

- RESTful, versioned API (/api/v1)

## Getting Started

### Project Structure

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

---

### Setup & Run

#### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "EXCHANGE_RATE_API_KEY=your_api_key_here" > .env

# Run the app
uvicorn app.main:app --reload

```
Visit: http://localhost:8000/docs

#### Docker

```bash
docker build -t currency-converter .
docker run --env-file .env -p 8000:8000 currency-converter
```
