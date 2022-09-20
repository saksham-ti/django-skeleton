def append_to_gitignore_file(ignored_line):
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write(ignored_line)
        gitignore_file.write("\n")


def main():
    append_to_gitignore_file(".env")
    append_to_gitignore_file(".envs/*")

if __name__ == "__main__":
    main()