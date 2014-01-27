# -*- coding: utf-8-*-
from osv import osv,fields
import datetime

class usuario(osv.Model):
	_name="gid.usuario"

	_columns={
		'name':fields.char('Primer Nombre',size=100,required=True),
		'segundo_nombre':fields.char('Segundo Nombre',size=100),
		'primer_apellido':fields.char('Primer Apellido',size=100,required=True),
		'segundo_apellido':fields.char('Segundo Apellido',size=100),
		'document_type_id':fields.many2one('gid.document_type','Tipo Documento',required=True),
		'celular':fields.char('Telefono Celular',size=10),
		'ref':fields.char('Numero Identificacion',size=15,required=True),
		'city_id':fields.many2one('gid.city','Ciudad',required=True),
		'fecha_nacimiento':fields.date('Fecha Nacimiento',required=True),
		'edad':fields.integer('Edad'),
	}

	def onchange_calcular_edad(self,cr,uid,ids,fecha_nacimiento):
		res={'value':{}}
		anio=int(fecha_nacimiento[0:4])
		mes=int(fecha_nacimiento[5:7])
		dia=int(fecha_nacimiento[8:10])
		fecha_actual=datetime.datetime.now()
		fecha_nacimiento=datetime.datetime(anio,mes,dia)
		diff=  fecha_actual - fecha_nacimiento
		edad= diff.days/365
		res['value']['edad']=edad
		return res



	def _check_name(self,cr,uid,ids):
		numero_prohibidos=['310','311','312','313','314','315','316','317','318','320','321']
		for cedula in self.browse(cr, uid, ids):
			for i in numero_prohibidos:
				if i in cedula.ref[0:3]:
					return False # No se permite esos numeros al iniciar una cedula
		return True
		

	_constraints = [(_check_name, 'Confirme que no sea un Numero Celular', ['ref'])]		
	sql_constraints = [('UKRef','unique(ref)', 'Esta Cedula ya Existe')]