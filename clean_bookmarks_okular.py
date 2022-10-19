from tempfile import mkstemp
from shutil import move
from os import remove
import shutil
import datetime

today = datetime.datetime.now()
time = str(today)[10:19]
dataHora = str(today)[0:10]
#print("Today's date:", dataHora)

def corrigir_bookmarks(source_file_path):
    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        with open(source_file_path, 'r') as source_file:            
            for idx,line in enumerate(source_file):                    

                 # achar a posição da tag <title> 

                title = '<title>'
                posicao_title = line.rfind(title);
                  
                #considera apenas as linhas com a tag <title>
                   
                if posicao_title != -1:
                    
                    # imprime o número da linha

                    print("Linha: "+ str(idx+1))      

                    # imprime a posição da tag <title> dessa linha

                    print("Posição final tag <title>: " + str(posicao_title+7)) 

                    # achar a posição da última barra desconsiderando a tag </title>

                    line_corrigida = line.replace("</t","")                 
                    
                    barra = '/'
                    posicao_barra = line_corrigida.rfind(barra);
                    print("Posição tag /: " + str(posicao_barra+1)) 
                    print(line.replace(line[posicao_title+7:posicao_barra+1],"",1))
                    target_file.write(line.replace(line[posicao_title+7:posicao_barra+1],"",1))
                else:
                    target_file.write(line)    

    remove(source_file_path)
    move(target_file_path, source_file_path)

    #remove(source_file_path)
    #move(target_file_path, source_file_path)

#pasta de origem 

src="/home/${USER}/.local/share/okular/bookmarks.xml"

#pasta de destino do backup antes de alterar

dst1="/home/${USER}/.local/share/okular/bookmarks_bkp_before_"+dataHora+time+".xml" 

# pasta de destino do backup após alterações

dst2="/home/${USER}/.local/share/okular/bookmarks_after_"+dataHora+time+".xml" 

# faz backup antes de alterar

shutil.copyfile(src, dst1) 

corrigir_bookmarks(src)

# faz backup após de alterar

shutil.copyfile(src, dst2) 