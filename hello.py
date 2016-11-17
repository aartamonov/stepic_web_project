def app(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain'), ('Connection', 'Close')
	]
	qs = environ['QUERY_STRING']	
	param_list = qs.split('&')
	result = ''
	for param in param_list:
		result = result + param + "\n"
	body = [result]
#	body = ['<html><body>'] + ['%s<br>' % (str(param)) for param in param_list] + ['</body></html>']
	
	print body
	start_response(status, headers);
	return body
