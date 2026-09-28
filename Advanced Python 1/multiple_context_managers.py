with (
    open("file1.txt", "r") as f1,
    open("file2.txt", "r") as f2,
    open("merged.txt", "w") as f3
):
    content1 = f1.read()
    content2 = f2.read()
    f3.write(content1 + "\n" + content2)