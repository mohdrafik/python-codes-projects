# ********* class and object in python

class PERSON:
    name = "jamunadas"
    occupation = "eng"
    sal = 2000

    def info(self):
        print(f"NAME OF THE EMPLOYEE is {self.name} and his occupation is {self.occupation}")
        x = ''
        print(x, end=" ")   # just give one character space, don't force next line.
        print("previous line just for check that its provide the one char space or go to the next line.")


a = PERSON()
b = PERSON()

a.name = "RAFIK"
a.occupation = "scientist"
a.sal = 45000
a.info()
