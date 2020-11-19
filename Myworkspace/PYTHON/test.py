def Layout(func):
    print("umumi saytin ust hissesinin goruntusu")
    func()
    print("umumi saytin alt hissesinin goruntusu")
def home():
    print("ana sehifeye aid hisseler")
def about():
    print("haqqimizda sehifesine aid hisseler")
Layout(home)
