class User:
    """
    A class representing a user.
    """
    
    def __init__(self, username):
        """
        Initializes a new instance of the User class with the given username.
        
        Args:
        username (str): The username of the user.
        """
        self.username = username
    
    def get_username(self):
        """
        Returns the username of the user.
        
        Returns:
        str: The username of the user.
        """
        return self.username


if __name__ == "__main__":
    user = User("johndoe")

    username = user.get_username()

    print(username)
