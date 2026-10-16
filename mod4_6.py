# -*- coding: utf-8 -*-
"""
Module 4 (Q61-Q80), Module 5 (Q81-Q100), Module 6 (Q101-Q120)
Comprehensive Bilingual Translations & Lecturer Explanations
"""

DATA_MOD_4_6 = {}

# MODULE 4: Constraints (Q61 - Q80)
DATA_MOD_4_6[61] = {
    "prompt_vi": "Câu lệnh ALTER TABLE nào sau đây dùng để thêm ràng buộc PRIMARY KEY trên cột MANUFACTURER_ID của bảng INVENTORY?",
    "options_vi": {
        "A": "ALTER TABLE inventory ADD PRIMARY KEY (manufacturer_id);",
        "B": "ALTER TABLE inventory ADD CONSTRAINT manufacturer_id PRIMARY KEY;",
        "C": "ALTER TABLE inventory MODIFY manufacturer_id CONSTRAINT PRIMARY KEY;",
        "D": "ALTER TABLE inventory MODIFY CONSTRAINT PRIMARY KEY manufacturer_id;"
    },
    "explanation_vi": "Để thêm khóa chính vào bảng đã tồn tại, ta dùng mệnh đề `ADD PRIMARY KEY (tên_cột)`. Phương án B sai vì đặt tên ràng buộc trùng tên cột và thiếu cặp ngoặc tròn chứa tên cột. Phương án C và D dùng sai từ khóa MODIFY.",
    "key_takeaway_vi": "Cú pháp thêm khóa chính cấp bảng: ALTER TABLE table_name ADD PRIMARY KEY (column_name);",
    "flashcard_front_vi": "Cú pháp thêm PRIMARY KEY vào bảng đã tồn tại?",
    "flashcard_back_vi": "ALTER TABLE table_name ADD PRIMARY KEY (column_name);"
}

DATA_MOD_4_6[62] = {
    "prompt_vi": "Câu lệnh nào sau đây ĐẶT TÊN TƯỜNG MINH cho một ràng buộc (explicitly names a constraint)?",
    "options_vi": {
        "A": "ALTER TABLE student_grades ADD CONSTRAINT student_id_fk FOREIGN KEY (student_id) REFERENCES students(student_id);",
        "B": "ALTER TABLE student_grades ADD FOREIGN KEY (student_id) REFERENCES students(student_id);",
        "C": "ALTER TABLE student_grades ADD CONSTRAINT NAME = student_id_fk FOREIGN KEY (student_id) REFERENCES students(student_id);",
        "D": "ALTER TABLE student grades ADD NAMED CONSTRAINT student_id_fk FOREIGN KEY (student_id) REFERENCES students(student_id);"
    },
    "explanation_vi": "Trong SQL chuẩn và Oracle, từ khóa `CONSTRAINT <tên_ràng_buộc>` được dùng để đặt tên tường minh cho ràng buộc. Nếu không có từ khóa CONSTRAINT và tên, Oracle sẽ tự sinh tên ngầm định dạng `SYS_Cn`. Cú pháp A là chuẩn xác nhất.",
    "key_takeaway_vi": "Đặt tên tường minh cho ràng buộc dùng từ khóa: CONSTRAINT constraint_name.",
    "flashcard_front_vi": "Làm thế nào để đặt tên tường minh cho ràng buộc trong SQL?",
    "flashcard_back_vi": "Dùng từ khóa CONSTRAINT theo sau bởi tên ràng buộc: CONSTRAINT tên_ràng_buộc LOẠI_RÀNG_BUỘC..."
}

DATA_MOD_4_6[63] = {
    "prompt_vi": "Xét lệnh tạo bảng ORDERS:\nCREATE TABLE orders (SER_NO NUMBER UNIQUE, ORDER_ID NUMBER, ORDER_DATE DATE NOT NULL, STATUS VARCHAR2(10) CHECK (status IN ('CREDIT', 'CASH')), PROD_ID NUMBER REFERENCES PRODUCTS(PRODUCT_ID), ORD_TOTAL NUMBER);\nCột nào sẽ được Oracle tự động tạo chỉ mục (index) duy nhất khi thực thi lệnh trên?",
    "options_vi": {
        "A": "SER_NO",
        "B": "ORDER_ID",
        "C": "STATUS",
        "D": "PROD_ID"
    },
    "explanation_vi": "Khi định nghĩa ràng buộc `PRIMARY KEY` hoặc `UNIQUE`, Oracle Server sẽ tự động tạo một chỉ mục duy nhất (Unique Index) trên cột đó để đảm bảo tính duy nhất và tăng tốc kiểm tra ràng buộc. Ở đây cột `SER_NO` có ràng buộc UNIQUE nên được tự động tạo index.",
    "key_takeaway_vi": "Oracle tự động tạo Unique Index cho các cột có ràng buộc PRIMARY KEY và UNIQUE.",
    "flashcard_front_vi": "Ràng buộc nào khiến Oracle tự động tạo Unique Index ngầm định?",
    "flashcard_back_vi": "PRIMARY KEY và UNIQUE."
}

DATA_MOD_4_6[64] = {
    "prompt_vi": "Đối với ràng buộc nào sau đây, Oracle Server sẽ tự động (ngầm định) tạo một chỉ mục duy nhất (unique index)?",
    "options_vi": {
        "A": "PRIMARY KEY",
        "B": "NOT NULL",
        "C": "FOREIGN KEY",
        "D": "CHECK"
    },
    "explanation_vi": "Ràng buộc `PRIMARY KEY` (và `UNIQUE`) yêu cầu tính duy nhất tuyệt đối của dữ liệu, do đó Oracle tự động tạo ngầm định một B-Tree Unique Index trên các cột cấu thành khóa chính. NOT NULL, CHECK, FOREIGN KEY không tự tạo chỉ mục ngầm định.",
    "key_takeaway_vi": "PRIMARY KEY luôn tự động sinh ra một Unique Index ngầm định.",
    "flashcard_front_vi": "FOREIGN KEY có tự động sinh chỉ mục ngầm định trong Oracle không?",
    "flashcard_back_vi": "KHÔNG. Chỉ có PRIMARY KEY và UNIQUE mới tự động sinh Unique Index. (DBA nên chủ động tạo index cho Foreign Key)."
}

DATA_MOD_4_6[65] = {
    "prompt_vi": "Nỗ lực vô hiệu hóa (disable) một ràng buộc của bạn gặp lỗi: ORA-02297: cannot disable constraint - dependencies exist.\nLoại ràng buộc nào sau đây nhiều khả năng đang gây xung đột phụ thuộc khiến bạn không thể disable?",
    "options_vi": {
        "A": "Ràng buộc khóa ngoại (Foreign key Constraints)",
        "B": "Ràng buộc kiểm tra (Check constraints)",
        "C": "Ràng buộc Not NULL (Not NULL constraints)",
        "D": "Ràng buộc duy nhất (Unique Constraints)"
    },
    "explanation_vi": "Lỗi `ORA-02297` xảy ra khi bạn cố gắng DISABLE hoặc DROP một khóa chính (Primary Key) hoặc khóa duy nhất (Unique Key) mà đang có một hoặc nhiều bảng con tham chiếu đến thông qua Khóa ngoại (Foreign Key). Muốn tắt được, bạn phải thêm mệnh đề `CASCADE` (`DISABLE CONSTRAINT ... CASCADE`).",
    "key_takeaway_vi": "ORA-02297 xảy ra do ràng buộc FOREIGN KEY ở bảng khác đang phụ thuộc vào khóa chính này.",
    "flashcard_front_vi": "Lỗi ORA-02297 dependencies exist là do loại ràng buộc nào gây ra?",
    "flashcard_back_vi": "Foreign Key Constraints ở các bảng con đang tham chiếu tới khóa chính bạn muốn disable."
}

DATA_MOD_4_6[66] = {
    "prompt_vi": "Từ khóa nào sau đây KHÔNG PHẢI là một loại ràng buộc (constraint type) hợp lệ trong Oracle?",
    "options_vi": {
        "A": "CASCADE",
        "B": "UNIQUE",
        "C": "CHECK",
        "D": "NOT NULL"
    },
    "explanation_vi": "`CASCADE` là một tùy chọn/mệnh đề phụ đi kèm lệnh DROP/DISABLE hoặc ON DELETE (`CASCADE CONSTRAINTS`, `ON DELETE CASCADE`), chứ bản thân nó KHÔNG PHẢI là một loại ràng buộc. Các loại ràng buộc hợp lệ trong Oracle chỉ có: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK.",
    "key_takeaway_vi": "5 loại ràng buộc chuẩn trong Oracle: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK. CASCADE chỉ là mệnh đề phụ.",
    "flashcard_front_vi": "Liệt kê 5 loại ràng buộc dữ liệu chính trong Oracle?",
    "flashcard_back_vi": "1. NOT NULL, 2. UNIQUE, 3. PRIMARY KEY, 4. FOREIGN KEY, 5. CHECK. (CASCADE không phải loại ràng buộc)."
}

DATA_MOD_4_6[67] = {
    "prompt_vi": "Ràng buộc nào sau đây đảm bảo rằng cột CUSTOMER_NAME của bảng CUSTOMERS luôn luôn phải chứa dữ liệu (không được để trống)?",
    "options_vi": {
        "A": "NOT NULL hoặc Primary Key",
        "B": "Chỉ Primary Key (Only Primary Key)",
        "C": "Unique",
        "D": "Foreign Key"
    },
    "explanation_vi": "Cả hai ràng buộc `NOT NULL` và `PRIMARY KEY` đều ép buộc cột không được chứa giá trị NULL (bắt buộc luôn phải có giá trị). Khóa chính (Primary Key) ngầm định chứa thuộc tính NOT NULL + UNIQUE.",
    "key_takeaway_vi": "Cột luôn có giá trị khi có ràng buộc NOT NULL hoặc PRIMARY KEY.",
    "flashcard_front_vi": "Ràng buộc nào cấm giá trị NULL trong cột?",
    "flashcard_back_vi": "NOT NULL và PRIMARY KEY."
}

DATA_MOD_4_6[68] = {
    "prompt_vi": "Khung nhìn từ điển dữ liệu (data dictionary view) nào người dùng nên truy vấn để xem các cột gắn liền với các ràng buộc trên bảng thuộc quyền sở hữu của mình?",
    "options_vi": {
        "A": "USER_CONS_COLUMNS",
        "B": "USER_CONSTRAINTS",
        "C": "USER_OBJECTS",
        "D": "ALL_CONSTRAINTS"
    },
    "explanation_vi": "Trong Oracle: `USER_CONSTRAINTS` lưu thông tin định nghĩa ràng buộc (tên, loại ràng buộc P/R/U/C, bảng); còn `USER_CONS_COLUMNS` lưu danh sách chi tiết các CỘT cấu thành nên ràng buộc đó và vị trí của chúng (`COLUMN_NAME`, `POSITION`).",
    "key_takeaway_vi": "Xem cột thuộc ràng buộc tra cứu view USER_CONS_COLUMNS; xem định nghĩa ràng buộc tra cứu USER_CONSTRAINTS.",
    "flashcard_front_vi": "Xem các cột tham gia vào ràng buộc tra cứu view nào trong Oracle?",
    "flashcard_back_vi": "USER_CONS_COLUMNS."
}

DATA_MOD_4_6[69] = {
    "prompt_vi": "Bạn cần sửa đổi bảng STUDENTS (hiện đang rỗng) để thêm khóa chính trên cột STUDENT_ID. Câu lệnh nào thực hiện đúng tác vụ?",
    "options_vi": {
        "A": "ALTER TABLE students ADD CONSTRAINT stud_id_pk PRIMARY KEY (student_id);",
        "B": "ALTER TABLE students ADD PRIMARY KEY student_id;",
        "C": "ALTER TABLE students ADD CONSTRAINT PRIMARY KEY (student_id);",
        "D": "ALTER TABLE students ADD CONSTRAINT stud_id_pk PRIMARY KEY student_id;"
    },
    "explanation_vi": "Cú pháp chuẩn xác: `ALTER TABLE <tên_bảng> ADD CONSTRAINT <tên_pk> PRIMARY KEY (<tên_cột>);`. Tên cột bắt buộc phải nằm trong cặp dấu ngoặc đơn.",
    "key_takeaway_vi": "Thêm khóa chính có đặt tên: ALTER TABLE table ADD CONSTRAINT pk_name PRIMARY KEY (col);",
    "flashcard_front_vi": "Cú pháp thêm khóa chính có đặt tên trong SQL?",
    "flashcard_back_vi": "ALTER TABLE table ADD CONSTRAINT pk_name PRIMARY KEY (col);"
}

DATA_MOD_4_6[70] = {
    "prompt_vi": "Phát biểu nào sau đây về mệnh đề CASCADE CONSTRAINTS là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Mệnh đề CASCADE CONSTRAINTS có thể được sử dụng khi TẠO ràng buộc để cho phép tự động xóa khóa ngoại khi khóa chính bị xóa.",
        "B": "Mệnh đề CASCADE CONSTRAINTS được dùng đi kèm với mệnh đề DROP COLUMN.",
        "C": "Mệnh đề CASCADE CONSTRAINTS sẽ xóa tất cả các ràng buộc toàn vẹn tham chiếu trỏ đến khóa chính và khóa duy nhất của cột bị xóa.",
        "D": "Mệnh đề CASCADE CONSTRAINTS cũng xóa tất cả các ràng buộc nhiều cột được định nghĩa trên cột bị xóa."
    },
    "explanation_vi": "Phát biểu A là SAI vì mệnh đề `CASCADE CONSTRAINTS` chỉ được sử dụng trong các lệnh `DROP TABLE` hoặc `ALTER TABLE ... DROP COLUMN / DROP CONSTRAINT`. Khi tạo bảng (CREATE TABLE), ta dùng mệnh đề `ON DELETE CASCADE` (chỉ định hành vi khi xóa bản ghi), chứ không dùng `CASCADE CONSTRAINTS` khi tạo ràng buộc.",
    "key_takeaway_vi": "CASCADE CONSTRAINTS chỉ dùng khi DROP (bảng, cột, ràng buộc), không dùng khi CREATE CONSTRAINT.",
    "flashcard_front_vi": "Mệnh đề CASCADE CONSTRAINTS dùng trong những câu lệnh nào?",
    "flashcard_back_vi": "Dùng trong DROP TABLE hoặc ALTER TABLE ... DROP COLUMN / DROP CONSTRAINT."
}

DATA_MOD_4_6[71] = {
    "prompt_vi": "Khung nhìn từ điển dữ liệu nào có thể được dùng để xem chi tiết các cột tham gia vào các ràng buộc?",
    "options_vi": {
        "A": "USER_CONS_COLUMNS",
        "B": "USER_COLS_CONSTRAINTS",
        "C": "USER_CONSTRAINTS",
        "D": "USER_OBJECTS"
    },
    "explanation_vi": "Khung nhìn `USER_CONS_COLUMNS` chứa thông tin về các cột tham gia vào ràng buộc (`OWNER`, `CONSTRAINT_NAME`, `TABLE_NAME`, `COLUMN_NAME`, `POSITION`). `USER_COLS_CONSTRAINTS` là tên giả không tồn tại trong Oracle.",
    "key_takeaway_vi": "USER_CONS_COLUMNS là view chứa chi tiết các cột tham gia ràng buộc.",
    "flashcard_front_vi": "Từ điển dữ liệu nào lưu tên cột tham gia ràng buộc?",
    "flashcard_back_vi": "USER_CONS_COLUMNS."
}

DATA_MOD_4_6[72] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây định nghĩa đúng ràng buộc FOREIGN KEY trên cột DEPTNO của bảng EMP tham chiếu đến bảng DEPT?",
    "options_vi": {
        "A": "CREATE TABLE EMP(empno NUMBER(4), ename VARCHAR2(35), deptno NUMBER(7,2) CONSTRAINT emp_deptno_fk REFERENCES dept (deptno)); (Lưu ý: đề gốc có lỗi in VARCNAR2)",
        "B": "CREATE TABLE EMP(empno NUMBER(4), ename VARCHAR2(35), deptno NUMBER(7,2) NOT NULL CONSTRAINT emp_deptno_fk FOREIGN KEY deptno REFERENCES dept deptno);",
        "C": "CREATE TABLE EMP(empno NUMBER(4), ename VARCHAR2(35), deptno NUMBER(7,2) NOT NULL, CONSTRAINT emp_deptno_fk REFERENCES dept (deptno) FOREIGN KEY (deptno));",
        "D": "CREATE TABLE EMP(empno NUMBER(4), ename VARCHAR2(35), deptno NUMBER(7,2) FOREIGN KEY CONSTRAINT emp deptno fk REFERENCES dept (deptno));"
    },
    "explanation_vi": "Ở cấp độ cột (Column-level constraint), cú pháp khai báo khóa ngoại là: `[CONSTRAINT <tên_fk>] REFERENCES <bảng_cha> (<cột_cha>)` (chú ý: ở cấp độ cột KHÔNG DÙNG cụm từ 'FOREIGN KEY'). Cụm từ 'FOREIGN KEY (cột)' chỉ dùng khi khai báo ở cấp độ bảng (Table-level).",
    "key_takeaway_vi": "Khai báo Foreign Key ở cấp cột: [CONSTRAINT tên_fk] REFERENCES bảng_cha(cột_cha). Không viết từ khóa FOREIGN KEY.",
    "flashcard_front_vi": "Khai báo Foreign Key ở cấp độ cột có viết từ khóa 'FOREIGN KEY' không?",
    "flashcard_back_vi": "KHÔNG. Cấp cột chỉ viết: REFERENCES bảng_cha (cột_cha). Cấp bảng mới viết: FOREIGN KEY (cột) REFERENCES bảng_cha(cột_cha)."
}

DATA_MOD_4_6[73] = {
    "prompt_vi": "Câu lệnh nào sau đây được sử dụng để thay đổi trạng thái ràng buộc (bật - ENABLE, tắt - DISABLE, hoặc xóa - DROP một ràng buộc)?",
    "options_vi": {
        "A": "ALTER TABLE",
        "B": "ALTER CONSTRAINT",
        "C": "DROP CONSTRAINT",
        "D": "ALTER OBJECT"
    },
    "explanation_vi": "Mọi thao tác quản lý ràng buộc (ENABLE, DISABLE, DROP CONSTRAINT, ADD CONSTRAINT) đều được thực hiện thông qua câu lệnh `ALTER TABLE <tên_bảng> ...`. Trong SQL không có câu lệnh độc lập nào là `ALTER CONSTRAINT`.",
    "key_takeaway_vi": "Mọi thao tác thay đổi trạng thái ràng buộc đều dùng lệnh ALTER TABLE.",
    "flashcard_front_vi": "Lệnh nào dùng để bật/tắt ràng buộc trong Oracle?",
    "flashcard_back_vi": "ALTER TABLE table_name ENABLE/DISABLE CONSTRAINT constraint_name;"
}

DATA_MOD_4_6[74] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG về việc sử dụng các ràng buộc (Constraints)?",
    "options_vi": {
        "A": "Ràng buộc giúp các câu truy vấn phức tạp trở nên dễ dàng hơn (Constraints make complex queries easy).",
        "B": "Ràng buộc thực thi các quy tắc nghiệp vụ ở cấp độ khung nhìn (view).",
        "C": "Ràng buộc thực thi các quy tắc nghiệp vụ ở cấp độ bảng (table).",
        "D": "Ràng buộc ngăn chặn việc xóa một bảng nếu bảng đó đang có các quan hệ phụ thuộc."
    },
    "explanation_vi": "Mục đích duy nhất của ràng buộc (Constraint) là bảo vệ và duy trì tính toàn vẹn dữ liệu (Data Integrity) theo quy tắc nghiệp vụ. Ràng buộc không có chức năng 'làm cho các câu truy vấn phức tạp trở nên dễ viết hơn'.",
    "key_takeaway_vi": "Ràng buộc dùng để bảo vệ tính toàn vẹn dữ liệu, không giúp đơn giản hóa việc viết truy vấn.",
    "flashcard_front_vi": "Mục đích chính của ràng buộc trong CSDL là gì?",
    "flashcard_back_vi": "Đảm bảo tính toàn vẹn và hợp lệ của dữ liệu (Data Integrity), ngăn dữ liệu sai quy tắc."
}

DATA_MOD_4_6[75] = {
    "prompt_vi": "Phát biểu nào sau đây về ràng buộc NOT NULL là ĐÚNG?",
    "options_vi": {
        "A": "Ràng buộc NOT NULL chỉ có thể được định nghĩa ở cấp độ cột (column level).",
        "B": "Bạn không thể thêm ràng buộc NOT NULL vào cột đã có bằng lệnh ALTER TABLE.",
        "C": "Bạn có thể thay đổi cấu trúc của ràng buộc NOT NULL bằng lệnh ALTER TABLE.",
        "D": "Ràng buộc NOT NULL được lưu trữ trong từ điển dữ liệu dưới dạng ràng buộc UNIQUE."
    },
    "explanation_vi": "Trong Oracle SQL, ràng buộc `NOT NULL` là ràng buộc duy nhất CHỈ CÓ THỂ ĐỊNH NGHĨA Ở CẤP ĐỘ CỘT (Column level), không thể định nghĩa ở cấp độ bảng (Table level). Khi muốn thêm NOT NULL cho cột đã có, ta phải dùng cú pháp `ALTER TABLE table MODIFY (column NOT NULL)`.",
    "key_takeaway_vi": "Ràng buộc NOT NULL chỉ có thể được khai báo ở cấp độ cột (Column level).",
    "flashcard_front_vi": "Ràng buộc nào chỉ khai báo được ở cấp độ cột, không khai báo được ở cấp độ bảng?",
    "flashcard_back_vi": "Ràng buộc NOT NULL."
}

DATA_MOD_4_6[76] = {
    "prompt_vi": "Bảng PO_DETAIL có các cột: PO_NUM NOT NULL PK, PO_LINE_ID NOT NULL PK, PRODUCT_ID FK, QUANTITY, UNIT_PRICE.\nĐánh giá câu lệnh: ALTER TABLE po_detail ENABLE CONSTRAINT po_num_pk;\nBạn thực hiện câu lệnh này nhằm mục đích gì?",
    "options_vi": {
        "A": "Kích hoạt lại ràng buộc đã bị vô hiệu hóa trước đó trên cột PO_NUM và đồng thời tạo chỉ mục khóa chính (PRIMARY KEY index).",
        "B": "Xóa và tạo lại ràng buộc PRIMARY KEY trên cột PO_NUM.",
        "C": "Tạo một ràng buộc PRIMARY KEY mới trên cột PO_NUM.",
        "D": "Kích hoạt bất kỳ ràng buộc FOREIGN KEY nào bị vô hiệu hóa trước đó phụ thuộc vào cột PO_NUM."
    },
    "explanation_vi": "Lệnh `ENABLE CONSTRAINT` dùng để kích hoạt lại một ràng buộc đang ở trạng thái DISABLED. Đối với ràng buộc khóa chính (Primary Key), khi ENABLE, Oracle sẽ tự động quét kiểm tra dữ liệu hiện có và tự động tạo lại một Unique Index trên các cột khóa chính.",
    "key_takeaway_vi": "ENABLE CONSTRAINT kích hoạt lại ràng buộc và tự động tạo index cho Primary Key.",
    "flashcard_front_vi": "Khi ENABLE một ràng buộc PRIMARY KEY bị tắt, Oracle làm gì?",
    "flashcard_back_vi": "Kiểm tra tính hợp lệ dữ liệu của bảng và tự động tạo chỉ mục Unique Index cho khóa chính."
}

DATA_MOD_4_6[77] = {
    "prompt_vi": "Phát biểu nào sau đây về các ràng buộc (constraints) là ĐÚNG?",
    "options_vi": {
        "A": "Ràng buộc ngăn chặn việc xóa một bảng nếu bảng đó đang có các quan hệ phụ thuộc (dependencies).",
        "B": "Ràng buộc chỉ thực thi các quy tắc ở cấp độ bảng.",
        "C": "Bạn bắt buộc phải đặt tên cho mỗi ràng buộc tại thời điểm tạo.",
        "D": "Tên ràng buộc không bắt buộc phải tuân theo quy tắc đặt tên đối tượng chuẩn."
    },
    "explanation_vi": "Nếu một bảng cha đang được tham chiếu bởi khóa ngoại của bảng con, lệnh `DROP TABLE bảng_cha` sẽ bị chặn (lỗi ORA-02449: unique/primary keys in table referenced by foreign keys) để bảo toàn tính toàn vẹn dữ liệu.",
    "key_takeaway_vi": "Ràng buộc khóa ngoại ngăn không cho xóa bảng cha nếu có bảng con đang phụ thuộc.",
    "flashcard_front_vi": "Tại sao không thể DROP bảng cha khi đang có khóa ngoại tham chiếu?",
    "flashcard_back_vi": "Vì ràng buộc toàn vẹn tham chiếu (Foreign Key) ngăn chặn để tránh sinh ra dữ liệu mồ côi."
}

DATA_MOD_4_6[78] = {
    "prompt_vi": "Cú pháp nào sau đây dùng để kích hoạt (bật) một ràng buộc đang tồn tại?",
    "options_vi": {
        "A": "ALTER TABLE table_name ENABLE CONSTRAINT constraint_name;",
        "B": "ALTER TABLE table_name ENABLE constraint_name;",
        "C": "ALTER TABLE table_name STATUS = ENABLE CONSTRAINT constraint_name;",
        "D": "ALTER TABLE table_name STATUS ENABLE CONSTRAINT constraint_name;"
    },
    "explanation_vi": "Cú pháp chuẩn xác trong Oracle SQL để bật lại một ràng buộc là: `ALTER TABLE <tên_bảng> ENABLE CONSTRAINT <tên_ràng_buộc>;`.",
    "key_takeaway_vi": "Cú pháp bật ràng buộc: ALTER TABLE table_name ENABLE CONSTRAINT constraint_name;",
    "flashcard_front_vi": "Cú pháp bật lại một ràng buộc trong Oracle?",
    "flashcard_back_vi": "ALTER TABLE table_name ENABLE CONSTRAINT constraint_name;"
}

DATA_MOD_4_6[79] = {
    "prompt_vi": "Phát biểu nào sau đây về việc tạo các ràng buộc là ĐÚNG?",
    "options_vi": {
        "A": "Các ràng buộc có thể được tạo sau khi bảng đã được tạo (Constraints can be created after the table is created).",
        "B": "Tên ràng buộc bắt buộc phải bắt đầu bằng SYS_C.",
        "C": "Tất cả các ràng buộc bắt buộc phải định nghĩa ở cấp độ cột.",
        "D": "Thông tin về các ràng buộc được tìm thấy trong view VIEW_CONSTRAINTS."
    },
    "explanation_vi": "Bạn có thể định nghĩa ràng buộc ngay khi tạo bảng (`CREATE TABLE`) hoặc thêm sau đó bất kỳ lúc nào bằng câu lệnh `ALTER TABLE table_name ADD CONSTRAINT...`.",
    "key_takeaway_vi": "Có thể thêm ràng buộc vào bảng bất kỳ lúc nào sau khi bảng đã tạo.",
    "flashcard_front_vi": "Có thể tạo ràng buộc sau khi bảng đã được tạo từ trước không?",
    "flashcard_back_vi": "CÓ. Sử dụng câu lệnh ALTER TABLE table_name ADD CONSTRAINT..."
}

DATA_MOD_4_6[80] = {
    "prompt_vi": "Ràng buộc nào sau đây CHỈ CÓ THỂ được định nghĩa ở cấp độ cột (column level)?",
    "options_vi": {
        "A": "NOT NULL",
        "B": "UNIQUE",
        "C": "CHECK",
        "D": "PRIMARY KEY"
    },
    "explanation_vi": "Trong Oracle SQL, các ràng buộc UNIQUE, CHECK, PRIMARY KEY, FOREIGN KEY đều có thể định nghĩa ở cả cấp độ cột lẫn cấp độ bảng. Riêng ràng buộc `NOT NULL` chỉ có thể được khai báo duy nhất ở cấp độ cột.",
    "key_takeaway_vi": "NOT NULL là ràng buộc duy nhất chỉ định nghĩa được ở cấp độ cột.",
    "flashcard_front_vi": "Ràng buộc nào không thể khai báo ở cấp độ bảng (Table level)?",
    "flashcard_back_vi": "Ràng buộc NOT NULL."
}

# MODULE 5: DML (Q81 - Q100)
DATA_MOD_4_6[81] = {
    "prompt_vi": "Một câu lệnh ngôn ngữ thao tác dữ liệu (DML) thực hiện nhiệm vụ gì?",
    "options_vi": {
        "A": "Sửa đổi dữ liệu nhưng không thay đổi cấu trúc của bảng (Modifies data but not structure).",
        "B": "Hoàn tất một giao dịch trên bảng.",
        "C": "Sửa đổi cả cấu trúc và dữ liệu trong bảng.",
        "D": "Sửa đổi cấu trúc nhưng không sửa đổi dữ liệu của bảng."
    },
    "explanation_vi": "DML (Data Manipulation Language - gồm INSERT, UPDATE, DELETE, MERGE) chỉ thao tác trên các bản ghi dữ liệu bên trong bảng. Việc thay đổi cấu trúc bảng (thêm/xóa cột, đổi kiểu dữ liệu) là trách nhiệm của DDL (ALTER TABLE, CREATE TABLE...).",
    "key_takeaway_vi": "DML chỉ sửa đổi dữ liệu (dòng), không làm thay đổi cấu trúc (cột/kiểu dữ liệu) của bảng.",
    "flashcard_front_vi": "DML khác DDL ở điểm mấu chốt nào?",
    "flashcard_back_vi": "DML (INSERT/UPDATE/DELETE) thao tác trên dữ liệu hàng; DDL (CREATE/ALTER/DROP) thao tác trên cấu trúc đối tượng."
}

DATA_MOD_4_6[82] = {
    "prompt_vi": "Phát biểu nào sau đây về chức năng của câu lệnh DML là ĐÚNG?",
    "options_vi": {
        "A": "Lệnh UPDATE có thể cập nhật nhiều cột trong cùng một bảng cùng lúc.",
        "B": "Lệnh DELETE có thể được dùng để xóa các dòng hoặc các cột khỏi bảng.",
        "C": "Lệnh MERGE sẽ xóa các dòng không tồn tại ở cả hai bảng.",
        "D": "Lệnh UPDATE sẽ thêm các dòng mới vào bảng nếu có mệnh đề INTO."
    },
    "explanation_vi": "Lệnh UPDATE cho phép cập nhật nhiều cột cùng lúc bằng cách liệt kê ngăn cách bởi dấu phẩy: `UPDATE table SET col1 = val1, col2 = val2 WHERE ...`. Phương án B sai vì DELETE chỉ xóa dòng, xóa cột phải dùng ALTER TABLE DROP COLUMN.",
    "key_takeaway_vi": "UPDATE có thể cập nhật nhiều cột trong một lệnh bằng cách ngăn cách bằng dấu phẩy.",
    "flashcard_front_vi": "Có thể cập nhật nhiều cột trong một câu lệnh UPDATE không?",
    "flashcard_back_vi": "CÓ. Cú pháp: UPDATE table SET col1 = val1, col2 = val2 WHERE..."
}

DATA_MOD_4_6[83] = {
    "prompt_vi": "Bạn là chủ sở hữu bảng EMPLOYEES. Điều gì xảy ra khi bạn thực thi câu lệnh: DELETE employees;",
    "options_vi": {
        "A": "Dữ liệu trong bảng EMPLOYEES bị xóa toàn bộ nhưng cấu trúc bảng vẫn được giữ nguyên.",
        "B": "Báo lỗi vi phạm khóa chính.",
        "C": "Cả dữ liệu và cấu trúc của bảng EMPLOYEES đều bị xóa.",
        "D": "Báo lỗi vì câu lệnh sai cú pháp."
    },
    "explanation_vi": "Khi chạy `DELETE employees;` (không có mệnh đề WHERE), tất cả các dòng dữ liệu trong bảng sẽ bị xóa sạch, nhưng cấu trúc bảng (các cột, ràng buộc, chỉ mục) vẫn còn nguyên và giao dịch này có thể ROLLBACK được nếu chưa COMMIT.",
    "key_takeaway_vi": "DELETE không có WHERE sẽ xóa sạch dữ liệu nhưng giữ nguyên cấu trúc bảng.",
    "flashcard_front_vi": "DELETE không có WHERE khác gì với DROP TABLE?",
    "flashcard_back_vi": "DELETE chỉ xóa hết các dòng dữ liệu, giữ lại cấu trúc bảng; DROP xóa luôn cả cấu trúc bảng."
}

DATA_MOD_4_6[84] = {
    "prompt_vi": "Xét cấu trúc bảng EMPLOYEES: EMPLOYEE_ID NUMBER Primary Key, FIRST_NAME VARCHAR2(25), LAST_NAME VARCHAR2(25).\nCâu lệnh nào sau đây sẽ THẤT BẠI khi chèn bản ghi vào bảng?",
    "options_vi": {
        "A": "INSERT INTO employees( first_name, last_name) VALUES( 'John', 'Smith');",
        "B": "INSERT INTO employees VALUES ( '1000', 'John', NULL);",
        "C": "INSERT INTO employees (employee_id) VALUES (1000);",
        "D": "INSERT INTO employees (employee_id, first_name, last_name) VALUES ( 1000, 'John', ' ');"
    },
    "explanation_vi": "Cột `EMPLOYEE_ID` là Khóa chính (Primary Key), do đó bắt buộc phải có giá trị và không được phép chứa giá trị NULL. Câu lệnh A không liệt kê cột `employee_id`, nên Oracle sẽ ngầm định gán NULL cho cột này, dẫn đến lỗi vi phạm ràng buộc khóa chính `ORA-01400: cannot insert NULL into (...)`.",
    "key_takeaway_vi": "Khóa chính bắt buộc phải có giá trị, không được phép chèn NULL.",
    "flashcard_front_vi": "Tại sao câu lệnh INSERT thiếu cột Primary Key sẽ bị lỗi?",
    "flashcard_back_vi": "Vì cột Primary Key không chấp nhận giá trị NULL; nếu không gán giá trị, Oracle sẽ báo lỗi ORA-01400."
}

DATA_MOD_4_6[85] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG về câu lệnh MERGE?",
    "options_vi": {
        "A": "Lệnh MERGE thay thế hoàn toàn toàn bộ dữ liệu của một bảng bằng dữ liệu của một bảng khác.",
        "B": "Lệnh MERGE được sử dụng để trộn dữ liệu của một bảng với dữ liệu từ bảng khác.",
        "C": "Lệnh MERGE có thể được dùng để chèn các dòng mới vào một bảng.",
        "D": "Lệnh MERGE có thể được dùng để cập nhật các dòng hiện có trong một bảng."
    },
    "explanation_vi": "Lệnh `MERGE` (còn gọi là UPSERT) thực hiện cập nhật có điều kiện: nếu bản ghi đã tồn tại thì UPDATE, nếu chưa tồn tại thì INSERT. Nó KHÔNG PHẢI là thao tác xóa và thay thế toàn bộ dữ liệu bảng (không phải truncate and reload). Do đó phát biểu A là SAI.",
    "key_takeaway_vi": "MERGE thực hiện chèn hoặc cập nhật có chọn lọc dựa trên điều kiện ON, không thay thế mù quáng toàn bảng.",
    "flashcard_front_vi": "Lệnh MERGE trong SQL làm nhiệm vụ gì?",
    "flashcard_back_vi": "Kết hợp INSERT và UPDATE trong một lệnh duy nhất (UPSERT) dựa trên điều kiện so khớp."
}

DATA_MOD_4_6[86] = {
    "prompt_vi": "Trong SQL, làm thế nào để chèn giá trị \"Olsen\" vào cột \"LastName\" trong bảng \"Persons\"?",
    "options_vi": {
        "A": "INSERT INTO Persons (LastName) VALUES ('Olsen')",
        "B": "INSERT INTO Persons ('Olsen') as LastName",
        "C": "INSERT LastName('Olsen') INTO Persons",
        "D": "Không có câu nào ở trên đúng."
    },
    "explanation_vi": "Cú pháp chèn dữ liệu chuẩn trong SQL: `INSERT INTO <tên_bảng> (<danh_sách_cột>) VALUES (<danh_sách_giá_trị>);`.",
    "key_takeaway_vi": "Cú pháp chèn chuẩn: INSERT INTO table (col) VALUES ('val');",
    "flashcard_front_vi": "Cú pháp INSERT INTO chuẩn trong SQL?",
    "flashcard_back_vi": "INSERT INTO table_name (column_name) VALUES (value);"
}

DATA_MOD_4_6[87] = {
    "prompt_vi": "Làm thế nào để đổi giá trị \"Hansen\" thành \"Nilsen\" trong cột \"LastName\" của bảng Persons?",
    "options_vi": {
        "A": "UPDATE Persons SET LastName='Nilsen' WHERE LastName='Hansen'",
        "B": "MODIFY Persons SET LastName='Hansen' INTO LastName='Nilsen'",
        "C": "UPDATE Persons SET LastName='Hansen' INTO LastName='Nilsen'",
        "D": "MODIFY Persons SET LastName='Nilsen' WHERE LastName='Hansen'"
    },
    "explanation_vi": "Cú pháp cập nhật dữ liệu chuẩn: `UPDATE <tên_bảng> SET <cột> = <giá_trị_mới> WHERE <điều_kiện>;`. Cần gán giá trị mới 'Nilsen' vào SET và đặt điều kiện tìm giá trị cũ 'Hansen' ở WHERE.",
    "key_takeaway_vi": "Cú pháp UPDATE chuẩn: UPDATE table SET col = new_val WHERE col = old_val;",
    "flashcard_front_vi": "Cú pháp UPDATE một cột có điều kiện trong SQL?",
    "flashcard_back_vi": "UPDATE table_name SET col = new_val WHERE condition;"
}

DATA_MOD_4_6[88] = {
    "prompt_vi": "Trong SQL, làm thế nào để xóa các bản ghi có \"FirstName\" là \"Peter\" trong bảng Persons?",
    "options_vi": {
        "A": "DELETE FROM Persons WHERE FirstName = 'Peter'",
        "B": "DELETE * FROM Persons WHERE FirstName = 'Peter'",
        "C": "DELETE FirstName FROM Persons WHERE FirstName = 'Peter'",
        "D": "DELETE 'Peter' FROM Persons"
    },
    "explanation_vi": "Cú pháp xóa bản ghi trong SQL là: `DELETE FROM <tên_bảng> WHERE <điều_kiện>;`. Không bao giờ có dấu sao `*` hoặc danh sách tên cột sau từ khóa DELETE.",
    "key_takeaway_vi": "Lệnh DELETE không bao giờ đi kèm dấu * hay tên cột: DELETE FROM table WHERE condition;",
    "flashcard_front_vi": "Câu lệnh DELETE có đi kèm dấu * như SELECT * không?",
    "flashcard_back_vi": "KHÔNG. Cú pháp chuẩn là DELETE FROM table_name WHERE condition."
}

DATA_MOD_4_6[89] = {
    "prompt_vi": "Câu lệnh nào sau đây sẽ chèn thành công chỉ các bản ghi của Sales Representative (job_id = 'SA_REP') từ bảng employees vào bảng mới sales_reps?",
    "options_vi": {
        "A": "INSERT INTO sales_reps(id, name, salary, commission_pct) SELECT employee_id, last_name, salary, commission_pct FROM employees WHERE job_id = 'SA_REP';",
        "B": "INSERT INTO sales_reps(id, name, salary, commission_pct) VALUES SELECT employee_id, last_name, salary, commission_pct FROM employees WHERE job_id = 'SA_REP';",
        "C": "INSERT INTO sales_reps(id, name, salary, commission_pct) SELECT employee_id, last_name, salary, commission_pct FROM employees;",
        "D": "INSERT INTO sales_reps(id, name, salary, commission_pct) SELECT last_name, employee_id, salary, commission_pct FROM employees WHERE job_id = 'SA_REP';"
    },
    "explanation_vi": "Khi chèn dữ liệu bằng câu truy vấn con (INSERT with Subquery), TUYỆT ĐỐI KHÔNG DÙNG từ khóa `VALUES`. Thứ tự các cột trong câu lệnh INSERT phải khớp tương ứng về mặt ý nghĩa và kiểu dữ liệu với thứ tự cột trong SELECT.",
    "key_takeaway_vi": "Khi dùng INSERT INTO ... SELECT, không được có từ khóa VALUES.",
    "flashcard_front_vi": "Có dùng từ khóa VALUES khi thực hiện INSERT bằng SELECT subquery không?",
    "flashcard_back_vi": "KHÔNG. Dùng trực tiếp: INSERT INTO table (cols) SELECT cols FROM source_table WHERE..."
}

DATA_MOD_4_6[90] = {
    "prompt_vi": "Trường hợp nào sau đây KHÔNG PHẢI là mục đích sử dụng hợp lệ của câu lệnh Merge?",
    "options_vi": {
        "A": "Vừa chèn vừa cập nhật trên cùng mỗi một dòng trong một bảng (Insert as well as update each row).",
        "B": "Cập nhật hoặc chèn dữ liệu có điều kiện vào bảng cơ sở dữ liệu.",
        "C": "Thực hiện UPDATE nếu dòng đã tồn tại, và thực hiện INSERT nếu đó là dòng mới.",
        "D": "Tăng hiệu năng và tăng tính tiện dụng khi đồng bộ dữ liệu."
    },
    "explanation_vi": "Trên mỗi dòng dữ liệu được so khớp, lệnh MERGE chỉ thực hiện MỘT trong hai nhánh: hoặc UPDATE (khi match), hoặc INSERT (khi không match). Nó không thể vừa INSERT vừa UPDATE trên cùng một dòng.",
    "key_takeaway_vi": "MERGE chỉ thực hiện hoặc INSERT hoặc UPDATE trên một bản ghi, không làm cả hai trên cùng một dòng.",
    "flashcard_front_vi": "Lệnh MERGE có thực hiện cả INSERT và UPDATE trên cùng một dòng không?",
    "flashcard_back_vi": "KHÔNG. Nó rẽ nhánh: MATCHED thì UPDATE, NOT MATCHED thì INSERT."
}

DATA_MOD_4_6[91] = {
    "prompt_vi": "Kết quả xuất ra của câu lệnh sau là gì?\nUPDATE employees a SET job_id = (SELECT job_id FROM new_employees b WHERE a.employee_id = b.employee_id);\n(Giả sử Employee và New_employees có cùng cấu trúc)",
    "options_vi": {
        "A": "Cập nhật job_id cho tất cả các bản ghi: Khớp trong New_employees thì lấy job_id mới; không khớp thì cập nhật job_id thành NULL.",
        "B": "Câu lệnh sẽ trả về lỗi.",
        "C": "Chỉ cập nhật những bản ghi có employee_id khớp trong bảng New_employees.",
        "D": "Cập nhật những bản ghi khớp, các bản ghi không khớp sẽ giữ nguyên job_id cũ."
    },
    "explanation_vi": "🔥 BẪY KINH ĐIỂN TRONG SQL: Câu lệnh UPDATE không có mệnh đề WHERE ở tầng ngoài cùng! Khi đó nó duyệt qua TẤT CẢ các dòng của bảng employees. Đối với các dòng không tìm thấy `employee_id` tương ứng trong `new_employees`, truy vấn con trả về giá trị `NULL`. Do đó, `job_id` của các dòng này sẽ bị gán thành `NULL`!",
    "key_takeaway_vi": "UPDATE dùng scalar subquery không có WHERE ngoài sẽ gán NULL cho các dòng không tìm thấy kết quả khớp.",
    "flashcard_front_vi": "Điều gì xảy ra khi UPDATE a SET col = (SELECT ...) mà không có WHERE ở câu UPDATE ngoài?",
    "flashcard_back_vi": "Tất cả các dòng không khớp trong bảng con sẽ bị ghi đè thành NULL!"
}

DATA_MOD_4_6[92] = {
    "prompt_vi": "Lệnh nào sau đây KHÔNG PHẢI là một câu lệnh thao tác dữ liệu (DML)?",
    "options_vi": {
        "A": "COMMIT",
        "B": "MERGE",
        "C": "UPDATE",
        "D": "DELETE"
    },
    "explanation_vi": "`COMMIT` là câu lệnh thuộc nhóm TCL (Transaction Control Language - Ngôn ngữ điều khiển giao dịch), dùng để lưu vĩnh viễn các thay đổi vào đĩa. DML chỉ gồm: INSERT, UPDATE, DELETE, MERGE.",
    "key_takeaway_vi": "COMMIT và ROLLBACK thuộc nhóm lệnh TCL, không phải DML.",
    "flashcard_front_vi": "COMMIT thuộc nhóm ngôn ngữ nào trong SQL?",
    "flashcard_back_vi": "TCL (Transaction Control Language)."
}

DATA_MOD_4_6[93] = {
    "prompt_vi": "Kết quả của câu lệnh sau là gì?\nINSERT INTO departments (department_id, department_name, manager_id) VALUES (300, 'Engineering', DEFAULT);",
    "options_vi": {
        "A": "Sẽ chèn một bản ghi với các giá trị (300, 'Engineering') và giá trị mặc định cho cột manager_id.",
        "B": "Chèn bản ghi với chuỗi chữ 'DEFAULT' cho manager_id.",
        "C": "Báo lỗi vì DEFAULT không phải là giá trị hợp lệ.",
        "D": "Báo lỗi cú pháp vì từ khóa DEFAULT không được dùng trong mệnh đề VALUES."
    },
    "explanation_vi": "Trong Oracle SQL, từ khóa `DEFAULT` là hoàn toàn hợp lệ trong mệnh đề `VALUES`. Khi chỉ định `DEFAULT`, Oracle sẽ tự động lấy giá trị mặc định được định nghĩa khi tạo bảng cho cột đó (hoặc NULL nếu không có giá trị mặc định).",
    "key_takeaway_vi": "Từ khóa DEFAULT được phép sử dụng trong mệnh đề VALUES của lệnh INSERT.",
    "flashcard_front_vi": "Có thể dùng từ khóa DEFAULT trong câu lệnh INSERT VALUES (...) không?",
    "flashcard_back_vi": "CÓ. Oracle sẽ gán giá trị mặc định đã định nghĩa của cột đó."
}

DATA_MOD_4_6[94] = {
    "prompt_vi": "Bạn có 2 bảng CUSTOMER và PROSPECT cùng cấu trúc. Bạn muốn đồng bộ: chèn các bản ghi từ PROSPECT vào CUSTOMER nếu chưa tồn tại; nếu đã tồn tại thì cập nhật thông tin khách hàng. Bạn nên dùng câu lệnh DML nào?",
    "options_vi": {
        "A": "MERGE",
        "B": "INSERT",
        "C": "UPDATE",
        "D": "Không thể thực hiện việc này chỉ với một câu lệnh DML."
    },
    "explanation_vi": "Lệnh `MERGE` được sinh ra chính xác cho bài toán này (Conditional Insert/Update hay UPSERT). Nó cho phép kiểm tra sự tồn tại của dữ liệu và thực hiện đồng thời INSERT bản ghi mới hoặc UPDATE bản ghi cũ trong một câu lệnh duy nhất.",
    "key_takeaway_vi": "Đồng bộ 2 bảng (chưa có thì chèn, có rồi thì cập nhật) dùng lệnh MERGE.",
    "flashcard_front_vi": "Lệnh DML nào dùng để đồng bộ dữ liệu (Upsert) giữa 2 bảng?",
    "flashcard_back_vi": "MERGE."
}

DATA_MOD_4_6[95] = {
    "prompt_vi": "Bạn vừa thêm cột PHONE-NUMBER kiểu NUMBER vào bảng EMPLOYEES hiện có 100 nhân viên. Bây giờ bạn cần nhập số điện thoại cho các nhân viên này. Bạn sử dụng thao tác thao tác dữ liệu (DML) nào?",
    "options_vi": {
        "A": "UPDATE (Trong đề thi gốc bị lỗi in ấn mất chữ U thành 'PDATE')",
        "B": "MERGE",
        "C": "INSERT",
        "D": "ADD"
    },
    "explanation_vi": "⚠️ LƯU Ý ĐỀ THI: Khi các dòng dữ liệu nhân viên đã tồn tại sẵn trong bảng, việc điền dữ liệu vào một cột mới thêm là hành động CẬP NHẬT các dòng đã có, do đó bắt buộc phải dùng lệnh `UPDATE`. (Trong tài liệu gốc CDAC, phương án A bị lỗi in ấn rụng mất chữ cái 'U', hiển thị thành 'PDATE').",
    "key_takeaway_vi": "Điền dữ liệu vào cột mới cho các dòng đã tồn tại dùng lệnh UPDATE.",
    "flashcard_front_vi": "Nhập dữ liệu vào một cột mới cho các hàng đã có sẵn trong bảng dùng lệnh gì?",
    "flashcard_back_vi": "UPDATE (Lưu ý trong đề thi CDAC có lỗi in ấn 'PDATE')."
}

DATA_MOD_4_6[96] = {
    "prompt_vi": "Đánh giá câu lệnh DELETE:\nDELETE employee_id, salary, job_id FROM employees WHERE dept_id = 90;\nTại sao câu lệnh DELETE này bị lỗi khi thực thi?",
    "options_vi": {
        "A": "Bạn không được phép chỉ định tên cột trong mệnh đề DELETE của câu lệnh DELETE.",
        "B": "Không có dòng nào có dept_id = 90 trong bảng.",
        "C": "Không thể xóa cột JOB_ID vì đó là cột NOT NULL.",
        "D": "Không thể xóa cột EMPLOYEE_ID vì đó là khóa chính của bảng."
    },
    "explanation_vi": "Lệnh `DELETE` dùng để xóa CẢ DÒNG (records), do đó cú pháp SQL không cho phép liệt kê tên cột sau từ khóa DELETE. Cú pháp đúng phải là `DELETE FROM employees WHERE dept_id = 90;`.",
    "key_takeaway_vi": "DELETE xóa cả bản ghi, không cho phép chỉ định danh sách tên cột.",
    "flashcard_front_vi": "Tại sao viết DELETE col1, col2 FROM table lại bị lỗi?",
    "flashcard_back_vi": "Vì DELETE thao tác trên toàn bộ hàng, không được phép liệt kê tên cột trong mệnh đề DELETE."
}

DATA_MOD_4_6[97] = {
    "prompt_vi": "Xét cấu trúc bảng EMPLOYEES: EMPLOYEE_ID NUMBER Primary Key, FIRST_NAME VARCHAR2(25), LAST_NAME VARCHAR2(25).\nCâu lệnh nào sau đây chèn thành công một dòng vào bảng?",
    "options_vi": {
        "A": "INSERT INTO employees VALUES ('1000','John',NULL);",
        "B": "INSERT INTO employees VALUES ( NULL, 'John','Smith');",
        "C": "INSERT INTO employees( first_name, last_name) VALUES('John','Smith');",
        "D": "INSERT INTO employees(first_name,last_name, employee_id) VALUES ( 1000, 'John','Smith'); (Thứ tự giá trị bị đảo lộn)"
    },
    "explanation_vi": "Cột `EMPLOYEE_ID` là Primary Key nên bắt buộc phải có giá trị khác NULL. Các cột `first_name` và `last_name` không có ràng buộc NOT NULL nên có thể nhận giá trị NULL. Phương án A truyền '1000' (chuỗi số tự động ép sang NUMBER) làm khóa chính, 'John' cho first_name và NULL cho last_name nên hoàn toàn hợp lệ.",
    "key_takeaway_vi": "Cột Primary Key bắt buộc phải có giá trị khác NULL, các cột khác cho phép NULL có thể nhận giá trị NULL.",
    "flashcard_front_vi": "Điều kiện tiên quyết của giá trị chèn vào cột Primary Key là gì?",
    "flashcard_back_vi": "Phải có giá trị duy nhất và KHÔNG ĐƯỢC LÀ NULL."
}

DATA_MOD_4_6[98] = {
    "prompt_vi": "Xem dữ liệu bảng CLASS (gồm CLASS_ID, CLASS_NAME, HOURS_CREDIT, INSTRUCTOR_ID). Bạn muốn xóa các lớp học CHƯA ĐƯỢC phân công giảng viên. Câu lệnh DELETE nào cho kết quả mong muốn?",
    "options_vi": {
        "A": "DELETE FROM class WHERE instructor_id IS NULL;",
        "B": "DELETE class_id, class_name, hours_credit, instructor_id FROM class WHERE instructor_id IS NULL;",
        "C": "DELETE FROM class WHERE instructor_id NOT IN(SELECT instructor_id FROM class);",
        "D": "DELETE FROM instructor NATURAL JOIN class WHERE instructor_id IS NOT NULL;"
    },
    "explanation_vi": "Để kiểm tra một cột có giá trị rỗng/chưa được phân công, toán tử chuẩn trong SQL là `IS NULL` (không được dùng `= NULL`). Do đó câu lệnh chính xác là `DELETE FROM class WHERE instructor_id IS NULL;`.",
    "key_takeaway_vi": "Kiểm tra giá trị rỗng trong SQL bắt buộc dùng toán tử IS NULL.",
    "flashcard_front_vi": "So sánh giá trị rỗng trong điều kiện WHERE của SQL như thế nào?",
    "flashcard_back_vi": "Dùng toán tử IS NULL (ví dụ: WHERE instructor_id IS NULL), không dùng = NULL."
}

DATA_MOD_4_6[99] = {
    "prompt_vi": "Bảng PRODUCT có các cột: PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, LIST_PRICE, COST.\nBạn cần tăng giá niêm yết (list price) và giá vốn (cost) thêm 5.5% cho tất cả các sản phẩm do nhà cung cấp ID = 105 cung cấp. Câu lệnh nào đúng?",
    "options_vi": {
        "A": "UPDATE product SET list_price = list_price * 1.055, cost = cost * 1.055 WHERE supplier_id = 105;",
        "B": "UPDATE product SET list_price = list_price * 1.055 SET cost = cost * 1.055 WHERE supplier_id = 105;",
        "C": "UPDATE product",
        "D": "UPDATE product SET list_price = list_price + (list_price * .055), cost = cost + (cost * .055) WHERE supplier_id LIKE 'Global Imports, Inc.' OR supplier_id = 105;"
    },
    "explanation_vi": "Để cập nhật nhiều cột trong câu lệnh UPDATE, các cặp phép gán được ngăn cách bằng dấu phẩy `,` sau duy nhất một từ khóa `SET`. Tăng 5.5% tương đương với nhân giá trị với `1.055` (`1 + 0.055`). Phương án B sai vì lặp lại từ khóa SET.",
    "key_takeaway_vi": "Cập nhật nhiều cột: SET col1 = val1, col2 = val2 (chỉ dùng một từ khóa SET, phân cách bằng dấu phẩy).",
    "flashcard_front_vi": "Cách viết nhiều cột trong mệnh đề SET của lệnh UPDATE?",
    "flashcard_back_vi": "SET col1 = expr1, col2 = expr2 (ngăn cách bằng dấu phẩy)."
}

DATA_MOD_4_6[100] = {
    "prompt_vi": "Xét cấu trúc bảng EVENT và NEW_EVENT. Bạn thực thi câu lệnh MERGE sau:\nMERGE INTO event e USING (SELECT * FROM new_event WHERE event_type_id = 4) n ON (e.event_id = n.event_id)\nWHEN MATCHED THEN UPDATE SET e.event_type_id = n.event_type_id, e.start_dt = n.start_dt\nWHEN NOT MATCHED THEN INSERT (event_id, event_name, event_type_id) VALUES (n.event_id, n.event_name, n.event_type_id);\nCâu lệnh MERGE này bị lỗi. Nguyên nhân là gì?",
    "options_vi": {
        "A": "Phần UPDATE của câu lệnh không hợp lệ (The UPDATE portion of the statement is invalid).",
        "B": "Không thể dùng subquery trong mệnh đề USING của câu lệnh MERGE.",
        "C": "Không được dùng bí danh bảng trong câu lệnh MERGE.",
        "D": "Mệnh đề ON của câu lệnh không hợp lệ."
    },
    "explanation_vi": "Trong Oracle SQL, mệnh đề `UPDATE SET` bên trong `MERGE` KHÔNG ĐƯỢC phép thêm tiền tố bí danh của bảng đích vào các cột được cập nhật (phải viết `event_type_id = n.event_type_id`, không được viết `e.event_type_id`). Ngoài ra, bảng EVENT không có cột `start_dt` (cột này chỉ có ở bảng `new_event`). Do đó phần UPDATE bị lỗi.",
    "key_takeaway_vi": "Trong MERGE UPDATE SET, không được đặt bí danh bảng đích vào tên cột cần sửa.",
    "flashcard_front_vi": "Lỗi phổ biến nhất trong mệnh đề UPDATE của lệnh MERGE là gì?",
    "flashcard_back_vi": "Gắn bí danh bảng đích vào cột cần cập nhật (ví dụ viết e.col = ... là vi phạm cú pháp Oracle)."
}

# MODULE 6: Single Row Function (Q101 - Q120)
DATA_MOD_4_6[101] = {
    "prompt_vi": "Hàm NVL trong Oracle SQL thực hiện tác vụ nào sau đây?",
    "options_vi": {
        "A": "Cho phép chỉ định một giá trị thay thế cho các giá trị cột là NULL (specify alternate output for NULL).",
        "B": "Hỗ trợ phân phối kết quả đầu ra trên nhiều cột.",
        "C": "Chỉ định giá trị thay thế cho các giá trị KHÔNG NULL.",
        "D": "Biến giá trị của cột thành NULL."
    },
    "explanation_vi": "Cú pháp `NVL(expr1, expr2)`: Nếu `expr1` là NULL thì hàm sẽ trả về `expr2`; nếu `expr1` không phải là NULL thì giữ nguyên giá trị `expr1`. Cả hai đối số phải có kiểu dữ liệu tương thích.",
    "key_takeaway_vi": "NVL(biểu_thức, giá_trị_thay_thế): Thay thế NULL bằng một giá trị cụ thể.",
    "flashcard_front_vi": "Cú pháp và tác dụng của hàm NVL trong Oracle?",
    "flashcard_back_vi": "NVL(expr1, expr2): Nếu expr1 là NULL thì trả về expr2, ngược lại trả về expr1."
}

DATA_MOD_4_6[102] = {
    "prompt_vi": "Câu lệnh SELECT nào sau đây trả về kết quả 'elloworld' từ chuỗi 'HelloWorld'?",
    "options_vi": {
        "A": "SELECT LOWER (TRIM ('H' FROM 'HelloWorld')) FROM dual;",
        "B": "SELECT SUBSTR ('HelloWorld', 1) FROM dual;",
        "C": "SELECT INITCAP (TRIM ('HelloWorld', 1, 1)) FROM dual;",
        "D": "SELECT LOWER (SUBSTR ('HelloWorld', 1, 1) FROM dual;"
    },
    "explanation_vi": "`TRIM ('H' FROM 'HelloWorld')` sẽ cắt bỏ ký tự 'H' ở đầu chuỗi, thu được `'elloWorld'`. Sau đó, hàm `LOWER()` chuyển toàn bộ chuỗi sang chữ thường, thu được kết quả chính xác là `'elloworld'`.",
    "key_takeaway_vi": "TRIM cắt ký tự chỉ định ở đầu/cuối chuỗi, LOWER chuyển toàn bộ thành chữ thường.",
    "flashcard_front_vi": "TRIM('H' FROM 'HelloWorld') trả về kết quả gì?",
    "flashcard_back_vi": "'elloWorld' (cắt bỏ ký tự 'H' ở đầu chuỗi)."
}

DATA_MOD_4_6[103] = {
    "prompt_vi": "Đoạn mã nào sau đây hiển thị '01-JAN-02' khi giá trị của ENROLL_DATE là '01-JUL-01'?",
    "options_vi": {
        "A": "SELECT ROUND (enroll_date, 'YEAR') FROM student;",
        "B": "SELECT ROUND (enroll_date, 'DAY') FROM student;",
        "C": "SELECT ROUND (enroll_date, 'MONTH') FROM student;",
        "D": "SELECT ROUND (TO_CHAR(enroll_date, 'YYYY')) FROM student;"
    },
    "explanation_vi": "Hàm `ROUND(date, 'YEAR')` làm tròn ngày đến ngày 1 tháng 1 gần nhất. Mốc làm tròn là ngày 1 tháng 7: từ ngày 1/7 trở đi sẽ được làm tròn lên năm tiếp theo. Ngày '01-JUL-01' đạt mốc làm tròn lên, nên kết quả là ngày đầu năm sau: '01-JAN-02'.",
    "key_takeaway_vi": "ROUND(date, 'YEAR') làm tròn lên năm tiếp theo nếu ngày từ 01-JUL trở đi.",
    "flashcard_front_vi": "Hàm ROUND(ngày, 'YEAR') làm tròn ngày theo quy tắc nào?",
    "flashcard_back_vi": "Nếu từ 01-JUL trở đi thì làm tròn lên ngày 01-JAN của năm sau; trước 01-JUL thì làm tròn về 01-JAN của năm hiện tại."
}

DATA_MOD_4_6[104] = {
    "prompt_vi": "Hàm nào có thể dùng trong truy vấn trên bảng department để chỉ hiển thị các phòng ban có tên chứa đúng 3 ký tự?",
    "options_vi": {
        "A": "LENGTH",
        "B": "REPLACE",
        "C": "SUBSTR",
        "D": "RPAD"
    },
    "explanation_vi": "Hàm `LENGTH(chuỗi)` trả về độ dài số lượng ký tự của chuỗi. Để lọc các tên phòng ban có 3 ký tự, ta dùng: `WHERE LENGTH(department_name) = 3`.",
    "key_takeaway_vi": "Hàm LENGTH(str) trả về số lượng ký tự trong chuỗi.",
    "flashcard_front_vi": "Hàm nào trong SQL đếm số lượng ký tự của một chuỗi?",
    "flashcard_back_vi": "LENGTH(string)."
}

DATA_MOD_4_6[105] = {
    "prompt_vi": "Phát biểu nào sau đây về các hàm trong SQL là ĐÚNG?",
    "options_vi": {
        "A": "Các hàm chuỗi (Character functions) có thể trả về giá trị kiểu chuỗi hoặc kiểu số.",
        "B": "Hàm chuyển đổi (Conversion functions) chuyển đổi định nghĩa cột từ kiểu dữ liệu này sang kiểu khác.",
        "C": "Hàm xử lý đơn dòng chỉ có thể được sử dụng trong các mệnh đề SELECT và WHERE.",
        "D": "Tất cả các hàm ngày tháng đều trả về giá trị kiểu dữ liệu DATE."
    },
    "explanation_vi": "Phát biểu A là hoàn toàn chính xác. Ví dụ: hàm `UPPER()`, `SUBSTR()` trả về kiểu chuỗi (character), trong khi hàm `LENGTH()`, `INSTR()` cũng là hàm xử lý chuỗi nhưng trả về kiểu số (number). Phương án C sai vì dùng được cả ở ORDER BY; phương án D sai vì MONTHS_BETWEEN trả về số.",
    "key_takeaway_vi": "Hàm chuỗi có thể trả về chuỗi (UPPER, LOWER) hoặc trả về số (LENGTH, INSTR).",
    "flashcard_front_vi": "Hàm chuỗi trong SQL có thể trả về kiểu dữ liệu số không?",
    "flashcard_back_vi": "CÓ. Ví dụ LENGTH(str) và INSTR(str, substr) là hàm chuỗi trả về kiểu số NUMBER."
}

DATA_MOD_4_6[106] = {
    "prompt_vi": "Đánh giá câu lệnh SQL sau:\nSELECT ROUND(45.953, -1), TRUNC(45.936, 2) FROM dual;\nNhững giá trị nào sẽ được hiển thị?",
    "options_vi": {
        "A": "50 và 45.93",
        "B": "46 và 45",
        "C": "46 và 45.93",
        "D": "50 và 45.9"
    },
    "explanation_vi": "`ROUND(45.953, -1)`: tham số -1 nghĩa là làm tròn đến hàng chục. 45.953 có hàng đơn vị là 5 nên làm tròn lên thành 50. `TRUNC(45.936, 2)`: cắt bớt sau 2 chữ số thập phân (không làm tròn) thu được 45.93.",
    "key_takeaway_vi": "ROUND(x, -1) làm tròn đến hàng chục; TRUNC(x, 2) cắt cụt chỉ giữ lại 2 số thập phân.",
    "flashcard_front_vi": "ROUND(45.953, -1) và TRUNC(45.936, 2) ra kết quả gì?",
    "flashcard_back_vi": "50 và 45.93."
}

DATA_MOD_4_6[107] = {
    "prompt_vi": "Hàm nào sau đây KHÔNG PHẢI là một hàm xử lý số (Number function)?",
    "options_vi": {
        "A": "TO_NUMBER",
        "B": "TRUNC",
        "C": "SQRT",
        "D": "ROUND"
    },
    "explanation_vi": "`TO_NUMBER` là một hàm chuyển đổi kiểu dữ liệu (Conversion Function) dùng để chuyển chuỗi ký tự thành kiểu số, không phải là hàm toán học xử lý số. Các hàm TRUNC, SQRT, ROUND, MOD là các hàm số (Number functions).",
    "key_takeaway_vi": "TO_NUMBER là hàm chuyển đổi (Conversion Function), không phải hàm toán học xử lý số.",
    "flashcard_front_vi": "TO_NUMBER thuộc nhóm hàm nào trong SQL?",
    "flashcard_back_vi": "Nhóm hàm chuyển đổi kiểu dữ liệu (Conversion Functions)."
}

DATA_MOD_4_6[108] = {
    "prompt_vi": "Khi sử dụng hàm đơn dòng trong câu lệnh SELECT, hàm nào sau đây có chức năng tương tự như cấu trúc lệnh rẽ nhánh IF-THEN-ELSE?",
    "options_vi": {
        "A": "DECODE",
        "B": "SQRT",
        "C": "NEW_TIME",
        "D": "ROWIDTOCHAR"
    },
    "explanation_vi": "Hàm `DECODE(col, val1, res1, val2, res2, default)` là hàm đặc trưng của Oracle cung cấp logic điều kiện tương tự câu lệnh `IF col = val1 THEN res1 ELSIF col = val2 THEN res2 ELSE default END`.",
    "key_takeaway_vi": "Hàm DECODE tương đương cấu trúc IF-THEN-ELSE trong Oracle SQL.",
    "flashcard_front_vi": "Hàm nào trong Oracle tương đương với mệnh đề IF-THEN-ELSE?",
    "flashcard_back_vi": "Hàm DECODE (và biểu thức CASE)."
}

DATA_MOD_4_6[109] = {
    "prompt_vi": "Đặc điểm nào sau đây KHÔNG PHẢI là đặc tính của các hàm đơn dòng (Single row functions)?",
    "options_vi": {
        "A": "Không thể lồng nhau (cannot be nested).",
        "B": "Thao tác trên từng phần tử dữ liệu.",
        "C": "Tác động trên mỗi dòng được trả về.",
        "D": "Trả về duy nhất một kết quả cho mỗi dòng."
    },
    "explanation_vi": "Phát biểu A là SAI vì các hàm đơn dòng trong SQL CÓ THỂ LỒNG NHAU đến độ sâu tùy ý. Ví dụ: `ROUND(TRUNC(MOD(1600, 10), -1), 2)` là lồng 3 hàm đơn dòng với nhau.",
    "key_takeaway_vi": "Hàm đơn dòng tác động lên từng dòng, trả về 1 kết quả mỗi dòng và có thể lồng nhau không giới hạn.",
    "flashcard_front_vi": "Các hàm đơn dòng trong SQL có thể lồng nhau được không?",
    "flashcard_back_vi": "CÓ. Có thể lồng các hàm đơn dòng với nhau tới bất kỳ độ sâu nào."
}

DATA_MOD_4_6[110] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây trả về một giá trị kiểu số (numeric value)?",
    "options_vi": {
        "A": "SELECT sysdate-hire_date FROM EMP;",
        "B": "SELECT ADD_MONTHS(MAX(hire_Date), 6) FROM EMP;",
        "C": "SELECT ROUND(hire_date) FROM EMP;",
        "D": "SELECT TO_NUMBER(hire_date + 7) FROM EMP;"
    },
    "explanation_vi": "Trong Oracle, phép trừ giữa hai giá trị ngày tháng (`DATE - DATE`) sẽ trả về kết quả là một số (NUMBER) biểu thị số ngày chênh lệch giữa hai thời điểm. Do đó `sysdate - hire_date` trả về số ngày làm việc.",
    "key_takeaway_vi": "Ngày trừ Ngày (DATE - DATE) trả về số lượng ngày (kiểu NUMBER).",
    "flashcard_front_vi": "Phép tính SYSDATE - hire_date trả về kiểu dữ liệu gì?",
    "flashcard_back_vi": "Kiểu số (NUMBER) - biểu thị khoảng thời gian chênh lệch tính theo số ngày."
}

DATA_MOD_4_6[111] = {
    "prompt_vi": "Loại nào sau đây KHÔNG PHẢI là một loại hàm đơn dòng (Single Row functions) trong SQL?",
    "options_vi": {
        "A": "calendar",
        "B": "string",
        "C": "character",
        "D": "Numeric"
    },
    "explanation_vi": "Các nhóm hàm đơn dòng chuẩn trong SQL gồm: Character/String (chuỗi), Number/Numeric (số), Date (ngày tháng), Conversion (chuyển đổi) và General (tổng quát). Không có nhóm hàm nào tên là 'calendar'.",
    "key_takeaway_vi": "SQL không có nhóm hàm nào tên là 'calendar'.",
    "flashcard_front_vi": "Các nhóm hàm đơn dòng chính trong SQL là gì?",
    "flashcard_back_vi": "Character (chuỗi), Number (số), Date (ngày), Conversion (chuyển đổi), General (tổng quát)."
}

DATA_MOD_4_6[112] = {
    "prompt_vi": "Ban quản lý yêu cầu tính giá trị `12 * salary * commission_pct` cho tất cả nhân viên trong bảng EMP. Bảng có các cột: LAST_NAME, SALARY, COMMISSION_PCT.\nCâu lệnh nào đảm bảo luôn hiển thị một giá trị cụ thể (không bị ra NULL) cho tất cả nhân viên?",
    "options_vi": {
        "A": "SELECT last_name, 12*salary*(nvl(commission_pct,0)) FROM emp;",
        "B": "SELECT last_name, 12*salary*commison_pct FROM emp;",
        "C": "SELECT last_name, 12*salary* (commission_pct,0) FROM emp;",
        "D": "SELECT last_name, 12*salary*(decode(commission_pct,0)) FROM emp;"
    },
    "explanation_vi": "Nếu một nhân viên không có hoa hồng, `commission_pct` sẽ là NULL. Khi đó phép nhân với NULL sẽ biến toàn bộ kết quả thành NULL. Hàm `NVL(commission_pct, 0)` sẽ chuyển các giá trị NULL thành số 0, đảm bảo phép nhân luôn ra một kết quả số xác định.",
    "key_takeaway_vi": "Sử dụng NVL(col, 0) để thay thế NULL bằng 0 trong các biểu thức tính toán số học.",
    "flashcard_front_vi": "Tại sao cần dùng NVL khi tính toán lương có hoa hồng?",
    "flashcard_back_vi": "Vì nếu hoa hồng là NULL, phép nhân sẽ ra NULL. NVL(comm, 0) giúp chuyển NULL thành 0."
}

DATA_MOD_4_6[113] = {
    "prompt_vi": "Đánh giá câu lệnh SQL:\nSELECT LPAD(salary, 10, *) FROM EMP WHERE EMP_ID = 1001;\nNếu nhân viên có lương là 17000, kết quả hiển thị sẽ là gì?",
    "options_vi": {
        "A": "Một thông báo lỗi (An error statement).",
        "B": "17000.00",
        "C": "17000*****",
        "D": "*****17000"
    },
    "explanation_vi": "⚠️ BẪY CÚ PHÁP: Ký tự đệm trong hàm LPAD bắt buộc phải là một chuỗi ký tự đặt trong dấu nháy đơn `'*'`. Ở đây câu lệnh viết dấu sao trần `*` không có dấu nháy đơn, do đó Oracle sẽ hiểu nhầm dấu sao là toán tử hoặc ký tự đại diện và báo lỗi cú pháp ngay lập tức!",
    "key_takeaway_vi": "Đối số ký tự đệm trong LPAD/RPAD bắt buộc phải đặt trong dấu nháy đơn: LPAD(col, 10, '*').",
    "flashcard_front_vi": "SELECT LPAD(salary, 10, *) có chạy được không?",
    "flashcard_back_vi": "Báo lỗi cú pháp vì thiếu dấu nháy đơn quanh ký tự '*': phải viết là LPAD(salary, 10, '*')."
}

DATA_MOD_4_6[114] = {
    "prompt_vi": "Bạn muốn hiển thị tên và thu nhập hoa hồng hàng năm `(salary * 12) * commission_pct`. Với những nhân viên có commission_pct là NULL, kết quả tính toán phải hiển thị là 0. Câu lệnh nào đúng?",
    "options_vi": {
        "A": "SELECT last_name, (salary * 12) * NVL(commission_pct, 0) FROM EMPLOYEES;",
        "B": "SELECT last_name, (salary * 12) * commission_pct FROM EMPLOYEES;",
        "C": "SELECT last_name, (salary * 12) * IFNULL(commission_pct,0) FROM EMPLOYEES;",
        "D": "SELECT last_name, (salary * 12) * NVL2(commission_pct, 0) FROM EMPLOYEES;"
    },
    "explanation_vi": "Hàm `NVL(commission_pct, 0)` kiểm tra nếu giá trị là NULL thì trả về 0, giúp phép tính trở thành `(salary * 12) * 0 = 0`. Oracle không có hàm `IFNULL` (đó là của MySQL) và `NVL2` yêu cầu 3 tham số.",
    "key_takeaway_vi": "Oracle dùng NVL(val, 0) để thay thế NULL trong biểu thức tính toán.",
    "flashcard_front_vi": "Oracle có hàm IFNULL(val, default) không?",
    "flashcard_back_vi": "KHÔNG. Hàm IFNULL thuộc MySQL. Trong Oracle sử dụng hàm NVL(val, default)."
}

DATA_MOD_4_6[115] = {
    "prompt_vi": "Bạn muốn hiển thị ngày hệ thống theo định dạng \"Monday, 01 June, 2001\". Bạn nên sử dụng câu lệnh SELECT nào?",
    "options_vi": {
        "A": "SELECT TO_CHAR(SYSDATE, 'FMDay, DD Month, YYYY') FROM dual;",
        "B": "SELECT TO_DATE(SYSDATE, 'FMDAY, DD Month, YYYY') FROM dual;",
        "C": "SELECT TO_CHAR(SYSDATE, 'FMDD, DY Month, 'YYY') FROM dual;",
        "D": "SELECT TO_CHAR(SYSDATE, 'FMDY, DDD Month, YYYY') FROM dual;"
    },
    "explanation_vi": "Để định dạng ngày thành chuỗi hiển thị, ta dùng `TO_CHAR(date, format)`. Mô hình định dạng: `Day` hiển thị đầy đủ tên thứ ('Monday'), `DD` hiển thị 2 chữ số ngày ('01'), `Month` hiển thị đầy đủ tên tháng ('June'), `YYYY` hiển thị 4 chữ số năm. Tiền tố `FM` (Fill Mode) loại bỏ các khoảng trắng thừa do Oracle tự đệm vào tên thứ và tháng.",
    "key_takeaway_vi": "TO_CHAR(SYSDATE, 'FMDay, DD Month, YYYY') định dạng ngày đầy đủ và loại bỏ khoảng trắng thừa.",
    "flashcard_front_vi": "Ký hiệu FM trong format model của TO_CHAR có tác dụng gì?",
    "flashcard_back_vi": "FM (Fill Mode) dùng để loại bỏ các khoảng trắng và số 0 đệm thừa trong kết quả ngày/tháng."
}

DATA_MOD_4_6[116] = {
    "prompt_vi": "Đánh giá câu lệnh SQL sau:\nSELECT ROUND(TRUNC(MOD(1600, 10), -1), 2) FROM dual;\nGiá trị nào sẽ được hiển thị?",
    "options_vi": {
        "A": "0",
        "B": "1",
        "C": "0.00",
        "D": "Một thông báo lỗi (An error statement)"
    },
    "explanation_vi": "Phân tích từng bước từ trong ra ngoài: 1. `MOD(1600, 10)` = 0 (1600 chia hết cho 10, dư 0). 2. `TRUNC(0, -1)` = 0. 3. `ROUND(0, 2)` = 0. Kết quả cuối cùng hiển thị là 0.",
    "key_takeaway_vi": "Các hàm lồng nhau thực thi từ trong ra ngoài: MOD(1600,10) = 0 -> kết quả cuối cùng = 0.",
    "flashcard_front_vi": "Các hàm lồng nhau trong SQL thực thi theo thứ tự nào?",
    "flashcard_back_vi": "Thực thi từ hàm trong cùng ra hàm ngoài cùng."
}

DATA_MOD_4_6[117] = {
    "prompt_vi": "Câu lệnh SELECT nào sau đây sẽ KHÔNG HIỂN THỊ số 2000 theo định dạng '$2,000.00'?",
    "options_vi": {
        "A": "SELECT TO_CHAR (2000, '$2,000.00') FROM dual;",
        "B": "SELECT TO_CHAR (2000, '$0,000.00') FROM dual;",
        "C": "SELECT TO_CHAR (2000, '$9,999.00') FROM dual;",
        "D": "SELECT TO_CHAR (2000, '$9,999.99') FROM dual;"
    },
    "explanation_vi": "Trong chuỗi định dạng (Format Model) số của hàm `TO_CHAR`, các ký tự định dạng vị trí số hợp lệ chỉ có thể là `9` (chữ số tùy chọn) hoặc `0` (chữ số bắt buộc hiển thị). Ký tự `'2'` không phải là một ký tự định dạng hợp lệ của format model, nên câu lệnh A là không hợp lệ.",
    "key_takeaway_vi": "Mô hình định dạng số trong TO_CHAR chỉ dùng ký tự 9 hoặc 0, không dùng số cụ thể như 2 trong format string.",
    "flashcard_front_vi": "Các ký hiệu đại diện cho chữ số trong format model của TO_CHAR là gì?",
    "flashcard_back_vi": "Ký tự 9 (hiển thị số hoặc khoảng trống) và ký tự 0 (bắt buộc hiển thị số 0 nếu thiếu)."
}

DATA_MOD_4_6[118] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG CHÍNH XÁC về các hàm có sẵn trong SQL?",
    "options_vi": {
        "A": "Hàm NVL2 trả về biểu thức khác null đầu tiên trong danh sách các biểu thức (first non-null expression).",
        "B": "Hàm DECODE biên dịch một biểu thức sau khi so sánh nó với từng giá trị tìm kiếm.",
        "C": "Hàm TRIM cắt bớt các ký tự đầu hoặc cuối (hoặc cả hai) khỏi một chuỗi ký tự.",
        "D": "Hàm NULLIF so sánh hai biểu thức và trả về null nếu chúng bằng nhau, hoặc trả về biểu thức thứ nhất nếu chúng không bằng nhau."
    },
    "explanation_vi": "Phát biểu A là SAI vì hàm trả về giá trị khác null đầu tiên trong danh sách là hàm `COALESCE(expr1, expr2, ...)`. Hàm `NVL2(expr1, expr2, expr3)` có cơ chế: nếu `expr1` khác NULL thì trả về `expr2`, ngược lại (nếu `expr1` là NULL) thì trả về `expr3`.",
    "key_takeaway_vi": "COALESCE trả về giá trị non-null đầu tiên; NVL2(expr1, expr2, expr3) kiểm tra expr1 để chọn expr2 hoặc expr3.",
    "flashcard_front_vi": "Phân biệt hàm COALESCE và hàm NVL2?",
    "flashcard_back_vi": "COALESCE trả về giá trị non-null đầu tiên trong danh sách. NVL2(a, b, c): nếu a khác null trả về b, nếu a null trả về c."
}

DATA_MOD_4_6[119] = {
    "prompt_vi": "Hàm nào sau đây là một hàm thao tác trên chuỗi ký tự (Character manipulation function)?",
    "options_vi": {
        "A": "TRIM",
        "B": "TRUNC",
        "C": "TO_DATE",
        "D": "MOD"
    },
    "explanation_vi": "`TRIM` là hàm thao tác trên chuỗi (cắt bỏ ký tự ở đầu/cuối chuỗi). TRUNC và MOD là hàm số (Number), TO_DATE là hàm chuyển đổi (Conversion).",
    "key_takeaway_vi": "TRIM là hàm thao tác chuỗi ký tự (Character Manipulation Function).",
    "flashcard_front_vi": "Hàm nào dùng để loại bỏ khoảng trắng hoặc ký tự thừa ở 2 đầu chuỗi?",
    "flashcard_back_vi": "Hàm TRIM."
}

DATA_MOD_4_6[120] = {
    "prompt_vi": "Tác vụ nào sau đây bạn có thể thực hiện bằng cách sử dụng hàm TO_CHAR?",
    "options_vi": {
        "A": "Chuyển đổi số hoặc ngày tháng sang dạng chuỗi (Convert number/date to character string).",
        "B": "Chuyển số 10 thành chữ 'TEN'.",
        "C": "Chuyển chuỗi '10' thành số 10.",
        "D": "Chuyển chữ 'TEN' thành số 10."
    },
    "explanation_vi": "Hàm `TO_CHAR` chuyên dùng để chuyển đổi kiểu dữ liệu ngày tháng (DATE) hoặc kiểu số (NUMBER) sang chuỗi ký tự (VARCHAR2) theo một định dạng cụ thể. Chuyển chuỗi thành số phải dùng `TO_NUMBER`.",
    "key_takeaway_vi": "Hàm TO_CHAR dùng để chuyển đổi kiểu số hoặc ngày tháng sang chuỗi ký tự có định dạng.",
    "flashcard_front_vi": "Hàm TO_CHAR dùng để làm gì?",
    "flashcard_back_vi": "Chuyển đổi kiểu NUMBER hoặc DATE thành kiểu chuỗi VARCHAR2 có định dạng."
}

print(f"Loaded {len(DATA_MOD_4_6)} questions for Modules 4-6.")
