#!/usr/bin/python
#-*- coding: utf-8 -*-
from ..Entities.Usuario import Usuario
class UsuarioService:
    def __init__(self):
        pass
    def registrarseEnEvento(self, Usuario, Evento):
        usuario_actual = Usuario.getUsuario(self, Usuario.getId())
        if usuario_actual is not None:
            usuario_actual.setEventos(Evento)
            Usuario.updateUsuario(self, Usuario.getId(), usuario_actual)
            return True
        else:
            return False

    def contactarPonente(self, Evento):
        pass

    def buscarEvento(self, String):
        pass

    def contactarOrganizador(self, Evento):
        pass

