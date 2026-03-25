class India():

    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoke language of India.")


class USA():
    def capital(self):
        print("Washington, D.C. is the captial of the USA.")

    def language(self):
        print("English is the primary language of the USA")

obj_ind = India()
obj_usa = USA()


for country in(obj_ind,obj_usa):
    country.capital()
    country.language()