from Item import Item as iI
from Phone import Phone as pP

if __name__ == '__main__':
    iI.instantiate_from_csv()  # class method called before instanced
    phone = pP("s21fe", 20, 21, 9)  # instanced with passing parameter to constructor __init__
    print(iI.all)
    print(pP.all)
