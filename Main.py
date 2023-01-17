
import os
import datetime
import shutil
import subprocess

dt_now = datetime.datetime.now()

class Tool():
   def __init__(self):
      pass
   
   # フォルダ作成
   def Folda_Ch(self,path):
      if not os.path.exists(path):
         os.mkdir(path)
   
   def Docker_Process(self):
      os.chdir("C:\\Project_Root")
      subprocess.run("docker-compose up -d", shell=True)

class Environment_php():
    def __init__(self,tool):
        self.tool = tool
        self.Doc_Path = "C:\\"

    def Folda_Create(self):
       #  プロジェクトフォルダパス
       Project_Folda = self.Doc_Path + "\\Project_Root"
       #  プロジェクトフォルダの作成
       self.tool.Folda_Ch(Project_Folda)
       
       #  設定フォルダのパス
       Config_Path = Project_Folda + "\\config"   
       #  プロジェクトフォルダの作成
       self.tool.Folda_Ch(Config_Path)
       
       #  mysqlフォルダパス
       Mysql_patn = Config_Path + "\\mysql"   
       #  mysqlフォルダパスの作成
       self.tool.Folda_Ch(Mysql_patn)
       #  mysql設定フォルダ作成
       self.tool.Folda_Ch(Mysql_patn + "\\my.cnf")
       
       #  PHPフォルダパスの作成
       self.tool.Folda_Ch(Config_Path + "\\php")
       
       #  ドキュメントルートパス
       self.tool.Folda_Ch(Project_Folda + "\\html")
       
       return Project_Folda
     
    def Contena_File_Create(self,Dir_Path):
        # Docker設定ファイルをコピー   
        shutil.copyfile("./Template/docker-compose.yaml", Dir_Path + "\\docker-compose.yaml")
        # DockerApatche設定ファイルのコピー
        shutil.copyfile("./Template/Dockerfile", Dir_Path + "\\Dockerfile")
        # mysql設定ファイルのコピー
        shutil.copyfile("./Template/my.conf", Dir_Path + "\\config\\mysql\\my.cnf\\my.conf")
        # php設定ファイルのコピー
        shutil.copyfile("./Template/php.ini", Dir_Path + "\\config\\php\\php.ini")
        
        # テストファイルのコピー(Apatche確認用)
        shutil.copyfile("./Template/index.php", Dir_Path + "\\html\\index.php")
        # テストファイルのコピー(mysql確認用)
        shutil.copyfile("./Template/connect.php", Dir_Path + "\\html\\connect.php")
       
       
       
if __name__ == "__main__": 
   tool = Tool()
   en = Environment_php(tool)
   
   # Dir_Path= en.Qusion()
   Project_Folda = en.Folda_Create()
   en.Contena_File_Create(Project_Folda)
   
   tool.Docker_Process()