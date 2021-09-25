from view import menu

def login(self,name,pw=""):
        """Function to check the if username and password is correct then destroy the login window
        and open the main menu to allow users interact with the application

        Args:
            name (string): username from user input
            pw (string): password from user input
        """
        self.destroy()
        menu.window(name)