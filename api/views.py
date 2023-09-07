from django.shortcuts import render
from django.http import JsonResponse
import datetime

# Create your views here.
def api_view(request):
	data = {
		'slack_name': request.GET.get('slack_name'),
		'current_day': datetime.datetime.today().strftime('%A'),
		'utc_time': datetime.datetime.utcnow().isoformat().split('.')[0]+'Z',
		'track': request.GET.get('track'),
		'github_file_url': 'https://github.com/TegaRorobi/HNGx-backend-stage1-task/blob/master/api/views.py',
		'github_repo_url': 'https://github.com/TegaRorobi/HNGx-backend-stage1-task/',
		'status_code': 200
	}

	return JsonResponse(data)