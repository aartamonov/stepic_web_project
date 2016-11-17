CONFIG = {
	'mode': 'wsgi',
	'working_dir': '/home/cahek/webProg/web',
	'args': (
		'--bind=0.0.0.0:8080',
		'--daemon',
		'--workers=2',
		'hello:app'
	)
}
