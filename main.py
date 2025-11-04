import database
import tui

def main():
    database.init_db()
    tui.main_menu()

if __name__ == "__main__":
    main()