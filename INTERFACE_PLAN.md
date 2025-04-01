# Interface Plan
This project is a simple interface in which we will make an example of an MCP server that allows us to connect with Coín Market Cap, for the prices of cryptocurrencies or coins.

## Structure

```
.
├── main.py
└── src
    ├── __init__.py
    └── core
        ├── common
        │   └── schema.py
        ├── config.py
        ├── settings
        │   ├── __init__.py
        │   ├── base.py
        │   ├── development.py
        │   ├── environment.py
        │   ├── local.py
        │   ├── production.py
        │   └── staging.py
        └── utils
            ├── datetime.py
            ├── extended_enum.py
            ├── filename_generator.py
            ├── passwords.py
            ├── query_utils.py
            └── redis.py
```

## Documentation
- https://coinmarketcap.com/api/documentation/v1/
- https://modelcontextprotocol.io/quickstart/server
- https://docs.astral.sh/uv/
