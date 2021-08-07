from flask import Flask, abort, request, jsonify
from flask_cors import CORS
import youtube_dl

app = Flask(__name__)

resources={
    r"/mp3": {"origins":"http://localhost:3000"}, 
}

CORS(app, resources=resources)


def GetMP3URL(url):
    YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        I_URL = info['formats'][0]['url']
        return I_URL


@app.errorhandler(400)
def client_error(e):
    return jsonify(e.description), 400


@app.route("/mp3", methods=["GET"])
def getrequest():
    url = request.args.get("url")
    if url == None:
        abort(400, description={
                "description": "Please pass the url as a param example: /mp3?url=myurl",
                "error": "no_url"
                })
    if "youtu" not in url:
        abort(400, description={
                "description": "The url is not from youtube",
                "error": "wrong_url"
                })
    try:
        mp3_url = GetMP3URL(url)
        return {"url":mp3_url}
    except youtube_dl.utils.DownloadError as e:
        if str(e.exc_info[1]) == "Sign in to confirm your age\nThis video may be inappropriate for some users.":
            abort(400, description={
                    "description": "The video is age restricted!",
                    "error": "age_restricted"
                    })


if __name__ == "__main__":
    app.run(threaded=True, port=5000)