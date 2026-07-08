from uuid import uuid4

def create_unique_string() -> str:
    """
    Generates a unique string using UUID4. 
    
    This string can be used for creating unique identifiers, such as document names or user IDs.
    """

    return str(uuid4())