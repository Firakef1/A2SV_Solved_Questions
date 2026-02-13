class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def getFileNameContents(fileStr: str) -> (str, str):
            items = fileStr.split("(")

            file_name = items[0]
            file_contents = items[1].rstrip(")")

            return (file_name, file_contents)

        def getDirectoryAndFiles(path: str) -> (str, List[str]):
            items = path.split(" ")

            directory = items[0]
            files = items[1:]

            return (directory, files)


        dup_files = collections.defaultdict(list)

        for path in paths:
            directory, file_list = getDirectoryAndFiles(path)

            for file in file_list:
                file_name, file_contents = getFileNameContents(file)
                dup_files[file_contents].append(directory + "/" + file_name)

        result = []
        for k, v in dup_files.items():
            if len(v) == 1:
                continue

            current = []
            for p in v:
                current.append(p)

            result.append(current)
        return result