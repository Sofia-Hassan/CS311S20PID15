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

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():  
    if request.method ==  "POST":
        A= request.form["text1"]
        B= request.form["text2"]
        #file1= request.files["name"]
        #file2=request.files["name"]
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
        return render_template("home.html")
    return render_template("home.html")

@app.route("/page1/<x>/<p1>/<p2>/<a>/<b>")
def page1(x,p1,p2,a,b):
    return render_template("page1.html",txt1=a,txt2=b,sub=x,p1=p1,p2=p2)


if __name__ ==  "__main__":
    app.run() 
