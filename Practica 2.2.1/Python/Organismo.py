#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Celula
from typing import List

class Organismo(object):
	def getReproduccion(self) -> str:
		return self.___reproduccion

	def setReproduccion(self, aReproduccion) -> None:
		pass

	def getEtapasdevida(self) -> int:
		return self.___etapasdevida

	def setEtapasdevida(self, aEtapasdevida) -> None:
		pass

	def __init__(self):
		self.___reproduccion : str = None
		self.___etapasdevida : int = None
		self._partOf : Celula = None
		"""# @AssociationKind Composition"""

