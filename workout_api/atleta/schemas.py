from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", examples="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", examples="00000000000", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=80.1)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", examples=1.80)]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples="M", max_length=1)]