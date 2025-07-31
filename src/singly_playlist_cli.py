# singly playlist challenge

class Song:
    def __init__(self, data):
        self.data = data
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.playlist_name = None

    def create_playlist(self):
        print("===SAVE SONGS===")
        self.playlist_name = str(input("Enter your playlist name: ")) + ".txt"
        with open(self.playlist_name, 'a') as file:
            pass
        print(f"Playlist {self.playlist_name} created!")
        print("================")

    def add_song(self):
        print("====ADD SONG====")
        user_song = str(input("Enter your song's name: "))
        new_song = Song(user_song)
        if self.head is None:
            self.head = new_song
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_song
        if self.playlist_name == None:
            print("It seems like you don't have a playlist created.")
            print("Let's make one!")
            self.create_playlist()
            
        with open(self.playlist_name, 'a') as file:
            file.write(user_song + '\n')

        print(f"Song added: {user_song}")
        print("================")
    
    def traverse(self):
        print("====PLAYLIST====")
        current = self.head
        if not current:
            print("Nothing here :(")
        while current:
            print(f"{current.data}")
            current = current.next
        print("================")
    
    def play_next(self):
        print("==PLAYING SONG==")
        if not self.head:
            print("End of the playlist has been reached :(")
            print("Add songs to continue listening!")
        else:
            print(f"Now playing {self.head.data}")
            self.head = self.head.next
        print("================")

def singly_playlist():
    play = Playlist()
    print("Welcome to the singly playlist!")
    while True:
        print("Whaddya wanna do?")
        print("======MENU======")
        user_choice = input("(1) Add songs\
        \n(2) Play Next\n(3) View Playlist\
        \n(4) Create Playlist\
        \n(5) Exit\n================\
        \nEnter your choice: ")
        if user_choice == "1":
            play.add_song()
        elif user_choice == "2":
            play.play_next()
        elif user_choice == "3":
            print("Here is your current playlist!")
            play.traverse()
        elif user_choice == "4":
            play.create_playlist()
        elif user_choice == "5":
            print("Bye-bye!")
            break
        else:
            print("Please input a valid option :(")
        
singly_playlist()
