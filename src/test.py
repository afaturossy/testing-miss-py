import requests


def test1():
    headers = {
        'Referer': 'https://missav.com/',
        'Origin': 'https://missav.com/'
    }

    url_preview = "https://cdn82.akamai-content-network.com/pppe-146-uncensored-leak/preview.mp4"
    url_playlist_master = "https://cdn152.akamai-content-network.com/bcdn_token=DUW0Ks70pPWifxh5zRhEN4lmO51z7u4g81ff6Erx8mo&expires=1699058042&token_path=%2Fef353afb-f884-4356-93cc-53484cc9cc4e%2F/ef353afb-f884-4356-93cc-53484cc9cc4e/playlist.m3u8"
    url_playlist_1 = "https://cdn152.akamai-content-network.com/bcdn_token=DUW0Ks70pPWifxh5zRhEN4lmO51z7u4g81ff6Erx8mo&expires=1699058042&token_path=%2Fef353afb-f884-4356-93cc-53484cc9cc4e%2F/ef353afb-f884-4356-93cc-53484cc9cc4e/640x360/video.m3u8"
    url_video_1ts = "https://cdn152.akamai-content-network.com/bcdn_token=DUW0Ks70pPWifxh5zRhEN4lmO51z7u4g81ff6Erx8mo&expires=1699058042&token_path=%2Fef353afb-f884-4356-93cc-53484cc9cc4e%2F/ef353afb-f884-4356-93cc-53484cc9cc4e/640x360/video0.ts"

    res = requests.get(url_video_1ts, headers=headers)

    # print(res.text)

    with open("video1.mp4", "wb") as f:
        f.write(res.content)


if __name__ == "__main__":
    test1()

