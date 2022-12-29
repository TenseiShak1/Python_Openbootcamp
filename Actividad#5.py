def año(año):
    if (año % 4 ==0 and (año %100 !=0 or año % 400 ==0)):
        print(f"El año {año} es bisisesto")
    else:
        print(f"El año {año} no es bisisesto")
        
    
año_inngreso = int(input("ingrese el año deseado\n==>"))    
año(año_inngreso)
