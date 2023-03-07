def uri():
   schema = get('database', 'schema')
   username = get('database', 'username')
   password = get('database', 'password')
   host = get('database', 'host')
   port = get('database', 'port')
   database = get('database', 'name')
   return "{}://{}:{}@{}:{}/{}".format(schema, username, password, host, port, database)
  