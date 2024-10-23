from functools import wraps

def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            # Optionally send an error message or log the error
            if hasattr(args[0], 'highrise'):
                bot = args[0]
                await print(f"An error occurred: {str(e)}")
    return wrapper

def handle_exceptions_def(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            # Optionally log the error
    return wrapper