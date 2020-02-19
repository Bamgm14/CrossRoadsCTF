from django.shortcuts import render
info=[{'title':'Cryptography','url':'/help/bi0s_wiki/crypto/intro/','desc':'''Cryptography or Cryptology is the practice and study of techniques 
for secure communication in the presence of third parties called 
adversaries.'''},
      {'title':'Forensics','url':'/help/bi0s_wiki/forensics/intro/','desc':'''Forensics. In a CTF context, "Forensics" challenges can include file 
format analysis, steganography, memory dump analysis, or network packet 
capture analysis.'''},
      {'title':'Web Exploitation','url':'/help/bi0s_wiki/web/intro/','desc':'''Web Exploitation.This module follows up on the previous auditing web 
applications module. In this module we will focus on exploiting those 
vulnerabilities.'''},
      {'title':'Reverse Engineering','url':'/help/bi0s_wiki/reversing/intro/','desc':'''Reverse engineering, also called back engineering, is the process by 
which a man-made object is deconstructed to reveal its designs, 
architecture, or to extract knowledge from the object; similar to 
scientific research, the only difference being that scientific research 
is about a natural phenomenon.'''},
      {'title':'Binary Exploitation','url':'/help/bi0s_wiki/pwning/intro','desc':'''Binary exploitation is the process of subverting a compiled 
application such that it violates some trust boundary in a way that is 
advantageous to you.'''},
      {'title':'Uncategorized Challenges','url':'/help/bi0s_wiki/','desc':'Hacking Qustion,Trivia,Hacking Knowledge,etc.'},
      ]
def index(request):
    context={
        'info':info
        }
    return render(request,'MainPage/index.html',context)
def pg1(request):
    return render(request,'bi0s_wiki.html')
def pg2(request):
    return render(request,'Introduction(Python) - bi0s wiki.html')
def pg3(request):
    return render(request,'Getting Started - bi0s wiki.html')
def pg4(request):
    return render(request,'Basics - bi0s wiki.html')
def pg5(request):
    return render(request,'Functions - bi0s wiki.html')
def pg6(request):
    return render(request,'Introduction(Reverse) - bi0s wiki.html')
def pg7(request):
    return render(request,'C Language - bi0s wiki.html')
def pg8(request):
    return render(request,'x86 assembly programming - bi0s wiki.html')
def pg9(request):
    return render(request,'GDB - bi0s wiki.html')
def pg10(request):
    return render(request,'radare - bi0s wiki.html')
def pg11(request):
    return render(request,'Process Explorer - bi0s wiki.html')
def pg12(request):
    return render(request,'Windows - bi0s wiki.html')
def pg13(request):
    return render(request,'Reverse engineering - bi0s wiki.html')
def pg14(request):
    return render(request,'Introduction(Binary) - bi0s wiki.html')
def pg15(request):
    return render(request,'Getting Started(Pwning) - bi0s wiki.html')
def pg16(request):
    return render(request,'Introduction to Stack - bi0s wiki.html')
def pg17(request):
    return render(request,'Smash the Stack - bi0s wiki.html')
def pg18(request):
    return render(request,'ret2libc - bi0s wiki.html')
def pg19(request):
    return render(request,'ret2shellcode - bi0s wiki.html')
def pg20(request):
    return render(request,'Introduction(FSV) - bi0s wiki.html')
def pg21(request):
    return render(request,'Leaking Memory - bi0s wiki.html')
def pg22(request):
    return render(request,'Integer Overflow - bi0s wiki.html')
def pg23(request):
    return render(request,'Introduction(Forensics) - bi0s wiki.html')
def pg24(request):
    return render(request,'Introduction(IF) - bi0s wiki.html')
def pg25(request):
    return render(request,'Introduction(Steg) - bi0s wiki.html')
def pg26(request):
    return render(request,'Basic Tools - bi0s wiki.html')
def pg27(request):
    return render(request,'Basic Tools Contd. - bi0s wiki.html')
def pg28(request):
    return render(request,'LSB Encoding - bi0s wiki.html')
def pg29(request):
    return render(request,'Introduction(NF) - bi0s wiki.html')
def pg30(request):
    return render(request,'Network protocols and the OSI model - bi0s wiki.html')
def pg31(request):
    return render(request,'Basic Wireshark Usage - bi0s wiki.html')
def pg32(request):
    return render(request,'Introduction(MF) - bi0s wiki.html')
def pg33(request):
    return render(request,'Volatility - bi0s wiki.html')
def pg34(request):
    return render(request,'Introduction(Crypto) - bi0s wiki.html')
def pg35(request):
    return render(request,'What is Encryption - bi0s wiki.html')
def pg36(request):
    return render(request,'Bruteforce - bi0s wiki.html')
def pg37(request):
    return render(request,'Encoding - bi0s wiki.html')
def pg38(request):
    return render(request,'Classification Of Cryptosystems - bi0s wiki.html')
def pg39(request):
    return render(request,'Evolution - bi0s wiki.html')
def pg40(request):
    return render(request,'Hashing - bi0s wiki.html')
def pg41(request):
    return render(request,'Introduction(SC) - bi0s wiki.html')
def pg42(request):
    return render(request,'Substitution Cipher - bi0s wiki.html')
def pg43(request):
    return render(request,'Transposition Cipher - bi0s wiki.html')
def pg44(request):
    return render(request,'XOR Encryption - bi0s wiki.html')
def pg45(request):
    return render(request,'RSA - bi0s wiki.html')
def pg46(request):
    return render(request,'Introduction(Web) - bi0s wiki.html')
def pg47(request):
    return render(request,'Cookies - bi0s wiki.html')
def pg48(request):
    return render(request,'File upload vulnerability - bi0s wiki.html')
def pg49(request):
    return render(request,'Local File Inclusion - bi0s wiki.html')
def pg50(request):
    return render(request,'SQL Injection - bi0s wiki.html')
def pg51(request):
    return render(request,'OS Command Injection - bi0s wiki.html')
def pg52(request):
    return render(request,'XSS - bi0s wiki.html')
def pg53(request):
    return render(request,'SOP - bi0s wiki.html')
def pg54(request):
    return render(request,'Refer - bi0s wiki.html')
# Create your views here.
