import subprocess
import requests
def subtitulos():
    url  ="https://www.opensubtitles.com/download/DE0203767C491132A8A4134AA85C713D9D7AB2B7620A0CBD2FE660E1666783CB6B3E4F5A66A022BAF11AD47061E00740E15E0909821CDA346F2F90FA9EBC3FA86A3626A7D4A716F746FE89B1E7EA2E11452099F5BC2BEEE8BFE849B426A778670529B38ED85C681403B0BFFA6D3DFE913AFAAB9C249355FE938ED9C3B18DA3B9BD3E17CF170DE100880C9E010EA91782341854A3FE83AC2E7DBBD1FE1A1DA74AF583B1F9FE98D6180B9608E44570BF279C632646882449CB599AB113A7517EF903961DBD6615578A88C916C7519D52E73C39A6E57B0542FD01155AEF40203F0AAF277994CF23A3A7D30E4ACE0234C478749BB50BCF94D0C09B5926144F2EFF95/subfile/The.Simpsons.S30E14.WEBRip.x264-ION10.srt"
    url_txt = requests.get(url)

    with open("subtitles.srt", "w") as file:
        file.write(url_txt.text)

    print("Subtitulos creados en la carpeta")
    #subprocess.call(["ffmpeg", "-i", "output.mp4", "-map", "0:2", "sub.srt"])
    subprocess.call(["ffmpeg", "-i", "output.mp4", "-i" , "subtitles.str", "-map", "0", "-map","1:s","-c", "copy","-c:s","mov_text", "subtitles.mp4"])


if __name__ == '__main__':
    subtitulos()