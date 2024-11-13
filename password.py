import re


class Password:
    def __init__(self):
        pass

    def add_data_to_file(self, file_name: str):  # user input
        password = input("Enter password: ")
        result = self.__password_validation(password)

        if result:
            with open(file_name, 'r+') as file:
                last_sym = file.readlines()[-1][-1]
                if last_sym == '\n':
                    file.write(password+'\n')
                else:
                    file.write('\n')
                    file.write(password + '\n')
            print(f'{password} successfully added to file')
        else:
            print("Incorrect password!")

    def data_from_file(self, file_name: str):  # data from file
        counter = 0
        password_from_file = []

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    if self.__password_validation(line):
                        counter += 1
                        password_from_file.append(line)
        except FileNotFoundError:
            print(f'file {file_name} not found')

        print(f'find {counter} valid password')

        return password_from_file

    @staticmethod
    def __password_validation(password):  # validation number
        if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&+=])(?=.*[A-Za-z0-9@$!%*#?&+=]{8,}).+$', password):
            return True
        else:
            return False