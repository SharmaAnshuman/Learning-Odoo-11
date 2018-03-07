# -*- coding: utf-8 -*-
{
    'name': "Project Management®",
    'summary': 'Projects milestones tasks and more',
    'author': 'Odoo India',
    'description': """
		
		A project management application is a software system used for project planning, resource allocation, tracking of project components, and change management. 
		
		•	Project planning: To define a project schedule, a project manager may use the software to map project tasks and visually describe task interactions.
		•	Task management: Allows the project manager to create and assign tasks, establish deadlines, and produce status reports.
		•	Resource management: Defines responsibilities – who is supposed to do what.
		•	Budgeting and cost tracking: A good project management application facilitates budget reporting as well as viewing, notifying, and updating costs for stakeholders.
		•	Time tracking: The software must have the ability to track time spent on all tasks and maintain records for third-party consultants.

    
	
    """,
    'website': 'http://www.ashusharma.com/',
    'sequence': '0',
    'category': 'Project',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/main.xml',
        'views/manager_view.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
