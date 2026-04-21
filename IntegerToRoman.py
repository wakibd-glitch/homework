class Roman:
    def convert(self, n):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        res = ""
        for i in range(len(val)):
            while n >= val[i]:
                res += sym[i]
                n -= val[i]
        return res


num = int(input("Enter number: "))
r = Roman()
print("Roman:", r.convert(num))