This repo is an API service that gives an audio url for a youtube video

default port: 5000
Endpoints: /mp3
argument: url=https://www.youtube.com/watch?v=xxxxxxxxxxx

example: 127.0.0.0:5000/mp3?https://www.youtube.com/watch?v=dQw4w9WgXcQ

response JSON:
{
  "url": "mp3.url.com...."
}

Error responses:
No parameter:
Error code: 400
{
  "description": "Please pass the url as a param example: /mp3?url=myurl",
  "error": "no_url"
}

Wrong url:
Error code: 400
{
  "description": "The url is not from youtube",
  "error": "wrong_url"
}

The video is age restricted:
Error code: 400
{
  "description": "The video is age restricted!",
  "error": "age_restricted"
}
