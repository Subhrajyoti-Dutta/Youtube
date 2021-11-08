from upload import Upload

uploadMyVid = Upload(
    CLIENT_SECRET_FILE = 'Client_Secret_File.json'
)

uploadMyVid.credentials(
    catID = 23,
    title = '12 oct 2021',
    desc  = 'Video1',
    tags  = ['durga']
)

uploadMyVid.scope(
    privacyStatus = 'public',
)

uploadMyVid.notifySubscribers(
    notify = False
)

uploadMyVid.uploadVideo(
    videoPath = 'Video1.mp4'
)