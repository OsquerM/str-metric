#Variables globales 
metric = 0

#Funciones
def run(text: str) -> int:
    # TODO
    global metric
    #Variables locales
    cadena = len(text) 
    vocal = text.count('a')
    vocal2 = text.count('e')
    vocal3 = text.count('i')
    vocal4 = text.count('o')
    vocal5 = text.count('u')

    resultado = vocal + vocal2 + vocal3 + vocal4 + vocal5

    metric = cadena * resultado
    
    
    
    return metric

#Código principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(metric)