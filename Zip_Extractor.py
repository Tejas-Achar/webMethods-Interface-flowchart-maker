from zipfile import ZipFile
import xml.etree.ElementTree as ElementTree
from enchant.checker import SpellChecker
import networkx as nx
from json2html import *

x =0
y= 1
chkr = SpellChecker("en_US")
extractedFiles = []
servcomments=[]
result = []
serresult = []
zipped_file = sys.argv[1]
pipresult = []
outputFileName = zipped_file + "_comment.html"
g = nx.DiGraph()
nodelist =[]



"""
For unzipping folder and extracts only xml file and stores in "extractedFiles"
"""
with ZipFile(zipped_file, 'r') as zipObj:
    listOfFileNames = zipObj.namelist()
    for fileName in listOfFileNames:
        if fileName.endswith('.xml'):
            extractedFiles.append(fileName)
            zipObj.extract(fileName)
        if fileName.endswith('.ndf'):
            servcomments.append(fileName)
            zipObj.extract(fileName)

"""
For getting required element from all the xml file from unzipped file
"""
with open(outputFileName, "a+") as f:
 f.write('<table bgcolor="#71AEA3" cellpadding="5" style = "margin-left: auto;margin-right: auto; width:100%"><tr><td><b>')
 f.write("SERVICE COMMENTS")
 f.write("</b>\n</td></tr></table>")

for servic in servcomments:
    serresult.append("\n")
    serresult.append(servic)
    rt = ElementTree.parse(servic).getroot()
    xmlcom = ElementTree.tostring(rt, encoding='unicode')
    sing = xmlcom.split('</value>')
    for indx, x in enumerate(sing):
        if '<value name="node_comment">' in x:
            print(x)
            m = x.replace('<value name="node_comment">', "")
            n = m.replace("""    </record>
  </record>""", "")
            q = n.replace("*","")
            with open(outputFileName, "a+") as f:
                f.write('<table border ="1" cellpadding="5"><tr><td>')
            with open(outputFileName, "a+") as f:
                f.write(q)
            with open(outputFileName, "a+") as f:
                f.write("</td></tr></table>")
with open(outputFileName, "a+") as f:
 f.write('<table bgcolor="#71AEA3" cellpadding="5" style = "margin-left: auto;margin-right: auto; width:100%"><tr><td><b>')
 f.write("CODE FLOW WITH COMMENTS")
 f.write("</b>\n</td></tr></table>")


def main():
    for file_path in extractedFiles:
        result.append("\n")
        result.append(file_path)
        root = ElementTree.parse(file_path).getroot()
        xmlstr = ElementTree.tostring(root, encoding='unicode')
        single = xmlstr.split('\n')
        with open(outputFileName, "a+") as f:

          f.write('<table bgcolor="#F6FBBA" style = "margin-left: auto;margin-right: auto; width:100%"><tr><td><p style="text-align:center">')
          f.write(result[-1])
          f.write("\n</p></td></tr></table>")
          f.write('<table cellpadding="5" style = "margin-left: auto;margin-right: auto;"><tr><td><font size="18">     </font></td></tr></table>')

        for index, s in enumerate(single):
            if '<COMMENT>' in s:

                r = s.replace("<COMMENT>", "")
                t = r.replace("</COMMENT>", "")
                stepname = single[index - 1]
                stepname1 = stepname.replace("<","")
                stepname2 = stepname1.replace("/>","")
                nodelist.append(t)
                print("Step Name : ", single[index - 1], "\n", "Comment : ", t)
                k = ['<font color="white">', "Step Name : ", stepname2,"</font>"]
                j = ["Comment : ",t]
                str1 = ''.join(k)  # converting k to a string
                str7 = ''.join(j)
                with open(outputFileName, "a+") as f:
                    f.write('<table cellpadding="9" bgcolor="#0D9A96" style = "margin-left: auto;border-radius: 4px;margin-right: auto;"><tr><td>\n')
                with open(outputFileName, "a+") as f:
                    f.write(str1)
                with open(outputFileName, "a+") as f:
                    f.write('<table cellpadding="5" bgcolor="#C7F9F8" style = "margin-left: auto;border-radius: 4px;margin-right: auto;"><tr><td>\n')
                    f.write(str7)
                    f.write("\n</td></tr></table>")
                for word in t.split(" "):
                    chkr.set_text(word)
                    for err in chkr:
                        print("Spell check  :  ", err.word)
                        x = ["\n", "Spell Check : ", err.word]
                        str2 = ''.join(x)
                        str3 = ['<p><font color="#F6FBBA"><b>',str2,'</b></font></p>']
                        str4 = ''.join(str3)
                        with open(outputFileName, "a+") as f:
                            f.write('<table cellpadding="5"style = "margin-left: auto;margin-right: auto;"><tr><td>\n')
                            f.write(str4)
                            f.write("\n</td></tr></table>")
                print(
                    "----------------------------------------------------------------------------------------------------------------------------------------------")

                with open(outputFileName,"a+") as f:
                    f.write("\n</td></tr></table>")
                with open (outputFileName,"a+") as f:
                    f.write('<table cellpadding="5" style = "margin-left: auto;margin-right: auto;"><tr><td><font size="10">&#8595;</font></td></tr></table>')

        """with open(outputFileName, "a+") as f:
         f.write("Disabled Flow steps")"""#Disabled flow steps.
        for indexs, ss in enumerate(single):
            if 'DISABLED' in ss:

                """print("Step Name : ", single[index - 1], "\n", "Comment : ", t)
                k = ["\n", "Step Name : ", single[index - 1], "\n", "Comment : ", t]
                str1 = ''.join(k)  # converting k to a string"""
                with open(outputFileName, "a+") as f:
                    f.write("\n")
                    f.write(ss)
                    f.write("\n")
                    rr = single[indexs + 1].replace("<COMMENT>", "")
                    tt = rr.replace("</COMMENT>", "")
                    zs = ["Description : ", tt]
                    str7 = ''.join(zs)
                    f.write("\n")
                    f.write(str7)
                    f.write("\n")






main()

"""
For displaying result
"""
for result_list in result:
    print(result_list)

with open(outputFileName, "a+") as f:
 f.write('<table cellpadding="5" bgcolor="#71AEA3" style = "margin-left: auto;margin-right: auto; width:100%"><tr><td>')
 f.write('<p style="text-align:center">*************************************************************END OF PACKAGE********************************************************</p>')
 f.write("\n</td></tr></table>")