import os
import datetime

# Buat file log.txt jika belum ada
if not os.path.exists("log.txt"):
    open("log.txt", "w").close()

def fakeCommit(days: int):
    if days < 1:
        os.system("git push")
    else:
        commit_date = datetime.datetime.now() - datetime.timedelta(days=days)
        date_str = commit_date.strftime("%Y-%m-%d")

        # Tambahkan tanggal commit ke dalam file log.txt
        with open("log.txt", "a") as file:
            file.write(f"{date_str}\n")

        # Lakukan commit
        os.system("git add log.txt")
        os.system(f'git commit --date="{date_str}" -m "Commit for the day {date_str}"')

        # Panggil fungsi fakeCommit dengan argumen days - 1
        fakeCommit(days - 1)

# Panggil fungsi fakeCommit dengan argumen 365
fakeCommit(365)
