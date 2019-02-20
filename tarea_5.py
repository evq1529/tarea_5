# Directorio de pacientes de una clínica

class Pacientes():
    diccionario_pacientes = {}

    def __init__(self, id = None, nombre = None, apellido = None,
                 telefono = None, direccion = None, list_enfermedades = None,
                 list_medicamentos = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.list_enfermedades = list_enfermedades
        self.list_medicamentos = list_medicamentos

        if self.id == None:
            self.x = []
            self.y = []
        else:
            self.x = [id]
            self.y = [[self.nombre, self.apellido, self.telefono, self.direccion,
                       self.list_enfermedades, self.list_medicamentos]]
            self.diccionario_pacientes = dict(zip(self.x, self.y))

    def AddPaciente(self, id, nombre, apellido, telefono, direccion, list_enfermedades,
        list_medicamentos):
        self.x.append(id)
        lista_auxiliar = [nombre, apellido, telefono, direccion,
              list_enfermedades, list_medicamentos]
        self.y.append(lista_auxiliar)
        self.diccionario_pacientes = dict(zip(self.x, self.y))

    def DeletePaciente(self, id):
        if self.diccionario_pacientes.get(id, None) != None:
            del self.diccionario_pacientes[id]

    def AgregarEnfermedad(self, id, enfermedad):
        if self.diccionario_pacientes.get(id, None) != None:
            lista_auxiliar = self.diccionario_pacientes[id]
            self.list_enfermedades = list(set(lista_auxiliar[4] + [enfermedad]))
            self.diccionario_pacientes[id][4] = self.list_enfermedades

    def AgregarMedicamentos(self, id, medicamento):
        if self.diccionario_pacientes.get(id, None) != None:
            lista_auxiliar = self.diccionario_pacientes[id]
            self.list_medicamentos = list(set(lista_auxiliar[5] + [medicamento]))
            self.diccionario_pacientes[id][5] = self.list_medicamentos

    def Reporte_Enfermedades(self):
        enfermedades = [self.diccionario_pacientes[i][4]
                        for i in list(self.diccionario_pacientes)]
        list_enfer = set()
        for i in range(len(enfermedades)):
            list_enfer = list_enfer | set(enfermedades[i])

        print("La lista de enfermedades es: {}".format(list(list_enfer)))

    def Reporte_Medicamentos(self):
        medicamentos = [self.diccionario_pacientes[i][5]
                        for i in list(self.diccionario_pacientes)]
        list_medi = set()
        for i in range(len(medicamentos)):
            list_medi = list_medi | set(medicamentos[i])

        print("La lista de medicamentos es: {}".format(list(list_medi)))

    def Comparando_Pacientes(self, id1, id2):
        if (self.diccionario_pacientes.get(id1, None) != None) & (self.diccionario_pacientes.get(id2, None) != None):
            enfermedades_id1 = self.diccionario_pacientes[id1][4]
            medicamentos_id1 = self.diccionario_pacientes[id1][5]
            enfermedades_id2 = self.diccionario_pacientes[id2][4]
            medicamentos_id2 = self.diccionario_pacientes[id2][5]
            enfermedades_comunes = list(set(enfermedades_id1) & set(enfermedades_id2))
            enfermedades_distintas_1_2 = list(set(enfermedades_id1) - set(enfermedades_id2))
            enfermedades_distintas_2_1 = list(set(enfermedades_id2) - set(enfermedades_id1))
            medicamentos_comunes = list(set(medicamentos_id1) & set(medicamentos_id2))
            medicamentos_distintos_1_2 = list(set(medicamentos_id1) - set(medicamentos_id2))
            medicamentos_distintos_2_1 = list(set(medicamentos_id2) - set(medicamentos_id1))
            print("Los pacientes tienen las siguientes "
              "enfermedades en común: {}".format(enfermedades_comunes))
            print("Los pacientes tienen los siguientes "
              "medicamentos en común: {}".format(medicamentos_comunes))
            print("El primer paciente tiene las siguientes "
              "enfermedades no comunes con respecto al segundo: {}".format(enfermedades_distintas_1_2))
            print("El segundo paciente tiene las siguientes "
              "enfermedades no comunes con repecto al primero: {}".format(enfermedades_distintas_2_1))
            print("El primer paciente tiene los siguientes "
              "medicamentos no comunes con respecto al segundo: {}".format(medicamentos_distintos_1_2))
            print("El segundo paciente tiene los siguientes "
              "medicamentos no comunes con respecto al primero: {}".format(medicamentos_distintos_2_1))
            print("--------------------------------------------")
        else:
            print("Algún id es incorrecto")

# Usando la clase
pacientes = Pacientes()

# Añadiendo pacientes
pacientes.AddPaciente(1, "Enrique", "Vílchez", 80808080,
                      "Heredia", ["Alergias", "Migraña"],
                      ["Acetaminofen"])
pacientes.AddPaciente(2, "Mario", "González", 80008080,
                      "San José", ["Dolor de estómago"],
                      ["AlcaD"])
pacientes.AddPaciente(3, "Jennifer", "Gutiérrez", 80000080,
                      "Cartago", ["Gripe", "Nauseas"],
                      ["Gravol", "Antifludes"])
pacientes.AddPaciente(4, "María", "Morales", 81000080,
                      "Cartago", ["Nauseas"],
                      ["Gravol", "Antifludes"])
print(pacientes.diccionario_pacientes)

# Eliminado paciente
pacientes.DeletePaciente(4)
print(pacientes.diccionario_pacientes)

# Añadiendo enfermedades
pacientes.AgregarEnfermedad(1, "Dolor de pie")
pacientes.AgregarEnfermedad(1, "Migraña")
pacientes.AgregarEnfermedad(2, "Migraña")
pacientes.AgregarEnfermedad(3, "Migraña")
print(pacientes.diccionario_pacientes)

# Añadiendo medicamentos
pacientes.AgregarMedicamentos(1, "Aceta")
pacientes.AgregarMedicamentos(1, "Operación")
pacientes.AgregarMedicamentos(1, "Aceta")
pacientes.AgregarMedicamentos(2, "Descanso")
pacientes.AgregarMedicamentos(3, "Aceta")
print(pacientes.diccionario_pacientes)

# Reportes de enfermedades y medicamentos
pacientes.Reporte_Enfermedades()
pacientes.Reporte_Medicamentos()

# Comparando dos pacientes
pacientes.Comparando_Pacientes(1, 3)
pacientes.Comparando_Pacientes(1, 2)
pacientes.Comparando_Pacientes(3, 2)