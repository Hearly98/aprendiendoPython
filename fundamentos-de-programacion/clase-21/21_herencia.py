class Vehículo:
  def __init__(self, marca, modelo, precio):
      self.marca = marca
      self.modelo = modelo
      self.precio = precio
      self.disponible = True

  def vender(self):
      if self.disponible:
          self.disponible = False
          print(f"El vehículo {self.marca} ha sido vendido.")
      else:
          print(f"El vehículo {self.marca} no está disponible.")

  def estado(self):
      return self.disponible

  def get_price(self):
      return self.precio

#Creando una clase Auto que herede de Vehículo

class Auto(Vehículo):
    def start(self):
        if self.disponible:
            return f"El motor del coche {self.marca} está en marcha."
        else:
            return f"El coche {self.marca} no está disponible."

    def stop(self):
        if self.disponible:
            return f"El motor del coche {self.marca} se ha detenido."
        else:
            return f"El coche {self.marca} no está disponible."