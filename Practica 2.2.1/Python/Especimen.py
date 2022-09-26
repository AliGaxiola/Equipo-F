#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Organismo
from typing import List

class Especimen(Organismo):
	def getEspecie(self):
		return self.___especie

	def setEspecie(self, aEspecie) -> None:
		self.___especie = aEspecie

	def getRaza(self):
		return self.___raza

	def setRaza(self, aRaza) -> None:
		self.___raza = aRaza

	def getDieta(self):
		return self.___dieta

	def setDieta(self, aDieta) -> None:
		self.___dieta = aDieta

	def __init__(self):
		self.___especie = None
		self.___raza = None
		self.___dieta = None

