class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def get_f_name(self):
        return self.first_name

    def get_l_name(self):
        return self.last_name

    def get_user_info(self):
        return f"User: { self.first_name}, {self.last_name}"

