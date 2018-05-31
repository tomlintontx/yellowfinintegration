from suds.client import Client

class WebServices():

	def login_user(username):
		url = 'http://panama.yellowfin.bi:8075/services/AdministrationService?wsdl'
		client = Client(url)

		orgRef = {
			'tom.linton@yellowfin.bi': 'North America',
			'matt.wilson@yellowfin.bi': 'North America',
			'conner.madigan@yellowfin.bi': 'North America',
			'tyler.mcgraw@yellowfin.bi': 'North America',
			'yulia.astrelina@yellowfin.bi': 'Australia',
			'tim.mcintosh@yellowfin.bi': 'Australia',
			'chithresh.suresh@yellowfin.bi': 'Australia',
			'rob.aldridge@yellowfin.bi': 'Australia',
			'emma.urli@yellowfin.bi': 'Australia',
			'sam.vadodaria@yellowfin.bi': 'Europe',
			'brett.churchill@yellowfin.bi': 'Europe'
		}


		asr1 = {		

			'loginId': 'tom.linton@yellowfin.bi',
			'password': 'test',
			'orgId': 1,
			'function': 'LOGINUSER',
			'orgRef': orgRef[username]
		}

		ap1 = {
			'userId': username,
			'password': 'test'
		}

		asr1['person'] = ap1

		result1 = client.service.remoteAdministrationCall(asr1)

		ssoURL = 'http://panama.yellowfin.bi:8075/logon.i4?LoginWebserviceId=' + result1['loginSessionId']
		iframeURL = 'http://panama.yellowfin.bi:8075/logon.i4?LoginWebserviceId=' + result1['loginSessionId'] + '&disableheader=true'
		reportsIframe = 'http://panama.yellowfin.bi:8075/logon.i4?LoginWebserviceId=' + result1['loginSessionId'] + '&entry=BROWSE' + '&disableheader=true' + '&yftoolbar=false' + '&disablelogoff=true'
		admin = 'http://panama.yellowfin.bi:8075/logon.i4?LoginWebserviceId=' + result1['loginSessionId'] + '&entry=ADMINISTRATION' + '&disableheader=true' + '&yftoolbar=false' + '&disablelogoff=true'

		urls = {
			'ssoURL': ssoURL,
			'iframeURL': iframeURL,
			'reportsIframe': reportsIframe,
			'administration': admin
		}

		return urls
		
