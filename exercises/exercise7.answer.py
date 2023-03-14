def get_database_uri():
    """
    Returns the database URI based on the values stored in the configuration file.

    Returns:
    str: The database URI.
    """
    config = get('database')
    
    return "{}://{}:{}@{}:{}/{}".format(
        config['schema'], 
        config['username'], 
        config['password'], 
        config['host'], 
        config['port'], 
        config['name']
    )
