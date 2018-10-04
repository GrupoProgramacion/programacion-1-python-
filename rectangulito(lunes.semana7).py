def letra(ancho,alto,fondo,borde,iteracion):
    if  iteracion % ancho == 0 and ancho != 0 :
        return borde+'\n'
    elif (iteracion - 1 ) % ancho == 0  :
        return borde
    elif iteracion <= ancho or iteracion > ancho * (alto-1):
        return borde
    else :
        return fondo
    
def dibujar(ancho,alto,borde,fondo):
    return list(map(lambda x : letra(ancho,alto,fondo,borde,x),range(1,ancho*alto+1)))

def valid(cadena):
    out = int(cadena)
    
    if out >= 3 :
        return out
    else :
        print("Error al ingresar los datos")
        raise SystemExit

print(*dibujar(valid(input()),valid(input()),input(),input()),sep='')
