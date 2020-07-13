def Plagiarism_Percentage( input,output):
    print(input/output *100)
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

# main function
A=input("Enter file name. ")
B=input("Enter second file name. ")
F1=txtfile_to_string(A)
F2=txtfile_to_string(B)
r=LCS_length(F1,F2)
print("The longest common sucequence is: ")
A=Print_LCS(r,F1,len(F1),len(F2))
#print(A)
for i in A:
    print(i)
Plagiarism_Percentage(len(i),len(F1))
Plagiarism_Percentage(len(i),len(F2))
