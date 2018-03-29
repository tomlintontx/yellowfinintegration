from suds.client import Client

class WebServices(object):

  def __init__(self):
    super(my_db, self).__init__()
    self.host = "http://panama.yellowfin.bi:8075/"
    self.uname = "tom.linton@yellowfin.bi"
    self.pword = 'test'

  def login_user(self):
	url = 'http://panama.yellowfin.bi:8075/services/AdministrationService?wsdl'
	client = Client(url)

	asr = {		

		'loginId': self.uname,
		'password': self.pword,
		'orgId': 1,
		'function': 'LOGINUSER'
	}

	ap = {
		'userId': self.uname,
		'password': self.pword
	}

	asr['person'] = ap

	result = client.service.remoteAdministrationCall(asr)

	newURL = self.host + 'logon.i4?LoginWebserviceId=' + result['loginSessionId']

	return newURL
