# Data Engineering Technical Challenge

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
