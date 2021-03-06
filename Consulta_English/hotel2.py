"""Classe Hotel"""
from datetime import date, timedelta
class Hotel:

    def __init__(self, idHotel):
     #   self.id = 0
     #   self.nomeHotel = " "
     #   self.categoria = " "
        self.hoteis = {1: ["Lakewood", 3],
                       2: ["Bridgewood", 4],
                       3: ["Ridgewood", 5]}
        self.id = idHotel
        self.nomeHotel = self.hoteis[idHotel][0]
        self.categoria = self.hoteis[idHotel][1]

    def getNome(self):
         return self.nomeHotel
    def getCategoria(self):
         return self.categoria
"""
Classe Taxa
"""
class Taxa:

      def __init__(self):
          pass

      def obtemTaxa(self,tipoCliente, diasPesquisa):
          taxa=0
          calculaDiaria = CalculaDiarias()
          maisBarato = ""
          if tipoCliente == 0:  #tipo=0 (Cliente Regular) Tipo=1 (Cliente Reward)
              calculaDiaria.calculaDiariasRegular(diasPesquisa)
          else:
               calculaDiaria.calculaDiariasReward(diasPesquisa)

          diariasLake = calculaDiaria.getValorLake()
          diariasBridge = calculaDiaria.getValorBridge()
          diariasRidge = calculaDiaria.getValorRidge()
          print("\nLakewood Daily Tax = {}".format(calculaDiaria.getValorLake()))
          print("Bridgewood Daily Tax = {}".format(calculaDiaria.getValorBridge()))
          print("Ridgewood Daily Tax = {}\n".format(calculaDiaria.getValorRidge()))
          """Acessa Classe Hotel acionando 3 instâncias (1 para cada hotel)
             Com isso, estamos a simular acesso a banco de dados
           """
          nomeMaisBarato=" "
          hotelInstancia1 = Hotel(1)  # Instancia com id=1  Lakewood
          hotelInstancia2 = Hotel(2)  # Instancia com id=2  Bridgewood
          hotelInstancia3 = Hotel(3)  # Instancia com id=3  Ridgewood
          if (diariasLake < diariasBridge):
              if (diariasLake < diariasRidge):
                  nomeMaisBarato = hotelInstancia1.getNome()  # Lakewood é mais barato de todos
              else:
                  if (diariasLake == diariasRidge):
                      if (hotelInstancia1.getCategoria() > hotelInstancia3.getCategoria()):
                          nomeMaisBarato = hotelInstancia1.getNome()

                          """ Lakewood e Ridgewood são iguais, porem  
                              Lakewood tem maior classificação"""

                      else:
                          nomeMaisBarato = hotelInstancia3.getNome()

                          """ Lakewood e Ridgewood são iguais, porem  
                              Ridgewood tem maior classificação"""

                  else:
                      nomeMaisBarato = hotelInstancia3.getNome()  # Ridgewood é mais barato de todos
          else:
              if (diariasBridge < diariasRidge):
                  nomeMaisBarato = hotelInstancia2.getNome()  # Bridgewood é o mais barato de todos
              else:
                  if (diariasBridge  == diariasRidge):
                      if (hotelInstancia2.getCategoria() > hotelInstancia3.getCategoria()):
                          nomeMaisBarato = hotelInstancia2.getNome()

                          """ Lakewood e Ridgewood são iguais, porem  
                                                        Lakewood tem maior classificação"""

                      else:
                          nomeMaisBarato = hotelInstancia3.getNome()

                          """ Lakewood e Ridgewood são iguais, porem  
                            Ridgewood tem maior classificação"""

                  else:
                      nomeMaisBarato = hotelInstancia3.getNome()  # Ridgewood é mais barato de todos
          return nomeMaisBarato


          #return nomeMaisBarato
#taxa= taxas["LakeSemana"][0]

class CalculaDiarias:
    def __init__(self):
        self.somaLake = 0
        self.somaBridge = 0
        self.somaRidge = 0

        """ Aqui utilizei dicionário, para facilitar o processo de pesquisa de taxas, pois
           temos o benefício de utilizar: Chave/Valor
        """

        self.taxas = {"LakeSemana": [110, 80], "LakeFIM": [90, 80],
                    "BridgeSemana": [160, 110], "BridgeFIM": [60, 50],
                    "RidgeSemana": [220, 110], "RidgeFIM": [150, 40]}

    def calculaDiariasRegular(self,diasPesquisa):

        for item in diasPesquisa:
           if  (item < 6):
               valorTaxa= self.taxas["LakeSemana"][0]
               self.somaLake += valorTaxa
               valorTaxa = self.taxas["BridgeSemana"][0]
               self.somaBridge += valorTaxa
               valorTaxa = self.taxas["RidgeSemana"][0]
               self.somaRidge += valorTaxa
           else:
               valorTaxa = self.taxas["LakeFIM"][0]
               self.somaLake += valorTaxa
               valorTaxa = self.taxas["BridgeFIM"][0]
               self.somaBridge += valorTaxa
               valorTaxa = self.taxas["RidgeFIM"][0]
               self.somaRidge += valorTaxa

    def calculaDiariasReward(self,diasPesquisa):

        for item in diasPesquisa:
            if (item < 6):
                valorTaxa = self.taxas["LakeSemana"][1]
                self.somaLake += valorTaxa
                valorTaxa = self.taxas["BridgeSemana"][1]
                self.somaBridge += valorTaxa
                valorTaxa = self.taxas["RidgeSemana"][1]
                self.somaRidge += valorTaxa
            else:
                valorTaxa = self.taxas["LakeFIM"][1]
                self.somaLake += valorTaxa
                valorTaxa = self.taxas["BridgeFIM"][1]
                self.somaBridge += valorTaxa
                valorTaxa = self.taxas["RidgeFIM"][1]
                self.somaRidge += valorTaxa

    def getValorLake(self):
        return self.somaLake
    def getValorBridge(self):
        return self.somaBridge
    def getValorRidge(self):
        return self.somaRidge