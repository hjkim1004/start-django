import os
import csv


# file class
class File:
    """
    파일 생성,저장 메소드 관리
    """

    def __init__(self):
        pass

    def isExistPath(self, path):
        if os.path.exists(path):
            return True
        return False

    def isExistFile(self, file):
        if os.path.isfile(file):
            return True
        return False

    def generateDirPath(self, dirs):
        fileDirPath = "./"
        for d in dirs:
            fileDirPath += d + "/"
            if not self.isExistPath(fileDirPath):
                os.mkdir(fileDirPath)

        return fileDirPath

    def generateFile(self, fileDirPath, keyword, strTime, filetype):
        """
        keyword 이름과 현재시각을 파일명으로 하는 CSV 파일 생성
        :param fileDirPath:
        :param keyword:
        :param presentTime:
        :param filetype:
        :return:
        """
        fileName = keyword + "_" + strTime + "." + filetype

        if self.isExistFile(fileDirPath + fileName):
            print(fileDirPath + fileName + " File Exsist!")
        else:
            f = open(fileDirPath + fileName, 'w', encoding='utf-8', newline='')
            f.close()
        return fileName


    def saveListToCsv(self, dataList, fileDirPath, fileName):
        """
        data_list 내용을 만들어둔 파일에 저장
        :param data_list: data list
        :return:
        """
        if not self.isExistFile(fileDirPath + fileName):
            print(fileDirPath + fileName + " File does not exist!")
        elif not fileName.endswith('.csv'):
            print("File is not .csv")
        else:
            f = open(fileDirPath + fileName, 'a', encoding='utf-8', newline='')
            wr = csv.writer(f)
            for row in dataList:
                wr.writerow(row)
            f.close()