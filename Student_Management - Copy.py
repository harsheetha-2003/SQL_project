from tkinter import*
from tkinter import ttk #stylish entry fields
from PIL import Image,ImageTk #pip install pillow
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x791+0+0") #windo size
        self.root.title("RUAS STUDENT MANAGEMENT SYSTEM")
       
        #variables
        self.var_SID=StringVar()   #DF1 
        self.var_Sname=StringVar()  
        self.var_Sphno=StringVar()  
        self.var_Seid=StringVar()
        self.var_Sbid=StringVar()
        self.var_Sadd=StringVar()
        self.var_sbname=StringVar() #DF2
        self.var_course=StringVar()
        self.var_pid=StringVar()  #df 3
        self.var_amt=IntVar()
        self.var_pdate=StringVar()
        self.var_cid=StringVar()  #Df4
        self.var_sem=StringVar()
        self.var_sgpa=StringVar()
        self.var_mmx=IntVar()
        self.var_SDOB=StringVar()
        self.Modify=StringVar()
    
        title_text = "        RUAS STUDENT MANAGEMENT SYSTEM               "
        lbltitle=Label(self.root,bd=5,relief=RIDGE,text=title_text,fg="dodger blue",bg="lavender",font=("times new roman",28,"bold"))
        # lbltitle.grid(row=0,column=1, sticky="nw", padx=0, pady=10)
        lbltitle.pack(side=TOP,fill=X)
    
        # self.btn_2 = Button(self.root, image=self.photoimg2, cursor="hand2")
        # # self.btn_1.place(x=0,y=0,width=20)
        # self.btn_2.grid(row=0, column=3, sticky="w", padx=10, pady=10)
       # ========bg img===========
        img3=Image.open(r"C:\Users\slv20\OneDrive\Desktop\DBMS-ER DIAGRAMS\student management system\university.png")
        img3=img3.resize((1520,720),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_lbl=Label(self.root,image=self.photoimg3,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=48,width=1535,height=755)
        # =========================================DATA FRAME============================
    
        #mange frame
    
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="lightpink")
        Manage_frame.place(x=20,y=17,width=1242,height=630)
        
    # =====================frame1====================================
        #LEFT FRAME
        Dataleftframe_1=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=20,
                                                  text="STUDENT DETAILS",fg="orange",bg="white",font=("times new roman",12,"bold"))
        Dataleftframe_1.place(x=0,y=0,width=255,height=320)

        # labels of student info

        lbl_ID=Label(Dataleftframe_1,text="Student_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_ID.grid(row=0,column=0,sticky=W)

        search_frame_ID=ttk.Entry(Dataleftframe_1,textvariable=self.var_SID,width=22,font=("arial","11","bold"))
        search_frame_ID.grid(row=2,column=0,padx=5)

           # lbl 2
        
        lbl_name=Label(Dataleftframe_1,text="Student_Name:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_name.grid(row=3,column=0,sticky=W)

        search_frame_name=ttk.Entry(Dataleftframe_1,textvariable=self.var_Sname,width=22,font=("arial","11","bold"))
        search_frame_name.grid(row=4,column=0,padx=5)
        
        #label 3

        lbl_Conct=Label(Dataleftframe_1,text="Student_PHNO:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_Conct.grid(row=5,column=0,sticky=W)

        search_frame_Conct=ttk.Entry(Dataleftframe_1,textvariable=self.var_Sphno,width=22,font=("arial","11","bold"))
        search_frame_Conct.grid(row=6,column=0,padx=5)

     # lbl 4
        
        lbl_eid=Label(Dataleftframe_1,text="Email_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_eid.grid(row=7,column=0,sticky=W)

        search_frame_eid=ttk.Entry(Dataleftframe_1,textvariable=self.var_Seid,width=22,font=("arial","11","bold"))
        search_frame_eid.grid(row=8,column=0,padx=5)
        
     # lbl 5
        lbl_bid=Label(Dataleftframe_1,text="DOB:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_bid.grid(row=10,column=0,sticky=W)

        search_frame_bid=ttk.Entry(Dataleftframe_1,textvariable=self.var_SDOB,font=("times new roman",11,"bold"),width=15)
        search_frame_bid.grid (padx=0.5,pady=1,row=11,column=0)

     #lbl 6
        lbl_add=Label(Dataleftframe_1,text="Address:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_add.grid(row=13,column=0,sticky=W)

        search_frame_ads=ttk.Entry(Dataleftframe_1,textvariable=self.var_Sadd,width=22,font=("arial","11","bold"))
        search_frame_ads.grid(row=14,column=0,padx=5)

    # ======================frame2===============================================
     
        #RIGHT FRAME
        Dataleftframe_2=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="BRANCH DETAILS",fg="orange",bg="white",font=("times new roman",12,"bold"))
        Dataleftframe_2.place(x=255,y=0,width=270,height=270)

        lbl_BID=Label(Dataleftframe_2,text="Branch_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_BID.grid(row=0,column=0,sticky=W)

        search_frame_BID=ttk.Entry(Dataleftframe_2,textvariable=self.var_Sbid,font=("times new roman",11,"bold"),width=15)
        search_frame_BID.grid (padx=0.2,pady=1,row=1,column=1)

           # lbl 2
        
        lbl_Bname=Label(Dataleftframe_2,text="Branch_Name:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_Bname.grid(row=3,column=0,sticky=W)

        combo_Bname=ttk.Entry(Dataleftframe_2,textvariable=self.var_sbname,font=("times new roman",11,"bold"),width=15)
        combo_Bname.grid (padx=0.5,pady=1,row=4,column=1)
        
        lbl_ID=Label(Dataleftframe_2,text="Student_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_ID.grid(row=5,column=0,sticky=W)

        search_frame_ID=ttk.Entry(Dataleftframe_2,textvariable=self.var_SID,width=22,font=("arial","11","bold"))
        search_frame_ID.grid(row=7,column=1,padx=0.5)
    # ==========================frame3========================================================       

        # current course label frame  information
        Dataleftframe_3 =LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="FEE DETAILS",fg="orange",bg="white",font=("times new roman",12,"bold"))
        Dataleftframe_3.place(x=510,y=0,width=261,height=270)
        #lbl 1
        lbl_PID=Label(Dataleftframe_3,text="Payment_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_PID.grid(row=0,column=0,sticky=W)

        search_frame_pid=ttk.Entry(Dataleftframe_3,textvariable=self.var_pid,width=22,font=("arial","11","bold"))
        search_frame_pid.grid(row=1,column=0,padx=5)

       # lbl 2
        
        lbl_SID=Label(Dataleftframe_3,text="Student_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_SID.grid(row=3,column=0,sticky=W)

        search_frame_ID=ttk.Entry(Dataleftframe_3,textvariable=self.var_SID,width=22,font=("arial","11","bold"))
        search_frame_ID.grid(row=4,column=0,padx=5)
        

        #label 3

        lbl_AMT=Label(Dataleftframe_3,text="Amount:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_AMT.grid(row=5,column=0,sticky=W)


        search_frame_amt=ttk.Entry(Dataleftframe_3,textvariable=self.var_amt,width=22,font=("arial","11","bold"))
        search_frame_amt.grid(row=6,column=0,padx=5)

        # lbl 4
        
        lbl_Pdate=Label(Dataleftframe_3,text="Payment_Date:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_Pdate.grid(row=7,column=0,sticky=W)

        search_frame_eid=ttk.Entry(Dataleftframe_3,textvariable=self.var_pdate,width=22,font=("arial","11","bold"))
        search_frame_eid.grid(row=8,column=0,padx=5)
    # ====================frame4================================================

        Dataleftframe_4 =LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="EXAM DETAILS",fg="orange",bg="white",font=("times new roman",12,"bold"))
        Dataleftframe_4.place(x=762,y=0,width=253,height=270)

        #lbl 1
   
        lbl_ID=Label(Dataleftframe_4,text="Student_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_ID.grid(row=0,column=0,sticky=W)

        combo_ID=ttk.Entry(Dataleftframe_4,textvariable=self.var_SID,font=("times new roman",11,"bold"),width=15)
        combo_ID.grid (padx=0.5,pady=1,row=1,column=0)

           # lbl 2
        
        lbl_sem=Label(Dataleftframe_4,text="Semister",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_sem.grid(row=3,column=0,sticky=W)

        combo_sem=ttk.Entry(Dataleftframe_4,textvariable=self.var_sem,font=("times new roman",11,"bold"),width=15)
        combo_sem.grid (padx=0.5,pady=1,row=4,column=0)
        

        #label 3

        lbl_sgpa=Label(Dataleftframe_4,text="SGPA:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_sgpa.grid(row=5,column=0,sticky=W)

        search_frame_sgpa=ttk.Entry(Dataleftframe_4,textvariable=self.var_sgpa,width=22,font=("arial","11","bold"))
        search_frame_sgpa.grid(row=6,column=0,padx=5)

    

     # lbl 4
        
        lbl_mmarks=Label(Dataleftframe_4,text="Max_Marks:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_mmarks.grid(row=7,column=0,sticky=W)

        search_frame_marks=ttk.Entry(Dataleftframe_4,textvariable=self.var_mmx,width=22,font=("arial","11","bold"))
        search_frame_marks.grid(row=8,column=0,padx=5)
        
     # lbl 5
        lbl_cid=Label(Dataleftframe_4,text="Course_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_cid.grid(row=10,column=0,sticky=W)

        combo_cid=ttk.Entry(Dataleftframe_4,textvariable=self.var_cid,font=("times new roman",11,"bold"),width=15)
        combo_cid.grid (padx=0.5,pady=1,row=11,column=0)

      #  ========================Data frame 5=======================================
         
        Dataleftframe_5 =LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="COURSE",fg="orange",bg="white",font=("times new roman",12,"bold"))
        Dataleftframe_5.place(x=1015,y=0,width=250,height=270)

         #lbl 1
   
        lbl_CID=Label(Dataleftframe_5,text="Course_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_CID.grid(row=0,column=0,sticky=W)

        combo_CID=ttk.Entry(Dataleftframe_5,textvariable=self.var_cid,font=("times new roman",11,"bold"),width=15)
        combo_CID.grid (padx=0.5,pady=1,row=1,column=0)

           # lbl 2
        
        lbl_Cname=Label(Dataleftframe_5,text="Course Name",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_Cname.grid(row=3,column=0,sticky=W)

        combo_Cname=ttk.Entry(Dataleftframe_5,textvariable=self.var_course,font=("times new roman",11,"bold"),width=15)
        combo_Cname.grid (padx=0.5,pady=1,row=4,column=0)
        
        #label 3
        lbl_ID=Label(Dataleftframe_5,text="Student_ID:",fg="Black",bg="white",font=("times new roman",11,"bold"))
        lbl_ID.grid(row=6,column=0,sticky=W)

        search_frame_ID=ttk.Entry(Dataleftframe_5,textvariable=self.var_SID,width=22,font=("arial","11","bold"))
        search_frame_ID.grid(row=7,column=0,padx=0.5)
    
      # =============================== button operation ==========================
      
      #  buttons

        Main_frame_1=Frame(bg_lbl,bd=2,relief=RIDGE,bg="lightpink")
        Main_frame_1.place(x=274,y=292,width=987,height=40)
        
        btn_Add=Button(Main_frame_1,text="SAVE",command=self.add_data,font=("times new roman",12,"bold"),width=26,bg="indigo",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)
      
        btn_update=Button(Main_frame_1,command=self.update_data,text="UPDATE",font=("times new roman",12,"bold"),width=26,bg="indigo",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_del=Button(Main_frame_1,text="DELETE",font=("times new roman",12,"bold"),width=26,bg="indigo",fg="white")
        btn_del.grid(row=0,column=2,padx=1)

        btn_reset=Button(Main_frame_1,text="RESET",font=("times new roman",12,"bold"),width=26,bg="indigo",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)

        Dataleftframe_6 =LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Information display",fg="orange",bg="white",font=("times new roman",10,"bold"))
        Dataleftframe_6.place(x=251,y=305,width=987,height=70)
         
        search_by=Label(Dataleftframe_6,font=("times new roman",12,"bold"),text="select column to modify:",fg="orange",bg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        combo_sby=ttk.Combobox(Dataleftframe_6,textvariable=self.Modify,font=("times new roman",11,"bold"),width=24)
        combo_sby["value"]=("Student","Course","Branch","Fee","Exam")
        combo_sby.grid (padx=0.5,pady=1,row=0,column=1)

        # lblModify=Label(Dataleftframe_6,text="Select column to modify",font=("times new roman",12,"bold"),padx=2,pady=6)
        # lblModify.grid(row=0,column=0)
        # comModify=ttk.Combobox(Data,textvariable=self.Modify,font=("times new roman",12,"bold"),width=15)
        # comModify["values"]=("Student","Course","Branch","Fee","Exam")
        # comModify.grid(row=1,column=0)
        
        search_frame=ttk.Entry(Dataleftframe_6,width=24,font=("arial","11","bold"))
        search_frame.grid(row=0,column=2,padx=5)

        btn_Add=Button(Dataleftframe_6,text="Search",font=("times new roman",12,"bold"),width=24,bg="indigo",fg="dodger blue")
        btn_Add.grid(row=0,column=3,padx=1)
      
        btn_update=Button(Dataleftframe_6,text="Show all",command=self.fetch_data(),font=("times new roman",12,"bold"),width=24,bg="indigo",fg="white")
        btn_update.grid(row=0,column=4,padx=1)
   
      # ===============================student table and scroll===============================
        Dataleftframe_7 =LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Information display",fg="orange",bg="white",font=("times new roman",12,"bold"))
        Dataleftframe_7.place(x=0,y=364,width=1238,height=255)

        scroll_x=ttk.Scrollbar(Dataleftframe_7,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataleftframe_7,orient=VERTICAL)

        self.STUDENT_DETAILS=ttk.Treeview(Dataleftframe_7,column=("S_ID","S_name","Coct","E_ID","DOB","ADD","B_ID","B_name","P_ID","Amt","PDT","sem","SGPA","MMX","C_ID","C_NAME"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        # self.BRANCH_DETAILS=ttk.Treeview(Dataleftframe_7,column=("B_ID","B_name","S_ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        # self.FEE_DETAILS=ttk.Treeview(Dataleftframe_7,column=("P_ID","S_ID","Amt","PDT"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        # self.EXAM_DETAILS=ttk.Treeview(Dataleftframe_7,column=("S_ID","sem","SGPA","MMX","C_ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        # self.COURSE_DETAILS=ttk.Treeview(Dataleftframe_7,column=("C_ID","C_NAME","B_ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

      #   scroll_x.configure(command=self.STUDENT_DETAILS.xview)
      #   scroll_y.configure(command=self.STUDENT_DETAILS.yview)

        # scroll_x_1st = ttk.Scrollbar(Dataleftframe_7, orient=HORIZONTAL)
        # scroll_y_1st = ttk.Scrollbar(Dataleftframe_7, orient=VERTICAL)
        # self.STUDENT_DETAILS.configure(xscrollcommand=scroll_x_1st.set, yscrollcommand=scroll_y_1st.set)
        scroll_x.config(command=self.STUDENT_DETAILS.xview)
        scroll_y.config(command=self.STUDENT_DETAILS.yview)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
      #   scroll_x_1st.pack(side=BOTTOM,fill=X)
      #   scroll_x_1st.pack(side=RIGHT,fill=Y)
        self.STUDENT_DETAILS.pack(side=LEFT, fill=BOTH, expand=1)



    #     scroll_x_2st = ttk.Scrollbar(Dataleftframe_7, orient=HORIZONTAL)
    #     scroll_y_2st = ttk.Scrollbar(Dataleftframe_7, orient=VERTICAL)
    #     self.BRANCH_DETAILS.configure(xscrollcommand=scroll_x_2st.set, yscrollcommand=scroll_y_2st.set)
    #     scroll_x_2st.config(command=self.BRANCH_DETAILS.xview)
    #     scroll_y_2st.config(command=self.BRANCH_DETAILS.yview)
    #     scroll_x_2st.pack(side=BOTTOM, fill=X)
    #     scroll_y_2st.pack(side=RIGHT, fill=Y)
    
    #     self.BRANCH_DETAILS.pack(side=LEFT, fill=BOTH, expand=1)

    #     scroll_x_3st = ttk.Scrollbar(Dataleftframe_7, orient=HORIZONTAL)
    #     scroll_y_3st = ttk.Scrollbar(Dataleftframe_7, orient=VERTICAL)
    #     self.FEE_DETAILS.configure(xscrollcommand=scroll_x_3st.set, yscrollcommand=scroll_y_3st.set)
    #     scroll_x_3st.config(command=self.FEE_DETAILS.xview)
    #     scroll_y_3st.config(command=self.FEE_DETAILS.yview)
    #     scroll_x_3st.pack(side=BOTTOM, fill=X)
    #     scroll_y_3st.pack(side=RIGHT, fill=Y)
    #   #   scroll_x.pack(side=BOTTOM,fill=X)
    #   #   scroll_x.pack(side=RIGHT,fill=Y)

    #     self.FEE_DETAILS.pack(side=LEFT, fill=BOTH, expand=1)

    #     scroll_x_4st = ttk.Scrollbar(Dataleftframe_7, orient=HORIZONTAL)
    #     scroll_y_4st = ttk.Scrollbar(Dataleftframe_7, orient=VERTICAL)
    #     self.EXAM_DETAILS.configure(xscrollcommand=scroll_x_4st.set, yscrollcommand=scroll_y_4st.set)
    #     scroll_x_4st.config(command=self.EXAM_DETAILS.xview)
    #     scroll_y_4st.config(command=self.EXAM_DETAILS.yview)
    #     scroll_x_4st.pack(side=BOTTOM, fill=X)
    #     scroll_y_4st.pack(side=RIGHT, fill=Y)
    #   #   scroll_x.pack(side=BOTTOM,fill=X)
    #   #   scroll_x.pack(side=RIGHT,fill=Y)

    #     self.EXAM_DETAILS.pack(side=LEFT, fill=BOTH, expand=1)

    #     scroll_x_5st = ttk.Scrollbar(Dataleftframe_7, orient=HORIZONTAL)
    #     scroll_y_5st = ttk.Scrollbar(Dataleftframe_7, orient=VERTICAL)
    #     self.COURSE_DETAILS.configure(xscrollcommand=scroll_x_5st.set, yscrollcommand=scroll_y_5st.set)
    #     scroll_x_5st.config(command=self.COURSE_DETAILS.xview)
    #     scroll_y_5st.config(command=self.COURSE_DETAILS.yview)
      
    #     scroll_x.pack(side=BOTTOM,fill=X)
    #     scroll_x.pack(side=RIGHT,fill=Y)
    #     self.COURSE_DETAILS.pack(side=LEFT, fill=BOTH, expand=1)

     
      
        self.STUDENT_DETAILS.heading("S_ID", text="Student_ID")
        self.STUDENT_DETAILS.heading("S_name", text="Student_Name")
        self.STUDENT_DETAILS.heading("Coct", text="Student_PHNO")
        self.STUDENT_DETAILS.heading("E_ID", text="Email_ID")
        self.STUDENT_DETAILS.heading("DOB", text="DOB")
        self.STUDENT_DETAILS.heading("ADD", text="Address")
        self.STUDENT_DETAILS.heading("B_ID", text="Branch_ID")
        self.STUDENT_DETAILS.heading("B_name", text="Branch_Name")
        self.STUDENT_DETAILS.heading("P_ID", text="Payment_ID")
        self.STUDENT_DETAILS.heading("Amt", text="Amount")
        self.STUDENT_DETAILS.heading("PDT", text="Payment_Date")
        self.STUDENT_DETAILS.heading("sem", text="Sem")
        self.STUDENT_DETAILS.heading("SGPA", text="SGPA")
        self.STUDENT_DETAILS.heading("MMX", text="Max_marks")
        self.STUDENT_DETAILS.heading("C_ID", text="Course_ID")
        self.STUDENT_DETAILS.heading("C_NAME", text="course_name")

        self.STUDENT_DETAILS["show"] = "headings"

        self.STUDENT_DETAILS.column("S_ID", width=150)
        self.STUDENT_DETAILS.column("S_name", width=150)
        self.STUDENT_DETAILS.column("Coct", width=150)
        self.STUDENT_DETAILS.column("E_ID", width=150)
        self.STUDENT_DETAILS.column("DOB", width=150)
        self.STUDENT_DETAILS.column("ADD", width=150)
        self.STUDENT_DETAILS.column("B_ID", width=150)
        self.STUDENT_DETAILS.column("B_name", width=150)
        self.STUDENT_DETAILS.column("P_ID", width=150)
        self.STUDENT_DETAILS.column("Amt", width=150)
        self.STUDENT_DETAILS.column("PDT", width=150)
        self.STUDENT_DETAILS.column("sem", width=150)
        self.STUDENT_DETAILS.column("SGPA", width=150)
        self.STUDENT_DETAILS.column("MMX", width=150)
        self.STUDENT_DETAILS.column("C_ID", width=150)
        self.STUDENT_DETAILS.column("C_NAME", width=150)
        self.STUDENT_DETAILS.pack(fill=BOTH,expand=1)
        # self.STUDENT_DETAILS.bind("<ButtonRelease>",self.get_cursor_data)
        self.STUDENT_DETAILS.bind("<ButtonRelease>", self.get_cursor_data)
        # fetch fun
        # self.fetch_data()

    #   #  =====branch table===========================
    #     self.BRANCH_DETAILS.heading("B_ID",text="Branch_ID")
    #     self.BRANCH_DETAILS.heading("B_name",text="Branch_Name")
    #     self.BRANCH_DETAILS.heading("S_ID",text="Student_ID")
    #     # self.BRANCH_DETAILS.heading("course",text="Course")

    #     self.BRANCH_DETAILS["show"]="headings"
        
    #     self.BRANCH_DETAILS.column("B_ID",width=70)
    #     self.BRANCH_DETAILS.column("B_name",width=70)
    #     self.BRANCH_DETAILS.column("S_ID",width=70)
      
    #     self.BRANCH_DETAILS.pack(fill=BOTH,expand=1)
    #     self.BRANCH_DETAILS.bind("<ButtonRelease>", lambda event: self.update_entry_widgets())
        
    #     #fetch fun
    #     self.fetch_data_branch()

    #   # =============fee_details ================
    #     self.FEE_DETAILS.heading("P_ID",text="payment_ID")
    #     self.FEE_DETAILS.heading("S_ID",text="Student_ID")
    #     self.FEE_DETAILS.heading("Amt",text="Amount")
    #     self.FEE_DETAILS.heading("PDT",text="Payment_Date")

    #     self.FEE_DETAILS["show"]="headings"
        
    #     self.FEE_DETAILS.column("P_ID",width=70)
    #     self.FEE_DETAILS.column("S_ID",width=70)
    #     self.FEE_DETAILS.column("Amt",width=70)
    #     self.FEE_DETAILS.column("PDT",width=70)
    #     self.FEE_DETAILS.pack(fill=BOTH,expand=1)
    #     self.FEE_DETAILS.bind("<ButtonRelease>", lambda event: self.update_entry_widgets())
        
    #     #fetch fun 
    #     self.fetch_data_fee()
       
    #   #  ==============exam_details table===============
    #     self.EXAM_DETAILS.heading("S_ID",text="Student_ID")
    #     self.EXAM_DETAILS.heading("sem",text="Semester")
    #     self.EXAM_DETAILS.heading("SGPA",text="SGPA")
    #     self.EXAM_DETAILS.heading("MMX",text="Max_marks")
    #     self.EXAM_DETAILS.heading("C_ID",text="Course_Id")
        
    #     self.EXAM_DETAILS["show"]="headings"

    #     self.EXAM_DETAILS.column("S_ID",width=70)
    #     self.EXAM_DETAILS.column("sem",width=70)
    #     self.EXAM_DETAILS.column("SGPA",width=70)
    #     self.EXAM_DETAILS.column("MMX",width=70)
    #     self.EXAM_DETAILS.column("C_ID",width=70)

    #     self.EXAM_DETAILS.pack(fill=BOTH,expand=1)
    #     self.EXAM_DETAILS.bind("<ButtonRelease>", lambda event: self.update_entry_widgets())
        
    #     #fetch fun
    #     self.fetch_data_exam()
    #   # ======================COURSE_DETAILS table==============
    #     self.COURSE_DETAILS.heading("C_ID",text="Course_Id")
    #     self.COURSE_DETAILS.heading("C_NAME",text="course_name")
    #     self.COURSE_DETAILS.heading("B_ID",text="branch_id")
           
    #     self.COURSE_DETAILS["show"]="headings"

    #     self.COURSE_DETAILS.column("C_ID",width=70)
    #     self.COURSE_DETAILS.column("C_NAME",width=70)
    #     self.COURSE_DETAILS.column("B_ID",width=70)
    #     self.COURSE_DETAILS.pack(fill=BOTH,expand=1)

    #     self.COURSE_DETAILS.bind("<ButtonRelease>", lambda event: self.update_entry_widgets())
    #     # fetch fun
    #     self.fetch_data_course()
        
      # ==============================================================
       
    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
            my_cursor = conn.cursor()
            if (self.var_SID.get()!="" and self.var_Sname.get()!="" and self.var_Sphno.get()!="" and
                            self.var_Seid.get()!="" and self.var_SDOB.get()!="" and self.var_Sadd.get()!=""):
    
        # Insert into student_details
                my_cursor.execute("INSERT INTO student_management_system.STUDENT_DETAILS VALUES (%s, %s, %s, %s, %s, %s)",
                           (self.var_SID.get(), self.var_Sname.get(), self.var_Sphno.get(),
                            self.var_Seid.get(), self.var_SDOB.get(), self.var_Sadd.get()))
                
            if (self.var_Sbid.get()!="" and self.var_sbname.get()!="" and self.var_SID.get()!=""):

                my_cursor.execute("INSERT INTO student_management_system.Branch_details VALUES (%s, %s,%s)",
                           (self.var_Sbid.get(), self.var_sbname.get(),self.var_SID.get()))
                
            if(self.var_pid.get()!="" and self.var_SID.get()!="" and self.var_amt.get()!="" and self.var_pdate.get()!=""):
                my_cursor.execute("INSERT INTO student_management_system.fee_details VALUES (%s, %s, %s, %s)",
                           (self.var_pid.get(), self.var_SID.get(), self.var_amt.get(), self.var_pdate.get()))
                
            if(self.var_SID.get()!=" " and self.var_sem.get()!= "" and self.var_sgpa.get()!="" and
                self.var_mmx.get()!="" and self.var_cid.get()!=""):
                 
                 my_cursor.execute("INSERT INTO student_management_system.exam_details VALUES (%s, %s, %s, %s, %s)",
                           (self.var_SID.get(), self.var_sem.get(), self.var_sgpa.get(),
                            self.var_mmx.get(), self.var_cid.get()))
            
            if(self.var_cid.get()!="" and self.var_course.get()!="" and self.var_Sbid.get()!=""):
                my_cursor.execute("INSERT INTO student_management_system.COURSE_DETAILS VALUES (%s, %s, %s)",
                           (self.var_cid.get(), self.var_course.get(), self.var_Sbid.get()))
                
             
            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("Sucess","Details has been added",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
        # # Insert into student_details
        #     my_cursor.execute("INSERT INTO student_management_system.STUDENT_DETAILS VALUES (%s, %s, %s, %s, %s, %s)",
        #                    (self.var_SID.get(), self.var_Sname.get(), self.var_Sphno.get(),
        #                     self.var_Seid.get(), self.var_SDOB.get(), self.var_Sadd.get()))
        #     conn.commit()

        # # Insert into Branch_details
        #     my_cursor.execute("INSERT INTO student_management_system.Branch_details VALUES (%s, %s,%s)",
        #                    (self.var_Sbid.get(), self.var_sbname.get(),self.var_SID.get()))
        #     conn.commit()

        # # Insert into fee_details
        #     my_cursor.execute("INSERT INTO student_management_system.fee_details VALUES (%s, %s, %s, %s)",
        #                    (self.var_pid.get(), self.var_SID.get(), self.var_amt.get(), self.var_pdate.get()))
        #     conn.commit()

        # # Insert into exam_details
        #     my_cursor.execute("INSERT INTO student_management_system.exam_details VALUES (%s, %s, %s, %s, %s)",
        #                    (self.var_SID.get(), self.var_sem.get(), self.var_sgpa.get(),
        #                     self.var_mmx.get(), self.var_cid.get()))
        #     conn.commit()

        # # Insert into COURSE_DETAILS
        #     my_cursor.execute("INSERT INTO student_management_system.COURSE_DETAILS VALUES (%s, %s, %s)",
        #                    (self.var_cid.get(), self.var_course.get(), self.var_Sbid.get()))
        #     conn.commit()

        #     conn.close()
        #     self.fetch_data_student()
        #     self.fetch_data_branch()
        #     self.fetch_data_fee()
        #     self.fetch_data_exam()
        #     self.fetch_data_course()
        #     messagebox.showinfo("Success", "Data added successfully", parent=self.root)

        # except Exception as es:
        #     messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root) 
    
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
            my_cursor = conn.cursor()
            a=self.Modify.get()
            if a=="Student" and self.var_SID.get()==0:
                my_cursor.execute("SELECT * FROM STUDENT_DETAILS")
                data = my_cursor.fetchall()
                if len(data) != 0:
                   self.STUDENT_DETAILS.delete(*self.STUDENT_DETAILS.get_children())
                   for i in data:
                       self.STUDENT_DETAILS.insert("", END, values=i)
                   conn.commit()   
                conn.close()
        
        
            elif a=="Student" and self.var_SID.get()!=0:
                my_cursor.execute("SELECT * FROM STUDENT_DETAILS where Student_ID=%s",(self.var_SID.get(),))
                data = my_cursor.fetchall()
                if len(data) != 0:
                   self.STUDENT_DETAILS.delete(*self.STUDENT_DETAILS.get_children())
                   for Student_ID,Student_Name,Student_PHNO,Email_ID,DOB,Address  in data:
                       self.STUDENT_DETAILS.insert("", END, values=(Student_ID,Student_Name,Student_PHNO,Email_ID,DOB,Address))
                   conn.commit()   
                conn.close()
            elif a=="Branch" and self.var_Sbid.get()==0:
                my_cursor.execute("SELECT * FROM BRANCH_DETAILS")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.STUDENT_DETAILS.delete(*self.STUDENT_DETAILS.get_children())
                    for i in data:
                        self.STUDENT_DETAILS.insert("", END, values=(Student_ID,"","","","","",Branch_ID,Branch_Name))
                        conn.commit() 
                conn.close()
            elif a=="Branch" and self.var_Sbid.get()!=0:
                my_cursor.execute("SELECT * FROM BRANCH_DETAILS where Branch_ID=%s",(self.var_Sbid.get(),))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.STUDENT_DETAILS.delete(*self.STUDENT_DETAILS.get_children())
                    for Branch_ID,Branch_Name,Student_ID in data:
                        self.STUDENT_DETAILS.insert("", END, values=(Student_ID,"","","","","",Branch_ID,Branch_Name))
                        conn.commit() 
                conn.close()

            elif a=="Course" and self.var_cid.get()==0:
                my_cursor.execute("SELECT * FROM COURSE_DETAILS")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.COURSE_DETAILS.delete(*self.COURSE_DETAILS.get_children())
                    for Course_ID,course_name,Student_ID in data:
                        self.COURSE_DETAILS.insert("", END, values=(Student_ID,"","","","","","","","","","","","","",Course_ID,course_name))
                        conn.commit() 
                conn.close()

            elif a=="Course" and self.var_cid.get()!=0:
                my_cursor.execute("SELECT * FROM COURSE_DETAILS where Course_ID=%s",(self.var_cid.get(),))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.COURSE_DETAILS.delete(*self.COURSE_DETAILS.get_children())
                    for Course_ID,course_name,Student_ID in data:
                        self.COURSE_DETAILS.insert("", END, values=(Student_ID,"","","","","","","","","","","","","","","","",Course_ID,course_name))
                        conn.commit() 
                conn.close()

            elif a=="Fee" and self.var_pid.get()==0:
                my_cursor.execute("SELECT * FROM FEE_DETAILS")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.FEE_DETAILS.delete(*self.FEE_DETAILS.get_children())
                    for Student_ID,Payment_ID,Amount,Payment_Date in data:
                       self.FEE_DETAILS.insert("", END, values=(Student_ID,"","","","","","","",Payment_ID,Amount,Payment_Date))
                       conn.commit()
                conn.close()   
            elif a=="Fee" and self.var_pid.get()!=0:
                my_cursor.execute("SELECT * FROM FEE_DETAILS where Payment_ID=%s ",(self.var_pid.get()))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.FEE_DETAILS.delete(*self.FEE_DETAILS.get_children())
                    for Student_ID,Payment_ID,Amount,Payment_Date  in data:
                       self.FEE_DETAILS.insert("", END, values=(Student_ID,"","","","","","","","",Payment_ID,Amount,Payment_Date))
                       conn.commit()
                conn.close()   
            elif a=="Exam" and self.var_SID.get()==0:
                my_cursor.execute("SELECT * FROM EXAM_DETAILS")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.EXAM_DETAILS.delete(*self.EXAM_DETAILS.get_children())
                    for Student_ID,Sem,SGPA,Max_marks,Course_ID in data:
                       self.EXAM_DETAILS.insert("", END, values=(Student_ID,"","","","","","","","","","",Sem,SGPA,Max_marks,Course_ID))
                       conn.commit()
                conn.close()                
            elif a=="Exam" and self.var_SID.get()!=0:
                my_cursor.execute("SELECT * FROM EXAM_DETAILS where Student_ID=%s",(self.var_SID.get()))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.EXAM_DETAILS.delete(*self.EXAM_DETAILS.get_children())
                    for Student_ID,Sem,SGPA,Max_marks,Course_ID in data:
                       self.EXAM_DETAILS.insert("", END, values=(Student_ID,"","","","","","","","","","",Sem,SGPA,Max_marks,Course_ID))
                       conn.commit()
                conn.close()
            messagebox.showinfo("Sucess","Details displayed",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
        
    

            
        
    #     conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")

    #     my_cursor = conn.cursor()
    #     my_cursor.execute("SELECT * FROM BRANCH_DETAILS")
    #     data = my_cursor.fetchall()
    #     if len(data) != 0:
    #         self.BRANCH_DETAILS.delete(*self.BRANCH_DETAILS.get_children())
    #         for i in data:
    #             self.BRANCH_DETAILS.insert("", END, values=i)
    #     conn.close()

    #     conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("SELECT * FROM FEE_DETAILS")
    #     data = my_cursor.fetchall()
    #     if len(data) != 0:
    #         self.FEE_DETAILS.delete(*self.FEE_DETAILS.get_children())
    #         for i in data:
    #             self.FEE_DETAILS.insert("", END, values=i)
    #     conn.close()

    # def fetch_data_exam(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("SELECT * FROM EXAM_DETAILS")
    #     data = my_cursor.fetchall()
    #     if len(data) != 0:
    #         self.EXAM_DETAILS.delete(*self.EXAM_DETAILS.get_children())
    #         for i in data:
    #           self.EXAM_DETAILS.insert("", END, values=i)
    #     conn.close()

    # def fetch_data_course(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("SELECT * FROM COURSE_DETAILS")
    #     data = my_cursor.fetchall()
    #     if len(data) != 0:
    #         self.COURSE_DETAILS.delete(*self.COURSE_DETAILS.get_children())
    #         for i in data:
    #             self.COURSE_DETAILS.insert("", END, values=i)
    #     conn.close()

    
    # def fetch_data(self):
    #     try:
    #         conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
    #         my_cursor = conn.cursor()
    #         option = self.Modify.get()
        
    #         if option == "Student":
    #             if self.var_SID.get() == 0:
    #                 my_cursor.execute("SELECT * FROM STUDENT_DETAILS")
    #             else:
    #                 my_cursor.execute("SELECT * FROM STUDENT_DETAILS WHERE Student_ID = %s", (self.var_SID.get(),))
                
    #         elif option == "Branch":
    #             if self.var_Sbid.get() == 0:
    #                 my_cursor.execute("SELECT * FROM BRANCH_DETAILS")
    #             else:
    #                 my_cursor.execute("SELECT * FROM BRANCH_DETAILS WHERE B_ID = %s", (self.var_Sbid.get(),))
                
    #         elif option == "Course":
    #             if self.var_cid.get() == 0:
    #                 my_cursor.execute("SELECT * FROM COURSE_DETAILS")
    #             else:
    #                 my_cursor.execute("SELECT * FROM COURSE_DETAILS WHERE C_ID = %s", (self.var_cid.get(),))
                
    #         elif option == "Fee":
    #             if self.var_pid.get() == 0:
    #                 my_cursor.execute("SELECT * FROM FEE_DETAILS")
    #             else:
    #                 my_cursor.execute("SELECT * FROM FEE_DETAILS WHERE P_ID = %s", (self.var_pid.get(),))
                
    #         elif option == "Exam":
    #             if self.var_SID.get() == 0:
    #                 my_cursor.execute("SELECT * FROM EXAM_DETAILS")
    #         else:
    #             my_cursor.execute("SELECT * FROM EXAM_DETAILS WHERE Student_ID = %s", (self.var_SID.get(),))
    #             data = my_cursor.fetchall()
    #             if len(data) != 0:
    #                 self.STUDENT_DETAILS.delete(*self.STUDENT_DETAILS.get_children())
    #             for row in data:
    #                 self.STUDENT_DETAILS.insert("", END, values=row)
    #             conn.commit()
        
    #         conn.close()
    #         messagebox.showinfo("Success", "Details displayed", parent=self.root)
    
    #     except Exception as es:
    #         messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    #get cursorm
    def get_cursor_data(self, event):
        cursor_row = event.focus()
        content = event.item(cursor_row)
        data = content["values"]
        a=self.Modify.get()
        if a=="Student":
            self.var_SID.set(data[0])
            self.var_Sname.set(data[1])
            self.var_Sphno.set(data[2])
            self.var_Seid.set(data[3])
            self.var_SDOB.set(data[4])
            self.var_Sadd.set(data[5])
            
        if a=="Branch":
            self.var_Sbid.set(data[6])
            self.var_sbname.set(data[7])
            self.var_SID.set(data[8])
        if a=="Fee":
            self.var_pid.set(data[9])
            self.var_SID.set(data[10])
            self.var_amt.set(data[11])
            self.var_pdate.set(data[12])
        if a=="Exam":
            self.var_SID.set(data[13])
            self.var_sem.set(data[14])
            self.var_sgpa.set(data[15])
            self.var_mmx.set(data[16])
            self.var_cid.set(data[17])
        if a=="Course":
            self.var_cid.set(data[18])
            self.var_course.set(data[19])
            self.var_SID.set(data[20])
    # def get_cursor_data(self, event):
    #     cursor_row = event.focus()
    #     content = event.item(cursor_row)
    #     data = content["values"]
    #     a=self.Modify.get()
    #     if a=="Student":
    #         self.var_SID.set(data[0])
    #         self.var_Sname.set(data[1])
    #         self.var_Sphno.set(data[2])
    #         self.var_Seid.set(data[3])
    #         self.var_SDOB.set(data[4])
    #         self.var_Sadd.set(data[5])
            
    #     if a=="Branch":
    #         self.var_Sbid.set(data[6])
    #         self.var_sbname.set(data[7])
    #         self.var_SID.set(data[8])
    #     if a=="Fee":
    #         self.var_pid.set(data[9])
    #         self.var_SID.set(data[10])
    #         self.var_amt.set(data[11])
    #         self.var_pdate.set(data[12])
    #     if a=="Exam":
    #         self.var_SID.set(data[13])
    #         self.var_sem.set(data[14])
    #         self.var_sgpa.set(data[15])
    #         self.var_mmx.set(data[16])
    #         self.var_cid.set(data[17])
    #     if a=="Course":
    #         self.var_cid.set(data[18])
    #         self.var_course.set(data[19])
    #         self.var_SID.set(data[20])
#    # Get data from EXAM_DETAILS table

#     # Get data from FEE_DETAILS table
        
#             fee_data = self.get_cursor_data(self.FEE_DETAILS)
#             self.var_pid.set(fee_data[0])
#             self.var_SID.set(fee_data[1])
#             self.var_amt.set(fee_data[2])
#             self.var_pdate.set(fee_data[3])
#    # Get data from EXAM_DETAILS table
        
#             exam_data = self.get_cursor_data(self.EXAM_DETAILS)
#             self.var_SID.set(exam_data[0])
#             self.var_sem.set(exam_data[1])
#             self.var_sgpa.set(exam_data[2])
#             self.var_mmx.set(exam_data[3])
#             self.var_cid.set(exam_data[4])

#    # Get data from COURSE_DETAILS table
        
#             course_data = self.get_cursor_data(self.COURSE_DETAILS)
#             self.var_cid.set(course_data[0])
#             self.var_course.set(course_data[1])
#             self.var_Sbid.set(course_data[2])



    def update_data(self):
        try:
          conn = mysql.connector.connect(host="localhost", username="root", password="H2003", database="student_management_system")
          my_cursor = conn.cursor() 
          a=self.Modify.get()
          if a=="Student":
             my_cursor.execute("update the STUDENT_DETAILS set S_name=%s,Coct=%s,E_ID=%s,DOB=%s,ADD=%s WHERE S_ID=%s",(
                                                                                                                  self.var_Sname.get(),
                                                                                                                  self.var_Sphno.get(),
                                                                                                                  self.var_Seid.get(), 
                                                                                                                  self.var_SDOB.get(), 
                                                                                                                  self.var_Sadd.get(),
                                                                                                                  self.var_SID.get() ))
          elif a=="branch":                                                                                                              
             my_cursor.execute("update the BRANCH_DETAILS set  B_name=%s ,S_ID=%s WHERE B_ID=%s",( 
                                                                                                          
                                                                                                          self.var_sbname.get(),
                                                                                                          self.var_SID.get(),
                                                                                                          self.var_Sbid.get() ))   
          elif a=="fee":
           my_cursor.execute("update the FEE_DETAILS set  S_ID=%s,Amt=%s,PDT=%s WHERE P_ID=%s",(
                                                                                                      
                                                                                                      self.var_SID.get(), 
                                                                                                      self.var_amt.get(), 
                                                                                                      self.var_pdate.get(),
                                                                                                      self.var_pid.get() ))  
          elif a=="exam":
           my_cursor.execute("update the EXAM_DETAILS set sem=%s,SGPA=%s,MMX=%s,C_ID=%s WHERE S_ID=%s",( 
                                                                                                                           
                                                                                                                          self.var_sem.get(),
                                                                                                                          self.var_sgpa.get(),
                                                                                                                          self.var_mmx.get(), 
                                                                                                                          self.var_cid.get(),
                                                                                                                          self.var_SID.get() ))    
           
          elif a=="course":
            my_cursor.execute("update the COURSE_DETAILS set C_ID=%s,C_NAME=%s,B_ID=%s WHERE C_ID=%s",( 
                                                                                                                  
                                                                                                                  self.var_course.get(),
                                                                                                                  self.var_Sbid.get(),
                                                                                                                  self.var_cid.get()))   
          conn.commit()
          conn.close()    
          messagebox.showinfo("Sucess","Details upadted",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    # def delete_data(self):
    #     try:
    #         conn=mysql.connector.connect(host="localhost",username="root",password="H2003",database="student_management_system")
    #         my_cursor=conn.cursor()
    #         a=self.Modify.get()
    #         if a=="Student":
    #             my_cursor.execute("delete from STUDENT_DETAILS where SID=%s",(self.SID.get(),))
    #         elif a=="Course":
    #             my_cursor.execute("delete from COURSE_DETAILS where SID=%s and CID=%s",(self.SID.get(),self.CourseID.get()))
    #         elif a=="Branch":
    #             my_cursor.execute("delete from BRANCH_DETAILS where SID=%s and BID=%s",(self.SID.get(),self.BranchID.get()))
    #         elif a=="Fee":
    #             my_cursor.execute("delete from FEE_DETAILS where TID=%s",(self.TransactionID.get(),))
    #         elif a=="Exam":
    #             my_cursor.execute("delete from EXAM_RESULT where SID=%s and Semester=%s",(self.SID.get(),self.Semester.get()))

    #         conn.commit()
    #         conn.close()    
    #         messagebox.showinfo("Sucess","Details deleted",parent=self.root)
    #     except Exception as es:
    #         messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
