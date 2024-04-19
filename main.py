To implement logging in an e-commerce website, you can use logging frameworks available in the programming language you're using for your back-end. Here's a basic example using Python and its built-in `logging` module:

```python
import logging

# Configure logging
logging.basicConfig(filename='ecommerce.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example functions where logging can be used
def add_to_cart(user_id, product_id):
    logging.info(f"User {user_id} added product {product_id} to cart.")

def checkout(user_id, cart_total):
    logging.info(f"User {user_id} checked out with total amount {cart_total}.")

# Example usage
add_to_cart(123, 456)
checkout(123, 100.50)
```

In this example:
- `logging.basicConfig()` configures the logging system. You can specify the log file name (`filename`), logging level (`level`), and log message format (`format`).
- Functions like `add_to_cart()` and `checkout()` log relevant events using `logging.info()`.

You can extend this by adding more detailed information to your log messages, such as timestamps, user IP addresses, product details, etc., depending on your specific requirements. Additionally, you can handle different logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) based on the severity of the event being logged.
