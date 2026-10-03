from fastapi import FastAPI
from pydantic import BaseModel

from urgencias import Urgencias

app = FastAPI()
urgencias = Urgencias()


class Paciente(BaseModel):
    documento: str
    nombre: str
    edad: int
    nivel: int
    motivo: str


@app.post("/pacientes")
def registrar(datos: Paciente):
    return urgencias.registrar(datos.documento, datos.nombre, datos.edad, datos.nivel, datos.motivo)


@app.get("/cola")
def ver_cola():
    return urgencias.ver_fila()


@app.get("/cola/siguiente")
def ver_siguiente():
    return urgencias.siguiente()


@app.post("/cola/atender")
def atender():
    return urgencias.atender()


@app.delete("/pacientes/{turno}")
def retirar(turno: str):
    return urgencias.retirar(turno)


@app.get("/cola/estado")
def ver_estado():
    return urgencias.estado()
