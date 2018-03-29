from suds.client import Client

class WebServices():

	def login_user():
		url = 'http://panama.yellowfin.bi:8075/services/AdministrationService?wsdl'
		client = Client(url)

		asr = {		

			'loginId': 'tom.linton@yellowfin.bi',
			'password': 'test',
			'orgId': 1,
			'function': 'LOGINUSER'
		}

		ap = {
			'userId': 'tom.linton@yellowfin.bi',
			'password': 'test'
		}

		asr['person'] = ap

		result = client.service.remoteAdministrationCall(asr)

		newURL = 'http://panama.yellowfin.bi:8075/logon.i4?LoginWebserviceId=' + result['loginSessionId']

		return newURL
