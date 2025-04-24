import json

def load_data():
    try:
        with open('youtube.txt' , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("""        ------Youtube Manager -------
            1 . fav video list
            2 . add youtube video
            3 . update youtube video 
            4 . delete a video 
            5 . exit 
            """)
        
        choice = input("enter your choice ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _ :
                print("Invalid choice")


if __name__ == "__main__":
    main()
    