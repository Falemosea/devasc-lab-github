# archivo: acl.py
acl = int(input("Ingresa numero de ACL: "))
 
# IMPORTANTE: incluir los rangos expandidos (1300-1999 y 2000-2699)
if (1 <= acl <= 99) or (1300 <= acl <= 1999):
    print("ACL Estandar")
elif (100 <= acl <= 199) or (2000 <= acl <= 2699):
    print("ACL Extendida")
else:
    print("No corresponde a una ACL")
