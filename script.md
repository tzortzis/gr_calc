# gr_calc
basic python calculator in greek

script:
def add(x, y):
#Προσθεση
   return x + y

def subtract(x, y):
#Αφαιρεση

   return x - y

def multiply(x, y):
#Πολλαπλασιασμος

   return x * y

def divide(x, y):
#Διαιρεση
   return x / y

print ("----- κομπιουτερακι-----")
print("Διαλεξτε πραξη.")
print("1.Προσθεση")
print("2.Αφαιρεση")
print("3.Πολλαπλασιασμος")
print("4.Διαιρεση")

choice = input("Eισαγετε επιλογη (1/2/3/4):")

num1 = int(input("Εισαγετε το πρωτο νουμερο: "))
num2 = int(input("Εισαγετε το δευτερο νουμερο: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Σφαλμα")

