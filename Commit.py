import os
import datetime

# Path ke folder tempat repositori git berada
REPO_PATH = "/path/to/your/git/repository"

# Ganti dengan URL remote repository Git Anda
REMOTE_REPO_URL = "https://github.com/user/repo.git"

# Ganti dengan email dan username Git Anda
GIT_EMAIL = "email@example.com"
GIT_USERNAME = "username"

# Inisialisasi folder tempat repositori berada dan remote repository
os.chdir(REPO_PATH)
os.system("git remote add origin " + REMOTE_REPO_URL)

# Buat file log.txt jika belum ada
if not os.path.exists("log.txt"):
    with open("log.txt", "w") as file:
        pass

# Fungsi untuk membuat commit
def fakeCommit(days: int):
    if days < 1:
        os.system("git push origin main")
    else:
        commit_date = datetime.datetime.now() - datetime.timedelta(days=days)
        date_str = commit_date.strftime("%Y-%m-%d")

        with open("log.txt", "a") as file:
            file.write(f"{date_str} \n")

        os.system("git add log.txt")
        os.system(f'git -c user.email="{GIT_EMAIL}" -c user.name="{GIT_USERNAME}" commit --date="{date_str}" -m "Commit for the day {date_str}"')

        # Recursive call to create commits for the next day
        fakeCommit(days - 1)

# Panggil fungsi fakeCommit dengan parameter 365 hari
fakeCommit(365)
