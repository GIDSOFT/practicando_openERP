# -*- coding: utf-8-*-

from osv import osv, fields

class city(osv.Model):
	_name= 'gid.city'
	_columns= {
		'code': fields.char('City Code', required= True, size= 4),
		'name': fields.char('City Name', required= True, size= 200),
		'state_id': fields.many2one('res.country.state', 'State', required= True),
	}


	sql_constraints = [('UKCity','unique(code,name)', 'Este Nombre o Codigo ya Existe..')]