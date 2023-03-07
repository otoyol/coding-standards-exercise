class user:  
    def __init__(self, username):
        self.username = username
    
    def get_username(self):
        return self.username


if __name__ == "__main__":
    u = user("johndoe")

    username = u.get_username()

    print(username)
