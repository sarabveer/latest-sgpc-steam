import subprocess

match_title = 'Sachkhand Sri Harmandir Sahib'
command = f'yt-dlp https://www.youtube.com/@SGPCSriAmritsar/streams -g -f "ba[ext=mp4]" --lazy-playlist --max-downloads 1 --match-filter "live_status = is_live & title *= \"{match_title}\""'

def get_stream():
  try:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    url = result.stdout.decode('utf-8').strip()
    
    if url == '':
      return None
    
    return url
 
  except:
    return None
