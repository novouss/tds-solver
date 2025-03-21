
def yt_transcribe(url: str) -> str:
    """ Transcribes a YouTube video using the provided URL.

    Args:
        url (str): The URL of the YouTube video to transcribe.

    Returns:
        int: The number of words (punctuations included) in the transcription.

    Example:
        >>> yt_transcribe("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        '152'
    """
    import os
    import json
    import yt_dlp
    import pandas as pd
    from helpers.authentication import client

    def clean_transcripts(df_export: pd.DataFrame) -> list[str]:
        export = df_export.to_string(index=False)
        export = export.split("\n")
        for idx, text in enumerate(export):
            export[idx] = text.strip()
        return export
    def download_audio(url: str, filename: str) -> None:
        ydl_opts = {
            "format": "ba[abr<50]/worstaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "32"
            }],
            "outtmpl": f"./data/{filename}.%(ext)s",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    video_code = url.split("=")[1]
    if not os.path.isfile(f"./data/{video_code}.mp3"):
        download_audio(url, video_code)
    audio = open(f"./data/{video_code}.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        file = audio,
        model = "whisper-1",
        response_format = "verbose_json",
        timestamp_granularities = ["word"]
    )
    words = json.loads(transcription.to_json())["words"]
    df = pd.DataFrame(words)
    clip = df[(df["start"] >= 173.4) & (df["end"] <= 229.7)]["word"]
    count = []
    for i in clean_transcripts(clip):
        if ord(i[0]) <= 90 and not (i == "Miranda" or i == "Edmund"):
            count.append(".")
        count.append(i)
    return str(len(count))
