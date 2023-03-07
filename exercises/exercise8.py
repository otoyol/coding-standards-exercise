if __name__ == "__main__":
    user = User("john","doe", "01/01/0000")

    fn = user.get_first_name()
    sn = user.get_last_name()
    db = user.get_date_of_birth()
