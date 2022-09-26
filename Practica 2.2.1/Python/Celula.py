#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Organismo
from typing import List

class Celula(object):
	def getTipoDeCelula(self) -> str:
		return self.___tipoDeCelula

	def setTipoDeCelula(self, aTipoDeCelula) -> None:
		pass

	def __init__(self):
		self.___tipoDeCelula : str = None
		self._partOf : Organismo = None

