# Data Engineering Technical Challenge

A practical, real-world simulation designed to assess your skills in building and managing a data pipeline using modern tools. You will ingest, transform, and expose data through an API while ensuring data quality, testing, and proper documentation.

## Prerequisites

- Python 3.8+
- Git 
- Docker
- DuckDB (Installation instructions below)
- Terminal/Command Line familiarity

### DuckDB Installation

**Mac:**
```bash 
brew install duckdb
```

**Windows:**
- Download the CLI tool from https://duckdb.org/docs/installation/
- Or install via Python: `pip install duckdb`

**Linux:**
```bash
sudo apt-get install duckdb
```

## Quick Start

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd data-engineering-challenge
```

2. **Set up the Python environment**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install DuckDB and other dependencies
pip install duckdb
pip install -r requirements.txt
```

3. **Generate sample data**
```bash
python generate_data.py
```

4. **Verify DuckDB installation**
```bash
# Start DuckDB CLI
duckdb

# Test a simple query
SELECT 1;

# Exit DuckDB CLI
.exit
```

5. **Start the local development server**
```bash
flask run
```

## Project Structure
```
data-engineering-challenge/
├── data/               # Generated CSV files
│   ├── customers.csv
│   ├── orders.csv
│   └── products.csv
├── src/
│   ├── models/        # dbt models
│   └── tests/         # Python tests
├── config/            # Configuration files
├── README.md
├── requirements.txt
├── .gitignore
└── Dockerfile
```

## Key Tasks

### 1. Data Ingestion (20 minutes)
- Load generated CSV files into DuckDB
- Define proper schemas
- Implement basic data quality checks:
  - Validate primary keys
  - Check date formats
  - Verify numeric ranges

Example DuckDB schema:
```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    country VARCHAR,
    join_date DATE
);
```

### 2. Data Transformation (20 minutes)
Use dbt to create models for:
- Daily sales aggregations
- Customer lifetime value
- Product performance metrics

Include:
- Model tests
- Documentation
- Lineage graphs

### 3. API Development (20 minutes)
Build a Flask API with endpoints:
- GET /api/v1/daily_sales
- GET /api/v1/top_customers
- GET /api/v1/product_metrics

Features:
- Error handling
- Basic authentication
- Request rate limiting

### 4. Data Quality & Testing (optional: 30 minutes)
Implement:
- Great Expectations validations
- Unit tests for API endpoints
- Integration tests for data pipeline
- Quality reports

### 5. Documentation & Deployment (optional: 30 minutes)
Provide:
- Setup instructions
- API documentation
- Data model documentation
- Docker deployment guide

## Bonus Features (optional: if Time Permits)
- Incremental dbt processing
- Swagger/OpenAPI documentation
- Streamlit dashboards
- Data versioning
- CI/CD pipeline using GitHub Actions

## Local Development

### Using Docker
```bash
# Build the container
docker build -t data-engineering-challenge .

# Run the container
docker run -p 5000:5000 data-engineering-challenge
```

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Start the application
flask run
```

## API Examples

### 1. Daily Sales Endpoint
```bash
GET /api/v1/daily_sales

Response:
{
    "status": "success",
    "data": [
        {
            "date": "2023-01-01",
            "total_sales": 15234.50,
            "order_count": 45,
            "average_order_value": 338.54
        }
    ]
}
```

### 2. Top Customers Endpoint
```bash
GET /api/v1/top_customers

Response:
{
    "status": "success",
    "data": [
        {
            "customer_id": 1,
            "name": "Customer 1",
            "total_spent": 25435.67,
            "order_count": 12
        }
    ]
}
```

## Troubleshooting

### Common Installation Issues

1. **DuckDB Installation**
```bash
# Verify DuckDB installation
duckdb --version

# If not found, try:
pip install --upgrade duckdb
```

2. **Virtual Environment Issues**
```bash
# If venv creation fails:
python3 -m pip install --user virtualenv
python3 -m venv venv
```

3. **Package Installation Errors**
```bash
# If requirements.txt install fails:
pip install --no-cache-dir -r requirements.txt
```

## Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.# Data Engineering Technical Challenge

A practical, real-world simulation designed to assess your skills in building and managing a data pipeline using modern tools. You will ingest, transform, and expose data through an API while ensuring data quality, testing, and proper documentation.

## Prerequisites

- Python 3.8+
- Git
- Docker
- Terminal/Command Line familiarity

## Quick Start

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd data-engineering-challenge
```

2. **Set up the Python environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. **Generate sample data**
```bash
python generate_data.py
```

4. **Start the local development server**
```bash
flask run
```

## Project Structure
```
data-engineering-challenge/
├── data/               # CSV files and raw data
├── src/
│   ├── models/        # dbt models
│   └── tests/         # Python tests
├── config/            # Configuration files
├── README.md
├── requirements.txt
├── .gitignore
└── Dockerfile
```

## Key Tasks

### 1. Data Ingestion
- Load e-commerce data (CSV files) into DuckDB
- Define proper schemas
- Implement basic data quality checks
  - Validate primary keys
  - Check date formats
  - Verify numeric ranges

### 2. Data Transformation
Use dbt to create the following models:
- Daily sales aggregations
- Customer lifetime value calculations
- Product performance metrics

Include:
- Model tests
- Documentation
- Lineage graphs

### 3. API Development
Build a Flask API with endpoints for:
- GET /api/v1/daily_sales
- GET /api/v1/top_customers
- GET /api/v1/product_metrics

Features:
- Error handling
- Basic authentication
- Request rate limiting

### 4. Data Quality & Testing
Implement:
- Great Expectations data validations
- Unit tests for API endpoints
- Integration tests for data pipeline
- Generated quality reports

### 5. Documentation & Deployment
Provide:
- Clear setup instructions
- API documentation
- Data model documentation
- Docker deployment guide

## Bonus Features
Optional enhancements:
- Incremental dbt processing
- Swagger/OpenAPI documentation
- Streamlit dashboards
- Data versioning
- CI/CD pipeline using GitHub Actions

## Local Development

### Using Docker
```bash
# Build the container
docker build -t data-engineering-challenge .

# Run the container
docker run -p 5000:5000 data-engineering-challenge
```

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Start the application
flask run
```

## API Documentation

### Authentication
```bash
curl -X GET http://localhost:5000/api/v1/daily_sales \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Available Endpoints
- GET /api/v1/daily_sales
- GET /api/v1/top_customers
- GET /api/v1/product_metrics

## Data Model Documentation
- customers: Customer demographic data
- orders: Transaction records
- products: Product catalog

## Testing
```bash
# Run all tests
pytest

# Run specific test suite
pytest src/tests/test_api.py
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
