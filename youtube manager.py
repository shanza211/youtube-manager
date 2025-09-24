# Youtube Manager Application
# This application allows users to manage a list of YouTube videos.

import json

def load_data():
    try:
        with open("Youtube.json", "r") as file:
            test = json.load(file) #loads json data from file
            print(type(test))
            return test
    except FileNotFoundError:
        return [] #returns empty list if file not found

def save_data_helper(videos):
    with open("Youtube.json", "w") as file:
        json.dump(videos, file) #dumps json data to file

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*"*70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of the video to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            videos[index] = {"name": name, "time": time}
            save_data_helper(videos)
            print("Video updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of the video to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted = videos.pop(index)
            save_data_helper(videos)
            print(f"Deleted video: {deleted['name']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option:")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting Youtube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
