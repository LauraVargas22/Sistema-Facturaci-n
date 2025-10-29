'''
Archivo principal para la ejecución del programa
'''

if (__name__=='__main__'):
    #Importación modulos
    import modules.customs as cu
    import modules.titles as t
    import modules.invoice as iv
    import modules.menus as me
    import modules.exit as ex
    import modules.messages as msg

    isActive = True

    while (isActive):
        try:
            cu.borrarPantalla()
            t.show_title()
            me.show_menu()
            opcMenu = int(input("Seleccione:__"))

            match opcMenu:
                case 1:
                    cu.borrarPantalla()
                    iv.main()
                    cu.pausarPantalla()
                    
                case 2:
                    isActive = ex.validateData(msg.msgInfo)
                
                case _:
                    print (msg.msgCase)
                    cu.pausarPantalla()

        except ValueError:
            print(msg.msgExcept)
            cu.pausarPantalla()
            continue        