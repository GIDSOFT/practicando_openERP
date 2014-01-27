#-*- coding: utf-8-*-
from osv import osv, fields

class gid_document_type(osv.Model):
	_name= 'gid.document_type'
	_columns={
		'code': fields.char('Code', required=True, size=4),
		'name': fields.char('Name', required=True, size=50),
	}


	_sql_constraints = [('UKDocument_type','unique(code,name)', 'Este Nombre o Codigo ya Existe..')]