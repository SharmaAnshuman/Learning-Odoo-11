# -*- coding: utf-8 -*-
{
    'name': "Zapp®",
    'summary': 'Manage your notes',
	'author': 'Odoo India',
    'description': """
		
		Zapp® is a simple and awesome notepad app. 
		It gives you a quick and simple notepad editing experience 
		when you write notes, memos, e-mails, messages, shopping lists and to-do lists. 
		Taking notes with Zapp® Notepad is easier than any other notepad or memo pad app. 
		
		
			- Zapp®
    
	
    """,
	'website': 'http://www.ashusharma.com/',
	'sequence': '0',
	'category': 'Developer',
    'depends': ['base'],
    'data': [
        'views/view.xml',
    ],
    'application':True,
    'installable':True,
    'auto_install':False,
}