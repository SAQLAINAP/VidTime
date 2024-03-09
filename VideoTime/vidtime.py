try:
    from pytube import YouTube as yt, Playlist as pl
    p=pl(input("Enter the playlist link (with https:// format) :  "))
    length=0
    number=0
    free=int(input("How many hours can you dedicate forlearning in a day? "))
    freew=free*7
    for video in p.videos:
        number=len(p.videos)
        length+=video.length
    print("Number of videos in the playlist: ", number)
    # print("Total length of the playlist: ", length, "seconds")
    print("Total length of the playlist: ", round(length/60, 2), "minutes")
    print("Total length of the playlist: ", round(length/3600, 2), "hours")

    if length <= freew * 3600:
        print("You can complete the playlist in under a day")
    elif length <= freew * 3600 * 24:
        print("You can complete the playlist in approximately a day")
    elif length <= freew * 3600 * 24 * 7:
        print("You can complete the playlist in a week")
    elif length <= freew * 3600 * 24 * 2:
        print("You can complete the playlist in 2 days")
    elif length <= freew * 3600 * 24 * 3:
        print("You can complete the playlist in 3 days")
    elif length <= freew * 3600 * 24 * 4:
        print("You can complete the playlist in 4 days")
    else:
        print("You can complete the playlist in more than 4 days")

    print("Do you want more statistics? (y/n)")
    if input() == 'y':
        print("the title of the playlist: ", p.title)
        print("the number of views in the playlist: ", p.views)
        # like_percentage = (pl.likes / p.views) * 100
        # dislike_percentage = (pl.dislikes / p.views) * 100 
        # print("Like percentage of the playlist: ", like_percentage, "%")
        # print("Dislike percentage of the playlist: ", dislike_percentage, "%")
        # print("The rating of the playlist: ", p.rating)
        # print("the author of the playlist: ", p.author)
    else:
        print("Goodbye")

    print("Wanna Try Beta Feature? (y/n)")
    if input() == 'y':
        print("Enter the video link (with https:// format) : ")
        link = input()
        video = yt(link)
        print("Title of the video: ", video.title)
        print("Number of views: ", video.views)
        length_minutes = video.length // 60
        length_seconds = video.length % 60
        print("Length of the video: ", length_minutes, "minutes", length_seconds, "seconds")
        print("Rating of the video: ", video.rating)
        print("Description of the video: ", video.description)
    else:
        print("Goodbye again!!")

    print("Thank you for using vidtime")
except Exception as e:
    print("An error occurred:", str(e))




    