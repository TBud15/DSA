class UserSettings:
    default_theme = 'light'  # Default theme for all users

    def __init__(self, username):
        self.username = username
        self.theme = UserSettings.default_theme  # Use the class's default theme

    def display_settings(self):
        return f"User: {self.username}, Theme: {self.theme}"

    @classmethod
    def change_default_theme(cls, new_theme):
        cls.default_theme = new_theme  # Change the class variable that affects all instances
        # This line above is where the class's behavior is changed globally

# Creating instances with the default theme
user1 = UserSettings('Alice')
user2 = UserSettings('Bob')
print(user1.display_settings())  # Output: User: Alice, Theme: light
print(user2.display_settings())  # Output: User: Bob, Theme: light

# Change the default theme using a class method
UserSettings.change_default_theme('dark')
# The call to change_default_theme above changes the behavior for all instances

# Existing users will see the change when their settings are evaluated again
print(user1.display_settings())  # Output: User: Alice, Theme: dark
print(user2.display_settings())  # Output: User: Bob, Theme: dark

# Any new users will also use the new default theme
user3 = UserSettings('Charlie')
print(user3.display_settings())  # Output: User: Charlie, Theme: dark
