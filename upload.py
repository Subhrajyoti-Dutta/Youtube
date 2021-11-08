import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


class Upload():
	# CLIENT_SECRET_FILE = 'Client_Secret_File.json'
	API_NAME = 'youtube'
	API_VERSION = 'v3'
	SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

	def __init__(self, CLIENT_SECRET_FILE):
		self.service = Create_Service(CLIENT_SECRET_FILE, Upload.API_NAME, Upload.API_VERSION, Upload.SCOPES)
		self.request_body = dict()


	def credentials(self, catID, title, desc, tags):
		self.request_body['snippet'] = {
				# 'categoryId': catID,
				'title': title,
				# 'description': desc,
				# 'tags': tags
			}

	def scope(self, privacyStatus, uploadDate = None, madeForKids = False):
		self.request_body['status'] = {
				'privacyStatus': privacyStatus,
				# 'publishAt': uploadDate,								# datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'
				'selfDeclaredMadeForKids': madeForKids,
			}
	
	def notifySubscribers(self, notify = True):
		self.request_body['notifySubscribers'] = notify

	def uploadVideo(self, videoPath):
		self.response_upload = self.service.videos().insert(
			part = 'snippet,status',
			body = self.request_body,
			media_body = MediaFileUpload(videoPath)
		).execute()

	def uploadThumbnail(self, imgPath):
		self.service.thumbnails().set(
			videoId = self.response_upload.get('id'),
			media_body = MediaFileUpload(imgPath)
		).execute()
