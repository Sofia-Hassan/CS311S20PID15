#integrated code
import os 
def Plagiarism_Percentage(input,output):
    return( input/output *100)
def Print_LCS(B, X, i, j):
    A = set()
    if i ==0 or j==0:
        A.add("")
        return A
    if B[i][j]=='/':
        tmp=Print_LCS(B,X,i-1,j-1)
        for s in tmp: 
            A.add(s + X[i - 1])
    elif B[i][j] == '|':
        A=Print_LCS(B, X, i - 1, j)
    else:
        A=Print_LCS(B, X, i, j - 1)
    return A
def LCS_length(X ,Y):
    m,n=len(X),len(Y)
    B=[["" for i in range(n+1)] for j in range(m+1)]
    C=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
         for j in range(1,n+1):
             if X[i-1]==Y[j-1]:
                 C[i][j]=C[i-1][j-1] +1
                 B[i][j]='/'
             elif C[i-1][j]>=C[i][j-1]:
                 C[i][j] = C[i-1][j]
                 B[i][j] = '|'
             else:
                 C[i][j]=C[i][j-1]
                 B[i][j]='-'    
    return B
    
def remove_spaces(A):
    A=A.replace(" ","")
    return A

def remove_sestivity(A):
    A=A.lower()
    B=remove_spaces(A)
    return B
def txtfile_to_string(A):
    f = open(A)
    string = f.read().replace("\n"," ")
    C=remove_sestivity(string)
    return C



from flask import Flask,render_template,request,redirect,url_for,session
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/Usama Hassan/Desktop/dsa lab codes/Project aoa/Project aoa/flask'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__,static_folder='files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST","GET"])
def home():  
    if request.method ==  "POST":
        A= request.form["text1"]
        B= request.form["text2"]
        if A!="" and B!="":
            txt1=remove_sestivity(A)
            txt2=remove_sestivity(B)
            r=LCS_length(txt1,txt2)
            A=Print_LCS(r,txt1,len(txt1),len(txt2))
            for i in A:
                x=i
            p1=Plagiarism_Percentage(len(i),len(txt1))
            p2=Plagiarism_Percentage(len(i),len(txt2))
            return redirect(url_for("page1",p1=p1,p2=p2,x=x,a=A,b=B))
        else:
            file1 = request.files['myfile1']
            file2 = request.files['myfile2']
            if 'myfile1' and 'myfile2' not in request.files:
                return "file not found"
            
            # if user does not select file, browser also
            # submit an empty part without filename
            if file1.filename == "" and file2.filename == "":
                return "file is empty"
            if file1 and file2 and allowed_file(file1.filename) and allowed_file(file2.filename):
                filename1 = secure_filename(file1.filename)
                filename2 = secure_filename(file2.filename)
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
                C=txtfile_to_string(filename1)
                D=txtfile_to_string(filename2)
                r=LCS_length(C,D)
                A=Print_LCS(r,C,len(C),len(D))
                for i in A:
                    y=i
                p3=Plagiarism_Percentage(len(i),len(C))
                p4=Plagiarism_Percentage(len(i),len(D))
                return redirect(url_for("page2",p3=p3,p4=p4,y=y,c=C,d=D)) 
    else:
        return render_template("home.html")
    return render_template("home.html")

@app.route("/page1/<x>/<p1>/<p2>/<a>/<b>")
def page1(x,p1,p2,a,b):
    return render_template("page1.html",txt1=a,txt2=b,sub=x,p1=p1,p2=p2)

@app.route("/page2/<y>/<p3>/<p4>/<c>/<d>")
def page2(y,p3,p4,c,d):
    return render_template("page2.html",sub=y,p1=p3,p2=p4,c=c,d=d)

if __name__ ==  "__main__":
    app.run() 
