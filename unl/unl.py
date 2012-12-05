# -*- encoding: utf-8 -*-

##############################################################################
#
# Copyright (c) 2004 TINY SPRL. (http://tiny.be) All Rights Reserved.
#                    Fabien Pinckaers <fp@tiny.Be>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from osv import osv, fields

areas = (('AEIRNNR', 'AEIRNNR'), 
         ('AARNR', 'AARNR'), 
         ('AEAC', 'AEAC'), 
         ('AJSA', 'AJSA'), 
         ('ASH', 'ASH'))

#class unl_carrera(osv.osv):
#    """Carreras"""
#    _name = 'unl.carrera'
#    _columns = {
#        'nombre': fields.char('Nombre',size=150, help='Nombre de la Carrera'),
#        'area': fields.selection(areas, "Area", help='Area Academica Administrativa')
#    }
#unl_carrera()
#

class unl_estudiante(osv.osv):
    """Estudiantes"""
    _name = 'unl.estudiante'
    _columns = {
        'dni': fields.char('Cedula', size=15, help='Cedula o Pasaprte de Identidad'),        
        'nombres': fields.char('Nombres',size=35, help='Nombres del Estudiante'),
        'apellidos': fields.char('Apellidos', size=35, help='Apellidos del Docente'),
        'ingreso': fields.date('Inicio de Estudios', help=u'Fecha en la que inició sus estudios'),
        'duracion_carrera': fields.integer(u'Duración en Años', help=u'Duración de la Carrera en años'),
        'egresado': fields.date('Egresado', help='Fecha en la que egreso de la carrera'),
        'semestre_egreso': fields.integer('Semestre_Egreso', help='Semestre en el que egreso'),
        'graduado': fields.date('Gradudado', help="Fecha de graduacion"),
        'titulo': fields.char('Titulo', size=35, help='Titulo que obtuvo en la Carrera'),
        'carrera': fields.char('Carrera',size=150, help='Nombre de la Carrera'),
        'area': fields.selection(areas, 'Area', help='Area Academica Administrativa de la UNL')
        'anio_ingreso' : fields.function (anio_ingreso, type = 'integer', string = u'Año de Ingreso'),
#	'carrera_ids': fields.many2many(
#            'unl.carrera',
#            'estudiante_carrera_rel',
#            'estudiante_id',
#            'carrera_id',
#            'Carreras'
#        )
    }

    def anio_ingreso(self, cr, uid, ids, fields, arg, context=None):
        records = self.browse(cr, uid, ids)
        print "testing ...", records
        r = records[0]
        result = {}
        result[r.id] = r.igreso.year
        return result

    _sql_constraints = [
        ('dni_carrera_unique', 'unique(dni, carrera)', u'La Cédula y la Carrera deben ser únicos !'),
        ]

    _defaults = { 
    }

unl_estudiante()

class unl_docente(osv.osv):
    """ Docentes """
    _name = 'unl.docente'
    _columns = {
        'dni': fields.char('Cedula', size=15, help='Cedula o Pasaprte de Identidad'),
        'nombres': fields.char('Nombres',size=35, help='Nombres del Docente'),
        'apellidos': fields.char('Apellidos',size=35, help='Apellidos del Docente'),
        'carrera': fields.char('Carrera',size=150, help='Nombre de la Carrera'),
        'area': fields.selection(areas, 'Area', help='Area Academica Administrativa de la UNL')
#        'carrera_ids': fields.many2many(
#            'unl.carrera',
#            'docente_carrera_rel',
#            'doente_id',
#            'carrera_id',
#            'Carreras'
#        )
    }

    _defaults = { 
    }      
unl_docente()

