from fabric.api import *
from django.utils import timezone
from datetime import *
import re

env.user="webasr"
env.hosts=["squeal.dcs.shef.ac.uk"]
env.password="asr4daweb"
env.host_string = "squeal.dcs.shef.ac.uk"

@hosts("squeal.dcs.shef.ac.uk")
def process_execute(localpaths,filename,command):

	month = datetime.now().month
	if month < 10:
		month = '0'+str(month)
	year = str(datetime.now().year)
	date = year+str(month)
	
	for localpath in localpaths:

		localpath = localpath.lstrip('/Users/jeremychristian/Documents/project/server/')

		print localpath
		# file_start = '.*?((?:[a-z][a-z\\.\\d_]+)\\.(?:[a-z\\d]{3}))(?![\\w\\.])'
		file_start = '(/[^/]*\.wav)'
		file_regex = re.compile(file_start,re.IGNORECASE|re.DOTALL)
		file_search = file_regex.search(localpath)
		if file_search:
			filename_old = file_search.group(1)
	
		put(localpath,'/share/spandh.ami1/srv/webasr/filestore/input/'+date+'/')
		if len(localpaths) == 1:
			run('mv '+'/share/spandh.ami1/srv/webasr/filestore/input/'+date+filename_old+' /share/spandh.ami1/srv/webasr/filestore/input/'+date+'/'+filename+'.wav')
		else: 
			run('mv '+'/share/spandh.ami1/srv/webasr/filestore/input/'+date+filename_old+' /share/spandh.ami1/srv/webasr/filestore/input/'+date+'/'+filename+'_chn-'+(('0000'+str(channel))[-5:])+'.wav')
			channel = channel + 1

	with cd('/share/spandh.ami1/srv/webasr'):
		run('mkdir proc/'+filename+' proc/'+filename+'/data')
		run('touch proc/'+filename+'/'+filename+'.cfg')
		run('touch proc/'+filename+'/'+filename+'.dal')
		with cd('proc/'+filename):
			run("echo '[Execute]' >> "+filename+'.cfg')
			run("echo 'Priority = 0' >> "+filename+'.cfg')
			for x in range(1,(len(localpaths)+1):
				run("echo '"+filename+'_chn-'+(('0000'+str(x))[-5:])+"' >> "+filename+'.dal')
				with cd('data/'):	
					run('ln -s /share/spandh.ami1/srv/webasr/filestore/input/201507/'+filename+'.wav '+filename+'_chn-'+(('0000'+str(x))[-5:])+'.audio')
	run(command+' '+filename)
