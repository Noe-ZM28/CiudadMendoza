#esto para el programa de p8 donde guardamos el tiempo transcurrido en una variable varchar
#import mysql.connector
import pymysql

class Operacion:

    def abrir(self):
        conexion=pymysql.connect(host="localhost",
                                 user="Aurelio",
                                 passwd="RG980320",
                                 database="Parqueadero1")

        #conexion = pymysql.connect(host="192.168.1.91",
        #                   user="Aurelio",
        #                   passwd="RG980320",
        #                   database="Parqueadero1")
        return conexion


    def altaRegistroRFID(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into Entradas(Entrada, CorteInc, Placas) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def guardacobro(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update Entradas set vobo = %s, Importe = %s, TiempoTotal = %s, Entrada = %s, Salida = %s,TarifaPreferente = %s where id = %s;"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Entrada, Salida from Entradas where id=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, Entrada, Salida from Entradas"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def recuperar_sincobro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, Entrada, Salida, Importe from Entradas where CorteInc = 0 and Importe is not null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def desglose_cobrados(self,Numcorte):
        cone=self.abrir()
        cursor=cone.cursor()
        #sql="SELECT TarifaPreferente,Importe, Count(*) as cuantos FROM Entradas where CorteInc = 6 "
        #sql="SELECT TarifaPreferente,Importe, Count(*) as cuantos FROM Entradas where CorteInc = %s GROUP BY TarifaPreferente,Importe;"
        sql="SELECT Count(*),TarifaPreferente,Importe, Count(*)*Importe  as cuantos FROM Entradas where CorteInc = %s GROUP BY TarifaPreferente,Importe;"
        #sql="select id, Entrada, Salida, Importe from Entradas where CorteInc = 0 and Importe is not null "
        cursor.execute(sql,Numcorte)
        cone.close()
        return cursor.fetchall()
    def Autos_dentro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, Entrada, Placas from Entradas where CorteInc = 0 and Importe is null and Salida is null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def CuantosAutosdentro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where CorteInc = 0 and Importe is null and Salida is null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def Quedados_Sensor(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Quedados from Cortes where Folio=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def NumBolQued(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select NumBolQued from Cortes where Folio=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()
    def EntradasSensor(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select EntSens from AccesosSens where Folio=1"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def SalidasSensor(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select SalSens from AccesosSens where Folio=1"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def CuantosBoletosCobro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where CorteInc = 0 and Importe is not null and Salida is not null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def BEDCorte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where ((vobo is null and TarifaPreferente is null) or (vobo = 'lmf' and TarifaPreferente = ''))"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def BAnteriores(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where vobo = 'ant' "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def corte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select sum(importe) from Entradas where CorteInc = 0"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def MaxfolioEntrada(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(id) from Entradas;"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def Maxfolio_Cortes(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(Folio) from Cortes;"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def ActualizarEntradasConcorte(self, maxnum):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update Entradas set CorteInc = %s, vobo = %s where TiempoTotal is not null and CorteInc=0;"
        #sql = "update Entradas set CorteInc=%s where TiempoTotal is not null and CorteInc=0;"
        cursor.execute(sql,maxnum)
        cone.commit()
        cone.close()

    def NocobradosAnt(self, vobo):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update Entradas set vobo = %s where Importe is null and CorteInc=0;"
        cursor.execute(sql,vobo)
        cone.commit()
        cone.close()

    def obtenerNumCorte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(Folio) from Cortes"
        #sql = "update Entradas set CorteInc = 1 WHERE Importe > 0"
        cursor.execute(sql)
        #cone.commit()
        cone.close()
        return cursor.fetchall()
    def MaxnumId(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(idInicial) from Cortes"
        #sql = "update Entradas set CorteInc = 1 WHERE Importe > 0"
        cursor.execute(sql)
        #cone.commit()
        cone.close()
        return cursor.fetchall()

    def GuarCorte(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into Cortes(Importe, FechaIni, FechaFin,Quedados,idInicial,NumBolQued) values (%s,%s,%s,%s,%s,%s)"
        #sql = "update Entradas set CorteInc = 1 WHERE Importe > 0"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def UltimoCorte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(FechaFin) from Cortes;"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
#### REPORTE DE CORTES A EXCEL ####   
    def Cortes_MaxMin(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT max(FechaIni), min(FechaIni), max(FechaFin) FROM Cortes where MONTH(FechaIni)=%s AND YEAR(FechaIni)=%s "
        #sql="SELECT max(FechaFin), min(FechaFin) FROM Cortes where MONTH(FechaFin)=%s AND YEAR(FechaFin)=%s " 
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Cortes_Folio(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Folio FROM Cortes where FechaIni=%s" 
        #sql="SELECT Folio FROM Cortes where FechaFin=%s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Registros_corte(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT id, Entrada, Salida, TiempoTotal, Importe, CorteInc, Placas, TarifaPreferente FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1)"  #CorteInc > (%s-1) AND CorteInc < (%s+1)
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Totales_corte(self, datos1):
        cone=self.abrir()
        cursor=cone.cursor()
        #sql="SELECT TarifaPreferente,Importe, Count(*) as cuantos FROM Entradas where CorteInc = 6 " sum(Importe), 
        #sql="SELECT TarifaPreferente,Importe, Count(*) as cuantos FROM Entradas where CorteInc = %s GROUP BY TarifaPreferente,Importe;"
        sql="SELECT sum(Importe), max(CorteInc), min(CorteInc), Count(TarifaPreferente) FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1)" #Entrada > %s AND Entrada < %s
        #sql="select id, Entrada, Salida, Importe from Entradas where CorteInc = 0 and Importe is not null "
        cursor.execute(sql,datos1)
        cone.close()
        return cursor.fetchall()
    def Resumen_promo(self, datos1):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Count(TarifaPreferente),TarifaPreferente,Importe, sum(Importe) as ImporteTot FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1) GROUP BY TarifaPreferente ORDER BY ImporteTot DESC;" #Entrada >= %s AND Salida <= %s
        #sql="SELECT Count(*),TarifaPreferente,Importe, Count(*)*Importe  as cuantos FROM Entradas where CorteInc = %s GROUP BY TarifaPreferente,Importe;"
        #sql="SELECT Count(TarifaPreferente),TarifaPreferente,Importe, Count(TarifaPreferente)*Importe as ImporteTot FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1) GROUP BY TarifaPreferente,Importe ORDER BY ImporteTot;"
        cursor.execute(sql,datos1)
        cone.close()
        return cursor.fetchall()

####PENSIONADOS####
    def ValidarRFID(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT id_cliente FROM Pensionados WHERE Num_tarjeta=%s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()       
    def AltaPensionado(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="INSERT INTO Pensionados(Num_tarjeta, Nom_cliente, Apell1_cliente, Apell2_cliente, Fecha_alta, Telefono1, Telefono2, Ciudad, Colonia, CP, Calle_num, Placas, Modelo_auto, Color_auto, Monto, Cortesia, Tolerancia, Vigencia) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #datos=(numtarjeta, Nombre, ApellidoPat, ApellidoMat, fechaAlta, Telefono1, Telefono2, Ciudad, Colonia, CP, Calle, Placa, Modelo, Color, montoxmes, cortesia, tolerancia)
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def ConsultaPensionado(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Nom_cliente, Apell1_cliente, Apell2_cliente, Telefono1, Telefono2, Ciudad, Colonia, CP, Calle_num, Placas, Modelo_auto, Color_auto, Fecha_vigencia, Estatus, Vigencia, Monto, Cortesia, Tolerancia FROM Pensionados where id_cliente=%s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def ModificarPensionado(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE Pensionados SET Num_tarjeta=%s, Nom_cliente=%s, Apell1_cliente=%s, Apell2_cliente=%s, Telefono1=%s, Ciudad=%s, Colonia=%s, CP=%s, Calle_num=%s, Placas=%s, Modelo_auto=%s, Color_auto=%s, Monto=%s, Cortesia=%s, Tolerancia=%s, Ult_Cambio=%s, Fecha_vigencia=%s WHERE id_cliente=%s"
        #datos=(numtarjeta, Nombre, ApellidoPat, ApellidoMat, Telefono1, Telefono2, Ciudad, Colonia, CP, Calle, Placa, Modelo,                    Color, montoxmes, cortesia, tolerancia, PensionadoOpen)
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def CobrosPensionado(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="INSERT INTO PagosPens(idcliente, num_tarjeta, Fecha_pago, Fecha_vigencia, Mensualidad, Monto) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def UpdPensionado(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE Pensionados SET Vigencia=%s, Fecha_vigencia=%s, Monto=%s WHERE id_cliente=%s"
        #sql = "update Entradas set CorteInc = %s, vobo = %s where TiempoTotal is not null and CorteInc=0;"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def UpdMovsPens(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE MovimientosPens SET Salida=%s, Estatus=%s WHERE idcliente=%s and Salida is null"
        #sql = "update Entradas set CorteInc = %s, vobo = %s where TiempoTotal is not null and CorteInc=0;"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def UpdPens2(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE Pensionados SET Estatus=%s WHERE id_cliente=%s"
        #sql = "update Entradas set CorteInc = %s, vobo = %s where TiempoTotal is not null and CorteInc=0;"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def ValidarTarj(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT id_cliente, Estatus FROM Pensionados WHERE Num_tarjeta=%s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
##### CONSULTA PENSIONADOS ADENTRO    
    def TreaPenAdentro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Placas, Modelo_auto from Pensionados where Estatus='Adentro'"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
###### VIGENCIAS Y REPORTE DE PENSIONADOS
    def ActualizaVigP(self, fecha):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update Pensionados set Vigencia = 'VENCIDA' where Fecha_vigencia < %s and Vigencia = 'Activo';"
        cursor.execute(sql,fecha)
        cone.commit()
        cone.close()
###### REPORTE DE PENSIONADOS
    def RptePensionado(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Id_cliente, Num_tarjeta, Nom_cliente, Apell1_cliente, Apell2_cliente, Placas, Modelo_auto, Fecha_vigencia, Vigencia, Monto, Cortesia, Estatus FROM Pensionados"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()                
    def RpteMovsPensionado(self, cliente):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT max(Entrada), max(Salida) FROM MovimientosPens where idcliente = %s"
        cursor.execute(sql,cliente)
        cone.close()
        return cursor.fetchall()    
    def RptePagoPensionado(self, cliente):
        cone=self.abrir()
        cursor=cone.cursor()
        print(str(cliente))
        sql="SELECT Monto, Fecha_pago, idcliente FROM PagosPens WHERE Fecha_pago = (SELECT MAX(Fecha_pago) FROM PagosPens as ult WHERE ult.idcliente = %s) AND idcliente = %s"
        cursor.execute(sql,cliente)
        cone.close()
        return cursor.fetchall() 
    def CuantosPenVig(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Count(*), Vigencia FROM Pensionados GROUP BY Vigencia"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()    
    def CuantosPenCort(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Count(*), Cortesia FROM Pensionados GROUP BY Cortesia"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
 
 #####USUARIOS###

    def ConsultaUsuario(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Id_usuario, Contrasena, Nom_usuario FROM Usuarios WHERE Usuario = %s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall() 
    def CajeroenTurno(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT min(id_movs), nombre, inicio, turno, Idusuario FROM MovsUsuarios where CierreCorte is null"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()   
    def IniciosdeTurno(self, dato):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT inicio, usuario FROM MovsUsuarios where inicio > %s" #and CierreCorte = 'No aplica'  Idusuario = %s and 
        cursor.execute(sql, dato)
        cone.close()
        return cursor.fetchall()                 
    def ActuaizaUsuario(self, actual):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="INSERT INTO MovsUsuarios(Idusuario, usuario, inicio, nombre, turno) values (%s,%s,%s,%s,%s)"
        #sql="INSERT INTO PagosPens(idcliente, num_tarjeta, Fecha_pago, Fecha_vigencia, Mensualidad, Monto) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,actual)
        cone.commit()
        cone.close()
    def Cierreusuario(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update MovsUsuarios set CierreCorte = %s where  id_movs = %s;"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def NoAplicausuario(self, dato):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update MovsUsuarios set CierreCorte = 'No aplica' where  id_movs > %s;"
        cursor.execute(sql,dato)        
        cone.commit()
        cone.close()
 
 
 
    def nombre_usuario_activo(self):
        """
        Esta función realiza una consulta a la base de datos para obtener el nombre del usuario que esta activo.
        Args:
        - self: referencia a la clase donde está definida la función.
        Returns:
        - resultados: lista de tuplas que contienen la siguiente información:
            - nombre: El nombre del usuario
        Esta función utiliza la librería de MySQL Connector para conectarse a la base de datos y ejecutar una consulta SQL.
        """

        # Se establece la conexión con la base de datos.
        cone = self.abrir()

        # Se crea un cursor para ejecutar la consulta.
        cursor = cone.cursor()

        # Se define la consulta SQL.
        sql = f"""SELECT nombre FROM MovsUsuarios WHERE CierreCorte IS Null"""

        # Se ejecuta la consulta y se almacenan los resultados en una lista de tuplas.
        cursor.execute(sql)
        resultados = cursor.fetchall()

        # Se cierra la conexión con la base de datos.
        cone.close()

        # Se devuelve la lista de tuplas con los resultados de la consulta.
        return resultados

    def total_pensionados_corte(self, corte):
        """
        Realiza una consulta a la base de datos para obtener la cantidad y el importe total de los pagos de pensiones 
        realizados en un corte específico.
        Args:
            self: referencia a la clase donde está definida la función.
            corte (int): el número de folio del corte que se desea consultar.
        Returns:
            resultados (list): una lista de tuplas que contienen la siguiente información:
                - Cuantos (int): la cantidad de pagos de pensiones realizados en el corte.
                - Concepto (str): una cadena que indica el tipo de pago (en este caso, siempre será "Pensionados").
                - ImporteTotal (float): el importe total de los pagos de pensiones realizados en el corte.
        Esta función utiliza la librería de MySQL Connector para conectarse a la base de datos y ejecutar una consulta SQL.
        """
        # Se establece la conexión con la base de datos.
        cone = self.abrir()

        # Se crea un cursor para ejecutar la consulta.
        cursor = cone.cursor()

        # Se define la consulta SQL.
        sql = f"""SELECT COUNT(*) AS Cuantos, TipoPago AS Concepto, COALESCE(FORMAT(SUM(p.Monto), 2), 0) AS ImporteTotal FROM PagosPens p INNER JOIN Cortes c ON p.Fecha_pago BETWEEN c.FechaIni AND c.FechaFin WHERE c.Folio = {corte} GROUP BY TipoPago;"""

        # Se ejecuta la consulta y se almacenan los resultados en una lista de tuplas.
        cursor.execute(sql)
        resultados = cursor.fetchall()

        # Se cierra la conexión con la base de datos.
        cone.close()

        # Se devuelve la lista de tuplas con los resultados de la consulta.
        return resultados
